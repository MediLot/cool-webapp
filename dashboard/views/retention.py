from django.views           import View
from django.shortcuts       import render
from collections            import defaultdict
import csv
import json
import os
import yaml
import threading
from .                      import request_bypass
from . import lang

from pdb                    import set_trace as st

class Retention( View ):
    def get(self, request):
        file = request.session['file_save']
        events = []
        # try:
        #     with open(('./cohana/%s/.dat')) as data_file:
        #         data = json.load(data_file)
        #         events = data['EVENTS']
        # except Exception as e:
        #     pass
        djangoData = {
            "table.yaml": yaml.load( open( './cohana/'+file+"/table.yaml" ) ),
            "cube.yaml":  yaml.load( open( './cohana/'+file+"/cube.yaml" ) ),
            "events": events,
            "datasource": file
        }
        djangoData = json.dumps( djangoData, indent=4 )
        # print(djangoData)

        def reload():
            request_bypass.pass_reload(file)
        t1 = threading.Thread(target=reload)
        t1.start()

        template = 'retention' + lang.getTemplateByLanguage(request)
        return render( request, template, locals() )
