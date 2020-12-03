from reportlab.graphics import renderPDF
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing
from reportlab.pdfgen import canvas


def qr_code(barcode_value):
    c = canvas.Canvas('pdfs-generated-by-codes/qr_code.pdf')
    qrcode = qr.QrCodeWidget(barcode_value)
    qrcode.barWidth = 145
    qrcode.barHeight = 145
    qrcode.qrVersion = 1
    # bounds = qrcode.getBounds()
    # width = bounds[2] - bounds[1]
    # height = bounds[3] - bounds[1]
    d = Drawing()
    d.add(qrcode)
    renderPDF.draw(d, c, 15, 700)
    c.save()



if __name__ == "__main__":
    qr_code('www.tareqmonwer.com')
