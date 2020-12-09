import json
import requests

# SERVER = 'http://127.0.0.1:9998'
SERVER = 'http://127.0.0.1:8200'
# SERVER = 'http://172.17.0.2:9998'

def pass_reload(datasource, server=SERVER):
    headers = { \
            'Connection':'keep-alive', \
            'Cookie':'', \
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36', \
            'Content-Type':'application/json', \
            'Accept' :'*/*'
            }
    r = requests.get(server+'/v1/reload?cube='+datasource, headers = headers)
    return json.loads(r.text)

def removeCohort(cohort, server=SERVER):
    url = server+'/v1/cohort/manage/remove/' + cohort
    print("Remove cohort: "+url)
    r = requests.get(url)
    return r.status_code

def pass_create_request(query, server=SERVER):
    headers = { \
            'Connection':'keep-alive', \
            'Cookie':'', \
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36', \
            'Content-Type':'application/json', \
            'Accept' :'*/*'
            }
    print("Create request:" + json.dumps(query))
    r = requests.post(server+'/v1/cohort/manage/create', data = json.dumps(query), headers = headers)
    print("Create response:" + r.text)
    return json.loads(r.text)

def pass_request(query, server=SERVER):
    headers = { \
            'Connection':'keep-alive', \
            'Cookie':'', \
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36', \
            'Content-Type':'application/json', \
            'Accept' :'*/*'
            }
    print("Request: " + json.dumps(query))
    r = requests.post(server+'/v1/cohort/analysis',data = json.dumps(query), headers = headers)
    print("Response: " + r.text)
    return json.loads(r.text)

def main():
    import numpy as np
    # test case 2: for the patient_records database
    pass_reload("20201204215934vFgT6yWA")
    removeCohort("loyal")
    q = '{"birthSequence": {"birthEvents": [{"eventSelection": [{"fieldValue": {"type": "AbsoluteValue", "values": ["Disease-B"], "baseField": null, "baseEvent": -1}, "cubeField": "diagnose", "filterType": "Set"}], "timeWindow": {"length": 7, "slice": false, "unit": "DAY"}, "minTrigger": 1, "maxTrigger": -1}]}, "outputCohort": "loyal", "dataSource": "20201204215934vFgT6yWA"}'
    pass_create_request(json.loads(q))
    q = '{"appKey": "fd1ec667-75a4-415d-a250-8fbb71be7cab", "birthSequence": {"birthEvents": [{"eventSelection": [{"fieldValue": {"type": "AbsoluteValue", "values": ["Medicine-A"], "baseField": null, "baseEvent": -1}, "cubeField": "prescribe", "filterType": "Set"}], "cohortFields": [{"numLevel": 5, "minLevel": 195, "logScale": false, "scale": 10, "field": "birthyear"}], "minTrigger": 1, "maxTrigger": -1}]}, "dataSource": "20201204215934vFgT6yWA", "measure": "example 10", "ageField": {"range": ["0|15"], "ageInterval": 1, "field": "time"}, "ageSelection": [{"fieldValue": {"type": "AbsoluteValue", "values": ["Labtest-C"], "baseField": null, "baseEvent": -1}, "cubeField": "labtest", "filterType": "Set"}, {"fieldValue": {"type": "AbsoluteValue", "values": ["45|130"], "baseField": null, "baseEvent": -1}, "cubeField": "value", "filterType": "Set"}], "inputCohort": "loyal"}'
    result = pass_request(json.loads(q))

    # test case 1: for the example database
    # pass_reload("20201127150305YK6WcNVH")
    # removeCohort("loyal")
    # q = '{"birthSequence": {"birthEvents": [{"eventSelection": [{"fieldValue": {"type": "AbsoluteValue", "values": ["covid-I"], "baseField": null, "baseEvent": -1}, "cubeField": "disease", "filterType": "Set"}], "timeWindow": {"length": 7, "slice": false, "unit": "DAY"}, "minTrigger": 1, "maxTrigger": -1}]}, "outputCohort": "loyal", "dataSource": "20201127150305YK6WcNVH"}'
    # pass_create_request(json.loads(q))
    # q = '{"appKey": "fd1ec667-75a4-415d-a250-8fbb71be7cab", "birthSequence": {"birthEvents": [{"eventSelection": [{"fieldValue": {"type": "AbsoluteValue", "values": ["therapy"], "baseField": null, "baseEvent": -1}, "cubeField": "medicine", "filterType": "Set"}], "cohortFields": [{"numLevel": 10, "minLevel": 0, "logScale": false, "scale": 10, "field": "age"}], "minTrigger": 1, "maxTrigger": -1}]}, "dataSource": "20201127150305YK6WcNVH", "measure": "demo 6", "ageField": {"range": ["1|7"], "ageInterval": 1, "field": "time"}, "ageSelection": [{"fieldValue": {"type": "AbsoluteValue", "values": ["PCR"], "baseField": null, "baseEvent": -1}, "cubeField": "labtest", "filterType": "Set"}, {"fieldValue": {"type": "AbsoluteValue", "values": ["1|1"], "baseField": null, "baseEvent": -1}, "cubeField": "value", "filterType": "Set"}], "inputCohort": "loyal"}'
    # result = pass_request(json.loads(q))

    with open('./test.dat', 'w') as jsonFile:
        json.dump(result, jsonFile)

if __name__ == "__main__":
    main()
