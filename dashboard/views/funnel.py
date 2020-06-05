from django.views           import View
from django.shortcuts       import render, redirect
import json
import csv
import yaml
import os
import threading
from . import request_bypass
from . import lang

class Funnel( View ):
    def get(self, request):
        dirs = [ name for name in os.listdir('./cohana/') if os.path.isdir(os.path.join('./cohana/', name)) ]
        if len(dirs) == 0:
                return redirect('/error')
        dirs.sort(reverse=True)
        file = dirs[0]
        events = []
        try:
            with open(('razer/data/'+file+'_event.dat')) as data_file:
                data = json.load(data_file)
                events = data['EVENTS']
        except Exception as e:
            pass
        djangoData = {
                "table.yaml": yaml.load( open( "./cohana/"+file+"/table.yaml" ) ),
                "cube.yaml":  yaml.load( open( "./cohana/"+file+"/cube.yaml" ) ),
                "events": events,
                "datasource": file
        }
        djangoData = json.dumps( djangoData, indent=4 )

        def reload():
            request_bypass.pass_reload(file)
        t1 = threading.Thread(target=reload)
        t1.start()

        template = 'funnel' + lang.getTemplateByLanguage(request)
        return render( request, template, locals() )
