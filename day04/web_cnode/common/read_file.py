import xlrd

class Read_Excel():
    def __init__(self,file_name,work_sheet_index):
        self.file_name = file_name
        self.work_sheet_index = work_sheet_index

    def get_excel_data(self):
        wb = xlrd.open_workbook(self.file_name)
        ws = wb.sheet_by_index(self.work_sheet_index)
        nrows = ws.nrows
        ncols = ws.ncols

        all_data = []    
        for i in range(1,nrows):
            row_data = []
            for j in range(ncols):
                row_data.append(ws.cell_value(i,j))
            all_data.append(row_data)

        return all_data

    
