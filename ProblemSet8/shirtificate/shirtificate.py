from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", size=45)
        self._pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
        self._pdf.image("shirtificate.png", w=self._pdf.epw)

        # Set font for user input text
        self._pdf.set_font_size(25)
        self._pdf.set_text_color(255, 255, 255)

        # Calculate text width and centering position
        text = f"{name} took CS50"
        text_width = self._pdf.get_string_width(text)
        x_position = (self._pdf.w - text_width) / 2

        # Add centered text at calculated position
        self._pdf.text(x=x_position, y=149, text=text)

    def output(self, name):
        self._pdf.output(name)

# Get user input and create PDF
name = input("Name: ")
pdf = PDF(name)
pdf.output("shirtificate.pdf")
