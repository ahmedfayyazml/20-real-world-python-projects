import pandas as pd
from fpdf import FPDF
import  glob
from pathlib import Path
filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    # Collected data from dataframe
    df = pd.read_excel(filepath,"Sheet 1")
    #set up pdf orientation
    pdf = FPDF(orientation="P",unit="mm",format="A4")
    # added page
    pdf.add_page()

    # added filename
    filename = Path(filepath).stem
    invoice_num,date = filename.split("-")

    #Number
    pdf.set_font(style="B",size=16,family="Times")
    pdf.cell(w=50,h=8,txt=f"Invoice nr{invoice_num}")

    #date
    pdf.set_font(style="B", size=16, family="Times")
    pdf.cell(w=50, h=8, txt=f"Date : {date}")
    pdf.output("PDFs/"+filename+".pdf")
