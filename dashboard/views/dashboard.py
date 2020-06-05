from django.views          import View
from django.shortcuts      import render, redirect
from dashboard.models import *
import json
import os

from .                      import lang

class Dashboard( View ):
    def get(self, request):

        request.session['user'] = "root"

        user = user_info.objects.filter(user_name="root")
        if not user.exists():
            new_user = user_info(
                user_name="root"
            )
            new_user.save()


        dirs = [ name for name in os.listdir('./cohana/') if os.path.isdir(os.path.join('./cohana/', name)) ]
        if len(dirs) == 0:
            return redirect('/error')

        # deal with continent chart
        with open('dashboard/data/continent.dat') as data_file:
            rawData = json.load(data_file)
        rawResult = rawData[u'result']
        i = 0
        continentLegend = []
        continentData = []
        for r in rawResult:
            continentLegend.append(r[u'cohort'])
            pair = {'value':r[u'measure'],'name':r[u'cohort']}
            continentData.append(pair)

        # deal with dau chart
        dauData = {}
        try:
            with open('dashboard/data/dap.dat') as data_file:
                dauData = json.load(data_file)
        except Exception as e:
            pass

        # deal with map
        mapData=[]
        with open('dashboard/data/country.dat') as data_file:
            rawData = json.load(data_file)
        rawResult = rawData[u'result']
        for r in rawResult:
            pair = {'name':r[u'cohort'],'value':r[u'measure']}
            mapData.append(pair)

        birthData={}
        try:
            with open('dashboard/data/age.dat') as data_file:
                birthData = json.load(data_file)
        except Exception as e:
            pass

        lastData={}
        try:
            with open('dashboard/data/last_loaded.dat') as data_file:
                lastData = json.load(data_file)
        except Exception as e:
            pass

        medicineData={}
        try:
            with open('dashboard/data/medicine.dat') as data_file:
                medicineData = json.load(data_file)
        except Exception as e:
            pass

        diseaseData={}
        try:
            with open('dashboard/data/disease.dat') as data_file:
                diseaseData = json.load(data_file)
        except Exception as e:
            pass

        genderData={}
        try:
            with open('dashboard/data/gender.dat') as data_file:
                genderData = json.load(data_file)
        except Exception as e:
            pass

        template = 'dashboard' + lang.getTemplateByLanguage(request)
        return render(request, template,{
                'medicineData':json.dumps(medicineData),
                'diseaseData':json.dumps(diseaseData),
                'genderData':json.dumps(genderData),
                'continentLegend':json.dumps(continentLegend),
                'continentData':json.dumps(continentData),
                'mapData':json.dumps(mapData),
                'dauData':json.dumps(dauData),
                'last_loaded':json.dumps(lastData),
                'birthData':json.dumps(birthData)
                })
