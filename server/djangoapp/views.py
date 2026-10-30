import json
import logging

from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .restapis import get_request
from .models import CarMake, CarModel

logger = logging.getLogger(__name__)


@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({
            "userName": username,
            "status": "Authenticated"
        })

    return JsonResponse({"userName": username})


def logout_request(request):
    logout(request)
    return JsonResponse({"userName": ""})


def get_dealer_reviews(request, dealer_id):
    try:
        reviews = get_request(f'fetchReviews/dealer/{dealer_id}')
        return JsonResponse(reviews, safe=False)
    except Exception as error:
        logger.error("Error fetching dealer reviews: %s", error)
        return JsonResponse(
            {"error": "Unable to fetch dealer reviews"},
            status=500
        )


def get_car_makes(request):
    makes = CarMake.objects.all()
    data = [
        {
            "id": make.id,
            "name": make.name,
            "description": make.description
        }
        for make in makes
    ]
    return JsonResponse(data, safe=False)


def get_car_models(request, make_id):
    models = CarModel.objects.filter(make_id=make_id)
    data = [
        {
            "id": model.id,
            "name": model.name,
            "car_type": model.car_type,
            "year": model.year,
            "make_id": model.make_id
        }
        for model in models
    ]
    return JsonResponse(data, safe=False)