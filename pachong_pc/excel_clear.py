import openpyxl
from package_201.common.R_r_excel import ReadExcel

wb = ReadExcel("result_715-835_bak.xlsx", "all")
wb.w_data(1, 1, "")
wb.w_save()
