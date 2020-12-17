from django.shortcuts import render
from .models import Contact
from django.http import JsonResponse


def home_page(request):
    return render(request, 'main/home_page.html')


def contact_ajax(request):
    if request.method == 'POST' and request.is_ajax:
        name = request.POST.get('name')
        message = request.POST.get('message')
        email = request.POST.get('email')
        address = request.POST.get('address')
        contact_obj = Contact(name=name, address=address, email=email, message=message)
        contact_obj.save()
        if contact_obj.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


def faq_questions(request):
    return render(request, 'main/faq-questions.html')


def contact_page(request):
    return render(request,'main/contact-page.html')