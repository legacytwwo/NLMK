import csv
import xlsxwriter

def get_csv():
  doc = open(f'file.csv', 'w', encoding='cp1251')
  writer = csv.writer(doc, delimiter=';')
  ##################
  header = ['GUID', 'NAME', 'COUNTRY', 'PRODUCER', 'PRICE', 'ReviewCount', 'ReviewRating', '1.1']
  writer.writerow(header)
  ##################
  doc.close()
  return True

def get_xlsx():
  workbook = xlsxwriter.Workbook('Expenses01.xlsx')
  worksheet = workbook.add_worksheet()
  ##################
  row = 0
  col = 0
  header = ['GUID', 'NAME', 'COUNTRY', 'PRODUCER', 'PRICE', 'ReviewCount', 'ReviewRating', '1.1']
  worksheet.write_row(row, col, header)
  # for item in header:
    # worksheet.write(row, col, item)
    # row += 1
  ##################
  workbook.close()
  return workbook.filename

a = get_xlsx()
print(a)