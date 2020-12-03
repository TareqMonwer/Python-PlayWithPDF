from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def font_demo(my_canvas, fonts, colors):
    pos_y = 750
    for index, font in enumerate(fonts):
        my_canvas.setFont(font, 12)
        try:
            my_canvas.setFillColor(colors[index])
        except:
            my_canvas.setFillColor('black')
        my_canvas.drawString(30, pos_y, f'{index}: {font}')
        pos_y -= 20


if __name__ == '__main__':
    my_canvas = canvas.Canvas(
        'pdfs-generated-by-codes/fonts.pdf', pagesize=letter)
    fonts = my_canvas.getAvailableFonts()
    colors = ['red', 'green', 'blue', 'orange', 'purple', 'black', 'yellow']
    font_demo(my_canvas, fonts, colors)
    my_canvas.save()
