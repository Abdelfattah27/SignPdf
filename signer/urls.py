from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),

    path('upload/', views.upload_pdf, name='upload_pdf'),
    # path('pdfs/', views.list_pdfs, name='list_pdfs'),
    path('sign/<int:pdf_id>/', views.sign_pdf, name='sign_pdf'),    
    path('assigned_pdfs/', views.list_assigned_pdfs, name='list_assigned_pdfs'),
    path('view_pdf/<int:assigned_pdf_id>/', views.view_pdf, name='view_pdf'),

]