## Yuria Loo
## IT 111: Practice in class 5
## 2024-05-05

'''
Thi program generates a HTML table beased on the user specified number
 of columns and rows.
'''

# User input
colNum = int(input('Enter number of column: '))
rowNum = int(input('Enter number of row: '))
header = str(input('Add a header (yes/no): ')).lower()

# Makes the function to make a table
def make_table(row, col, header):
    col_count = 0
    row_count = 0
  
    print("<table>")
    if header == "yes":
        print("<tr>")
        for i in range(col):
            print("<th>header</th>")
        print("</tr>")
    while row_count < row:
        print("<tr>")
        while col_count < col:
            print("<td>test</td>")
            col_count += 1
        print("</tr>")
        row_count += 1
        col_count = 0
     
    print("</table>")

    
# Calls the function
make_table(rowNum, colNum, header)
