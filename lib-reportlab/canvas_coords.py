from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm


def coord(x, y, height, unit=1):
    x, y = x * unit, height - y * unit
    return x, y

c = canvas.Canvas('hello2.pdf', pagesize=letter)
width, height = letter

my_text = "This is my dummy text for you, PDF!"
c.drawString(*coord(30, 30, height, mm), text=my_text)
c.showPage()
c.save()
