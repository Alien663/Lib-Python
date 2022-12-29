import csv
import xlrd

class Table:
    def __init__(self, filename, header=0):
        self.filename= filename
        self.header = header
    
    def read(self):
        print("read data from %s" % self.filename)

class Excel(Table):
    def __init__(self, filename, header=0, sheetIndex=0):
        super().__init__(filename, header)
        self.sheetIndex = sheetIndex

    def read(self):
        result = []
        keys = []
        wb = xlrd.open_workbook(self.filename)
        sheet = wb.sheet_by_index(self.sheetIndex)
        for i in range(sheet.ncols):
            keys.append(sheet.cell(self.header, i).value)
        for i in range(self.header + 1, sheet.nrows):
            row = dict()
            for j in range(len(keys)):
                row[keys[j]] = sheet.cell(i, j).value
            result.append(row)
        return(result)

    def insert(self):
        pass
    
    def newSheet(self):
        pass

class Csv(Table):
    def __init__(self, filename, header=0):
        super().__init__(filename, header)
    
    def read(self):
        i = 0
        Flag = False
        cols, result = [], []
        with open(self.filename, 'r', encoding='utf-8', newline='') as fp:
            raw_rows = csv.reader(fp)
            for item in raw_rows:
                if Flag:
                    result.append(dict(zip(cols, item)))
                elif(i == self.header):
                    Flag = True
                    cols = item
                i += 1
        fp.close()
        return(result)

    def insert(self):
        pass

