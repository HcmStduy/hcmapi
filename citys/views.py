import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import CityModel,CityAreaModel
from api.citys_set import CityModelSerializers,CityAreaModelSerializers
class CityApi(View):
    def get(self, request):
        city_letter_set = []
        city_dict ={'A':[],'B':[],'C':[],'D':[],'E':[],'F':[],'G':[],'H':[],'I':[],'J':[],'K':[],'L':[],'M':[],'N':[],'O':[],'P':[],'Q':[],'R':[],
                    'S':[],'T':[],'U':[],'V':[],'W':[],'X':[],'Y':[],'Z':[]}

        hot_city = CityModel.objects.filter(city_hot__gt=200).all()
        ser = CityModelSerializers(hot_city, many=True)
        city_letter = CityModel.objects.values('city_letter').all()
        for i in range(len(city_letter)):
            city_letter_set.append(city_letter[i]['city_letter'])
        city_letter_set = set(city_letter_set)
        city_name = sorted(city_letter_set)
        print(city_name)
        for j in range(len(city_name)):
            city = CityModel.objects.filter(city_letter=city_name[j]).all()
            ser_city = CityModelSerializers(city, many=True)
            # city_name[j] = [ser_city.data]
            city_letter = ser_city.data[0]['city_letter'][0:1]
            print(city_dict[city_letter])
            city_dict[city_letter].append(ser_city.data)
            print(city_dict[city_letter])

        return JsonResponse({'data': {
            'hot_city': ser.data,
            'A': city_dict['A'],
            'B': city_dict['B'],
            'C': city_dict['C'],
            'D': city_dict['D'],
            'E': city_dict['H'],
            'F': city_dict['L'],
            'G': city_dict['S'],
            'H': city_dict['T'],
            'I': city_dict['X'],
            'J': city_dict['J'],
            'K': city_dict['K'],
            'L': city_dict['L'],
            'M': city_dict['M'],
            'N': city_dict['N'],
            'O': city_dict['O'],
            'P': city_dict['P'],
            'Q': city_dict['Q'],
            'R': city_dict['R'],
            'S': city_dict['S'],
            'T': city_dict['T'],
            'U': city_dict['U'],
            'V': city_dict['V'],
            'W': city_dict['W'],
            'X': city_dict['X'],
            'Y': city_dict['Y'],
            'Z': city_dict['Z'],
        }})


class CityAreaApi(View):
    def get(self, request):
        a = request.GET.get('city_id', None)
        area_all = CityAreaModel.objects.filter(city_id=a).all()
        ser = CityAreaModelSerializers(area_all, many=True)
        return JsonResponse({'data': ser.data})


class SetCity(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        area_id = json.loads(request.body, encoding='utf-8').get('area_id')
        city = CityAreaModel.objects.get(pk=area_id).city_id
        request.session['city'] = CityModelSerializers(instance=city).data
        return JsonResponse({'status': 200})