import qrcode

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Image


def get_qr_code(barcode_value):
    doc = SimpleDocTemplate('pdfs-generated-by-codes/qr_code2.pdf')
    flowables = []

    qr_img = qrcode.make(barcode_value)
    qr_img.save('test_qr.png')
    flowables.append(Image('test_qr.png'))

    doc.build(flowables)



if __name__ == "__main__":
    get_qr_code('www.tareqmonwer.com')
