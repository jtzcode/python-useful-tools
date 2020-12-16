import openpyxl, pprint

work_book = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = work_book.get_sheet_by_name('Population by Census Tract')

countries = {}
for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    country = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    countries.setdefault(state, {})
    countries[state].setdefault(country, {'tracts': 0, 'pop': 0})

    countries[state][country]['tracts'] += 1
    countries[state][country]['pop'] += int(pop)

resultFile = open('censusResult.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countries))
resultFile.close()

