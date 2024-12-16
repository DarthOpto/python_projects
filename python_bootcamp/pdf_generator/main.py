from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

data = pd.read_csv("topics.csv")


def add_footer(line_breaks):
    pdf.ln(line_breaks)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


for index, row in data.iterrows():
    pdf.add_page()
    # Set Header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 20, 200, 20)

    # Footer
    add_footer(265)

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Footer
        add_footer(277)

pdf.output("output.pdf")
