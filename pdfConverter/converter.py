import os

import pdfkit

class Converter:

    @staticmethod
    def convert(html, css):
        if not os.path.exists('doc'):
            os.makedirs('doc')

        with open('doc/html.html', 'wb+') as destination:
            for chunk in html.chunks():
                destination.write(chunk)

        cssname = css.name
        with open('doc/'+cssname, 'wb+') as destination:
            for chunk in css.chunks():
                destination.write(chunk)

        htmlFile = 'doc/html.html'
        options = {
            'page-size': 'A4',
            'dpi': 130,
            'orientation': 'Landscape',
            'margin-top': '0in',
            'margin-right': '0in',
            'margin-bottom': '0in',
            'margin-left': '0in',
            'encoding': "UTF-8",
            'no-outline': None
        }
        pdfkit.from_file(htmlFile, 'pdf.pdf', options=options)