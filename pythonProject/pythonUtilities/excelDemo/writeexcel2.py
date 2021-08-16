from openpyxl import Workbook
from openpyxl.styles import PatternFill

wb=Workbook()
wb['Sheet'].title="Report of automation"
sh1=wb.active

data=[('S.no','Name','ID'),(1,'Mukesh',80),(2,'Python',9),(3,'java',98)]

for i in data:
    sh1.append(i)

wb.save("FinalReportNew.xlsx")