from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm


def coord(x, y, height, unit=1):
    x, y = x * unit, height - y * unit
    return x, y


c = canvas.Canvas('pdfs-generated-by-codes/hello2.pdf', pagesize=letter)
width, height = letter

my_text = "HELLO 2 RUNNIG TEST AFTER FOLDER REFACTORING."
c.drawString(*coord(30, 30, height, mm), text=my_text)
c.showPage()
c.save()
