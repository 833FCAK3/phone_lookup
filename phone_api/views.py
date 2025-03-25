import requests
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")


def search_phone(request):
    phone_number = request.GET.get("num")
    if not phone_number:
        return JsonResponse({"error": "No phone number provided"}, status=400)

    url = f"https://opendata.digital.gov.ru/api/v1/abcdef/phone?num={phone_number}"

    headers = {
        "User-Agent": "Mozilla/5.0",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": f"Failed to fetch data ({response.status_code})"}, status=response.status_code)
