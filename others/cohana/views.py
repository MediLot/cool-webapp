from django.shortcuts import render,redirect
import numpy as np
import json
import random,string
import datetime
import os
import yaml
import pandas as pd
import shutil
import csv
import sqlite3
import subprocess

from .models import *

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

json_path = BASE_DIR + "/json/"
upload_path = BASE_DIR + "/upload/"
data_path = BASE_DIR + "/data/"
if not os.path.exists(upload_path):
    os.mkdir(upload_path)
if not os.path.exists(data_path):
    os.mkdir(data_path)

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

# Create your views here.
def test(request):
    result = {}
    count = 0
    data = to_range_num("20200505115128_GQl4KSbx","range")
    result[count] = data
    result[count]['title'] = "D_dimer"
    result[count]['type'] = 'range'
    # count += 1
    # fig5_2_data = avg_value(json_path + "level5/D_dimer.json")
    # result['fig5_2'] = fig5_2_data
    # result['fig5_2']['title'] = "D_dimer analysis"
    # result['fig5_2']['type'] = "range"
    return redirect("/hello/",foo="a")
    # return render(request, "dashboard.html", {"figures":result})

def hello(request):
    print(request.foo)
    return render(request, "base.html")

def file_list(request):
    result = {}
    if request.method == "GET":
        user = user_info.objects.get(user_name=request.session['user'])
        files = csv_file.objects.filter(user_id=user)
        if files.exists():
            result['files'] = {}
            for index,file in enumerate(files):
                result['files'][index] = {
                    "index": index+1,
                    "file_name": file.file_name,
                    "file_save": file.file_save,
                    "file_date": file.file_save[:4]+"/"+file.file_save[4:6]+"/"+file.file_save[6:8]
                }
        return render(request, "file_list.html", result)
    elif request.method == "POST":
        file_operation = request.POST.get('file_operation')
        file_save = request.POST.get('file_save')

        if file_operation == "delete":
            if csv_file.objects.filter(file_save=file_save).exists():
                csv_file.objects.filter(file_save=file_save).delete()
                shutil.rmtree(data_path+file_save)
                os.remove(upload_path+file_save+".csv")

            return redirect("/database")
        else:
            request.session['file_save'] = file_save

            columns = []
            with open(data_path+'/%s/table.yaml'%file_save, 'r') as f:
                data = yaml.load(f.read())
                for col in data['fields']:
                    columns.append(col['name'])

            result['columns'] = columns
            request.session['columns'] = columns

            return render(request, "figure_design.html", result)

def figure_design(request):
    result = {}
    if request.method == "GET":
        return render(request, "figure_design.html", result)
    elif request.method == "POST":
        sub_path = data_path + "/%s" % request.session['file_save']
        agg = request.POST.get("aggregator")
        analysis_name = request.POST.get("name")
        table_name = request.POST.get("tableFieldName")
        if agg == "RETENTION" or agg == "RANGE":
            with open(sub_path+'/cube.yaml', 'w') as f:
                fields = []
                fields.append({
                    "aggregator": agg,
                    "name": analysis_name,
                    "tableFieldName": table_name,
                })
                f.write(yaml.dump({'measures': fields}, default_flow_style=False))

        elif agg == "SIMPLE":
            pass

        request.session['agg'] = agg
        request.session['analysis_name'] = analysis_name
        result['columns'] = request.session['columns']
        result['analysis'] = agg
        result['analysis_name'] = analysis_name
        file_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        request.session['analysis_file'] = file_name + ''.join(random.sample(string.ascii_letters + string.digits, 8))

        if agg == "RETENTION" or agg == "RANGE":
            result['events'] = get_info(request.session['file_save'])
            return render(request, "cohort_analysis.html", result)
        elif agg == "SIMPLE":
            return render(request, "simple_analysis.html", result)

