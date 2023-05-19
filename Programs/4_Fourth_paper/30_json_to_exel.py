import pandas as pd
import json
import openpyxl

with open('data.json', 'r') as f:           # Load the data from the JSON file
    data = json.load(f)

company_name = data['company_name']         # Extract the company name 
employee_data = data['employees']           # Extract the employee data
employees_df = pd.DataFrame(employee_data)  # Create a Pandas DataFrame with the employee data

writer = pd.ExcelWriter('report.xlsx', engine='openpyxl')   # Create a new Pandas ExcelWriter object

employees_df.to_excel(writer, sheet_name='Employees', index=False)  # Write the data to an Excel sheet

workbook = writer.book                      # Get the workbook 
worksheet = writer.sheets['Employees']      # Get the worksheet objects

worksheet.write(0, 0, 'company_name')       # Add the company name to the worksheet
worksheet.write(0, 1, company_name)

worksheet.write(1, 0, 'Name')               # Add column headers to the worksheet
worksheet.write(1, 1, 'Location')

writer.save()                               # Close the Pandas ExcelWriter object
