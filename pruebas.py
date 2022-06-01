#!/usr/bin/env  python3

from reportlab.platypus import Paragraph, Spacer, Table, Image, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from datetime import date

today = date.today().strftime('%B %d, %Y')

fruit = {
    "elderberries": 1,
    "figs": 1,
    "apples": 2,
    "durians": 3,
    "bananas": 5,
    "cherries": 8,
    "grapes": 13
}

report = SimpleDocTemplate("report.pdf")

styles = getSampleStyleSheet()

report_title = Paragraph(f"A Complete Inventory of My Fruit on {today}", styles["h1"])

table_data = []

for k, v in fruit.items():
    table_data.append([k, v])

report_table = Table(data=table_data)

table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]

report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

report_pie = Pie(width=3*inch, height=3*inch)

report_pie.data = []

report_pie.labels = []

for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

report_chart = Drawing()

report_chart.add(report_pie)

report.build([report_title, report_table, report_chart])