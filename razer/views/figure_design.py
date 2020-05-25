#!/usr/bin/python
from django.http            import HttpResponseRedirect

from django.shortcuts       import render, redirect
from django.views           import View

import os, yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
upload_path = "upload/"
data_path = "cohana/"

class Figure_design(View):
    def get(self, request):
        result = {}
        result['columns'] = request.session['columns']
        return render(request, "figure_design.html", result)

    def post( self,request ):
        result = {}
        sub_path = data_path + "/%s" % request.session['file_save']
        agg = request.POST.get("aggregator")
        analysis_name = request.POST.get("name")
        table_name = request.POST.get("tableFieldName")
        if agg == "RETENTION":
            with open(sub_path + '/cube.yaml', 'w') as f:
                fields = []
                fields.append({
                    "aggregator": agg,
                    "name": analysis_name,
                    "tableFieldName": table_name,
                })
                f.write(yaml.dump({'measures': fields}, default_flow_style=False))

        elif agg == "SIMPLE":
            pass

        request.session['analysis_name'] = analysis_name
        request.session['agg'] = agg

        return HttpResponseRedirect('/retention/advance')