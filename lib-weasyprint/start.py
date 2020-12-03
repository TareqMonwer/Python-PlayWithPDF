from weasyprint import HTML


html = HTML('https://tareqmonwer.com/')
html.write_pdf('generated_pdfs/tareqmonwer.com.pdf')
