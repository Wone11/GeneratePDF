from reportlab.platypus import Table ,Paragraph , SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

'''fruits list'''
fruits = {
        "Elderberries":1,
        "Figs":1,
        "Apples":2,
        "Durians":3,
        "Bananas":5,
        "Cheries":8,
        "Grapes":13
    }

try:   
    table_data=[]
    report = SimpleDocTemplate('Fruits.pdf')
    style= getSampleStyleSheet()
    table_stles = [('GRID',(0,0),(-1,-1),1,colors.blue)]
    report_title = Paragraph("A complete Inventory of My Fruits :",style["h1"])
    for k, v in fruits.items():
        table_data.append([k,v])
        
    report_table = Table(data=table_data, style=table_stles,hAlign="LEFT")
    report.build([report_title,report_table])

except Exception as error:
    print("Error happened during the pdf table creation!",error)