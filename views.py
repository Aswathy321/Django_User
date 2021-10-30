from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import loader
from .models import primary
from rest_framework.decorators import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from django.http import JsonResponse


def page_1(req):
    temp=loader.get_template('login.html')
    data={}
    res=temp.render(data,req)
    return HttpResponse(res)

def page_2(req):
    temp=loader.get_template('signup.html')
    objects=primary.objects.all()
    data={'signup':objects}
    res=temp.render(data,req)
    return HttpResponse(res)

def page_3(req):
    temp = loader.get_template('userdetail.html')
    data = {}
    res = temp.render(data, req)
    return HttpResponse(res)
    '''
    print(req.GET)  # to get all details in a dictionary
    print(req.GET['name'])  # instead of getting details seprately
    print(req.GET['email'])
    print(req.GET['address'])

    user = primary(name=req.GET['name'], email=req.GET['email'],
                  password=req.GET['address'])
    user.save()
    return HttpResponse('Received')
'''
'''
    name=req.GET['name']
    email=req.GET['email']
    address=req.GET['address']
    print(req.headers['User-Agent'])
   
    p=primary(name=req.GET["name"],email=req.GET["email"],
              address=req.GET["address"])
    p.save()
    
    storage={}
    req.session.set_expiry(300)
    if req.session.__contains__('userdetail'):
        storage=req.session['userdetail']
    storage[name]=email
    req.session['userdetail']=storage
    print(req.session['userdetail'])
    return HttpResponse("Data saved to server !")

'''
'''
class userid(APIView):
    def get(self,req,key):
        try:
            pro=primary.objects.get(id=key)
            serializer=UserSerializer(pro)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response('Invalid Id')
    def put(self,req,key):
        print(key)
        pro=primary.objects.get(id=key)
        seializer=UserSerializer(pro,req.data)
        if seializer.is_valid():
            seializer.save()
            return Response(seializer.data)
        else:
            return Response('Data Updated Successfully')
    def delete(self,req,key):
        pro=primary.objects.get(id=key)
        pro.delete()
        return Response('id deleted ')
class userview(APIView):
    def get(self,req):
        pro=primary.objects.all()
        print(pro)
        serializer=UserSerializer(pro,many=True)
        return Response(serializer.data)
    def post(self,req):
        print(req.data)
        serializer=UserSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Invalid') 
'''