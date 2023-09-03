import requests
from django.shortcuts import render






def Hompage(request):
    
    response = requests.get('https://api.quran.com/api/v4/chapter_recitations/1?language=en').json()    
    suras = requests.get(url='https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/info.json').json()
    
        
    return render(request, 'main/index.html', {'response':response,'suras':suras})




def Suras(request):
    response = requests.get(url='https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/info.json').json()
    return render(request, 'main/category.html', {'response': response})




def get_sura(request, sura):
    response = requests.get(f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/{sura}.json').json()
    

    return render(request, 'main/oyat.html', {'response': response})






def Buttons(request):
   
    return render(request, 'main/buttons.html')