from django.shortcuts import render,HttpResponse, redirect
from .models import *
from .forms import *
from django.http import FileResponse
import io
from xhtml2pdf import pisa
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import FileResponse
from django.template.loader import get_template
from django.contrib.staticfiles import finders

# Create your views here.

def main(request):

    formularz = CVform()

    if request.method == 'POST':

        formularz = CVform(request.POST,request.FILES)
        if formularz.is_valid():

           formularz.save()
           return redirect('resume:pdf')

    return render(request,'Resume\home.html',context={'rzeczy':formularz})

def pdf(request):

    z = CV.objects.last()

    template_path = 'Resume\est.html'
    context = {'myvar': z}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #attachment;
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def testing(request):


    b = CV.objects.last()

    return render(request,'Resume\esting.html',context={'myvar':b})