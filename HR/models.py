from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import os


sub=[
        ('python', 'python'),
        ('java', 'java'),
        ('django', 'django'),
        ('spring boot' , 'spring boot' ),
        ('Hibernate', 'Hibernate'),
        ('React js', 'React js'),
        ('Mern', 'Mern'),
        ('Node JS', 'Node JS'),
        ('Next js','Next js'),
        ('Webtech', 'Webtech')
    ]  
cources=[
    ('python fullstack development', 'python fullstack development'),
    ('java fullstack development','java fullstack development'),
    ('MERN fullstack development', 'MERN fullstack development'),
    ('Software Testing', 'Software Testing')
]
# Create your models here.
class Ratings(models.Model): 
    raatings=[
        ('*', '*'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3')
    ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    student=models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating')
    subjects=models.CharField(max_length=50, choices=sub, default='python')
    communication=models.CharField(max_length=50, choices=raatings, default='1')
    technical=models.CharField(max_length=50, choices=raatings, default='1')
    programming=models.CharField(max_length=50, choices=raatings, default='1')
    remarks=models.CharField(max_length=200)
    conducted_by=models.ForeignKey(User, on_delete=models.CASCADE, related_name='by')
    conducted_on=models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.student.username

class scheduling(models.Model):
    
    def get_upload_path(self, filename):
        ext=filename.split('.')[-1]
        filename=f"Slot_{self.trainer.username}.{ext}"
        return os.path.join("Slots", filename)

    slot_id=models.IntegerField(primary_key=True)
    student=models.FileField(upload_to=get_upload_path,max_length=100, validators=[FileExtensionValidator(['csv'])])
    trainer=models.ForeignKey(User, on_delete=models.CASCADE, related_name='slots')
    subject=models.CharField(max_length=100, choices=sub)
    cource=models.CharField(max_length=100, choices=cources)
    date=models.DateField(auto_now=False, auto_now_add=False)
    time=models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.trainer.username}_{self.slot_id}"