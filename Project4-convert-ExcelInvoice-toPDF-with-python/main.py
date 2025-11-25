import pandas as pd

import  glob
filepaths = glob.glob("invoices/*xlsx")


for filepath in filepaths:
    df = pd.read_excel(filepath,"Sheet 1")
    print(df)