from django.db import models

# Create your models here.
class Question(models.Model):
    questions_text=models.CharField( max_length=200)
    pub_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.questions_text
    
class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name="choices") # Question-The model this choice belongs to
    choice_text=models.CharField(max_length=100                                           )#on_delete What happens if the question is deleted
    votes=models.IntegerField(default=0)                                                     # related_name-Name to access all choices from a question

    
    def __str__(self):
        return self.choice_text