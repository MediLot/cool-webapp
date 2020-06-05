from django.views	   import View
from django.shortcuts	   import render, redirect
import os
import csv
import json
import yaml
import threading
from . import request_bypass
from . import lang

class SimpleRetention( View ):
	def get(self, request):
		dirs = [ name for name in os.listdir('./cohana/') if os.path.isdir(os.path.join('./cohana/', name)) ]
		if len(dirs) == 0:
			return redirect('/error')

		dirs.sort(reverse=True)
		file = dirs[0]

		cohort_attr = []
		age_field = None
		table = yaml.load( open( "./cohana/"+file+"/table.yaml" ))
		for field in table['fields']:
			if field['fieldType'] in ['Metric', 'Segment']:
				cohort_attr.append(field['name'])
			elif field['fieldType'] == 'ActionTime':
				age_field = field['name']

		events = []
		try:
			with open('razer/data/'+file+'_event.dat') as data_file:
				data = json.load(data_file)
				events = data['EVENTS']
		except Exception as e:
			pass

		measures = []
		cube = yaml.load( open( "./cohana/"+file+"/cube.yaml" ))
		for m in cube['measures']:
			measures.append(m['name'])

		def reload():
			request_bypass.pass_reload(file)
		t1 = threading.Thread(target=reload)
		t1.start()

		template = 'simple-retention' + lang.getTemplateByLanguage(request)
		return render(request, template, {
			"events": events,
			"datasource": file,
			"ageField": age_field,
			"measures": measures,
			"cohortAttr": cohort_attr})