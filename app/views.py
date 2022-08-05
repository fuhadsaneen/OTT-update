from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import EditForm

# Create your views here.
from . models import Movies


def hello(request):
    res = Movies.objects.all()
    return render(request, "index.html", {'key': res})


def detail(request, movies_id):
    res1 = Movies.objects.get(id=movies_id)
    return render(request, "details.html", {'key1': res1})


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name', )
        year = request.POST.get('year', )
        des = request.POST.get('des', )
        img = request.FILES['img']
        movie = Movies(name=name, year=year, des=des, img=img)
        movie.save()

    return render(request, 'add.html')


def update(request, id):
    mov = Movies.objects.get(id=id)
    form = EditForm(request.POST or None, request.FILES, instance=mov)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'edit.html', {'mov': mov, 'form': form})


def delete(request, id):
    if request.method == 'POST':
        movie = Movies.objects.get(id=id)
        movie.delete()
        return redirect('/')

    return render(request, 'delete.html')
