from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas


def rotate_demo():
    c = canvas.Canvas('rotated.pdf', pagesize=letter)
    c.translate(inch, inch)
    c.setFont('Helvetica', 14)
    c.drawString(inch, inch, 'Normal')
    c.line(inch, inch, inch + 45, inch)

    c.rotate(45)
    c.drawString(inch, -inch, '45 Degrees')
    c.line(inch, -inch, inch + 70, -inch)

    c.rotate(45)
    c.drawString(inch, -inch, '90 Degrees')
    c.line(inch, -inch, inch + 70, -inch)
    c.save()



if __name__ == "__main__":
    rotate_demo()
