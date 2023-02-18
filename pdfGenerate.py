from reportlab.pdfgen import canvas
from reportlab.lib  import pdfencrypt

'''tyr generating a pdf and handle an exception during pdf generating '''
try:
    pdf = canvas.Canvas("Generated.pdf",bottomup=0) #generate a pdf by a given name!
    pdf.drawString(10,10, 'test pdf file')
    pdf.showPage()
    pdf.save()

except Exception as error:
    print("Error happened during pdf generate ... ", error)