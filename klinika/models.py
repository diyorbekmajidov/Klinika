from django.db import models

class Kilinikalar(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

    
class Xizmatlar(models.Model):
    name = models.CharField(max_length=100)
    bulim = models.ForeignKey(Kilinikalar, on_delete=models.CASCADE, related_name='xizmatlar')

    def __str__(self):
        return self.name
    
class Narxlar(models.Model):
    xizmat = models.ForeignKey(Xizmatlar, on_delete=models.CASCADE, related_name='narxlar')
    narx = models.IntegerField()
    
    def __str__(self):
        return self.narx
    
class Shifokorlar(models.Model):
    name = models.CharField(max_length=100)
    qavat = models.IntegerField()
    info = models.TextField()
    ish_kunlari = models.CharField(max_length=100)
    ish_vaqt = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/', default="")
    xizmatlar = models.OneToOneField(Xizmatlar, on_delete=models.CASCADE, related_name='shifokorlar')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    




class Navbatlar(models.Model):
    xizmat = models.ForeignKey(Xizmatlar, on_delete=models.CASCADE)
    shifokor = models.ForeignKey(Shifokorlar, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name
    
