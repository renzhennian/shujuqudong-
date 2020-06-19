import xlrd

class Excel_data():
    def __init__(self,Excelpath,sheetname="sheet2"):
        self.data=xlrd.open_workbook(Excelpath)
        self.table=self.data.sheet_by_name(sheetname)
        #获取第一行关键词
        self.keys=self.table.row_values(0)
        print(self.keys)
        #获取总行数
        self.rowNUM=self.table.nrows
        #获取总列数
        self.colnum=self.table.ncols
    def post_data(self):
        if self.rowNUM<=1:
            print("总行数小于1")
        else:
            result1=[]
            for line in range(self.rowNUM):
                shuju = self.table.row_values(line)
                result1.append(shuju)
            print(result1)
            return result1
if __name__ == '__main__':
    path = "C:\\Users\\Administrator\\PycharmProjects\\shujuqudong_ddt\\123.xlsx"
    sheetname = "Sheet2"
    run = Excel_data(path,sheetname)
    run.post_data()




