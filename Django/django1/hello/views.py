from typing import Any
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
# Create your views here.

def index(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path = request.path
    return HttpResponse(f"""
        <h1>Main Page</h1>
        <p>Host: {host}</p>
        <p>Path: {path}</p>
        <p>User-agent: {user_agent}</p>
    """)

def products(request):
    return HttpResponse('Goods list')

def new(request):
    return HttpResponse('New')

def top(request):
    return HttpResponse('Top')

def product_id(request, id):
    return HttpResponse(f'Product: {id}')

def comment_id(request, id):
    return HttpResponse(f'Comment: {id}')

def question_id(request, id):
    return HttpResponse(f'Question: {id}')


def index2(request):
    return HttpResponse("Произошла ошибка", status=400, reason="Incorrect data")

def user(request, name="Ud", age=-1):
    if name == "Ud":
        name = request.GET.get("name", "Ud")
    if age == -1:
        age = request.GET.get('age', -1)
    return HttpResponse(f"<h2>Name: {name}\nAge: {age}</h2>")
 
def about(request, name, age):
    return HttpResponse(f"""
                        <h2>About user</h2>
                        <p>Name: {name}</p>
                        <p>Age: {age}</p>
                        """)
 
def contact(request):
    return HttpResponseRedirect('/about/')

def details(request):
    return HttpResponsePermanentRedirect('/')

def index3(request, id):
    people = ['Kek', 'Memes', 'Bob']

    if id in range(0, len(people)):
        return HttpResponse(people[id])
    return HttpResponseNotFound("Not found")

def access(request, age):
    if age not in range(1, 111):
        return HttpResponseBadRequest("Data is not correct")
    
    if age > 17:
        return HttpResponse("Access permitted")
    
    return HttpResponseForbidden("Access denied")

def index4(request):
    bob = Person('Bob', 34)
    return JsonResponse(bob, safe=False, encoder=PersonEncoder)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class PersonEncoder(DjangoJSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, Person):
            return {'name' : o.name, 'age' : o.age}
        return super().default(o)


def set(request):
    username = request.GET.get('username', 'Ud')
    response = HttpResponse(f'Hello set {username}')
    response.set_cookie('username', username)
    return response

def get(request):
    username = request.COOKIES['username']
    return HttpResponse(f'Hello get {username}')

def index5(request, name="Ud", age=-1):
    data = {"person" : Person(name, age)}
    return render(request, "index.html", context=data)