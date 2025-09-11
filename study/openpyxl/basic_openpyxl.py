from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

wb = Workbook()
sheet = wb.active
sheet.title = "Sample"

data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

for row in data:
    sheet.append(row)

wb.save("sample.xlsx")
