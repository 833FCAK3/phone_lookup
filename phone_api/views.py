import json
from functools import lru_cache

import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import PhonesLookedUp


# Create your views here.
def index(request) -> HttpResponse:
    return render(request, "index.html")


@lru_cache
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
            operator = json.loads(response.content)["data"][0]["operator"]
            region = json.loads(response.content)["data"][0]["region_gar"]

            data = {
                "phone_number": phone_number,
                "operator": operator,
                "region": region,
            }

            new_phone = PhonesLookedUp.objects.create(
                phone_number=phone_number,
                operator=operator,
                region=region,
            )
            new_phone.save()

            return JsonResponse(data, json_dumps_params={"ensure_ascii": False})
        except requests.exceptions.RequestException as e:
            return JsonResponse({"error": f"Failed to fetch data: {str(e)}"}, status=500)

    return JsonResponse({"error": "Unsupported request method"}, status=405)


def edit_number(number: str) -> str:
    if len(number) == 10:
        number = "7" + number
    return number
