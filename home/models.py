from django.db import models

# Create your models here.
class Book(models.Model):
    nomi=models.CharField(max_length=200)
    muallif=models.ForeignKey('Autor',on_delete=models.CASCADE)
    nashriyot=models.ForeignKey('Nashriyot',on_delete=models.CASCADE)
    turi=models.ForeignKey('Turi',on_delete=models.CASCADE)
    yil=models.DateField()
    beti=models.IntegerField()
    holat=models.BooleanField()
    udk=models.IntegerField()
    def __str__(self) -> str:
        return self.nomi


class Autor(models.Model):
    nomi=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.nomi
    
class Nashriyot(models.Model):
    nomi=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.nomi  
     
class Turi(models.Model):
    nomi=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.nomi       

class Jarayon(models.Model):
    book=models.ForeignKey('Book',on_delete=models.CASCADE)
    user=models.ForeignKey('People',on_delete=models.CASCADE)
    olgan_vaqt=models.DateTimeField()
    bergan_vaqt=models.DateTimeField()
    def __str__(self) -> str:
        return self.book.nomi  

class People(models.Model):
    nomi=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.nomi  
