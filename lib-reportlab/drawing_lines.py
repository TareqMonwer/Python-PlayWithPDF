from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def draw_lines(c, start_y):
    c.setLineWidth(.3)
    c.line(30, start_y, 580, start_y)



if __name__ == "__main__":
    canvas_ = canvas.Canvas('lines.pdf', pagesize=letter)
    start_y = 710
    for _ in range(10):
        draw_lines(canvas_, start_y)
        start_y -= 20

    canvas_.save()
