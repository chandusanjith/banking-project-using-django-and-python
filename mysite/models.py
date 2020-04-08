from django.db import models

class mastercustomernumber(models.Model):
  customernumber = models.CharField(max_length=16)

class masteraccountnumber(models.Model):
  accountnumber = models.CharField(max_length=16)

class cusm(models.Model):
   loginid =  models.CharField(max_length=16)
   name = models.CharField(max_length=30)
   custnum = models.CharField(max_length=16)
   email = models.CharField(max_length=16)
   phone = models.CharField(max_length=10)
   nationality = models.CharField(max_length=10)
   state = models.CharField(max_length=10)
   district = models.CharField(max_length=10)
   occupency = models.CharField(max_length=20)
   address =  models.CharField(max_length=100)
   idtype =  models.CharField(max_length=2)
   idnumber =  models.CharField(max_length=10)

class invm(models.Model):
   loginid = models.CharField(max_length=16)
   custnum = models.CharField(max_length=16)
   acctype =  models.CharField(max_length=2)
   opendate = models.CharField(max_length=15)
   status = models.CharField(max_length=2)
   curency = models.CharField(max_length=3)
   balance = models.CharField(max_length=17)
   accname = models.CharField(max_length=50)
   intrest = models.CharField(max_length=3)
   intfreq = models.CharField(max_length=5)
   matdate = models.CharField(max_length=15)
   narration = models.CharField(max_length=50)

class glif(models.Model):
  accno = models.CharField(max_length=16)
  drcr = models.CharField(max_length=2)
  balbefore = models.CharField(max_length=17)
  balafter = models.CharField(max_length=17)
  tranamt = models.CharField(max_length=17)
  trandate = models.CharField(max_length=15)
  sysnarr = models.CharField(max_length=50)
  usernarr = models.CharField(max_length=50)

