from django.views           import View
from django.shortcuts       import render, redirect
import json
import csv
import yaml
import os
import threading
from . import request_bypass
from . import lang

class SimpleFunnel( View ):
    def get(self, request):
        dirs = [ name for name in os.listdir('./cohana/') if os.path.isdir(os.path.join('./cohana/', name)) ]
        if len(dirs) == 0:
            return redirect('/error')

        dirs.sort(reverse=True)
        file = dirs[0]

        table = yaml.load( open( "./cohana/"+file+"/table.yaml" ))

        for field in table['fields']:
            if field['fieldType'] == 'Action':
                eventCol = field['name']

        events = []
        try:
            with open('razer/data/'+file+'_event.dat') as data_file:
                data = json.load(data_file)
                events = data['EVENTS']
        except Exception as e:
            pass

        def reload():
            request_bypass.pass_reload(file)
        t1 = threading.Thread(target=reload)
        t1.start()
        
        template = 'simple-funnel' + lang.getTemplateByLanguage(request)
        return render(request, template, {"events": events, "datasource": file,})
