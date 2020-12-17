from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from office.models import EngineerStatus
from django.core.files.storage import FileSystemStorage
from django.core import serializers
from office.models import RequestWorkOfEngineer

def check_email(request):
    if request.method == 'POST' and request.is_ajax:
        email = request.POST.get('email')
        user_obj = User.objects.get(email=email)
        if user_obj.pk:
            return JsonResponse(
                {"status": 1, "user_name": user_obj.first_name, "user_id": user_obj.pk, "user_type": user_obj.user_type,
                 "email": user_obj.email})
        else:
            return JsonResponse({"status": 0})


def loginPage(request):
    if request.method == 'POST' and request.is_ajax:
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            if user.user_type == 2:
                login(request, user)
                return JsonResponse({"status": 'done', "user_pk": user.pk})
            else:
                login(request, user)
                return JsonResponse({"status": 'done', "user_pk": user.pk})


        else:
            return JsonResponse({"status": 'Username OR password is incorrect'})

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def home_engineer(request):
    return render(request, 'accounts/home-engineer.html')


def registerEngineer(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        picture = request.FILES['picture']
        fs = FileSystemStorage()
        fs.save(picture.name, picture)
        user = User.objects.create_engineeruser(email=email, first_name=first_name, last_name=last_name,
                                                address=address, password=password, phone=phone, profile_pic=picture
                                                )
        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            messages.add_message(request, messages.error, 'Please Review Your Data Failed To Register')
    context = {}
    return render(request, 'accounts/register-outdoor.html', context)


def register_customer(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        picture = request.FILES['picture']
        fs = FileSystemStorage()
        fs.save(picture.name, picture)
        user = User.objects.create_customeruser(email=email, first_name=first_name, last_name=last_name,
                                                address=address,profile_pic=picture, password=password, phone=phone)
        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            messages.add_message(request, messages.error, 'Please Review Your Data Failed To Register')
    context = {}
    return render(request, 'accounts/register_customer.html', context)


def register_outdoorEngineer(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        picture = request.FILES['picture']
        fs = FileSystemStorage()
        fs.save(picture.name, picture)
        user = User.objects.create_outdoor_engineeruser(email=email,profile_pic=picture, first_name=first_name, last_name=last_name,
                                                        address=address, password=password, phone=phone)
        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            messages.add_message(request, messages.error, 'Please Review Your Data Failed To Register')
    context = {}
    return render(request, 'accounts/register-engineer.html', context)


def user_detail(request):
    return render(request, 'accounts/user-detail.html')


def change_status(request, pk):
    engineer = User.objects.get(pk=pk)
    if request.method == 'GET':
        status = EngineerStatus.objects.filter(engineer=engineer).exists()
        if status:
            perv_status = EngineerStatus.objects.get(engineer=engineer)
            return render(request, 'accounts/change-status.html', context={"status": perv_status.status})
        else:
            return render(request, 'accounts/change-status.html', context={"status": 0})

    elif request.method == 'POST' and request.is_ajax:
        status_var = request.POST.get('status')
        st = EngineerStatus.objects.filter(engineer=engineer).exists()
        if st:
            st_obj = EngineerStatus.objects.get(engineer=engineer)
            st_obj.status = status_var
            st_obj.save()
            return JsonResponse({"data": 1})

        else:
            obj = EngineerStatus(status=status_var, engineer=engineer)
            obj.save()
            if obj.pk:
                return JsonResponse({"data": 1})
            else:
                return JsonResponse({"data": -1})


def engineer_detail(request,pk):
    eng= User.objects.get(pk=pk)
    context = {"engineer":eng}
    return render(request , 'accounts/engineer-detail.html',context=context)


def emp_info(request):
    if request.method=='GET' and request.is_ajax:
        emp_obj = User.objects.get(pk =request.user.pk)
        emp_data = User.objects.filter(pk=request.user.pk)
        emp_json =  serializers.serialize('json', emp_data)
        requests = RequestWorkOfEngineer.objects.filter(engineer=emp_obj)
        request_json =  serializers.serialize('json', requests)
        return JsonResponse({"employee": emp_json , "requests":request_json , "request_count":requests.count()}, content_type='application/json')

