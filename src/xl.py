'''
Created on 21-Mar-2014

@author: ARCHANA

'''
import xlrd
file_location = "C:/Users/ARCHANA/Desktop/data.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
sheet.cell_value(0, 0)
sheet.nrows
sheet.ncols
for col in range(sheet.ncols):
    print sheet.cell_value(2, col)
    
