from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def string_alignment(c):
    """ Takes c as canvas and draws text into it"""
    width, height = letter
    
    c.drawString(80, 700, 'Standard String')
    c.drawRightString(80, 680, 'Right String')

    numbers = [987.15, 42, -1, 234.56, (456.78)]
    y = 650

    for num in numbers:
        c.drawAlignedString(80, y, str(num))
        y -= 20
    
    c.drawCentredString(width / 2, 550, 'Centered String')
    c.showPage()



if __name__ == "__main__":
    canvas_ = canvas.Canvas('string_alignment.pdf')
    string_alignment(canvas_)
    canvas_.save()
