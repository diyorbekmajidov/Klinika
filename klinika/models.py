from django.db import models

class Kilinikalar(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Bulimlar(models.Model):
    shifokor = models.CharField(max_length=100)
    xizmat = models.CharField(max_length=100)
    narxlar = models.CharField(max_length=100)

    def __str__(self):
        return self.shifokor
    
class Shifokorlar(models.Model):
    name = models.CharField(max_length=100)
    lavozim = models.CharField(max_length=100)
    qavat = models.IntegerField()
    info = models.TextField()
    ish_kunlari = models.CharField(max_length=100)
    ish_vaqt = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/')
    bulim = models.ForeignKey(Bulimlar, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

class Xizmatlar(models.Model):
    name =models.CharField(max_length=100)
    xizmat = models.ForeignKey(Bulimlar, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Navbatlar(models.Model):
    xizmat = models.ForeignKey(Xizmatlar, on_delete=models.CASCADE)
    shifokor = models.ForeignKey(Shifokorlar, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name
    
