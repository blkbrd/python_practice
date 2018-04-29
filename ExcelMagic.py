import openpyxl, pprint
print ('Opening Workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}
print ('Reading Rows...')
for row in range(2, sheet.max_row + 1):
    state  = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop    = sheet['D' + str(row)].value
    countyData.setdefault(state, {}) # Make sure the key for this state exists.
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})# Make sure the key for this county in this state exists.
    countyData[state][county]['tracts'] += 1 # Each row represents one census tract, so increment by one.
    countyData[state][county]['pop'] += int(pop) # Increase the county pop by the pop in this census tract.

    # Open a new text file and write the contents of countyData to it.
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')
