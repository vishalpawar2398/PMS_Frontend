from django.shortcuts import render
from .form import contactform
from django.http import HttpResponseRedirect
def con(r):
    form=contactform()
    if r.method=='POST':
        form=contactform(r.POST)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect('/')
    return render(r,'contactus/contactus.html',{'form':form})


def test(r):
    test = contactform()
    if r.method == 'POST':
        test = contactform(r.POST)
        if test.is_valid():
            test.save()
    return render(r,'contactus/test.html',{'test':test})
