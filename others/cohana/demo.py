#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@version:0.1
@author:Cai Qingpeng
@file: demo.py
@time: 2020/5/8 6:20 PM
'''

from .views import *


def hybrid_analysis(path):
    with open(path, 'r') as load_f:
        data = json.load(load_f)
    y_label = list(data.keys())
    x_label = []
    result = {}
    for group_id, group in enumerate(y_label):
        sub_data = data[group]
        x_label = list(sub_data.keys())
        result[group] = {}
        result[group]['dead'] = []
        result[group]['live'] = []
        result[group]['whole'] = []
        for key, value in sub_data.items():
            result[group]['dead'].append(value['dead'])
            result[group]['live'].append(value['live'])
            result[group]['whole'].append(value['whole'])

    return {
        "y_label": y_label,
        "x_label": x_label,
        "data": result,
        "list": ["dead", "live", "whole"]
    }

def heat_number(path):
    with open(path, 'r') as load_f:
        data = json.load(load_f)
    # print(data)
    y_label = list(data.keys())
    x_label = []
    result = {}
    full_data = []
    for group_id, group in enumerate(y_label):
        sub_data = data[group]['number']
        x_label = list(sub_data.keys())
        result[group] = []
        for day_id, day in enumerate(sub_data):
            result[group].append(sub_data[day])
            full_data.append(sub_data[day])

    min_value = min(full_data)
    max_value = max(full_data)

    return {
        "y_label": y_label,
        "x_label": x_label,
        "data": result,
        "min": 0,
        "max": max_value,
    }

def heat_percent(path):
    with open(path, 'r') as load_f:
        data = json.load(load_f)
    # print(data)
    y_label = list(data.keys())
    x_label = []
    result = []
    full_data = []
    for group_id, group in enumerate(y_label):
        sub_data = data[group]['percent']
        x_label = list(sub_data.keys())
        for day_id, day in enumerate(sub_data):
            result.append([day_id, group_id, "%.2f" % sub_data[day]])
            full_data.append(sub_data[day])
    min_value = min(full_data)
    max_value = max(full_data)

    return {
        "y_label": y_label,
        "x_label": x_label,
        "data": result,
        "min": 0,
        "max": 100,
    }

def avg_value(path):
    with open(path, 'r') as load_f:
        data = json.load(load_f)
    # print(data)
    y_label = list(data.keys())
    if 'upper' in y_label:
        y_label.remove("upper")
    if 'lower' in y_label:
        y_label.remove("lower")

    error = {}
    line = {}
    output = {
        "y_label": y_label,
    }
    for g_key, g_value in data.items():
        if g_key == 'upper' or g_key == 'lower':
            output[g_key] = g_value
        else:
            output['x_label'] = list(g_value.keys())
            line[g_key] = []
            error[g_key] = []
            for day_id, day in enumerate(g_value.keys()):
                sub_data = g_value[day]
                error[g_key].append([day_id, sub_data['high'], sub_data['low']])
                line[g_key].append(sub_data['avg'])

    output['error'] = error
    output['line'] = line

    return output

def demo_dashboard(request):
    result = {}
    request.session['user'] = "qingpeng"

    user = user_info.objects.filter(user_name="qingpeng")
    if not user.exists():
        new_user = user_info(
            user_name="qingpeng"
        )
        new_user.save()
    #
    #
    # user = user_info.objects.get(user_name=request.session['user'])
    # new_file = csv_file(
    #     user_id=user,
    #     file_name="20200502095912_NyZdIYj1"
    # )
    # new_file.save()
    #
    # file = csv_file.objects.get(file_name="20200502095912_NyZdIYj1")
    # new_analysis = analysis(
    #     file_id=file,
    #     analysis_type="RETENTION",
    #     analysis_name="id-RETENTION",
    # )
    # new_analysis.save()

    fig4_1_data = heat_percent(json_path + "level4/medication_in_ICU.json")
    result['fig4_1'] = fig4_1_data
    result['fig4_1']['title'] = "The healing time of the patient in ICU after taking the medication"
    result['fig4_1']['type'] = "heatmap"

    fig4_2_data = heat_number(json_path + "level4/medication_in_ICU.json", )
    result['fig4_2'] = fig4_2_data
    result['fig4_2']['title'] = "The healing time of the patient in ICU after taking the medication"

    fig5_1_data = hybrid_analysis(json_path + "level5/age_comorbidities.json")
    result['fig5_1'] = fig5_1_data
    result['fig5_1']['title'] = "age & comorbidities analysis"

    fig5_2_data = avg_value(json_path + "level5/D_dimer.json")
    result['fig5_2'] = fig5_2_data
    result['fig5_2']['title'] = "D_dimer analysis"
    result['fig5_2']['vital'] = "D_dimer"

    return render(request, "demo_dashboard.html", result)
