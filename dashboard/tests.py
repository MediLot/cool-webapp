from django.test import TestCase

# Create your tests here.


# a = [1,2,3,'a']
# print(a)
#
# # while a != []:
# a.remove('a')
# print(a)

# import pandas as pd
#
# data = pd.read_csv("../../covid_web/example/patient_records.csv")
#
# data['time'] = pd.to_datetime(data['time'])
# data['time'] = data['time'].dt.strftime("%Y-%m-%d")
# data.to_csv("../../covid_web/example/patient_records.csv",index=False)
# print(data)


import json
import re
import numpy as np
# with open("../cohana/20200519180823RE90PlNK/20200520124425nbP2ZO7C.dat") as data_file:
#     data = json.load(data_file)
#
# # print(json.dumps(data, indent=4, separators=(',', ':')))
#
# print(data["data"]["values"])
# print(data["data"]["columes"])
# print(data["data"]["heatmap"])

# def to_line(data):
#     result = {}
#     result['y_label'] = data['data']['columes']
#     result['data'] = {}
#     for sub_data in data['data']["values"]:
#         result['data'][sub_data['name']] =
#
#
# to_line(data)

# a = [[7, 568.0], [6, 568.0], [5, 568.0], [4, 568.0], [3, 568.0], [2, 568.0], [1, 568.0], [0, 568.0]]
# a.reverse()
# print(a)
# b = [x[0] for x in a]

# null = "null"
# false = False
#
# # querry = {"dataSource":"20200519180823RE90PlNK","appKey":"fd1ec667-75a4-415d-a250-8fbb71be7cab","birthSequence":{"birthEvents":[{"minTrigger":1,"maxTrigger":1,"eventSelection":[{"fieldValue":{"type":"AbsoluteValue","values":["therapy"],"baseField":null,"baseEvent":-1},"filterType":"Set","cubeField":"medicine"}],"aggrSelection":[],"timeWindow":null,"cohortFields":[{"field":"age","numLevel":10,"minLevel":0,"logScale":false,"scale":10.0}]}]},"ageField":{"field":"time","unit":"DAY","ageInterval":1,"eventSelection":[],"range":["1|20"]},"ageSelection":[{"fieldValue":{"type":"AbsoluteValue","values":["labtest"],"baseField":null,"baseEvent":-1},"filterType":"Set","cubeField":"event"},{"fieldValue":{"type":"AbsoluteValue","values":["PCR"],"baseField":null,"baseEvent":-1},"filterType":"Set","cubeField":"labtest"},{"fieldValue":{"type":"AbsoluteValue","values":["0|100"],"baseField":null,"baseEvent":-1},"filterType":"Set","cubeField":"value"}],"measure":"example","inputCohort":"loyal","outputCohort":null,"userId":null}
# querry = {"dataSource":"20200520081235d1T3fBQb","appKey":"fd1ec667-75a4-415d-a250-8fbb71be7cab","birthSequence":{"birthEvents":[{"minTrigger":1,"maxTrigger":-1,"eventSelection":[{"fieldValue":{"type":"AbsoluteValue","values":["Medicine-A"],"baseField":null,"baseEvent":-1},"filterType":"Set","cubeField":"prescribe"}],"aggrSelection":[],"timeWindow":null,"cohortFields":[{"field":"birthyear","numLevel":5,"minLevel":195,"logScale":false,"scale":10.0}]}]},"ageField":{"field":"time","unit":"DAY","ageInterval":1,"eventSelection":[],"range":["1|7"]},"ageSelection":[{"fieldValue":{"type":"AbsoluteValue","values":["labtest"],"baseField":null,"baseEvent":-1},"filterType":"Set","cubeField":"event"},{"fieldValue":{"type":"AbsoluteValue","values":["Labtest-C"],"baseField":null,"baseEvent":-1},"filterType":"Set","cubeField":"labtest"},{"fieldValue":{"type":"AbsoluteValue","values":["0|100"],"baseField":null,"baseEvent":-1},"filterType":"Set","cubeField":"value"}],"measure":"example","inputCohort":"loyal","outputCohort":null,"userId":null}

