import json
import pyodbc

class Sql:
    def __init__(self, domain, config):
        self.domain = domain
        self.config = config

    def exec(self):
        print("exec the command but can't read data out")

    def read(self):
        print("read the data out but can't exec command")

class Mssql(Sql):
    def __init__(self, domain="Default", config=r"settings.json"):
        super().__init__(domain, config)
        with open(self.config, 'r') as fp:
            Data = json.load(fp)
        fp.close()
        self.con = Data['ConnectionString'][self.domain]
        self.__connection = 'DRIVER={SQL Server};SERVER='+ self.con['Server'] + ';DATABASE=' + self.con['DataBase'] +';UID=' + self.con['Account'] + ';PWD=' + self.con['Password']

    def exec(self, command):
        cnxn = pyodbc.connect(self.__connection)
        cursor = cnxn.cursor()
        cursor.execute(command)
        cursor.commit()
        cnxn.close()

    def read(self, command):
        cnxn = pyodbc.connect(self.__connection)
        cursor = cnxn.cursor()
        cursor.execute(command)
        cols = []
        rows = []
        for item in cursor.description:
            cols.append(item[0])
        while True:
            try:
                one_row = cursor.fetchone()
                if one_row:
                    rows.append(list(one_row))
                else:
                    break
            except:
                continue
        mydata = []
        for i in range(len(rows)):
            mydata.append(dict(zip(cols, rows[i])))
        cursor.commit()
        cnxn.close()
        return(mydata)

    def makeQuery(self, data, tablename):
        result = ''
        cols = []
        for item in data:
            result += "declare @" + item + " nvarchar(max) = N'" + str(data[item]).replace("'", "''") + """'
            """
            cols.append(item)
        return(result + """insert into """ + tablename + """(""" + ','.join(cols) + """)
                values(@""" + ',@'.join(cols) + """)
            """)
