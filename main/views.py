from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406432425',
        'name': 'Jarred Muhammad Radithya',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
# Create your views here.