# data = {"code": 200, "data": {"values": [{"name": "(40, 50]", "type": "line", "data": [[7, 179.0], [6, 201.0], [5, 243.0], [4, 286.0], [3, 339.0], [2, 402.0], [1, 472.0], [0, 568.0]]}, {"name": "(30, 40]", "type": "line", "data": [[7, 83.0], [6, 114.0], [5, 146.0], [4, 174.0], [3, 220.0], [2, 274.0], [1, 338.0], [0, 436.0]]}, {"name": "(20, 30]", "type": "line", "data": [[7, 100.0], [6, 122.0], [5, 144.0], [4, 187.0], [3, 215.0], [2, 268.0], [1, 332.0], [0, 409.0]]}, {"name": "(50, 60]", "type": "line", "data": [[7, 120.0], [6, 140.0], [5, 171.0], [4, 199.0], [3, 232.0], [2, 282.0], [1, 338.0], [0, 389.0]]}, {"name": "(60, 70]", "type": "line", "data": [[7, 201.0], [6, 214.0], [5, 230.0], [4, 241.0], [3, 252.0], [2, 266.0], [1, 281.0], [0, 291.0]]}, {"name": "(70, 80]", "type": "line", "data": [[7, 128.0], [6, 131.0], [5, 137.0], [4, 144.0], [3, 153.0], [2, 158.0], [1, 166.0], [0, 177.0]]}, {"name": "(10, 20]", "type": "line", "data": [[7, 28.0], [6, 37.0], [5, 49.0], [4, 54.0], [3, 82.0], [2, 99.0], [1, 124.0], [0, 152.0]]}, {"name": "(80, 90]", "type": "line", "data": [[7, 106.0], [6, 110.0], [5, 117.0], [4, 125.0], [3, 130.0], [2, 135.0], [1, 142.0], [0, 146.0]]}, {"name": "(0, 10]", "type": "line", "data": [[7, 25.0], [6, 29.0], [5, 32.0], [4, 39.0], [3, 49.0], [2, 61.0], [1, 78.0], [0, 93.0]]}, {"name": "(90, 100]", "type": "line", "data": [[7, 33.0], [6, 33.0], [5, 36.0], [4, 38.0], [3, 38.0], [2, 40.0], [1, 42.0], [0, 48.0]]}, {"name": "(-inf, 0]", "type": "line", "data": [[7, 3.0], [6, 3.0], [5, 4.0], [4, 5.0], [3, 6.0], [2, 8.0], [1, 12.0], [0, 13.0]]}, {"name": "(100, inf", "type": "line", "data": [[6, 1.0], [5, 1.0], [4, 1.0], [3, 1.0], [2, 1.0], [1, 1.0], [0, 1.0]]}], "columes": ["(40, 50]", "(30, 40]", "(20, 30]", "(50, 60]", "(60, 70]", "(70, 80]", "(10, 20]", "(80, 90]", "(0, 10]", "(90, 100]", "(-inf, 0]", "(100, inf"], "heatmap": [[0, 11, 100], [1, 11, 83], [2, 11, 70], [3, 11, 59], [4, 11, 50], [5, 11, 42], [6, 11, 35], [7, 11, 31], [0, 10, 100], [1, 10, 77], [2, 10, 62], [3, 10, 50], [4, 10, 39], [5, 10, 33], [6, 10, 26], [7, 10, 19], [0, 9, 100], [1, 9, 81], [2, 9, 65], [3, 9, 52], [4, 9, 45], [5, 9, 35], [6, 9, 29], [7, 9, 24], [0, 8, 100], [1, 8, 86], [2, 8, 72], [3, 8, 59], [4, 8, 51], [5, 8, 43], [6, 8, 35], [7, 8, 30], [0, 7, 100], [1, 7, 96], [2, 7, 91], [3, 7, 86], [4, 7, 82], [5, 7, 79], [6, 7, 73], [7, 7, 69], [0, 6, 100], [1, 6, 93], [2, 6, 89], [3, 6, 86], [4, 6, 81], [5, 6, 77], [6, 6, 74], [7, 6, 72], [0, 5, 100], [1, 5, 81], [2, 5, 65], [3, 5, 53], [4, 5, 35], [5, 5, 32], [6, 5, 24], [7, 5, 18], [0, 4, 100], [1, 4, 97], [2, 4, 92], [3, 4, 89], [4, 4, 85], [5, 4, 80], [6, 4, 75], [7, 4, 72], [0, 3, 100], [1, 3, 83], [2, 3, 65], [3, 3, 52], [4, 3, 41], [5, 3, 34], [6, 3, 31], [7, 3, 26], [0, 2, 100], [1, 2, 87], [2, 2, 83], [3, 2, 79], [4, 2, 79], [5, 2, 75], [6, 2, 68], [7, 2, 68], [0, 1, 100], [1, 1, 92], [2, 1, 61], [3, 1, 46], [4, 1, 38], [5, 1, 30], [6, 1, 23], [7, 1, 23], [0, 0, 100], [1, 0, 100], [2, 0, 100], [3, 0, 100], [4, 0, 100], [5, 0, 100], [6, 0, 100]]}}
# print(json.dumps(data, indent=4, separators=(',', ':')))

import requests