def get_info(file_name):
    file_path = "./data/%s/"%file_name

    file = pd.read_csv(file_path+"dim.csv",index_col=0)

    with open(file_path+"table.yaml","r") as f:
        events_type = yaml.load(f.read())

    events_tree={}

    # print(file)
    # print(file.index.unique())
    # print(file.loc[['event'],:])
    events = file.loc[['event'],:]
    for id,row in events.iterrows():
        event = row[0]
        sub_data = file.loc[[event],:]
        events_tree[event] = []
        for sub_id,sub_row in sub_data.iterrows():
            events_tree[event].append(sub_row[0])

    # print(result)

    return {
        "events_list": file.index.unique(),
        "events_tree": events_tree,
        "events_type": events_type
    }


def figure_list(request):
    result = {}

    user = user_info.objects.get(user_name=request.session['user'])
    files = csv_file.objects.filter(user_id=user)
    count = 0
    if files.exists():
        for file in files:
            alys = analysis.objects.filter(file_id=file)
            if alys.exists():
                for aly in alys:
                    if aly.analysis_type == "RETENTION":
                        result[count] = to_heat_num(file.file_save,aly.analysis_save)
                        result[count]['title'] = aly.analysis_name + "(line map)"
                        result[count]['type'] = "line"
                        count += 1
                        result[count] = to_heat_percent(file.file_save,aly.analysis_save)
                        result[count]['title'] = aly.analysis_name + "(heat map)"
                        result[count]['type'] = "heatmap"
                        count += 1

                    if aly.analysis_type == "SIMPLE":
                        output = to_pie(file.file_save, aly.analysis_save)
                        result[count] = output
                        result[count]['title'] = output['feature']+ "(pie map)"
                        result[count]['type'] = 'pie'
                        count += 1

                    if aly.analysis_type == "RANGE":
                        output = to_range_num(file.file_save, aly.analysis_save)
                        result[count] = output
                        result[count]['title'] = aly.analysis_name + "(range map)"
                        result[count]['type'] = 'range'
                        count += 1


    return render(request, "dashboard.html", {"figures":result})

# to show the figures
def to_range_num(file_name, analysis_name):
    input_path = "./data/%s/%s.json" % (file_name,analysis_name)
    with open(input_path, "r") as json_file:
        data = json.load(json_file)
    # print(data)

    y_label = []
    x_label = []
    line = {}
    error = {}
    for key,value in data.items():
        if value['interval'] == 1:
            label = str(value['group_min'])
        else:
            label = "[%s,%s)"%(value['group_min'],value['group_min']+value['interval'])
        y_label.append(label)
        x_label = list(value['data'].keys())
        sub_line = []
        sub_error = []
        for key,value in value['data'].items():
            if value == {}:
                sub_error.append([0,0,0])
                sub_line.append(0)
            else:
                sub_error.append([key,value['max'],value['min']])
                sub_line.append(value['avg'])
        line[label] = sub_line
        error[label] = sub_error
    result = {
        "y_label": y_label,
        "x_label": x_label,
        "error":error,
        "line":line
    }
    return result

def to_heat_num(file_name, analysis_name):
    input_path = "./data/%s/%s.json" % (file_name, analysis_name)
    with open(input_path, "r") as json_file:
        data = json.load(json_file)
    # print(data)

    y_label = []

    result = {}
    full_data = []
    for key,value in data.items():
        label = "[%s,%s)" % (value['group_min'], value['group_min'] + value['interval'])
        x_label = [i for i in range(value['check_days'])]
        y_label.append(label)
        result[label] = value['data']
        full_data.extend(result[label])
    # print(full_data)
    return {
        "y_label": y_label,
        "x_label": x_label,
        "data": result,
        "min": 0,
        "max": max(full_data),
    }

def to_heat_percent(file_name, analysis_name):
    input_path = "./data/%s/%s.json" % (file_name, analysis_name)
    with open(input_path, "r") as json_file:
        data = json.load(json_file)
    # print(data)

    y_label = []
    result = []
    group_id=0
    full_data = []
    for key,value in data.items():
        label = "[%s,%s)" % (value['group_min'], value['group_min'] + value['interval'])
        x_label = [i for i in range(value['check_days'])]
        y_label.append(label)
        # result.append([0,group_id,'100'])
        for id,sub in enumerate(value['data']):
            full_data.append(sub/value['data'][0]*100)
            result.append([id,group_id,"%.2f"%(sub/value['data'][0]*100)])
        group_id+=1

    return {
        "y_label": y_label,
        "x_label": x_label,
        "data": result,
        "min": 0,
        "max": max(full_data),
    }

