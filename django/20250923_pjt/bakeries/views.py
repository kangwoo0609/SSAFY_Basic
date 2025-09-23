from django.shortcuts import render
from .models import Bakery

# Create your views here.
def index(request):
    # DB의 Bakery 테이블에서 데이터를 모두 가져온다
    bakeries = Bakery.objects.all()
    print(bakeries)
    for bakery in bakeries:
        print(bakery)
        # print(bakery.name)
        # print(bakery.address)
        # print(bakery.rating)

    context = {
        "bakeries": bakeries,
    }
    
    return render(request, "bakeries/index.html", context)