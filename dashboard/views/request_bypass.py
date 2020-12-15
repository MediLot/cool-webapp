import logging
import requests
import re
import json

SERVER = 'http://cool-backend:9998'
# SERVER = 'http://127.0.0.1:8188'
# SERVER = 'http://poi.life:9998'

logger = logging.getLogger('django')

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

def pass_request(query, server=SERVER):
    headers = { \
            'Connection':'keep-alive', \
            'Cookie':'', \
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36', \
            'Content-Type':'application/json', \
            'Accept' :'*/*'
            }
    logger.debug("pass request: " + json.dumps(query))
    print("pass request: " + json.dumps(query))
    r = requests.post(server+'/v1/cohort/analysis',data = json.dumps(query), headers = headers)
    logger.debug(r.text)
    return json.loads(r.text)

def pass_funnel(query, server=SERVER):
    headers = { \
            'Connection':'keep-alive', \
            'Cookie':'', \
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36', \
            'Content-Type':'application/json', \
            'Accept' :'*/*'
            }
    logger.debug("pass funnel: " + json.dumps(query))
    r = requests.post(server+'/v1/cohort/funnel',data = json.dumps(query), headers = headers)
    return json.loads(r.text)

def get_danger_request(server=SERVER):
    headers = { \
            'Connection':'keep-alive', \
            'Cookie':'', \
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36', \
            'Content-Type':'application/json', \
            'Accept' :'*/*'
            }

    r = requests.get(server+'/v1/cohort/listUser/danger', headers = headers)
    return json.loads(r.text)

def pass_create_request(query, server=SERVER):
    headers = { \
            'Connection':'keep-alive', \
            'Cookie':'', \
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36', \
            'Content-Type':'application/json', \
            'Accept' :'*/*'
            }
    print("pass create request:" + json.dumps(query))
    logger.debug("pass create request:" + json.dumps(query))
    r = requests.post(server+'/v1/cohort/manage/create', data = json.dumps(query), headers = headers)
    logger.debug("pass create response:" + r.text)
    return json.loads(r.text)

def removeCohort(cohort, server=SERVER):
    url = server+'/v1/cohort/manage/remove/' + cohort
    logger.debug("Remove cohort: "+url)
    print("Remove cohort: "+url)
    r = requests.get(url)
    return r.status_code

def get_plotdata(result):
    rawResult = result[u'result']
    i = 0
    legend = []
    data = []
    for r in rawResult:
        name = re.findall(r"\((.+?)\)",r[u'cohort'])[0]
        legend.append(name)
        pair = {'value':r[u'measure'],'name':name}
        data.append(pair)
    ret = {'Legend': legend,'Data': data}
    #print ret
    return ret

def get_plotdata_linechart(result):
    rawResult = result[u'result']
    legend = []
    data = []
    for r in rawResult:
        pair = []
        pair.append(r[u'age'])
        pair.append(r[u'measure'])
        data.append(pair)
    ret = {'Data': data}
    return ret


import numpy as np
def get_plotdata_chart(result):
    rawResult = result[u'result']
    col = []
    data = {}
    series = []
    heat = []

    for r in rawResult:
        # cohort = re.findall(r"\((.+?)\)", r[u'cohort'])[0]
        cohort = r['cohort'][1:-1]
        if cohort not in col:
            col.append(cohort)
            data[cohort] = []

    # print(col)

    for r in rawResult:
        # for r in sorted(rawResult, key=lambda x: x[u'age'], reverse=True):
        # cohort = re.findall(r"\((.+?)\)", r[u'cohort'])[0]
        cohort = r['cohort'][1:-1]
        if cohort in col:
            age = r[u'age']
            pair = []
            pair.append(age)
            pair.append(r[u'measure'])
            pair.append(r[u'max'])
            pair.append(r[u'min'])
            pair.append(float(r[u'sum']) / r[u'num'])
            pair.append(r[u'num'])
            data[cohort].append(pair)

    # print(data)
    range_dict = {}
    range_dict['series'] = []
    range_dict['cols'] = []
    for cohort in col:
        line = {}
        line['name'] = cohort
        line['type'] = 'line'
        line['data'] = np.array(data[cohort])[:, :2].astype(int).tolist()
        series.append(line)
        index = col.index(cohort)
        data0 = sorted(data[cohort], key=lambda x: x[0])

        for x in data0:
            heat.append([x[0], index, int((x[1] + 1e-10) / (data0[0][1] + 1e-10) * 100)])

        range_dict['cols'].append("%s_max" % (cohort))
        tem = {}
        tem['name'] = "%s_max" % (cohort)
        tem['type'] = "custom"
        tem['data'] = [[x[0], x[2], round(x[4], 2)] for x in data0]
        range_dict['series'].append(tem)

        range_dict['cols'].append("%s_min" % (cohort))
        tem = {}
        tem['name'] = "%s_min" % (cohort)
        tem['type'] = "custom"
        tem['data'] = [[x[0], x[3], round(x[4], 2)] for x in data0]
        range_dict['series'].append(tem)

        range_dict['cols'].append("%s_%s" % (cohort, "avg"))
        tem = {}
        tem['name'] = "%s_avg" % (cohort)
        tem['type'] = "line"
        tem['data'] = [[x[0], round(x[4], 2)] for x in data0]
        range_dict['series'].append(tem)

    ret = {'values': series, 'columes': col, 'heatmap': heat, 'range': range_dict}
    return ret

def transfer_retention_chart(result):
    rawdata = result[u'result']
    y_label = []
    line_data = {}
    for sub_result in rawdata['result']:
        if sub_result['cohort'] not in y_label:
            y_label.append(sub_result['cohort'])
            line_data[sub_result['cohort']] = []
        line_data[sub_result['cohort']].append([sub_result['age'], sub_result['measure']])

    lens = []
    for k, v in line_data.items():
        lens.append(len(v))
    x_label = list(range(max(lens)))
    line_figure = {
        "x_label": x_label,
        "y_label": y_label,
        "data": line_data
    }
    # print(line_figure)

    y_label = []
    heatmap_data = []
    count = 0
    full_data = []
    for k, v in line_data.items():
        y_label.append(k)
        for sub_data in v:
            if sub_data[0] == 0:
                init = sub_data[1]
        for sub_data in v:
            full_data.append((sub_data[1] / init * 100))
            heatmap_data.append([count, sub_data[0], "%.2f" % (sub_data[1] / init * 100)])
        count += 1

    heatmap_figure = {
        "x_label": x_label,
        "y_label": y_label,
        "data": heatmap_data,
        "min": min(full_data),
        "max": max(full_data),
    }

    output = {
        "line":line_figure,
        "heatmap": heatmap_figure
    }
    return output