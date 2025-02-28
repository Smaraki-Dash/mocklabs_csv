from django.db import models
from django.contrib.auth.models import User
import os
from django.core.validators import FileExtensionValidator
# Create your models here.
class StudentProfile(models.Model):
    cources=[
        ('Python Fullstack Development', 'Python Fullstack Development'),
        ('Java Fullstack Development', 'Java Fullstack Development'),
        ('MERN Fullstack Development', 'MERN Fullstack Development'),
        ('Fullstack Development', 'Fullstack Development')
    ]
    def get_upload_path(self,filename):
        ext=filename.split('.')[-1]
        filename=f"{self.username.first_name}{self.username.last_name}_resume.{ext}"
        return os.path.join("student_resumes", filename)

    username=models.ForeignKey(User, on_delete=models.CASCADE)
    pno=models.CharField(max_length=200)
    add=models.TextField()
    course=models.CharField(max_length=200, choices=cources, default='Python Fullstack Development')
    profile_pic=models.ImageField(upload_to='students_profiles/')
    resume=models.FileField(upload_to=get_upload_path, validators=[FileExtensionValidator(['pdf', 'docx'])])

    def __str__(self):
        return self.username.username
    