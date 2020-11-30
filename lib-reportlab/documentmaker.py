import time
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch


document = SimpleDocTemplate('budget_template.pdf',
                            pagesize=letter,
                            rightMargin=100, leftMargin=100,
                            topMargin=0, bottomMargin=100)
story = []
logo = 'DPI-logo.png'
title = '<font size="25">DPI Budget Approval Form</font>'
proposer = 'Tareq Monwer'
proposer_design = 'Web Developer'
proposer_department = 'Administration'
date = '30/11/2020'

image = Image(logo, 1.5 * inch, 1.5 * inch)
story.append(image)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Centered', alignment=TA_CENTER))
story.append(Paragraph(title, styles['Centered']))
story.append(Spacer(1, 50))

story.append(Paragraph('To', styles['Normal']))
story.append(Paragraph('The Chief Executive Officer', styles['Normal']))
story.append(Spacer(1, 10))

story.append(Paragraph(f'PROPOSED BY: {proposer}', styles['Normal']))
# story.append(Spacer(1, 30))
story.append(Paragraph(f'DEPARTMENT: {proposer_department}', styles['Normal']))
# story.append(Spacer(1, 30))

# Finally, make the file based of story list.
document.build(story)