def pass_request(query, server="http://localhost:8200"):
    headers = { \
            'Connection':'keep-alive', \
            'Cookie':'', \
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36', \
            'Content-Type':'application/json', \
            'Accept' :'*/*'
            }

    datasource = '2017-10-15_18:34'
    r = requests.get(server + '/v1/reload?cube=' + datasource, headers=headers)
    print(r.text)

    requests.get(server+'/v1/cohort/manage/remove/' + 'loyal')

    query1 = {u'birthSequence': {u'birthEvents': [{u'maxTrigger': -1, u'timeWindow': {u'length': 7, u'slice': False, u'unit': u'DAY'}, u'minTrigger': 1, u'eventSelection': [{u'filterType': u'Set', u'cubeField': u'event', u'fieldValue': {u'values': [u'diagnose'], u'type': u'AbsoluteValue', u'baseField': None, u'baseEvent': -1}}, {u'filterType': u'Set', u'cubeField': u'disease', u'fieldValue': {u'values': [u'Disease-B'], u'type': u'AbsoluteValue', u'baseField': None, u'baseEvent': -1}}]}]}, u'outputCohort': u'loyal', u'dataSource': u'2017-10-15_18:34'}
    print(json.dumps(query1, indent=4, separators=(',', ':')))
    r = requests.post(server+'/v1/cohort/manage/create', data = json.dumps(query1), headers = headers)
    print(r.text)

    # query2 = {u'appKey': u'fd1ec667-75a4-415d-a250-8fbb71be7cab', u'birthSequence': {u'birthEvents': [{u'cohortFields': [{u'logScale': False, u'field': u'birthyear', u'numLevel': 5, u'scale': 10, u'minLevel': 195}], u'maxTrigger': -1, u'minTrigger': 1, u'eventSelection': [{u'filterType': u'Set', u'cubeField': u'event', u'fieldValue': {u'values': [u'prescribe'], u'type': u'AbsoluteValue', u'baseField': None, u'baseEvent': -1}}, {u'filterType': u'Set', u'cubeField': u'medicine', u'fieldValue': {u'values': [u'Medicine-A'], u'type': u'AbsoluteValue', u'baseField': None, u'baseEvent': -1}}]}]}, u'ageSelection': [{u'filterType': u'Set', u'cubeField': u'event', u'fieldValue': {u'values': [u'labtest'], u'type': u'AbsoluteValue', u'baseField': None, u'baseEvent': -1}}, {u'filterType': u'Set', u'cubeField': u'labtest', u'fieldValue': {u'values': [u'Labtest-C'], u'type': u'AbsoluteValue', u'baseField': None, u'baseEvent': -1}}, {u'filterType': u'Set', u'cubeField': u'value', u'fieldValue': {u'values': [u'45|100'], u'type': u'AbsoluteValue', u'baseField': None, u'baseEvent': -1}}], u'dataSource': datasource, u'measure': u'id-RETENTION', u'inputCohort': u'loyal', u'ageField': {u'field': u' time', u'range': [u'1|7'], u'ageInterval': 1}}
    query2 = {u'appKey': u'fd1ec667-75a4-415d-a250-8fbb71be7cab', u'birthSequence': {u'birthEvents': [{u'cohortFields': [{u'logScale': False, u'field': u'birthyear', u'numLevel': 5, u'scale': 10, u'minLevel': 195}], u'maxTrigger': -1, u'minTrigger': 1, u'eventSelection': [{u'filterType': u'Set', u'cubeField': u'event', u'fieldValue': {u'values': [u'prescribe'], u'type': u'AbsoluteValue', u'baseField': None, u'baseEvent': -1}}, {u'filterType': u'Set', u'cubeField': u'medicine', u'fieldValue': {u'values': [u'Medicine-A'], u'type': u'AbsoluteValue', u'baseField': None, u'baseEvent': -1}}]}]}, u'ageSelection': [{u'filterType': u'Set', u'cubeField': u'event', u'fieldValue': {u'values': [u'labtest'], u'type': u'AbsoluteValue', u'baseField': None, u'baseEvent': -1}}, {u'filterType': u'Set', u'cubeField': u'labtest', u'fieldValue': {u'values': [u'Labtest-C'], u'type': u'AbsoluteValue', u'baseField': None, u'baseEvent': -1}}, {u'filterType': u'Set', u'cubeField': u'value', u'fieldValue': {u'values': [u'0|100'], u'type': u'AbsoluteValue', u'baseField': None, u'baseEvent': -1}}], u'dataSource': datasource, u'measure': u'id-RETENTION', u'inputCohort': u'loyal', u'ageField': {u'field': u' time', u'range': [u'1|7'], u'ageInterval': 1}}
    print(json.dumps(query2, indent=4, separators=(',', ':')))

    print(query2)
    print("**" * 30)

    r = requests.post(server+'/v1/cohort/analysis', data = json.dumps(query2), headers = headers)
    print(r.text)
    # return json.loads(r.text)

# pass_request("")

def pass_request2(query, server="http://localhost:8200"):
    headers = { \
            'Connection':'keep-alive', \
            'Cookie':'', \
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36', \
            'Content-Type':'application/json', \
            'Accept' :'*/*'
            }

    datasource = '20200525161811C8249HVY'
    r = requests.get(server + '/v1/reload?cube=' + datasource, headers=headers)
    print(r.text)

    requests.get(server+'/v1/cohort/manage/remove/' + 'loyal')

    query1 = {'birthSequence': {'birthEvents': [{'eventSelection': [{'fieldValue': {'type': 'AbsoluteValue', 'values': ['covid-I'], 'baseField': None, 'baseEvent': -1}, 'cubeField': 'disease', 'filterType': 'Set'}], 'timeWindow': {'length': 7, 'slice': False, 'unit': 'DAY'}, 'minTrigger': 1, 'maxTrigger': -1}]}, 'outputCohort': 'loyal', 'dataSource': datasource}
    print(json.dumps(query1, indent=4, separators=(',', ':')))
    r = requests.post(server+'/v1/cohort/manage/create', data = json.dumps(query1), headers = headers)
    print(r.text)

    query2 = {'appKey': 'fd1ec667-75a4-415d-a250-8fbb71be7cab', 'birthSequence': {'birthEvents': [{'eventSelection': [{'fieldValue': {'type': 'AbsoluteValue', 'values': ['therapy'], 'baseField': None, 'baseEvent': -1}, 'cubeField': 'medicine', 'filterType': 'Set'}], 'cohortFields': [{'numLevel': 10, 'minLevel': 0, 'logScale': False, 'scale': 10, 'field': 'age'}], 'minTrigger': 1, 'maxTrigger': 1}]}, 'dataSource': datasource, 'measure': 'example', 'ageField': {'range': ['1|20'], 'ageInterval': 1, 'field': 'time'}, 'ageSelection': [{'fieldValue': {'type': 'AbsoluteValue', 'values': ['labtest'], 'baseField': None, 'baseEvent': -1}, 'cubeField': 'event', 'filterType': 'Set'}, {'fieldValue': {'type': 'AbsoluteValue', 'values': ['PCR'], 'baseField': None, 'baseEvent': -1}, 'cubeField': 'labtest', 'filterType': 'Set'}, {'fieldValue': {'type': 'AbsoluteValue', 'values': ['1|1'], 'baseField': None, 'baseEvent': -1}, 'cubeField': 'value', 'filterType': 'Set'}], 'inputCohort': 'loyal'}

    print(json.dumps(query2, indent=4, separators=(',', ':')))

    print(query2)
    print("**" * 30)

    r = requests.post(server+'/v1/cohort/analysis', data = json.dumps(query2), headers = headers)
    print(r.text)
    # return json.loads(r.text)
    return r.text

