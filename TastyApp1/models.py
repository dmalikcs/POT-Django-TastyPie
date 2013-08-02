from django.db import models
from django.contrib.auth.models import User
from django.db import models
from tastypie.models import create_api_key

models.signals.post_save.connect(create_api_key, sender=User)

class A1M1_information(models.Model):
    """
    This Models is created only for the tastypie setting
    """
    Fname=models.CharField(max_length=30,
            verbose_name="First name",
            )
    Lname=models.CharField(max_length=30,
            verbose_name="Last Name",
            )
    email=models.EmailField(
            verbose_name='email',
            )
    message=models.CharField(
            max_length=30,
            verbose_name="Message",
            )
    def __unicode__(self):
        return self.Fname

class A1M2_extainfo(models.Model):
    users_fk=models.ForeignKey(A1M1_information,
            verbose_name="User",
            )
    Fextra=models.CharField(max_length=70,
            verbose_name="F extra info",
            )
    Lextra=models.CharField(max_length=80,
            verbose_name="L Name",
            )
    def __unicode__(self):
        return self.users_fk.Fname


