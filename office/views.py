from django.shortcuts import render
from .models import EngineerStatus, RequestWorkOfCustomer, RequestWorkOfEngineer, Work, Reply, BestEngineer, \
    EngineerInformation
from accounts.models import User
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage


def engineer_online_list(request):
    context = {"engineers": EngineerStatus.objects.filter(status=1)}
    return render(request, 'office/engineer-list.html', context=context)


def request_work_engineer(request, pk):
    engineer = User.objects.get(pk=pk)
    cus_obj = User.objects.get(pk=request.user.pk)
    if request.method == 'GET':
        return render(request, 'office/request-work-engineer.html', context={"engineer": engineer})
    elif request.method == 'POST' and request.is_ajax:
        req = request.POST.get('request')
        service = request.POST.get('service')
        req_obj_eng = RequestWorkOfEngineer(customer_email=cus_obj.email, service=int(service), request=req,
                                            engineer=engineer)
        req_obj_cus = RequestWorkOfCustomer(engineer_email=engineer.email, service=int(service), request=req,
                                            customer=cus_obj)
        req_obj_eng.save()
        req_obj_cus.save()
        if req_obj_eng.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


def request_list_engineer(request):
    eng = User.objects.get(pk=request.user.pk)
    requests = RequestWorkOfEngineer.objects.filter(engineer=eng)
    return render(request, 'office/request-engineer-work-list.html', context={"requests": requests})


def request_work_customer(request):
    customer = User.objects.get(pk=request.user.pk)
    reqs = RequestWorkOfCustomer.objects.filter(customer=customer)
    return render(request, 'office/request-work-customer.html', context={"requests": reqs})


def send_to_customer(request, email):
    customer = User.objects.get(email=email)
    engineer = User.objects.get(pk=request.user.pk)
    if request.method == 'GET':
        return render(request, 'office/send-to-customer.html', context={"customer": customer})
    elif request.method == 'POST' and request.is_ajax:
        message = request.POST.get('message')
        reply_obj = Reply(sender=engineer, receiver=customer, reply_message=message)
        reply_obj.save()
        if reply_obj.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


def customer_messages_list(request):
    cus = User.objects.get(pk=request.user.pk)
    messages = Reply.objects.filter(receiver=cus)
    return render(request, 'office/customer-message-inbox.html', context={"messages": messages})


def send_to_engineer(request, email):
    eng = User.objects.get(email=email)
    cus = User.objects.get(pk=request.user.pk)
    if request.method == 'GET':
        return render(request, 'office/send-to-engineer.html', context={"engineer": eng})
    elif request.method == 'POST' and request.is_ajax:
        message = request.POST.get('message')
        reply_obj = Reply(receiver=eng, sender=cus, reply_message=message)
        reply_obj.save()
        if reply_obj.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


def engineer_messgae_list(request):
    eng = User.objects.get(pk=request.user.pk)
    messages = Reply.objects.filter(receiver=eng)
    return render(request, 'office/engineer-message-inbox.html', context={"messages": messages})


def best_engineer(request):
    if request.method == 'GET':
        engineers = User.objects.filter(user_type=2)
        admins = User.objects.filter(user_type=1)
        outdoors = User.objects.filter(user_type=4)
        return render(request, 'office/add-engineer-month.html',
                      context={"engineers": engineers, "outdoors": outdoors, "admins": admins})
    elif request.method == 'POST' and request.is_ajax:
        month = request.POST.get('month')
        outdoors = request.POST.getlist('outdoors[]')
        engineers = request.POST.getlist('engineers[]')
        best = BestEngineer(month=int(month))
        best.save()
        for eng in engineers:
            eng_obj = User.objects.get(pk=eng)
            best.engineer.add(eng_obj)
        for out in outdoors:
            out_obj = User.objects.get(pk=out)
            best.engineer.add(out_obj)
        if best.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


def add_info(request):
    if request.method == 'GET':
        return render(request, 'office/add-info.html')
    elif request.method == 'POST':
        cv = request.FILES['cv']
        fs = FileSystemStorage()
        fs.save(cv.name, cv)
        cer = request.FILES['cer']
        fs.save(cer.name, cer)
        detail = request.POST.get('detail')
        min_pay = request.POST.get('min_pay')
        max_pay = request.POST.get('max_pay')
        engineer = User.objects.get(pk=request.user.pk)
        info_obj = EngineerInformation(engineer=engineer, cv=cv, detail=detail, certificate=cer, min_pay=min_pay,
                                       max_pay=max_pay)
        info_obj.save()
