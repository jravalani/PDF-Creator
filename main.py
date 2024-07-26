from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

print(df["Topic"])

pdf = FPDF(orientation="P", unit="mm", format="A4")
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.line(10, 17, 200, 17)
    pdf.cell(w=0, txt=row["Topic"], align="L", ln=1)
    for x in range(1, row["Pages"]):
        pdf.add_page()


pdf.output("output.pdf")

