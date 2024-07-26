from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

print(df["Topic"])

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    # setting up the header
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.line(10, 17, 200, 17)
    pdf.cell(w=0, txt=row["Topic"], align="L", ln=1)

    # student challenge below; adding horizontal lines every 10mm
    page_height = int(pdf.h)
    page_width = int(pdf.w)
    for i in range (17, page_height, 10):
        pdf.line(10, i, page_width-10, i)

    # setting up the footer
    pdf.ln(268)
    pdf.set_font(family="Times", style="I", size=10)
    pdf.cell(0, 10, txt=row["Topic"], align="R")

    # adding subpages
    for x in range(1, row["Pages"]):
        pdf.add_page()
        # setting up footer for subsequent pages
        pdf.ln(268)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.cell(0, 10, txt=row["Topic"], align="R")
        for i in range(17, page_height, 10):
            pdf.line(10, i, page_width-10, i)


pdf.output("output.pdf")

