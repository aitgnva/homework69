from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import json



def index(request):
    return render(request, 'index.html')

def add_view(request):
    request_data = json.loads(request.body)
    num_a, num_b = request_data.values()
    try:
        a = float(num_a)
        b = float(num_b)
        answer = a + b
        return JsonResponse({'answer': answer})
    except:
        return JsonResponse({"error": "Not number"}, status=400)

def subtract_view(request):
    request_data = json.loads(request.body)
    num_a, num_b = request_data.values()
    try:
        a = float(num_a)
        b = float(num_b)
        answer = a - b
        return JsonResponse({'answer': answer})
    except:
        return JsonResponse({"error": "Not number"}, status=400)


def divide_view(request):
    request_data = json.loads(request.body)
    num_a, num_b = request_data.values()

    try:
        a = float(num_a)
        b = float(num_b)
        if b == 0:
            return JsonResponse({"error": "Division by zero!"}, status=400)
        else:
            answer = a / b
            return JsonResponse({'answer': answer})
    except:
        return JsonResponse({"error": "Not number"}, status=400)



def multiply_view(request, *args, **kwargs):
    request_data = json.loads(request.body)
    num_a, num_b = request_data.values()
    try:
        a = float(num_a)
        b = float(num_b)
        answer = a * b
        return JsonResponse({'answer': answer})
    except:
        return JsonResponse({"error": "Not number"}, status=400)


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])





