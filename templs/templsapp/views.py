from django.shortcuts import render


def index(request):
    data = {"place": "ГАПОУ 'ЕПК' - АЛАБУГА ПОЛИТЕХ",
            "group": "215-8-1",
            "spec": "Web-programmer",
            "work": "Frontend-developer/3D artist"}
    return render(request, 'index.html', context={'data': data})
def about(request):
    dataabout = {"fio": "Зекрин Тимур Ильдусович",
                "age": "16 лет",
                "weight": "50 кг",
                "height": "173 см"}
    return render(request,"about.html",context={'dataabout': dataabout})
def contacts(request):
    datacontacts = {"GitHub":"https://github.com/tabbep0h",
                    "Telegram":"@tabbep0h",
                    "Vk":"https://vk.com/tabbep0h",
                    "Tel-Number":"8-950-453-00-14",
                    "YouTube":"https://www.youtube.com/channel/UCeMQuzB8eOf7OyHb-nrkWkQ"}

    return render(request,"contacts.html",context={'datacontacts': datacontacts})
def form(request):
    return render(request, "form.html")

