from django.shortcuts import render, redirect
from .models import Convinienttable, Libraries, Seoulparking, Trainconvinienttable, Wheelcharger
from django.http import HttpResponse, HttpResponseRedirect
from django.forms.models import model_to_dict
from bs4 import BeautifulSoup
import requests
import json

user_key = 'm2kuifjxx1'
secrete = 'XGncmSKeqYNjbrD3m9kJRWwdoJSKIs2yAp0kvshe'


def index(request):
    return render(request, 'index.html')


def model_views(request):
    models = Convinienttable.objects.all()
    model_list = []
    for i in models.values_list():
        if i[3] == '중구':
            model_list.append(list(i))
    return render(request, 'models.html', {'model_list':model_list})


def DB_selector(requestData):
    DBnum = requestData
    if (DBnum == '1'):
        models = Convinienttable.objects.all()
    elif (DBnum == '2'):
        models = Libraries.objects.all()
    elif (DBnum == '3'):
        models = Seoulparking.objects.all()
    elif (DBnum == '4'):
        models = Trainconvinienttable.objects.all()
    else:
        models = Wheelcharger.objects.all()
    return models


def DB_with_Gu(paramList):
    db = DB_selector(paramList[0])

    container_list = []
    temp_list = []
    return_list = []
    # print(db[0].toJSON())
    #
    # if (paramList[0] == '1'):
    #     for i in db:
    #         if i.담당구 == paramList[1]:
    #             # i = list(i)
    #             # i[2] = i[2].replace(",", "")
    #             # i[2] = i[2].replace(")(", "/")
    #             # i = tuple(i)
    #             temp_list.append(db[0].toJSON())
    #
    #     # for i in temp_list:
    #     #     for j in paramList:
    #     #         if i[20] == j:
    #     #             container_list.append(i)
    #     # if container_list[0] == 'false':
    #     #     container_list.append('-1')

    if (paramList[0] == '1'):
        for i in db.values_list():
            if i[3] == paramList[1]:
                i = list(i)
                i[2] = i[2].replace(",", "")
                i[2] = i[2].replace(")(", "/")
                i = tuple(i)
                temp_list.append(i)

        for i in temp_list:
            for j in paramList:
                if i[20] == j:
                    container_list.append(i)
        if container_list[0] == 'false':
            container_list.append('-1')

    elif paramList[0] == '2':
        for i in db.values_list():
            if i[3] == paramList[1]:
                i = list(i)
                i[1] = i[1].replace(",", "")
                i[1] = i[1].replace(")(", "/")
                i = tuple(i)
                container_list.append(i)

    elif paramList[0] == '3':
        for i in db.values_list():
            if i[1] == paramList[1]:
                i = list(i)
                i[0] = i[0].replace(",", "")
                i[0] = i[0].replace(")(", "/")
                i = tuple(i)
                container_list.append(i)

    elif paramList[0] == '4':
        for i in db.values_list():
            if i[0] == paramList[1]:
                temp_list.append(i)
        if len(paramList) == 2:
            container_list = temp_list

        else:
            for j in temp_list:
                for k in paramList:
                    print(k)
                    print(int(j[3]))
                    if k == '엘리베이터' and int(j[2]) != 0:
                        container_list.append(j)
                    if k == '에스컬레이터' and int(j[3]) != 0:
                        container_list.append(j)
                    if k == '휠체어리프트' and int(j[4]) != 0:
                        container_list.append(j)

        container_list = list(set(container_list))


    elif paramList[0] == '5':
        for i in db.values_list():
            if i[2] == paramList[1]:
                i = list(i)
                i[0] = i[0].replace(",", "")
                i[0] = i[0].replace(")(", "/")
                i = tuple(i)
                container_list.append(i)

    return container_list



# def make_requestList(dataList):
#
#     return dataDict


def DB_viewer(request):
    if request.method == 'POST':
        paramList = []

        for key, value in request.POST.items():
            paramList.append(value)


        dataList = DB_with_Gu(paramList)



        return HttpResponse(dataList)




