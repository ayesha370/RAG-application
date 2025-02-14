from django.db import models

class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    content = models.TextField(blank=True, null=True)  # Store parsed text content
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
