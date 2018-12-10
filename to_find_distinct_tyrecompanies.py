import xlrd
workbook = xlrd.open_workbook("allbrands.xlsx")
worksheet = workbook.sheet_by_index(0)
total_rows = worksheet.nrows                        #to get total no. of rows
total_cols = worksheet.ncols                        #to get total no. of columns
print("No. of rows: {0}, and no. of columns: {1}".format(total_rows,total_cols))
table = list()
record = list()
for x in range(total_rows):
    for y in range(total_cols):
        record.append(worksheet.cell(x,y).value)    #appending values from each cell to record list
        table.append(record)                        #appending values from record list to table list
        record = []
        x+=1
var = list()
print(table)
for i in table:
    var.append(str(i[0]).split(' ')[0])
print(set(var))



        
       
        
        
        
        
    
    
        
        
    
    
