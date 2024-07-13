from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from cars.models import Car
from cars.forms import CarModelForm


def cars_view(request: HttpRequest) -> HttpResponse:
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')
    if search:
        cars = cars.filter(model__icontains=search)

    return render(
        request,
        'cars.html',
        {'cars': cars}
    )


def new_car_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if (new_car_form.is_valid()):
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarModelForm()

    return render(request, 'new_car.html', {'new_car_form': new_car_form})
