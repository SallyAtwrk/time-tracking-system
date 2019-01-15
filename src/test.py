import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
f = open('12.dat','r')
id_lst = []
date_lst = []
for rows in f:
    row = rows[0:29].replace(" ", "").replace("	", "!")
    row_index = row.split("!")
    id_lst.append(row_index[0])
    date_lst.append((row_index[1][0:10] + " " + row_index[1][10:29]))


