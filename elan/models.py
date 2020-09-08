from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class elan(models.Model):
    cixis_yeri = models.CharField(max_length=150)
    catma_yeri = models.CharField(max_length=150)
    cixis_vaxti = models.DateField()
    catma_vaxti = models.DateField()
    elaqe_nomresi = models.IntegerField()
    sirket = models.CharField(max_length=100,blank=True,null=True)
    elave_melumatlar = models.TextField(null=True,blank=True)
    silinme_vaxti = models.DateTimeField()
    user = models.ForeignKey('auth.User',verbose_name='paylasan',on_delete=models.CASCADE)
    favorit = models.ManyToManyField(User,blank=True,related_name="favorit")

    def __str__(self):
        return self.cixis_yeri


    class Meta:
        ordering = ['-id']

