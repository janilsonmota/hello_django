from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome} de {idade} anos. </h1>')


def soma(request, num, number):
    return HttpResponse(f'{num} + {number} = {num+number}')


def subtracao(request, num, number):
    return HttpResponse(f'{num} - {number} = {num-number}')


def multiplicacao(request, num, number):
    return HttpResponse(f'{num} * {number} = {num*number}')


def divisao(request, num, number):
    return HttpResponse(f'{num} / {number} = {num/number}')


def mod(request, num, number):
    return HttpResponse(f'{num} % {number} = {num%number}')


def expoente(request, num, number):
    return HttpResponse(f'{num} ** {number} = {num**number}')
