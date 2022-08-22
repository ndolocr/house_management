from django.shortcuts import render

# Create your views here.

def index(request):
    tenants = {
        {"name":"Ginora Kalama", "id": 123456, "tel": "0721345678" },
        {"name":"Godi Mwakasungu", "id": 123456, "tel": "0721345678" },
        {"name":"Florence Akinyi Atieno", "id": 123456, "tel": "0721345678" },
        {"name":"Jackson Zaule", "id": 123456, "tel": "0721345678" },
        {"name":"Martin Ntongoi", "id": 123456, "tel": "0721345678" },

    }

    context = { "tenants": tenants}
    return render(request, "dashboard/index.html", context)