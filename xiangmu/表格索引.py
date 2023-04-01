# coding=utf-8
import xlrd


# 创建对象时，获取对应excel 表格
# 读取Excel行数
# 获取单元格内容
class OperationExcel:

    def __init__(self, file_name=None, sheet_id=0):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../data.xlsx'
            self.sheet_id = 0
        self.data = self.get_data ()

    def get_line(self):
        return self.data.nrows

    def get_cell_value(self, row, col):
        return self.data.cell_value ( row, col )

    def get_data(self):
        data = xlrd.open_workbook ( self.file_name )
        tables = data.sheets ()[self.sheet_id]
        return tables


if __name__ == '__main__':
    opers = OperationExcel ()
    # print
    opers.get_line ()
    # print
    opers.get_cell_value ( 1, 0 )