"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite.views import main, signup,login, index, createcust, addcust, logout, opsavings, fdload, addfd, addsb,loadselftran, selftran, loadtranother, othertran, loadpassbook, loadpbac, loaddepwith, depdraw, custdet, accdet, developer, html_to_pdf_view

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('main/', main),
    path('signup/', signup),
    path('login/', login),
    path('index/', index),
    path('createcust/', createcust),
    path('addcust/', addcust),
    path('logout/', logout),
    path('saving/', opsavings),
    path('fd/', fdload),
    path('addfd/', addfd),
    path('addsb/', addsb),
    path('tranself/', loadselftran),
    path('selftran/', selftran ),
    path('tranother/', loadtranother),
    path('othertran/', othertran),
    path('pass/', loadpbac),
    path('checkpb/', loadpassbook),
    path('depwith/', loaddepwith),
    path('dradepmoney/', depdraw),
    path('cusdet/', custdet),
    path('accdet/', accdet),
    path('developer/', developer),
    path('printcustpdf/', html_to_pdf_view)

]