from django.db import models

# Create your models here.

from django.conf import settings

class Resume(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='resumes'
    )

    file = models.FileField(upload_to='resumes/')

    uploaded_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.file.name