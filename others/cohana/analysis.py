#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@version:0.1
@author:Cai Qingpeng
@file: analysis.py
@time: 2020/5/8 6:19 PM
'''

from .views import *
import json
from django.http import JsonResponse

def simple_analysis(request):
    result = {}
    if request.method == "GET":
        return render(request,"simple_analysis.html",result)
    elif request.method == "POST":
        feature_name = request.POST.get("Simple_feature")
        feature_type = request.POST.get("Simple_feature_type")
        group_num = request.POST.get("group_num")
        agg = request.session['agg']
        file_save = request.session['file_save']
        analysis_file = request.session['analysis_file']
        analysis_name =request.session['analysis_name']


        if feature_type == "CONTINUES":
            output = continues_divide(file_save, analysis_file, feature_name, int(group_num))
        elif feature_type == "CATEGORIZE":
            output = categorize_divide(file_save, analysis_file, feature_name)

        result[0] = output
        result[0]['title'] = feature_name
        result[0]['type'] = 'pie'

        file = csv_file.objects.get(file_save=request.session['file_save'])
        new_analysis = analysis(
            file_id=file,
            analysis_type=agg,
            analysis_name=analysis_name,
            analysis_save=analysis_file
        )
        new_analysis.save()

        return render(request, "dashboard.html", {"figures":result})

def continues_divide(file_name,analysis_name,feature,group_num):
    input_path = upload_path + "/%s.csv" % file_name
    data = pd.read_csv(input_path)
    data = list(data[feature])
    data.sort()
    # print(data)

    group_min = min(data)
    group_max = max(data)
    # print(group_min,group_max)
    print(group_max,group_min,group_num)
    interval = int((group_max-group_min)/group_num)
    # print(interval)

    y_labels = []
    groups = {}
    count = 0
    for i in range(group_min,group_max,interval):
        start = i
        end = min(i+interval-1,group_max)
        num = data.index(end) - data.index(start) + 1
        name = "%d-%d" % (start,end)
        y_labels.append(name)

        groups[name] = num
        count += 1

    result = {
        "group_min":group_min,
        "group_max":group_max,
        "group_num":group_num,
        "interval":interval,
        "y_label":y_labels,
        "feature":feature,
        "data": groups,
    }

    with open(data_path+"./%s/%s.json"%(file_name,analysis_name), 'w') as f:
        json.dump(result, cls=MyEncoder, fp=f)

    return result

def categorize_divide(file_name,analysis_name,feature):
    input_path = upload_path + "/%s.csv" % file_name
    data = pd.read_csv(input_path)
    data = list(data[feature])

    cates = list(set(data))
    num = len(cates)
    print(cates)

    groups= {}
    count = 0
    for i in cates:
        groups[i] = data.count(i)
        count+=1
    result = {
        "class_num":num,
        "y_label":cates,
        "feature":feature,
        "data": groups,
    }
    with open(data_path+"./%s/%s.json"%(file_name,analysis_name), 'w') as f:
        json.dump(result, cls=MyEncoder, fp=f)

    return result

def get_json(type):
    # NOTE: May14 change the cohort_metrix events to single event
    # NOTE: age_range will be plural, day -> days, year -> years
    # NOTE: events change to array [{}, {}, ...]
    # NOTE: birth_criteria group_by and eventN under same item {} in array
    # NOTE: the updated schema:
    """
{
  "cohort_metrix": {
    "measure": "retention",
    "event": {
      "event": "labtest",
      "labtest": "Labtest-C",
      "value": {
        "min": "45",
        "max": "100"
      }
    },
    "age_range": {
      "min": 1,
      "max": 7,
      "by": "days"
    }
  },
  "user_selection": {
    "events": [
      {
        "frequency": {
          "select": {
            "mode": "any",
            "days": 7
          },
          "min": 1,
          "max": 100
        },
        "event": "disease",
        "disease": "Disease-B"
      }
    ]
  },
  "birth_criteria": {
    "events": [
      {
        "frequency": {
          "min": 2,
          "max": 100
        },
        "group_by": {
          "name": "id",
          "min": 0,
          "max": 0,
          "interval": 10
        },
        "event": "labtest",
        "labtest": "Medicine-A"
      }
    ]
  }
}
    """
    data1 = {
        "cohort_metrix":{
            "measure": "retention",
            "events":{
                "event1":{
                    "event": "labtest",
                    "labtest": "Labtest-C",
                    "value": {
                        "min": "45",
                        "max": "100",
                    }
                }
            },
            "age_range":{
                "min": "1",
                "max": "7",
                "by": "day"
            }
        },
        "user_selection":{
            "events":{
                "event1":{
                    "event":"disease",
                    "disease": "Disease-B",
                    "frequency":{
                        "min": "1",
                        "max": "100",  # ∞
                        "select":{
                            "mode": "any",
                            "days": "7",
                        }
                    }
                }
            }
        },
        "birth_criteria":{
            "events": {
                "event1": {
                    "event": "prescribe",
                    "prescribe": "Medicine-A",
                    "frequency": {
                        "min": "2",
                        "max": "100",
                    }
                }
            },
            "group_by":{
                "name": "birthyear",
                "min":"1950",
                "max":"2000",
                "interval":"10"
            }
        }
    }
    data2 = {
        "cohort_metrix": {
            "measure": "retention",
            "events": {
                "event1": {
                    "event": "labtest",
                    "labtest": "PCR",
                    "value": {
                        "min": "1",
                        "max": "1",
                    }
                }
            },
            "age_range": {
                "min": "1",
                "max": "7",
                "by": "day"
            }
        },
        "user_selection": {
            "events": {
                "event1": {
                    "event": "disease",
                    "disease": "covid-I",
                    "frequency": {
                        "min": "1",
                        "max": "100",  # ∞
                        "select": {
                            "mode": "any",
                            "days": "7",
                        }
                    }
                }
            }
        },
        "birth_criteria": {
            "events": {
                "event1": {
                    "event": "medicine",
                    "medicine": "therapy",
                    "frequency": {
                        "min": "1",
                        "max": "100",
                    }
                }
            },
            "group_by": {
                "name": "age",
                "min": "0",
                "max": "104",
                "interval": "10"
            }
        }
    }
    data3 = {
        "cohort_metrix": {
            "measure": "range",
            "events": {
                "event1": {
                    "event": "labtest",
                    "labtest": "D-dimer",
                }
            },
            "age_range": {
                "min": "1",
                "max": "15",
                "by": "day"
            }
        },
        "user_selection": {
            "events": {
                "event1": {
                    "event": "disease",
                    "disease": "covid-I",
                    "frequency": {
                        "min": "1",
                        "max": "100",  # ∞
                        "select": {
                            "mode": "any",
                            "days": "7",
                        }
                    }
                }
            }
        },
        "birth_criteria": {
            "events": {
                "event1": {
                    "event": "position",
                    "position": "ICU",
                    "frequency": {
                        "min": "1",
                        "max": "100",
                    }
                }
            },
            "group_by": {
                "name": "dead",
                "min": "0",
                "max": "1",
                "interval": "1",
                "category": True
            }
        }
    }
    if type == 1:
        return data1
    if type == 2:
        return data2
    if type == 3:
        return data3

def cohort_analysis(request):
    result = {}

    if request.method == "GET":
        return render(request, "cohort_analysis.html", result)
    elif request.method == "POST":
        print("\n cohort_analysis POST called")
        print("request.POST.items(): ", list(request.POST.items()))
        # print("request.POST.dict(): ", request.POST.dict())
        file_name = request.session['file_save']
        analysis_name = request.session['analysis_name']
        analysis_file = request.session['analysis_file']
        agg = request.session['agg']

        cohort_matrix = json.loads(list(request.POST.items())[0][0])
        test = analysis.objects.filter(analysis_save=analysis_file)
        if not test.exists():
            if agg == "RETENTION":
                sub_result = Retention(cohort_matrix,file_name, analysis_file)
            elif agg == "RANGE":
                sub_result = Range(cohort_matrix, file_name, analysis_file)

            file = csv_file.objects.get(file_save=request.session['file_save'])
            new_analysis = analysis(
                file_id=file,
                analysis_type=agg,
                analysis_name=analysis_name,
                analysis_save=analysis_file
            )
            new_analysis.save()

        if agg == "RETENTION":
            # file_name = "20200502095912_NyZdIYj1"
            heat_num = to_heat_num(file_name, analysis_file)
            heat_percent = to_heat_percent(file_name, analysis_file)

            result['heat_num'] = heat_num
            result['heat_num']['title'] = analysis_name + "(line map)"
            result['heat_num']['type'] = "line"

            result['heat_percent'] = heat_percent
            result['heat_percent']['title'] = analysis_name + "(heat map)"
            result['heat_percent']['type'] = "heatmap"

        elif agg == "RANGE":
            range_num = to_range_num(file_name, analysis_file)

            result['range'] = range_num
            result['range']['title'] = analysis_name + "(range map)"
            result['range']['type'] = "range"

        # return render(request, "dashboard.html", {"figures":result})
        print("Result: ", result)
        return JsonResponse(result)

def Retention(cohort_matrix,file_name,analysis_name):
    # file_name = "20200502095912_NyZdIYj1.csv"

    # index = get_json(2)
    # print(index)
    index = cohort_matrix

    # file_name = "patient_records.csv"
    # input_path = "./example/" + file_name
    input_path = "./upload/" + file_name + ".csv"
    output_path = data_path + "/%s" % file_name


    with open(output_path+"/table.yaml") as f:
        type_data = yaml.load(f.read())
    for field in type_data['fields']:
        if field['fieldType'] == "ActionTime":
            time_name = field['name']
        elif field['fieldType'] == "UserKey":
            id_name = field['name']

    data = pd.read_csv(input_path)

    selected_users = data[id_name].unique()
    # print(len(selected_users))

    for value in index['user_selection']['events']:
        event = value['event']
        event_related = value[event]
        frequency_min = int(value['frequency']['min'])
        frequency_max = int(value['frequency']['max'])
        tem = data[data[event] == event_related]
        tem_user = tem[id_name].value_counts()
        if frequency_max != -1:
            tem_user = tem_user[(tem_user >= frequency_min) & (tem_user <= frequency_max)]
        else:
            tem_user = tem_user[(tem_user >= frequency_min)]
        selected_users = [i for i in selected_users if i in tem_user.index]

    # print(len(selected_users))

    for value in index['birth_criteria']['events']:
        event = value['event']
        event_related = value[event]
        frequency_min = int(value['frequency']['min'])
        frequency_max = int(value['frequency']['max'])
        tem = data[data[event] == event_related]
        tem_user = tem[id_name].value_counts()
        if frequency_max != -1:
            tem_user = tem_user[(tem_user >= frequency_min) & (tem_user <= frequency_max)]
        else:
            tem_user = tem_user[(tem_user >= frequency_min)]
        selected_users = [i for i in selected_users if i in tem_user.index]

    # print(len(selected_users))

    data = data[data[id_name].isin(selected_users)]
    # print(data)
    data[time_name] = pd.to_datetime(data[time_name])

    group_min = int(index['birth_criteria']["events"][0]['group_by']['min'])
    group_max = int(index['birth_criteria']["events"][0]['group_by']['max'])
    interval = int(index['birth_criteria']["events"][0]['group_by']['interval'])

    group_num = int((group_max - group_min) / interval)
    if group_num * interval + group_min != group_max:
        group_num += 1

    check_day_start = int(index['cohort_metrix']['age_range']['min'])
    check_day_end = int(index['cohort_metrix']['age_range']['max'])
    check_days = check_day_end - check_day_start + 1

    measure = index['cohort_metrix']['measure']

    start = group_min
    result = {}

    # print(len(data))

    for id in range(group_num):
        end = min(start + interval, group_max)
        # print(start,end)
        result[id] = {
            "group_min": start,
            "interval": interval,
            "num": 0,
            "check_days": check_days,
            "data": [0 for i in range(check_days)],
        }

        sub_data = data[(data[index['birth_criteria']["events"][0]['group_by']['name']] >= start) &
                        (data[index['birth_criteria']["events"][0]['group_by']['name']] < end)]
        sub_users = list(sub_data[id_name].unique())
        result[id]["num"] = len(sub_users)
        for user in sub_users:
            tem = sub_data[sub_data[id_name] == user]
            base_time_list = []
            for value in index['user_selection']['events']:
                event = value['event']
                event_related = value[event]
                frequency_min = int(value['frequency']['min'])
                temp = tem[tem[event] == event_related]
                base_time_list.append(list(temp[time_name])[frequency_min - 1])

            base_time = max(base_time_list)
            base_time_list = []
            for value in index['birth_criteria']['events']:
                event = value['event']
                event_related = value[event]
                frequency_min = int(value['frequency']['min'])
                frequency_max = int(value['frequency']['max'])
                temp = tem[(tem[event] == event_related) & (tem[time_name] >= base_time)]
                if len(list(temp[time_name])) < frequency_min:
                    break
                if frequency_max != -1 and len(list(temp[time_name])) >= frequency_max:
                    break
                base_time_list.append(list(temp[time_name])[frequency_min - 1])

            if base_time_list == []:
                continue

            base_time = max(base_time_list)

            value = index['cohort_metrix']['event']
            event = value['event']
            event_related = value[event]
            temp = tem[(tem[event] == event_related) & (tem[time_name] >= base_time)]
            if "value" in value.keys():
                value_min = float(value['value']['min'])
                value_max = float(value['value']['max'])
                for _, row in temp.iterrows():
                    if row['value'] >= value_min and row['value'] <= value_max:
                        day = int((row[time_name] - base_time) / datetime.timedelta(days=1))
                        if day < check_days:
                            result[id]["data"][day] += 1
        start += interval
    with open(output_path + "/%s.json" % analysis_name, 'w') as f:
        json.dump(result, cls=MyEncoder, fp=f)
    return result

def Range(cohort_matrix,file_name, analysis_name):
    # file_name = "20200502095912_NyZdIYj1.csv"

    # index = get_json(3)
    # print(index)
    index = cohort_matrix

    # file_name = "patient_records.csv"
    # input_path = "./example/" + file_name
    input_path = "./upload/" + file_name + ".csv"
    output_path = data_path + "/%s" % file_name


    with open(output_path+"/table.yaml") as f:
        type_data = yaml.load(f.read())
    for field in type_data['fields']:
        if field['fieldType'] == "ActionTime":
            time_name = field['name']
        elif field['fieldType'] == "UserKey":
            id_name = field['name']

    data = pd.read_csv(input_path)

    selected_users = data[id_name].unique()
    # print(len(selected_users))

    for value in index['user_selection']['events']:
        event = value['event']
        event_related = value[event]
        frequency_min = int(value['frequency']['min'])
        frequency_max = int(value['frequency']['max'])
        tem = data[data[event] == event_related]
        tem_user = tem[id_name].value_counts()
        if frequency_max != -1:
            tem_user = tem_user[(tem_user >= frequency_min) & (tem_user <= frequency_max)]
        else:
            tem_user = tem_user[(tem_user >= frequency_min)]
        selected_users = [i for i in selected_users if i in tem_user.index]

    # print(len(selected_users))

    for value in index['birth_criteria']['events']:
        event = value['event']
        event_related = value[event]
        frequency_min = int(value['frequency']['min'])
        frequency_max = int(value['frequency']['max'])
        tem = data[data[event] == event_related]
        tem_user = tem[id_name].value_counts()
        if frequency_max != -1:
            tem_user = tem_user[(tem_user >= frequency_min) & (tem_user <= frequency_max)]
        else:
            tem_user = tem_user[(tem_user >= frequency_min)]
        selected_users = [i for i in selected_users if i in tem_user.index]

    # print(len(selected_users))

    data = data[data[id_name].isin(selected_users)]
    # print(data)
    data[time_name] = pd.to_datetime(data[time_name])

    group_min = int(index['birth_criteria']["events"][0]['group_by']['min'])
    group_max = int(index['birth_criteria']["events"][0]['group_by']['max'])
    interval = int(index['birth_criteria']["events"][0]['group_by']['interval'])

    group_num = int((group_max-group_min+1)/interval)
    if group_num*interval+group_min < group_max:
        group_num+=1

    check_day_start = int(index['cohort_metrix']['age_range']['min'])
    check_day_end = int(index['cohort_metrix']['age_range']['max'])
    check_days = check_day_end-check_day_start+1


    measure = index['cohort_metrix']['measure']

    start = group_min
    result = {}
    for id in range(group_num):
        end = min(start+interval,group_max)
        # print(start,end)
        result[id] = {
            "group_min":start,
            "interval":interval,
            "num": 0,
            "check_days": check_days,
            "data": {}
        }
        if interval == 1:
            sub_data = data[(data[index['birth_criteria']["events"][0]['group_by']['name']] == start)]
        else:
            sub_data = data[(data[index['birth_criteria']["events"][0]['group_by']['name']]>=start)&
                            (data[index['birth_criteria']["events"][0]['group_by']['name']]<end)]
        sub_users = list(sub_data[id_name].unique())
        result[id]["num"] = len(sub_users)
        collection = [[] for i in range(check_days)]
        for user in sub_users:
            tem = sub_data[sub_data[id_name]==user]
            base_time_list = []
            for value in index['user_selection']['events']:
                event = value['event']
                event_related = value[event]
                frequency_min = int(value['frequency']['min'])
                temp = tem[tem[event]==event_related]
                base_time_list.append(list(temp[time_name])[frequency_min-1])

            base_time = max(base_time_list)
            base_time_list = []

            for value in index['birth_criteria']['events']:
                event = value['event']
                event_related = value[event]
                frequency_min = int(value['frequency']['min'])
                temp = tem[(tem[event]==event_related)&(tem[time_name]>=base_time)]
                if len(list(temp[time_name]))<frequency_min:
                    break
                base_time_list.append(list(temp[time_name])[frequency_min-1])

            if base_time_list == []:
                continue

            base_time = max(base_time_list)
            value = index['cohort_metrix']['event']
            event = value['event']
            event_related = value[event]
            temp = tem[(tem[event] == event_related) & (tem[time_name] >= base_time)]
            for _, row in temp.iterrows():
                day = int((row[time_name] - base_time) / datetime.timedelta(days=1))
                if day < check_days:
                    collection[day].append(row['value'])

        for i in range(check_days):
            if collection[i] == []:
                result[id]["data"][i]={}
            else:
                tem_result = {
                    "min": "%.2f"%min(collection[i]),
                    "avg": "%.2f"%np.average(collection[i]),
                    "max": "%.2f"%max(collection[i])
                }
                result[id]["data"][i]=tem_result

        start += interval

    # print(result)
    with open(output_path + "/%s.json" % analysis_name, 'w') as f:
        json.dump(result, cls=MyEncoder, fp=f)
    return result


def address(request,addr_id):
    return {}