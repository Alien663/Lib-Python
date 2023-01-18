import os
import csv
import openpyxl

class Excel():
    def __init__(self, filename, header=1):
        self.filename = filename
        self.header = header
        self.__excend = self.filename.split(".")[-1]
        if(self.__excend not in ["xlsx", "xls", "csv"]):
            raise Exception("Can not know this file with extend file name : ." + self.__excend)
    
    def __str__(self):
        return "read data from %s" % self.filename

    def read(self):
        match extend:
            case "xlsx":
                return self.__read_excel()
            case "xls":
                return self.__read_excel()
            case "csv":
                return self.__raed_csv()

    def __read_excel(self):
        result = dict()
        workbook = openpyxl.load_workbook(self.filename)
        for sheetname in workbook.sheetnames:
            sheet = workbook[sheetname]
            temp_sheet = []
            headers = ["nothing"]
            for i in range(1, sheet.max_column + 1):
                headers.append(sheet.cell(self.header, i).value)
            
            for i in range(1, sheet.max_row + 1):
                temp_row = dict()
                for j in range(1, sheet.max_column + 1):
                    temp_row[headers[j]] = sheet.cell(i, j).value
                temp_sheet.append(temp_row)
        result[sheetname] = temp_sheet
        return result

    def __raed_csv(self):
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
