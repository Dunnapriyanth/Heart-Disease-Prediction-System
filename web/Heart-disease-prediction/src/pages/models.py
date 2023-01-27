from django.db import models
# Create your models here.
class userInfoModel(models.Model):
    user=models.CharField(max_length=100, unique=True)
    age=models.IntegerField()
    sex=models.CharField(max_length=200) # max_length = required
    cp=models.CharField(max_length=200)
    trestbps=models.IntegerField()
    chol=models.IntegerField()
    fbs=models.CharField(max_length=200)
    restecg=models.TextField()
    thalach=models.IntegerField()
    exang=models.CharField(max_length=200)
    oldpeak=models.IntegerField()
    slope=models.IntegerField()
    ca=models.IntegerField()
    thal=models.CharField(max_length=200)

# declare a new model with a name "GeeksModel"
# class userModel(models.Model):
#     # fields of the model
#     username = models.CharField(max_length=100, unique=True)
#     email = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)

