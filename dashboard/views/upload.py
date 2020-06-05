from django.http            import HttpResponseRedirect
from django.shortcuts       import render, redirect
from django.views           import View
from datetime               import datetime

import json
import os
import subprocess
import yaml
import pandas as pd
import string
import random
from dashboard.models import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
upload_path = "upload/"
data_path = "cohana/"

# class Upload( View ):
#
#     def get(self, request):
#         return render(request, "upload.html")
#
#     def post( self,request ):
#         data   = json.loads( request.POST['data' ] )
#         prefix = datetime.now().strftime('%Y%m%d%H%M%S')
#         rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
#         prefix += rand_str
#         request.session['file_save']=prefix
#
#         self._save_file( request, prefix )
#         self._table_yaml( data, prefix )
#         self._cube_yaml ( data, prefix )
#         self._process_file( prefix )
#
#         user = user_info.objects.get(user_name=request.session['user'])
#         new_file = csv_file(
#             user_id=user,
#             file_name = request.session['file_name'],
#             file_save = prefix,
#         )
#         new_file.save()
#
#         return HttpResponseRedirect('/retention/advance')
#
#     def _save_file( self, request, prefix ):
#         file        = request.FILES ['file']
#         request.session['file_name'] = file.name
#         save_name   = prefix
#         with open ( upload_path + '/%s.csv' % save_name, 'wb' ) as outfile:
#             for i, chunk in enumerate( file.chunks( 1000 ) ):
#                 outfile.write( chunk )
#
#         rawdata = pd.read_csv(upload_path + '/%s.csv' % prefix)
#         columns = rawdata.columns
#         columns = [i.strip() for i in columns if i != '' and i != '\r']
#         rawdata.columns = columns
#
#         os.mkdir(data_path+save_name)
#         rawdata.to_csv(data_path + '/%s/data.csv' % (save_name), index=False)
#
#     def _table_yaml( self, data, prefix ):
#         with open( data_path + '%s/table.yaml' % prefix, 'w' ) as f:
#             fields = []
#             for field in data['fields']:
#                 fields.append({
#                     "name":      field['name'],
#                     "fieldType": field['fieldType']['type'],
#                     "dataType":  field['fieldType']['dataType'],
#                 })
#             f.write( yaml.dump({ 'fields': fields , 'charset': 'utf-8'}, default_flow_style=False ))
#
#     def _cube_yaml( self, data, prefix ):
#         with open(data_path+'%s/cube.yaml' % prefix, 'w' ) as f:
#             fields = []
#             for field in data['metrics']:
#                 aggregator     = field['alligator']
#                 tableFieldName = field['column']
#                 name           = field.get('name') or ( '%s-%s' % (tableFieldName, aggregator) )
#                 fields.append({
#                     "aggregator":       aggregator,
#                     "name":             name,
#                     "tableFieldName":   tableFieldName,
#                 })
#             f.write( yaml.dump({ 'measures': fields }, default_flow_style=False ))
#
#
#
#     def _process_file( self, prefix ):
#         subprocess.call(['utils/preprocess.sh', prefix])

fieldTypes = {
    'User ID':{
        'type': "UserKey",
        "datatype": "String"
    },
    # 'attribute':{
    #     'type': "Attribute",
    #     "datatype": "String"
    # },
    'Event':{
        'type': "Action",
        "datatype": "String"
    },
    'Event Related':{
        'type': "Segment",
        "datatype": "String"
    },
    'Time':{
        'type': "ActionTime",
        "datatype": "Int32"
    },
    'Value':{
        'type': "Metric",
        "datatype": "Int32"
    },
}

class Upload( View ):

    def get(self, request):
        return render(request, "upload.html")

    def post( self,request ):
        result = {}
        csv_file = request.FILES["csv_file"]
        file_name = request.POST.get("name")

        rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        file_save = datetime.now().strftime('%Y%m%d%H%M%S') + rand_str
        f = open(upload_path + file_save + ".csv", 'wb')
        for chunk in csv_file.chunks():
            f.write(chunk)
        f.close()

        rawdata = pd.read_csv(upload_path + file_save + ".csv")
        columns = rawdata.columns
        columns = [i.lower().strip() for i in columns if i != '' and i != '\r']
        rawdata.columns = columns

        # print(columns)
        os.mkdir(data_path+file_save)
        # rawdata.to_csv(data_path + "%s/data.csv" % file_save, index=False)

        request.session['columns'] = columns
        request.session['csv_name'] = file_name
        request.session['csv_save'] = file_save

        return redirect("/column_list/")

class Column_list( View ):

    def get(self, request):
        result = {}

        file_save = request.session['csv_save']
        data = pd.read_csv(upload_path + file_save + ".csv")

        columns = list(data.columns)
        result['columns'] = columns
        result['options'] = fieldTypes

        result['column_type'] = {}

        if "id" in columns:
            result['column_type']["id"] = "User ID"
            columns.remove("id")
        if "time" in columns:
            result['column_type']["time"] = "Time"
            columns.remove("time")
        if "event" in columns:
            result['column_type']["event"] = "Event"
            columns.remove("event")
            relateds = list(data["event"].unique())
            for related_col in relateds:
                if related_col in columns:
                    result['column_type'][related_col] = "Event Related"
                    columns.remove(related_col)
        for col in columns:
            result['column_type'][col] = "Value"

        return render(request, "column_list.html", result)

    def post( self,request ):
        file_save = request.session['csv_save']
        data = pd.read_csv(upload_path + file_save + ".csv")

        sub_path = data_path + "/%s" % request.session['csv_save']
        if not os.path.exists(sub_path):
            os.mkdir(sub_path)
        with open(sub_path + '/table.yaml', 'w') as f:
            fields = []
            for field in request.session['columns']:
                fields.append({
                    "name": field.replace('\r', ''),
                    "fieldType": fieldTypes[request.POST.get(field)]['type'],
                    "dataType": fieldTypes[request.POST.get(field)]['datatype'],
                })
                if fieldTypes[request.POST.get(field)]['type'] == "ActionTime":
                    data['time'] = pd.to_datetime(data['time'])
                    data['time'] = data['time'].dt.strftime("%Y-%m-%d")

            f.write(yaml.dump({'fields': fields, 'charset': 'utf-8'}, default_flow_style=False))

        data.to_csv(data_path + "%s/data.csv" % file_save, index=False)

        subprocess.call(['utils/preprocess.sh', request.session['csv_save']])

        user = user_info.objects.get(user_name=request.session['user'])
        new_file = csv_file(
            user_id=user,
            file_name=request.session['csv_name'],
            file_save=request.session['csv_save'],
        )
        new_file.save()

        return redirect("/database/")
