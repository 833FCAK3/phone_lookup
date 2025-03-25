import json

import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
def index(request) -> HttpResponse:
    return render(request, "index.html")


def search_phone(request) -> JsonResponse:
    print(type(request))
    if request.method == "GET":
        phone_number = request.GET.get("num")
        if not phone_number:
            return JsonResponse({"error": "No phone number provided"}, status=400)
        phone_number = edit_number(phone_number)

        url = f"https://opendata.digital.gov.ru/api/v1/abcdef/phone?num={phone_number}"

        headers = {
            "User-Agent": "Mozilla/5.0",
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad status codes
            data = {
                "phone_number": phone_number,
                "operator": json.loads(response.content)["data"][0]["operator"],
                "region": json.loads(response.content)["data"][0]["region_gar"],
            }
            return JsonResponse(data, json_dumps_params={"ensure_ascii": False})
        except requests.exceptions.RequestException as e:
            return JsonResponse({"error": f"Failed to fetch data: {str(e)}"}, status=500)

    return JsonResponse({"error": "Unsupported request method"}, status=405)


def edit_number(number: str) -> str:
    if len(number) == 10:
        number = "7" + number
    return number
