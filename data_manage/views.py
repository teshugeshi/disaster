from django.shortcuts import render
from django.http import Http404
from .models import Area,Data
from django.core.paginator import Paginator
import datetime

def data_manage_index(request):
    return render(request, "data_manage/data_manage.html")

def data_manage_show(request):
    area_name = request.GET.get('area_name')
    if len(area_name) == 0:
        return render(request, "data_manage/data_manage.html")
    start_time = request.GET.get('start_time')
    end_time = request.GET.get('end_time')
    try:
        area = Area.objects.get(name=area_name)
        data_all = area.data_set.all()
    except:
        data_all = []
    time_format = '%Y-%m-%d'
    if len(start_time) > 0  and len(end_time) > 0 \
            and datetime.datetime.strptime(start_time, time_format) \
            <= datetime.datetime.strptime(end_time, time_format):
        data_all = data_all.filter(datetime__lte=end_time, datetime__gte=start_time)
    
    paginator = Paginator(data_all, 30)      
    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)
    
    context = {
        "area_name": area_name,
        "start_time": start_time,
        "end_time": end_time,
        "data": data,
    }
    return render(request, "data_manage/data_manage.html", context)
