from django.db import models
from django.contrib.auth.models import User

class PDF(models.Model):
    hash = models.CharField(max_length=64, unique=True)
    file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.hash

class Signature(models.Model):
    pdf = models.ForeignKey(PDF, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    signed_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} signed {self.pdf.hash}"
    
    
class AssignedPDF(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assignments")
    pdf = models.ForeignKey(PDF, on_delete=models.CASCADE, related_name="assignments")
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} assigned to {self.pdf.hash}"