from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class todo (models.Model) :
    peserta     = models.ForeignKey(User, on_delete=models.CASCADE, null= True )
    kegiatan    = models.CharField(max_length=225)
    is_done     = models.BooleanField(default=False)
    waktu       = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return "{} - {}".format(self.peserta, self.kegiatan)

