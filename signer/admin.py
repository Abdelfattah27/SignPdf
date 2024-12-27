from django.contrib import admin
from .models import PDF, Signature, AssignedPDF

from django.contrib import admin
from .models import PDF
import hashlib

@admin.register(PDF)
class PDFAdmin(admin.ModelAdmin):
    list_display = ('hash', 'file')
    search_fields = ('hash',)
    readonly_fields = ["hash"]

    def save_model(self, request, obj, form, change):
        if obj.file:
            file_content = obj.file.read()
            obj.hash = hashlib.sha256(file_content).hexdigest()
            obj.file.seek(0)
        super().save_model(request, obj, form, change)

@admin.register(Signature)
class SignatureAdmin(admin.ModelAdmin):
    list_display = ('pdf', 'user', 'signed_at')
    list_filter = ('signed_at',)
    search_fields = ('pdf__hash', 'user__username')

@admin.register(AssignedPDF)
class AssignedPDFAdmin(admin.ModelAdmin):
    list_display = ('user', 'pdf', 'status')
    list_filter = ('status',)
    search_fields = ('user__username', 'pdf__hash')