from django.views          import View
from django.shortcuts      import render, redirect
from dashboard.models import *
import json
import yaml

from .                      import lang

data_path = "cohana/"

def strTotime(name):
    return name[:4] + "/" + name[4:6] + "/" + name[6:8]

class Dashboard( View ):
    def get(self, request):
        if request.user.username == "root":
            all_users = User.objects.count()
            all_figures = analysis.objects.count()
            all_datasets = csv_file.objects.count()
            all_storage = 0
            root_flag =True
            for db in csv_file.objects.all():
                all_storage += db.file_size
            print(all_users,all_figures,all_datasets)

        databases = {}
        count = 0
        selected_datasets = csv_file.objects.filter(user_id=request.user.id)
        sel_datasets = selected_datasets.count()
        sel_figures = 0
        sel_storage = 0

        figures = {}
        figure_index = 0
        for dataset in selected_datasets:
            databases[count] = {}
            databases[count]["name"] = dataset.file_name
            databases[count]['date'] = strTotime(dataset.file_save)
            databases[count]['num_ids'] = dataset.num_ids
            databases[count]['num_records'] = dataset.num_records
            databases[count]['involved_dates'] = dataset.involved_dates

            sel_figures += analysis.objects.filter(file_id=dataset.file_id).count()
            sel_storage += dataset.file_size

            with open(data_path + dataset.file_save + "/demographic.yaml", 'r') as stream:
                demographic_info = yaml.load(stream)

            databases[count]['figures'] = []

            figures[figure_index] = {
                "title": demographic_info['Event']['name'],
                "type": 'pie',
                "y_label": list(demographic_info['Event']['data'].keys()),
                "data": demographic_info['Event']['data'],

            }
            databases[count]['figures'].append(figure_index)
            figure_index += 1

            for value in demographic_info['Value']:
                if value['type'] == 'pie':
                    figures[figure_index] = {
                        "title": value['name'],
                        "type": 'pie',
                        "y_label": [str(i) for i in list(value['data'].keys())],
                        "data": value['data'],

                    }
                elif value['type'] == 'bar':
                    figures[figure_index] = {
                        "title": value['name'],
                        "type": 'bar',
                        "y_label": value['data']['y'],
                        "data": value['data']['x'],
                    }
                databases[count]['figures'].append(figure_index)
                figure_index += 1

            count += 1

        template = 'dashboard' + lang.getTemplateByLanguage(request)
        return render(request, template, locals())

class Example_dashboard( View ):
    def get(self, request):
        # print(request.user)
        # print(request.user.id)

        # dirs = [ name for name in os.listdir('./cohana/') if os.path.isdir(os.path.join('./cohana/', name)) ]
        # if len(dirs) == 0:
        #     return redirect('/error')

        # deal with continent chart
        with open('dashboard/data/continent.dat') as data_file:
            rawData = json.load(data_file)
        rawResult = rawData[u'result']

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

        template = 'example_dashboard' + lang.getTemplateByLanguage(request)
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