from django.shortcuts import render

def front(r):
    return render(r,'base.html')


def new(r):
    return render(r,'base1.html')
