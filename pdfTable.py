from reportlab.platypus import Table ,Paragraph , SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

'''graphics liberaries imported'''
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie



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
    '''graphics intiations'''
    inch=12
    report_pie=Pie(width = 3*inch ,height=3*inch)
    report_pie.sideLabels=True

    report_pie_data=[]
    report_pie_labels=[]
    for fruit_name in sorted(fruits):
        report_pie_data.append(fruits[fruit_name])
        report_pie_labels.append(fruit_name)


    #draw pie chart 
    report_pie.data = report_pie_data
    report_pie.labels=report_pie_labels
    report_chart = Drawing()
    report_chart.add(report_pie)

    '''table data and styles'''
    table_data=[]
    report = SimpleDocTemplate('Fruits.pdf')
    style= getSampleStyleSheet()
    table_stles = [('GRID',(0,0),(-1,-1),1,colors.blue)]
    report_title = Paragraph("A complete Inventory of My Fruits :",style["h1"])
    for k, v in fruits.items():
        table_data.append([k,v])
        
    report_table = Table(data=table_data, style=table_stles,hAlign="LEFT")
    report.build([report_title,report_table,report_chart])

except Exception as error:
    print("Error happened during the pdf table creation!",error)