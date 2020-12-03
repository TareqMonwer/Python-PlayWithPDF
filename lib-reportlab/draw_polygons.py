from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def draw_shapes():
    c = canvas.Canvas('pdfs-generated-by-codes/shapes.pdf', pagesize=letter)
    c.setStrokeColorRGB(0.2, 0.5, 0.3)
    c.rect(10, 580, 200, 200, stroke=1, fill=1)
    c.setFillColorRGB(.5,.8, .6)
    c.ellipse(10, 600, 100, 500, fill=1)
    c.setFillColorRGB(.9, .5, .3)
    c.wedge(10, 480, 100, 350, 0, 180, stroke=1, fill=1)
    c.setFillColorRGB(.5, .9, .3)
    c.circle(60, 340, 50, stroke=1, fill=1)
    c.save()



if __name__ == "__main__":
    draw_shapes()
