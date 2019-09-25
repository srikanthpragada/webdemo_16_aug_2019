from django.http import HttpResponse


def welcome(request):
    if 'name' in request.GET:
        name = request.GET['name']
    else:
        name = "Guest"

    return HttpResponse(f"<h1 style='color:blue'>{name}, Welcome To Django!</h1>")
