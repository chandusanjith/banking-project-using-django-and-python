from django.shortcuts import render
from datetime import datetime, date
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, login
from django.contrib import messages
from .models import mastercustomernumber, masteraccountnumber, cusm, invm, glif

def main(request):
  return render(request, 'main.html')

def signup(request):
  fname = request.POST['fname']
  sname = request.POST['sname']
  user = request.POST['user']
  pass1 = request.POST['pass1']
  pass2 = request.POST['pass2']
  emailaddress = request.POST['emailaddress']
  userexist = User.objects.filter(username = user)
  print(userexist)
  if pass1 != pass2:
    messages.info(request, 'Passwords not matching')
    return render(request, 'main.html')
  elif  User.objects.filter(username = user).exists():
    messages.info(request, 'User already exist')
    return render(request, 'main.html')
  else:
    user = User.objects.create_user(username = user, password = pass1, email = emailaddress, first_name = fname, last_name = sname )
    user.save()
    return render(request, 'main.html')
  

def login(request):
  id = request.POST['usernamelolgin']
  password = request.POST['passsed']

  user = auth.authenticate(username = id, password = password)
  
  if user is not None:
    auth.login(request, user)
    return HttpResponseRedirect('/index/')
  else:
    messages.info(request, 'Invalid login details')
    return render(request, 'main.html')


def index(request):
  if not request.user.is_authenticated:
        return render(request, 'main.html')
  else:
      user = request.user
      details = cusm.objects.filter(loginid = user)
      acdetails = invm.objects.filter(loginid = user)
      myDate = datetime.now()
      formatedDate = myDate.strftime("%Y-%m-%d %H:%M:%S")

      context={'details_cust' : details,
               'details_acct' : acdetails,
               'date': formatedDate}
      return render(request, 'index.html', context)


def createcust(request):
  user = request.user
  if not request.user.is_authenticated:
        return render(request, 'main.html')
  elif cusm.objects.filter(loginid = user).exists():
      messages.info(request,'Customer number already exist, try logging using new account ')
      return HttpResponseRedirect('/index/')
  else: 
      return render(request, 'createcusm.html')

def addcust(request):
  if not request.user.is_authenticated:
        return render(request, 'main.html')
  else:
    name420 = request.POST['fullname']
    email = request.POST['email']
    phone = request.POST['phone']
    nationality = request.POST['nationality']
    satate = request.POST['state']
    city = request.POST['city']
    occupancyname = request.POST['occupancy']
    dob = request.POST['dob']
    idtype = request.POST['idtype']
    idnumber = request.POST['idnumber']
    address = request.POST['address']
    user = request.user
    print(name420)
    print(phone)
    print(email)
    if cusm.objects.filter(loginid = user).exists():
      return HttpResponseRedirect('/index/')
    else:
       print("coming till here")
       a = mastercustomernumber.objects.filter(id = 1)
       custnumber = a[0].customernumber
       customernumbers = custnumber
       z = cusm(loginid = user, name = name420 , custnum = custnumber , email = email, phone = phone , nationality = nationality, state = satate, district = city , occupency = occupancyname, address = address, idtype = idtype , idnumber = idnumber )
       z.save()
       custnumber = int(custnumber)
       custnumber = custnumber + 1
       mastercustomernumber.objects.filter(id = 1).update(customernumber = custnumber )
       return HttpResponseRedirect('/index/')

def logout(request):
  django_logout(request)
  return render(request, 'main.html')



def opsavings(request):
  
  return render(request, 'opsavings.html')  


def fdload(request):
  return render(request, 'fdaccount.html')


def addfd(request):
  if not request.user.is_authenticated:
        return render(request, 'main.html')
  else:
    currency = request.POST['currency']
    opbal = request.POST['opbal']
    acname = request.POST['acname']
    intfreq = request.POST['intfreq']
    matdate = request.POST['matdate']
    nar = request.POST['nar']
    user = request.user
    a = masteraccountnumber.objects.filter(id = 1)
    accountnumber = a[0].accountnumber
    z = invm(loginid = user, custnum = accountnumber, acctype = 'FD', opendate = date.today(), status = '00', curency = currency, balance = opbal, accname = acname, intrest = '2', intfreq = intfreq, matdate = matdate, narration = nar  )
    z.save()
    accountnumber = int(accountnumber)
    accountnumber = accountnumber + 1
    accountnumber = str(accountnumber)
    masteraccountnumber.objects.filter(id = 1).update(accountnumber = accountnumber )
    return HttpResponseRedirect('/index/')

