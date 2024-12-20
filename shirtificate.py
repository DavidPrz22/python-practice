from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, title=""):
        super().__init__()
        self.title = title

    def header(self):
        self.set_font("helvetica", style="B", size=55)
        width = self.get_string_width(self.title) + 6
        self.set_x((210 - width) / 2)
        self.set_line_width(1)
        self.ln(20)
        self.cell(
            width,
            9,
            self.title,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C"
        )
        self.ln(10)

# Create PDF with the title
pdf = PDF("CS50 SHIRTIFICATE")
pdf.add_page()
pdf.set_font("helvetica", style="B", size=16)

pdf.image("./shirtificate.png", x=0, y=70)  # Centered image

pdf.set_text_color(255)
pdf.cell(0, 200, "DAVID PEREZ TOOK CS50", new_x="LMARGIN", new_y="NEXT", align='C')
pdf.output("cs50pdf.pdf")

