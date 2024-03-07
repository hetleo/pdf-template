from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    for i in range(row["Pages"]):
        pdf.add_page()
        x = 10
        y = 10
        z = 200 
        
        # lines after header
        for i in range(26):
            y = y + 10
            pdf.line(x, y, z, y)

        # set the header
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(254,43,98)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
        pdf.line(10, y, 200, y)
        
        pdf.ln(260)
        
        # set the footer    
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
        

pdf.output("output.pdf")