def addsb(request):
  if not request.user.is_authenticated:
        return render(request, 'main.html')
  else:
    currency = request.POST['currency']
    opbal = request.POST['opbal']
    acname = request.POST['acname']
    nar = request.POST['nar']
    user = request.user
    a = masteraccountnumber.objects.filter(id = 1)
    accountnumber = a[0].accountnumber
    z = invm(loginid = user, custnum = accountnumber, acctype = 'SB', opendate = date.today(), status = '00', curency = currency, balance = opbal, accname = acname, intrest = '2', narration = nar  )
    z.save()
    accountnumber = int(accountnumber)
    accountnumber = accountnumber + 1
    accountnumber = str(accountnumber)
    masteraccountnumber.objects.filter(id = 1).update(accountnumber = accountnumber )
    return HttpResponseRedirect('/index/')

def loadselftran(request):
  user = request.user
  acdetails = invm.objects.filter(loginid = user)
  print(acdetails)
  context={'accnum': acdetails}
  return render(request, 'selftran.html', context)


def selftran(request):
  if not request.user.is_authenticated:
        return render(request, 'main.html')
  else:
     fromaccount = request.POST['fracct']
     toaccount = request.POST['toacct']
     tranamt = request.POST['trbal']
     narr = request.POST['nar']
     if fromaccount == toaccount:
       messages.info(request,'From Account and TO Account Cannot be same ')
       return HttpResponseRedirect('/index/')
     else: 
          fa = invm.objects.filter(custnum = fromaccount )
          balance = fa[0].balance
          balance = int(balance)
          tranamt = int(tranamt)
          dbbal = balance - tranamt
          dbbal = str(dbbal)
          invm.objects.filter(custnum = fromaccount).update(balance = dbbal)
          piece1 = "transfer by self from"
          piece2 = " to " 
          sysnarr = piece1 + fromaccount + piece2 + toaccount
          glifentry = glif(accno = fromaccount, drcr = 'DR', balbefore = balance, balafter = dbbal, tranamt = tranamt, trandate =  date.today(), sysnarr = sysnarr,usernarr = narr  )
          glifentry.save()
          ta = invm.objects.filter(custnum = toaccount )
          tobalance = ta[0].balance
          tobalance = int(tobalance)
          tocrbal = tobalance + tranamt
          tocrbal = str(tocrbal)
          invm.objects.filter(custnum = toaccount).update(balance = tocrbal) 
          glifentry = glif(accno = toaccount, drcr = 'CR', balbefore = tobalance, balafter = tocrbal, tranamt = tranamt, trandate =  date.today(), sysnarr = sysnarr,usernarr = narr )
          glifentry.save()
          messages.info(request, sysnarr)
          return HttpResponseRedirect('/index/')

def loadtranother(request):
  user = request.user
  acdetails = invm.objects.filter(loginid = user)
  print(acdetails)
  context={'accnum': acdetails}
  return render(request, 'othertran.html', context)

def othertran(request):
   if not request.user.is_authenticated:
        return render(request, 'main.html')
   else:
     fromaccount = request.POST['fracct']
     toaccount = request.POST['toacct']
     tranamt = request.POST['trbal']
     narr = request.POST['nar']
     if fromaccount == toaccount:
       messages.info(request,'From Account and TO Account Cannot be same ')
       return HttpResponseRedirect('/index/')
     else: 
          fa = invm.objects.filter(custnum = fromaccount )
          ta = invm.objects.filter(custnum = toaccount )
          namecr = ta[0].loginid
          balance = fa[0].balance
          namedr = fa[0].loginid
          balance = int(balance)
          tranamt = int(tranamt)
          dbbal = balance - tranamt
          dbbal = str(dbbal)
          invm.objects.filter(custnum = fromaccount).update(balance = dbbal)
          piece1 = "transfer to "
          piece2 = " by " 
          sysnarr = piece1 + namecr + piece2 + namedr
          glifentry = glif(accno = fromaccount, drcr = 'DR', balbefore = balance, balafter = dbbal, tranamt = tranamt, trandate =  date.today(), sysnarr = sysnarr,usernarr = narr  )
          glifentry.save()          
          tobalance = ta[0].balance          
          tobalance = int(tobalance)
          tocrbal = tobalance + tranamt
          tocrbal = str(tocrbal)
          invm.objects.filter(custnum = toaccount).update(balance = tocrbal) 
          glifentry = glif(accno = toaccount, drcr = 'CR', balbefore = tobalance, balafter = tocrbal, tranamt = tranamt, trandate =  date.today(), sysnarr = sysnarr,usernarr = narr )
          glifentry.save()
          messages.info(request, sysnarr)
          return HttpResponseRedirect('/index/')

def loadpbac(request):
  user = request.user
  acdetails = invm.objects.filter(loginid = user)
  print(acdetails)
  context={'accnum': acdetails}
  return render(request, 'selectaccforpass.html', context)

def loadpassbook(request):
  acct = request.POST['acct']
  transactions = glif.objects.filter(accno = acct)
  context={'trandet': transactions}
  return render(request, 'passbook.html', context)