# pass_request2("")


def transfer():
    rawdata = {
  "status" : "OK",
  "result" : [ {
    "cohort" : "((0, 10])",
    "age" : 0,
    "measure" : 93.0
  }, {
    "cohort" : "((0, 10])",
    "age" : 1,
    "measure" : 78.0
  }, {
    "cohort" : "((0, 10])",
    "age" : 2,
    "measure" : 61.0
  }, {
    "cohort" : "((0, 10])",
    "age" : 3,
    "measure" : 49.0
  }, {
    "cohort" : "((0, 10])",
    "age" : 4,
    "measure" : 39.0
  }, {
    "cohort" : "((0, 10])",
    "age" : 5,
    "measure" : 32.0
  }, {
    "cohort" : "((0, 10])",
    "age" : 6,
    "measure" : 29.0
  }, {
    "cohort" : "((0, 10])",
    "age" : 7,
    "measure" : 25.0
  }, {
    "cohort" : "((0, 10])",
    "age" : 8,
    "measure" : 19.0
  }, {
    "cohort" : "((0, 10])",
    "age" : 9,
    "measure" : 15.0
  }, {
    "cohort" : "((0, 10])",
    "age" : 10,
    "measure" : 13.0
  }, {
    "cohort" : "((0, 10])",
    "age" : 11,
    "measure" : 13.0
  }, {
    "cohort" : "((0, 10])",
    "age" : 12,
    "measure" : 11.0
  }, {
    "cohort" : "((0, 10])",
    "age" : 13,
    "measure" : 8.0
  }, {
    "cohort" : "((0, 10])",
    "age" : 14,
    "measure" : 8.0
  }, {
    "cohort" : "((0, 10])",
    "age" : 15,
    "measure" : 7.0
  }, {
    "cohort" : "((10, 20])",
    "age" : 0,
    "measure" : 152.0
  }, {
    "cohort" : "((10, 20])",
    "age" : 1,
    "measure" : 124.0
  }, {
    "cohort" : "((10, 20])",
    "age" : 2,
    "measure" : 99.0
  }, {
    "cohort" : "((10, 20])",
    "age" : 3,
    "measure" : 82.0
  }, {
    "cohort" : "((10, 20])",
    "age" : 4,
    "measure" : 54.0
  }, {
    "cohort" : "((10, 20])",
    "age" : 5,
    "measure" : 49.0
  }, {
    "cohort" : "((10, 20])",
    "age" : 6,
    "measure" : 37.0
  }, {
    "cohort" : "((10, 20])",
    "age" : 7,
    "measure" : 28.0
  }, {
    "cohort" : "((10, 20])",
    "age" : 8,
    "measure" : 18.0
  }, {
    "cohort" : "((10, 20])",
    "age" : 9,
    "measure" : 16.0
  }, {
    "cohort" : "((10, 20])",
    "age" : 10,
    "measure" : 13.0
  }, {
    "cohort" : "((10, 20])",
    "age" : 11,
    "measure" : 12.0
  }, {
    "cohort" : "((10, 20])",
    "age" : 12,
    "measure" : 9.0
  }, {
    "cohort" : "((10, 20])",
    "age" : 13,
    "measure" : 8.0
  }, {
    "cohort" : "((10, 20])",
    "age" : 14,
    "measure" : 6.0
  }, {
    "cohort" : "((10, 20])",
    "age" : 15,
    "measure" : 6.0
  }, {
    "cohort" : "((20, 30])",
    "age" : 0,
    "measure" : 409.0
  }, {
    "cohort" : "((20, 30])",
    "age" : 1,
    "measure" : 332.0
  }, {
    "cohort" : "((20, 30])",
    "age" : 2,
    "measure" : 268.0
  }, {
    "cohort" : "((20, 30])",
    "age" : 3,
    "measure" : 215.0
  }, {
    "cohort" : "((20, 30])",
    "age" : 4,
    "measure" : 187.0
  }, {
    "cohort" : "((20, 30])",
    "age" : 5,
    "measure" : 144.0
  }, {
    "cohort" : "((20, 30])",
    "age" : 6,
    "measure" : 122.0
  }, {
    "cohort" : "((20, 30])",
    "age" : 7,
    "measure" : 100.0
  }, {
    "cohort" : "((20, 30])",
    "age" : 8,
    "measure" : 82.0
  }, {
    "cohort" : "((20, 30])",
    "age" : 9,
    "measure" : 68.0
  }, {
    "cohort" : "((20, 30])",
    "age" : 10,
    "measure" : 56.0
  }, {
    "cohort" : "((20, 30])",
    "age" : 11,
    "measure" : 47.0
  }, {
    "cohort" : "((20, 30])",
    "age" : 12,
    "measure" : 39.0
  }, {
    "cohort" : "((20, 30])",
    "age" : 13,
    "measure" : 31.0
  }, {
    "cohort" : "((20, 30])",
    "age" : 14,
    "measure" : 26.0
  }, {
    "cohort" : "((20, 30])",
    "age" : 15,
    "measure" : 24.0
  }, {
    "cohort" : "((30, 40])",
    "age" : 0,
    "measure" : 436.0
  }, {
    "cohort" : "((30, 40])",
    "age" : 1,
    "measure" : 338.0
  }, {
    "cohort" : "((30, 40])",
    "age" : 2,
    "measure" : 274.0
  }, {
    "cohort" : "((30, 40])",
    "age" : 3,
    "measure" : 220.0
  }, {
    "cohort" : "((30, 40])",
    "age" : 4,
    "measure" : 174.0
  }, {
    "cohort" : "((30, 40])",
    "age" : 5,
    "measure" : 146.0
  }, {
    "cohort" : "((30, 40])",
    "age" : 6,
    "measure" : 114.0
  }, {
    "cohort" : "((30, 40])",
    "age" : 7,
    "measure" : 83.0
  }, {
    "cohort" : "((30, 40])",
    "age" : 8,
    "measure" : 66.0
  }, {
    "cohort" : "((30, 40])",
    "age" : 9,
    "measure" : 50.0
  }, {
    "cohort" : "((30, 40])",
    "age" : 10,
    "measure" : 43.0
  }, {
    "cohort" : "((30, 40])",
    "age" : 11,
    "measure" : 36.0
  }, {
    "cohort" : "((30, 40])",
    "age" : 12,
    "measure" : 27.0
  }, {
    "cohort" : "((30, 40])",
    "age" : 13,
    "measure" : 23.0
  }, {
    "cohort" : "((30, 40])",
    "age" : 14,
    "measure" : 18.0
  }, {
    "cohort" : "((30, 40])",
    "age" : 15,
    "measure" : 13.0
  }, {
    "cohort" : "((40, 50])",
    "age" : 0,
    "measure" : 568.0
  }, {
    "cohort" : "((40, 50])",
    "age" : 1,
    "measure" : 472.0
  }, {
    "cohort" : "((40, 50])",
    "age" : 2,
    "measure" : 402.0
  }, {
    "cohort" : "((40, 50])",
    "age" : 3,
    "measure" : 339.0
  }, {
    "cohort" : "((40, 50])",
    "age" : 4,
    "measure" : 286.0
  }, {
    "cohort" : "((40, 50])",
    "age" : 5,
    "measure" : 243.0
  }, {
    "cohort" : "((40, 50])",
    "age" : 6,
    "measure" : 201.0
  }, {
    "cohort" : "((40, 50])",
    "age" : 7,
    "measure" : 179.0
  }, {
    "cohort" : "((40, 50])",
    "age" : 8,
    "measure" : 146.0
  }, {
    "cohort" : "((40, 50])",
    "age" : 9,
    "measure" : 124.0
  }, {
    "cohort" : "((40, 50])",
    "age" : 10,
    "measure" : 108.0
  }, {
    "cohort" : "((40, 50])",
    "age" : 11,
    "measure" : 88.0
  }, {
    "cohort" : "((40, 50])",
    "age" : 12,
    "measure" : 79.0
  }, {
    "cohort" : "((40, 50])",
    "age" : 13,
    "measure" : 64.0
  }, {
    "cohort" : "((40, 50])",
    "age" : 14,
    "measure" : 54.0
  }, {
    "cohort" : "((40, 50])",
    "age" : 15,
    "measure" : 51.0
  }, {
    "cohort" : "((50, 60])",
    "age" : 0,
    "measure" : 389.0
  }, {
    "cohort" : "((50, 60])",
    "age" : 1,
    "measure" : 338.0
  }, {
    "cohort" : "((50, 60])",
    "age" : 2,
    "measure" : 282.0
  }, {
    "cohort" : "((50, 60])",
    "age" : 3,
    "measure" : 232.0
  }, {
    "cohort" : "((50, 60])",
    "age" : 4,
    "measure" : 199.0
  }, {
    "cohort" : "((50, 60])",
    "age" : 5,
    "measure" : 171.0
  }, {
    "cohort" : "((50, 60])",
    "age" : 6,
    "measure" : 140.0
  }, {
    "cohort" : "((50, 60])",
    "age" : 7,
    "measure" : 120.0
  }, {
    "cohort" : "((50, 60])",
    "age" : 8,
    "measure" : 104.0
  }, {
    "cohort" : "((50, 60])",
    "age" : 9,
    "measure" : 90.0
  }, {
    "cohort" : "((50, 60])",
    "age" : 10,
    "measure" : 81.0
  }, {
    "cohort" : "((50, 60])",
    "age" : 11,
    "measure" : 68.0
  }, {
    "cohort" : "((50, 60])",
    "age" : 12,
    "measure" : 57.0
  }, {
    "cohort" : "((50, 60])",
    "age" : 13,
    "measure" : 49.0
  }, {
    "cohort" : "((50, 60])",
    "age" : 14,
    "measure" : 47.0
  }, {
    "cohort" : "((50, 60])",
    "age" : 15,
    "measure" : 45.0
  }, {
    "cohort" : "((60, 70])",
    "age" : 0,
    "measure" : 291.0
  }, {
    "cohort" : "((60, 70])",
    "age" : 1,
    "measure" : 281.0
  }, {
    "cohort" : "((60, 70])",
    "age" : 2,
    "measure" : 266.0
  }, {
    "cohort" : "((60, 70])",
    "age" : 3,
    "measure" : 252.0
  }, {
    "cohort" : "((60, 70])",
    "age" : 4,
    "measure" : 241.0
  }, {
    "cohort" : "((60, 70])",
    "age" : 5,
    "measure" : 230.0
  }, {
    "cohort" : "((60, 70])",
    "age" : 6,
    "measure" : 214.0
  }, {
    "cohort" : "((60, 70])",
    "age" : 7,
    "measure" : 201.0
  }, {
    "cohort" : "((60, 70])",
    "age" : 8,
    "measure" : 192.0
  }, {
    "cohort" : "((60, 70])",
    "age" : 9,
    "measure" : 185.0
  }, {
    "cohort" : "((60, 70])",
    "age" : 10,
    "measure" : 175.0
  }, {
    "cohort" : "((60, 70])",
    "age" : 11,
    "measure" : 168.0
  }, {
    "cohort" : "((60, 70])",
    "age" : 12,
    "measure" : 163.0
  }, {
    "cohort" : "((60, 70])",
    "age" : 13,
    "measure" : 156.0
  }, {
    "cohort" : "((60, 70])",
    "age" : 14,
    "measure" : 150.0
  }, {
    "cohort" : "((60, 70])",
    "age" : 15,
    "measure" : 140.0
  }, {
    "cohort" : "((70, 80])",
    "age" : 0,
    "measure" : 177.0
  }, {
    "cohort" : "((70, 80])",
    "age" : 1,
    "measure" : 166.0
  }, {
    "cohort" : "((70, 80])",
    "age" : 2,
    "measure" : 158.0
  }, {
    "cohort" : "((70, 80])",
    "age" : 3,
    "measure" : 153.0
  }, {
    "cohort" : "((70, 80])",
    "age" : 4,
    "measure" : 144.0
  }, {
    "cohort" : "((70, 80])",
    "age" : 5,
    "measure" : 137.0
  }, {
    "cohort" : "((70, 80])",
    "age" : 6,
    "measure" : 131.0
  }, {
    "cohort" : "((70, 80])",
    "age" : 7,
    "measure" : 128.0
  }, {
    "cohort" : "((70, 80])",
    "age" : 8,
    "measure" : 121.0
  }, {
    "cohort" : "((70, 80])",
    "age" : 9,
    "measure" : 116.0
  }, {
    "cohort" : "((70, 80])",
    "age" : 10,
    "measure" : 114.0
  }, {
    "cohort" : "((70, 80])",
    "age" : 11,
    "measure" : 108.0
  }, {
    "cohort" : "((70, 80])",
    "age" : 12,
    "measure" : 105.0
  }, {
    "cohort" : "((70, 80])",
    "age" : 13,
    "measure" : 98.0
  }, {
    "cohort" : "((70, 80])",
    "age" : 14,
    "measure" : 93.0
  }, {
    "cohort" : "((70, 80])",
    "age" : 15,
    "measure" : 89.0
  }, {
    "cohort" : "((80, 90])",
    "age" : 0,
    "measure" : 146.0
  }, {
    "cohort" : "((80, 90])",
    "age" : 1,
    "measure" : 142.0
  }, {
    "cohort" : "((80, 90])",
    "age" : 2,
    "measure" : 135.0
  }, {
    "cohort" : "((80, 90])",
    "age" : 3,
    "measure" : 130.0
  }, {
    "cohort" : "((80, 90])",
    "age" : 4,
    "measure" : 125.0
  }, {
    "cohort" : "((80, 90])",
    "age" : 5,
    "measure" : 117.0
  }, {
    "cohort" : "((80, 90])",
    "age" : 6,
    "measure" : 110.0
  }, {
    "cohort" : "((80, 90])",
    "age" : 7,
    "measure" : 106.0
  }, {
    "cohort" : "((80, 90])",
    "age" : 8,
    "measure" : 102.0
  }, {
    "cohort" : "((80, 90])",
    "age" : 9,
    "measure" : 99.0
  }, {
    "cohort" : "((80, 90])",
    "age" : 10,
    "measure" : 95.0
  }, {
    "cohort" : "((80, 90])",
    "age" : 11,
    "measure" : 94.0
  }, {
    "cohort" : "((80, 90])",
    "age" : 12,
    "measure" : 87.0
  }, {
    "cohort" : "((80, 90])",
    "age" : 13,
    "measure" : 85.0
  }, {
    "cohort" : "((80, 90])",
    "age" : 14,
    "measure" : 76.0
  }, {
    "cohort" : "((80, 90])",
    "age" : 15,
    "measure" : 72.0
  }, {
    "cohort" : "((90, inf))",
    "age" : 0,
    "measure" : 49.0
  }, {
    "cohort" : "((90, inf))",
    "age" : 1,
    "measure" : 43.0
  }, {
    "cohort" : "((90, inf))",
    "age" : 2,
    "measure" : 41.0
  }, {
    "cohort" : "((90, inf))",
    "age" : 3,
    "measure" : 39.0
  }, {
    "cohort" : "((90, inf))",
    "age" : 4,
    "measure" : 39.0
  }, {
    "cohort" : "((90, inf))",
    "age" : 5,
    "measure" : 37.0
  }, {
    "cohort" : "((90, inf))",
    "age" : 6,
    "measure" : 34.0
  }, {
    "cohort" : "((90, inf))",
    "age" : 7,
    "measure" : 33.0
  }, {
    "cohort" : "((90, inf))",
    "age" : 8,
    "measure" : 29.0
  }, {
    "cohort" : "((90, inf))",
    "age" : 9,
    "measure" : 25.0
  }, {
    "cohort" : "((90, inf))",
    "age" : 10,
    "measure" : 23.0
  }, {
    "cohort" : "((90, inf))",
    "age" : 11,
    "measure" : 22.0
  }, {
    "cohort" : "((90, inf))",
    "age" : 12,
    "measure" : 21.0
  }, {
    "cohort" : "((90, inf))",
    "age" : 13,
    "measure" : 20.0
  }, {
    "cohort" : "((90, inf))",
    "age" : 14,
    "measure" : 19.0
  }, {
    "cohort" : "((90, inf))",
    "age" : 15,
    "measure" : 18.0
  }, {
    "cohort" : "((-inf, 0])",
    "age" : 0,
    "measure" : 13.0
  }, {
    "cohort" : "((-inf, 0])",
    "age" : 1,
    "measure" : 12.0
  }, {
    "cohort" : "((-inf, 0])",
    "age" : 2,
    "measure" : 8.0
  }, {
    "cohort" : "((-inf, 0])",
    "age" : 3,
    "measure" : 6.0
  }, {
    "cohort" : "((-inf, 0])",
    "age" : 4,
    "measure" : 5.0
  }, {
    "cohort" : "((-inf, 0])",
    "age" : 5,
    "measure" : 4.0
  }, {
    "cohort" : "((-inf, 0])",
    "age" : 6,
    "measure" : 3.0
  }, {
    "cohort" : "((-inf, 0])",
    "age" : 7,
    "measure" : 3.0
  }, {
    "cohort" : "((-inf, 0])",
    "age" : 8,
    "measure" : 2.0
  }, {
    "cohort" : "((-inf, 0])",
    "age" : 9,
    "measure" : 2.0
  }, {
    "cohort" : "((-inf, 0])",
    "age" : 10,
    "measure" : 2.0
  }, {
    "cohort" : "((-inf, 0])",
    "age" : 11,
    "measure" : 1.0
  }, {
    "cohort" : "((-inf, 0])",
    "age" : 12,
    "measure" : 1.0
  }, {
    "cohort" : "((-inf, 0])",
    "age" : 13,
    "measure" : 1.0
  } ],
  "elapsedInMS" : 11
}
    # print(json.dumps(data, indent=4, separators=(',', ':')))
    # print(data['result'])

    # y_label = []
    # line_data = {}
    # for sub_result in rawdata['result']:
    #     if sub_result['cohort'] not in y_label:
    #         y_label.append(sub_result['cohort'])
    #         line_data[sub_result['cohort']] = []
    #     line_data[sub_result['cohort']].append([sub_result['age'],sub_result['measure']])
    #
    # lens = []
    # for k,v in line_data.items():
    #     lens.append(len(v))
    # x_label = list(range(max(lens)))
    # line_figure = {
    #     "x_label": x_label,
    #     "y_label": y_label,
    #     "data":line_data
    # }
    # print(line_figure)
    #
    # y_label = []
    # heatmap_data = []
    # count = 0
    # full_data = []
    # for k, v in line_data.items():
    #     y_label.append(k)
    #     for sub_data in v:
    #         if sub_data[0] == 0:
    #             init = sub_data[1]
    #     for sub_data in v:
    #         full_data.append((sub_data[1] / init * 100))
    #         heatmap_data.append([count, sub_data[0], "%.2f" % (sub_data[1] / init * 100)])
    #     count += 1
    #
    # heatmap_figure = {
    #     "x_label": x_label,
    #     "y_label": y_label,
    #     "data": heatmap_data,
    #     "min": min(full_data),
    #     "max": max(full_data),
    # }
    # print(heatmap_figure)

    rawResult = rawdata[u'result']
    col = []
    data = {}
    series = []
    heat = []

    top = 20
    # r0 = sorted(rawResult, key=lambda x: x[u'measure'], reverse=True)
    r0 = rawResult
    for i in range(0, top):
        for r in r0:
            cohort = re.findall(r"\((.+?)\)", r[u'cohort'])[0]
            if cohort not in col:
                col.append(cohort)
                data[cohort] = []
                break
    top = len(col)

    for r in rawResult:
    # for r in sorted(rawResult, key=lambda x: x[u'age'], reverse=True):
        cohort = re.findall(r"\((.+?)\)", r[u'cohort'])[0]
        if cohort in col:
            age = r[u'age']
            notFound = True
            for d in data[cohort]:
                if d[0] == age:
                    d[1] = d[1] + r[u'measure']
                    notFound = False
            if notFound:
                pair = []
                pair.append(age)
                pair.append(r[u'measure'])
                data[cohort].append(pair)
                data[cohort].reverse()
    for cohort in col:
        line = {}
        line['name'] = cohort
        line['type'] = 'line'
        line['data'] = data[cohort]
        series.append(line)
        index = col.index(cohort)
        data0 = sorted(data[cohort], key=lambda x: x[0])
        # prev = data0[0][1]
        # print(data0)

        for x in data0:
            heat.append([index, x[0] , int(x[1] / data0[0][1] * 100)])
            # heat.append([x[0], index, x[1]])
            # prev = x[1]

    ret = {'values': series, 'columes': col, 'heatmap': heat}
    print(series)
    print(col)
    print(heat)
    # return ret


transfer()