from django.shortcuts       import render, redirect
from django.views           import View

from dashboard.models import *
import json

upload_path = "upload/"
data_path = "cohana/"

class Figure(View):
    def get(self, request):
        result = {}
        user = user_info.objects.get(user_name=request.session['user'])
        files = csv_file.objects.filter(user_id=user)
        count = 0
        if files.exists():
            for file in files:
                alys = analysis.objects.filter(file_id=file)
                if alys.exists():
                    for aly in alys:
                        with open(data_path + "%s/%s.dat" % (file.file_save, aly.analysis_save)) as f:
                            data = json.load(f)
                        if aly.analysis_type == "RETENTION":

                            result[count] = self.to_line(data)
                            result[count]['title'] = aly.analysis_name + "(line map)"
                            result[count]['type'] = "line"
                            count += 1
                            result[count] = self.to_heatmap(data)
                            result[count]['title'] = aly.analysis_name + "(heat map)"
                            result[count]['type'] = "heatmap"
                            count += 1

        return render(request, "figure.html", {"figures": result})

    def to_line(self, data):
        result = {}
        result['y_label'] = data['data']['columes']

        result['data'] = {}
        lens = []
        for sub_data in data['data']["values"]:
            sub = sub_data['data']
            sub.reverse()
            lens.append(len(sub_data['data']))
            result['data'][sub_data['name']] = sub

        result['x_label'] = list(range(max(lens)))
        return result



    def to_heatmap(self,data):
        result = {}
        result['y_label'] = data['data']['columes']
        lens = []
        for sub_data in data['data']['heatmap']:
            lens.append(sub_data[0])
        # print(lens)
        # print(max(lens))
        result['x_label'] = list(range(max(lens)+1))
        result['data'] = data['data']['heatmap']
        result['min'] = 0
        result['max'] = 100
        return result
