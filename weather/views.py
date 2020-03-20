from django.shortcuts import render

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=fe475d5fe5289a24973a57d3bd80a575'
    return render(request, 'weather/weather.html')
