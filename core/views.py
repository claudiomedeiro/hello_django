from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos<h1>'.format(nome, idade))

def soma(request, numero1, numero2):
    return HttpResponse('<h1>A soma de {} + {} é {}<h1>'.format(numero1, numero2, numero1 + numero2))
