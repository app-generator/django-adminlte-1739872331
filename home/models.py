# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Skrivere(models.Model):

    #__Skrivere_FIELDS__
    navn = models.TextField(max_length=255, null=True, blank=True)
    lokasjon = models.TextField(max_length=255, null=True, blank=True)
    ip adresse = models.TextField(max_length=255, null=True, blank=True)
    brukernavn = models.TextField(max_length=255, null=True, blank=True)
    passsord = models.TextField(max_length=255, null=True, blank=True)
    moddel = models.TextField(max_length=255, null=True, blank=True)

    #__Skrivere_FIELDS__END

    class Meta:
        verbose_name        = _("Skrivere")
        verbose_name_plural = _("Skrivere")


class Pc(models.Model):

    #__Pc_FIELDS__
    hovedbruker = models.TextField(max_length=255, null=True, blank=True)
    merke = models.TextField(max_length=255, null=True, blank=True)
    modell = models.TextField(max_length=255, null=True, blank=True)
    ram (gb) = models.TextField(max_length=255, null=True, blank=True)
    cpu = models.TextField(max_length=255, null=True, blank=True)
    gpu = models.TextField(max_length=255, null=True, blank=True)

    #__Pc_FIELDS__END

    class Meta:
        verbose_name        = _("Pc")
        verbose_name_plural = _("Pc")



#__MODELS__END
