from django.http.response import HttpResponse
from django.shortcuts import render
from .models import House, Images
# from .forms import HouseForm, ImageForm
# Create your views here.


def index(request):
    return render (request, 'index.html')


def add_house(request):
    # h_form = HouseForm(request.POST)
    # i_form = ImageForm(request.FILES)
    # TODO form validation
    if request.method == 'POST':
        title = request.POST['title']
        location = request.POST['location']
        price = request.POST['price']
        rooms = request.POST['rooms']
        parking = request.POST['parking']
        typer = request.POST['type']
        images = request.FILES.getlist('image')
        house = House.objects.create(title=title, location=location, price=price, rooms=rooms, parking=parking, typer=typer)
        for image in images:
            print('Image Added')
            Images.objects.create(image=image, house=house)
        return render(request, HttpResponse("<span class='HttpResponse notification'>Successfully Added House</span>"))
    return render(request, 'add_house.html')


"""
def save_pic(request):
    house = House(field=[content])
    house.save()
    Images.objects.create(image=[content from browser], house=house)
"""