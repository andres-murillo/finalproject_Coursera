#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet


styles = getSampleStyleSheet()
report = SimpleDocTemplate('processed.pdf')
report_title = Paragraph('Processed Update on ', styles['h1'])

def generate_report(attachment, title, paragraph):
    pass
