from multiprocessing import context
from django.shortcuts import render

from house.models import Plot
# Create your views here.

def view_all_plots(request):
    try:
        plots = Plot.objects.all()

        context = { "plots": plots }
        return render(request, "house/all-plots.html", context)
    except Plot.DoesNotExist:
        context={ "plot": "Error Accessing Plot Infromtion"}
        return render(request, "house/all-plots.html", context)

def view_plot(request, id):
    try:
        plot = Plot.objects.get(pk=id)
        context = {"plot": plot}
        return render(request, "house/view-plot.html", context)
    except Plot.DoesNotExist:        
        context = {"plot": "Error Accessing Plot Information"}
        return render(request, "house/view-plot.html", context)

def view_all_houses(request):
    pass

def view_all_rooms(request):
    pass

def view_all_room_types(request):
    pass

def view_all_house_types(request):
    pass

def view_all_tenants(request):
    pass

def view_single_house(request):
    pass

def view_single_room(request):
    pass

def view_single_tenant(request):
    pass