import xlsxwriter

workbook = xlsxwriter.Workbook('write_excel_1.xlsx')
worksheet = workbook.add_worksheet('Buah')

dataBuah = [
    ['No', 1, 2, 3],
    ['Nama Buah', 'Apel', 'Jeruk', 'Anggur'],
    ['Jumlah', 30, 40, 33]]

row = 0

for col, data in enumerate(dataBuah):
    worksheet.write_column(row, col, data)

workbook.close()
