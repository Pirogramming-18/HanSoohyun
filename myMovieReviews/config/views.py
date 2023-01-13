from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    html = "<html><body>링크뒤에 /review 를 붙이세요</body></html>"
    return HttpResponse(html)

def template_test(request):
    return render(request, 'test.html')