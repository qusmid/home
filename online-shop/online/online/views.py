from django.shortcuts import render


def main(request):
    return render(request, 'mainpage.html')


def contacts(request):
    return render(request, 'contacts.html')


def faq(request):
    return render(request, 'faq.html')


def models(request):
    return render(request, 'models.html')


def service(request):
    return render(request, 'service.html')
