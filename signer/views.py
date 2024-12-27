from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import PDF, Signature , AssignedPDF
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required


@login_required
def upload_pdf(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['pdf']
        pdf_hash = get_random_string(64)  # Replace with actual hash function
        pdf = PDF.objects.create(hash=pdf_hash, file=uploaded_file)
        return redirect('list_pdfs')
    return render(request, 'upload_pdf.html')

@login_required
def list_pdfs(request):
    pdfs = PDF.objects.all()
    print(pdfs)
    return render(request, 'list_pdfs.html', {'pdfs': pdfs})

@login_required
def sign_pdf(request, pdf_id):
    pdf = PDF.objects.get(id=pdf_id)
    Signature.objects.create(pdf=pdf, user=request.user)
    
    assigned_pdf = get_object_or_404(AssignedPDF, id=pdf_id, user=request.user)
    if not assigned_pdf.status:
        assigned_pdf.status = True
        assigned_pdf.save()
    return redirect('list_assigned_pdfs')

@login_required
def list_assigned_pdfs(request):
    assigned_pdfs = AssignedPDF.objects.filter(user=request.user)
    return render(request, 'list_assigned_pdfs.html', {'pdfs': assigned_pdfs})

@login_required
def view_pdf(request, assigned_pdf_id):
    assigned_pdf = get_object_or_404(AssignedPDF, id=assigned_pdf_id, user=request.user)
    return render(request, 'view_pdf.html', {'assigned_pdf': assigned_pdf})

@login_required
def home(request):
    return render(request, 'home.html')