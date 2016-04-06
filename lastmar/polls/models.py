from django.db import models

class mcsv(models.Model):
    col1 = models.CharField(max_length=200)
    col2 = models.CharField(max_length=200)
    col3 = models.CharField(max_length=200)
    
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
   
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     c1 = models.CharField(max_length=200)
#     c2 = models.CharField(max_length=200)
#     c3 = models.CharField(max_length=200)
#     sub = models.BooleanField(default = False)

