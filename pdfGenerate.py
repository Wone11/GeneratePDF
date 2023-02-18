from reportlab.pdfgen import canvas
from reportlab.lib  import pdfencrypt

'''tyr generating a pdf and handle an exception during pdf generating '''
try:
    '''
    choice 1. for generate a pdf 
    choice 2. generate encrypted pdf
    '''
    choice = int(input("please enter a choice "))
    match choice:
            case 1:
                pdf = canvas.Canvas("Generated.pdf",bottomup=0) #generate a pdf by a given name!
                pdf.drawString(10,10, 'test pdf file')
                pdf.showPage()
                pdf.save()

            case 2:
                test = pdfencrypt.StandardEncryption("Gandayiki!")
                pdf  = canvas.Canvas("Encryptedpdf.pdf",bottomup=0,encrypt=test)
                pdf.drawString(20,30,"Encryped pdf generated")
                pdf.save()

except Exception as error:
    print("Error happened during pdf generate ... ", error)