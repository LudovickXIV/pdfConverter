import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
from pdfConverter import converter
# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        converter.Converter.convert(request.FILES['fileToUploadHTML'], request.FILES['fileToUploadCSS'])
        file_path = 'pdf.pdf'
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
    else:
        form = UploadFileForm()
    return render(request, 'home.html', {'form': form})

def handle_uploaded_file(f):
    with open('doc/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)