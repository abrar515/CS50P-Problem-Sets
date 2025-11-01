from fpdf import FPDF, Align

class Shirtificate(FPDF):
    def __init__(self, name):
        super().__init__()
        self.name = name

        self.add_page()

        self.set_font("helvetica", style="B", size=50)
        self.cell(0, 20, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')

        self.image("./shirtificate.png", x=Align.C, y=self.h/4.5,  w=self.epw)

        self.set_font(style="", size=40)
        self.set_text_color(r=255, g=255, b=255)
        width = self.get_string_width(f'{self.name} took CS50')
        self.set_y(self.h/2.5)
        self.set_x((self.w - width) / 2)
        self.cell(None, 20, f'{self.name} took CS50', align='C')

        self.output("shirtificate.pdf")


if __name__=="__main__":
    name = input("Name: ")
    Shirtificate(name)
