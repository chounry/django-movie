from django.http import HttpResponse
from django.shortcuts import render
from home.models import Movie

# Create your views here.
def add_rate(request):
    movie_id = request.GET.get('movie_id')
    rate = request.GET.get('rate')
    print(movie_id,rate)

    try:
        movie_id = int(movie_id)
        rate = int(rate)
    except:
        return HttpResponse('ok')

    try:
        movie_obj = Movie.objects.get(id=movie_id)
    except:
        return HttpResponse('ok')

    if(rate >= 1 and rate <= 10):
        old_rate = movie_obj.rate_aver
        number_rater = movie_obj.number_rater
        reverse = old_rate * number_rater
        new_rate = format((reverse + rate) / (number_rater + 1), '.1f')

        # update data base
        movie_obj.rate_aver = new_rate
        movie_obj.number_rater += 1 # increament rater
        movie_obj.save()
        return HttpResponse(new_rate)

    return HttpResponse('ok')
