from django.shortcuts import render
from django.http import HttpResponse


def index(self):
    return HttpResponse("<h2>HEY!</h2>")