def to_pie(file_name, analysis_name):
    input_path = "./data/%s/%s.json" % (file_name, analysis_name)
    with open(input_path, "r") as json_file:
        data = json.load(json_file)
    return data

# def LocalLoader(file_name):
#     input_path = upload_path + "/%s" % file_name + ".csv"
#     output_path = data_path + "/%s" % file_name
#     raw_output = os.path.join(output_path, "/raw.csv")
#     yaml_input = os.path.join(output_path, "/table.yaml")
#     yaml_input2 = os.path.join(output_path, "/cube.yaml")
#     dim_output = os.path.join(output_path, "/dim.csv")
#
#     if os.path.exists(output_path):
#         os.mkdir(output_path+"/000000")
#     os.system("java -jar utils/LocalLoader.jar '" + yaml_input + "' '" + dim_output + "'  '" + raw_output + "'  '" + output_path + "/000000' 65536")
#
#     return 0
#
# def preprocess(file_name):
#     input_path = upload_path + "/%s" % file_name + ".csv"
#     output_path = data_path + "/%s" % file_name
#     raw_output = os.path.join(output_path, "/raw.csv")
#     yaml_input = os.path.join(output_path, "/table.yaml")
#     yaml_input2 = os.path.join(output_path, "/cube.yaml")
#     dim_output = os.path.join(output_path, "/dim.csv")
#
#     print("Preprocessing Started")
#     rawdata = pd.read_csv(input_path)
#     rawdata.fillna("null", inplace=True)
#     rawdata.to_csv(raw_output, header=False, index=False)
#     print("raw save finished")
#
#     spec = yaml.load(yaml_input)
#     with open(dim_output, 'w') as csvfile:
#         dimwriter = csv.writer(csvfile)
#         for field in spec['fields']:
#             if field['dataType'] == 'String':
#                 for key in rawdata[field['name']].astype('str').unique():
#                     try:
#                         dimwriter.writerow([field['name'], key])
#                     except Exception:
#                         pass
#             elif field['fieldType'] == 'ActionTime':
#                 dimwriter.writerow(
#                     [field['name'], str(rawdata[field['name']].min()) + '|' + str(rawdata[field['name']].max())])
#             elif field['dataType'] == 'Int32':
#                 dimwriter.writerow([field['name'], str(int(rawdata[field['name']].min())) + '|' + str(
#                     int(rawdata[field['name']].max()))])
#             else:
#                 pass
#
#     table = file_name
#     conn = None
#     print('creating dim...')
#     try:
#         conn = sqlite3.connect('dim.db')
#         c = conn.cursor()
#
#         sql = 'select name from sqlite_master where type = "table" and name = "%s";' % table
#         if all(t[0] != table for t in c.execute(sql)):
#             sql = 'create table "%s" (col VARCHAR(200), value VARCHAR(200));' % table
#             c.execute(sql)
#             print('table "%s" created' % table)
#         else:
#             sql = 'delete from "%s"' % table
#             c.execute(sql)
#             print('table "%s" deleted' % table)
#
#         insert_sql = 'INSERT INTO "%s" (col, value) VALUES ' % table
#         sql = insert_sql
#         i = 0
#         with io.open(dim_output) as ifile:
#             while ifile.readable():
#                 line = ifile.readline().strip('\n').split(',')
#                 if len(line) < 2:
#                     break
#                 sql += '("%s", "%s"),' % (line[0], line[1])
#                 i += 1
#                 if i == 200:
#                     c.execute(sql.rstrip(',')+';')
#                     sql = insert_sql
#                     i = 0
#         c.execute(sql.rstrip(',')+';')
#         print('value inserted')
#
#         conn.commit()
#         conn.close()
#
#     except Exception as e:
#         conn.close()
#         raise e
#
#     print("Preprocessing Finished")

