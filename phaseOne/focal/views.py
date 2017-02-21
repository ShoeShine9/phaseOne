from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.


def hello(request):

    today = datetime.datetime.now().date()

    return render(request, "test.html", {"date": today})


def photo(request, num):

    resp = "<h> showing photo number: {}".format(num)

    return HttpResponse(resp)


def django(request):

    return render(request, "bootstrapDemo.html")
