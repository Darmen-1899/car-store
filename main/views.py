from django.http import Http404
from django.shortcuts import render

from main.models import Car


def index(request):
    cars_list = Car.objects.order_by('engine_volume')
    return render(request, 'main/index.html', {'cars_list': cars_list})


def car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except:
        raise Http404("Статья не найдена")

    images = car.images.order_by('id')
    return render(request, 'main/car.html', {'car': car, 'images': images})


def search(request):
    search_by_fuel = str(request.POST['fuel'])
    search_by_body = str(request.POST['body_car'])
    search_by_unit = request.POST['drive_unit']

    my_car = Car.objects.filter(body=search_by_body, fuel=search_by_fuel, drive_unit=search_by_unit).order_by("-id")
    return render(request, 'main/searched.html', {'my_car': my_car})

