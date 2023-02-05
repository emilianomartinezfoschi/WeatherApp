from django.shortcuts import render
from .forms import Entrada
import requests, json
from .models import History

def formprocess(request):
    userinput= Entrada(request.POST)
    if request.POST.__contains__('ciudad'):
        try:
            # print(request.POST['ciudad'])
            userciudad= request.POST.__getitem__('ciudad')
            url = "https://weatherapi-com.p.rapidapi.com/current.json"

            querystring = {"q":userciudad}

            headers = {
                "X-RapidAPI-Key": "f5bd4bb3b5mshf1c76a001a30f98p1c4a6ejsnbeba24448f94",
                "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            result = json.loads(response.text)
            
            dbentry=History(city=result['location']['name'],country=result['location']['country'],temperature=result['current']['temp_c'],thermal_sensation=result['current']['feelslike_c'], humidity=result['current']['humidity'], cloud=result['current']['cloud'],uv=result['current']['uv'],date=str(result['location']['localtime']))
            dbentry.save()
            
            count=History.objects.all().count()
            table = History.objects.filter(id__gt=count-8)
            
            context = {
                'form':result,
                'dbtable':table
            }
            
            # print(type(result['location']['localtime']))
            return render(request, 'result.html', context)
        except:
            context = {
                'form':userinput,
                'msj':"El nombre ingresado no se corresponde con ninguna ciudad.\nIntente con otro."
            }
            return render(request, 'index.html', context)    
    else:
        return render(request, 'index.html', {'form':userinput})