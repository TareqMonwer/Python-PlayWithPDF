from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def coord(x, y, height, unit=1):
    """ SO Knows better :/ """
    x, y = x * unit, height - y * unit
    return x, y


c = canvas.Canvas('hello.pdf')
first_page_content = 'page 1: Hello World From PDFGEN CANVAS.'
c.drawString(10, 825, first_page_content)
c.showPage()
c.drawString(10, 825, 'page 2: Oww, really! This is working?')
c.save()
