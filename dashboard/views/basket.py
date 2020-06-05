from django.views          import View
from django.shortcuts      import render, redirect
import json
import os

from .                      import lang

class BASKET( View ):
    def get(self, request):
        dirs = [ name for name in os.listdir('./cohana/') if os.path.isdir(os.path.join('./cohana/', name)) ]
        if len(dirs) == 0:
            return redirect('/error')

        spendData={}
        try:
            with open('dashboard/data/spend.dat') as data_file:
                spendData = json.load(data_file)
        except Exception as e:
            pass

        spend2Data={}
        try:
            with open('dashboard/data/spend2.dat') as data_file:
                spend2Data = json.load(data_file)
        except Exception as e:
            pass

        spend3Data={}
        try:
            with open('dashboard/data/spend3.dat') as data_file:
                spend3Data = json.load(data_file)
        except Exception as e:
            pass

        heat1Data={}
        try:
            with open('dashboard/data/heat1.dat') as data_file:
                heat1Data = json.load(data_file)
        except Exception as e:
            pass

        heat2Data={}
        try:
            with open('dashboard/data/heat2.dat') as data_file:
                heat2Data = json.load(data_file)
        except Exception as e:
            pass

        heat3Data={}
        try:
            with open('dashboard/data/heat3.dat') as data_file:
                heat3Data = json.load(data_file)
        except Exception as e:
            pass

        heat4Data={}
        try:
            with open('dashboard/data/heat4.dat') as data_file:
                heat4Data = json.load(data_file)
        except Exception as e:
            pass

        heat5Data={}
        try:
            with open('dashboard/data/heat5.dat') as data_file:
                heat5Data = json.load(data_file)
        except Exception as e:
            pass


        template = 'basket.html'
        return render(request, template, {
                'spendData':json.dumps(spendData),
                'spend2Data':json.dumps(spend2Data),
                'spend3Data':json.dumps(spend3Data),
                'heat1Data':json.dumps(heat1Data),
                'heat2Data':json.dumps(heat2Data),
                'heat3Data':json.dumps(heat3Data),
                'heat4Data':json.dumps(heat4Data),
                'heat5Data':json.dumps(heat5Data),
            })
