# Import pandas
import pandas as pd

# Assign spreadsheet filename to `file`
fileCsv = "tutorial_python_1.csv"

# Load spreadsheet
df = pd.read_csv(fileCsv)

# Print data in the sheet
print(df)