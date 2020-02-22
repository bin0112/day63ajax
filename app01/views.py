from django.shortcuts import render,HttpResponse

# Create your views here.

from app01.models import UserInfo
import json


def index(request):



    return render(request,'index.html')


def handle_ajax(request):

    print(request.body)  # 传输过来的是字节，需要解码
    print(request.POST)
    '''
    
    Django解析：
    
        if contentType: 'urlencoded':
        
            request.Post = data
            
        else:
            
            request.POST = {}
    
    
    
    '''

    import json
    json_dict = json.loads(request.body.decode('utf8'))   # key3
    print(json_dict['num1'])

    return HttpResponse('OK')


def cal(request):
    # import time
    # time.sleep(5)
    # print(request.GET)
    # num1 = request.GET.get('num1')
    # num2 = request.GET.get('num2')
    num1 = request.POST.get('num1')
    num2 = request.POST.get('num2')


    ret = int(num1) + int(num2)

    return HttpResponse(str(ret))


def login(request):

    if request.method=='POST':

        res = {'user':None,'error':''}
        print(request.POST)
        user=request.POST.get('user')
        pwd=request.POST.get('pwd')
        use_obj = UserInfo.objects.filter(user=user,pwd=pwd).first()
        if use_obj:

            res['user']=user

        else:
            res['error']='账号或密码错误'
        return HttpResponse(json.dumps(res))
    else:
        return render(request,'login.html')



def name(request):

    return HttpResponse("OK")


import os
from day63ajax import settings

def file_put(request):

    print(request.POST)
    print(request.FILES)
    file_obj = request.FILES.get("file_obj")

    print(file_obj.name)
    path = file_obj.name

    path=os.path.join(settings.BASE_DIR,"media","image",path)

    with open(path,"wb") as f:
        for line in file_obj:
            f.write(line)

    return HttpResponse('OK')