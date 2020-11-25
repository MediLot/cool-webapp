from django.views           import View
from django.http            import HttpResponse
from django.shortcuts       import render, redirect
import json
import sys
import traceback
from . import request_bypass
from dashboard.models import *
import string,random
from datetime import datetime

upload_path = "upload/"
data_path = "cohana/"

class Api( View ):
    def get(self, request):
        response = {}
        response['code'] = 500
        response['message'] = "ERROR"
        return HttpResponse(json.dumps(response))

    def post(self, request):
        mode = request.POST.get("mode", "funnel")
        print(mode)

        analysis_name = request.session['analysis_name']
        agg = request.session['agg']
        file_save = request.session['file_save']

        print(analysis_name)

        rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        analysis_save = datetime.now().strftime('%Y%m%d%H%M%S') + rand_str

        response = {}
        try:
            # if mode == "simple-funnel":
            #     response['code'] = 200
            #     datasource = request.POST.get("datasource", "")
            #
            #     with open("dashboard/queries/funnel.json", "r") as funnel_file:
            #         funnel = json.load(funnel_file)
            #
            #     request_data = request.POST.get("data", "")
            #     request_obj = json.loads(request_data)
            #
            #     # print(stage, funnel)
            #
            #     for stage_text in request_obj:
            #         with open("dashboard/queries/funnel_stage.json", "r") as stage_file:
            #             stage = json.load(stage_file)
            #             stage['birthEvents'] = []
            #             for key in stage_text:
            #                 with open("dashboard/queries/birthEvent.json","r") as birthEvent_file:
            #                     birthEvent = json.load(birthEvent_file)
            #                     birthEvent['eventSelection'][0]['fieldValue']['values'] = [key['name']]
            #                     birthEvent['minTrigger'] = key['minTrigger']
            #                     birthEvent['maxTrigger'] = key['maxTrigger']
            #                     stage['birthEvents'].append(birthEvent)
            #             funnel['stages'].append(stage)
            #     funnel['dataSource'] = datasource
            #     try:
            #         response['data'] = request_bypass.pass_funnel(funnel)
            #     except Exception as e:
            #         raise Exception("Invalid Query")
            #     response['message'] = "OK"
            #     # return HttpResponse(json.dumps(response))
            #
            # elif mode == "simple-funnel":
            #     response['code'] = 200
            #     query = request.POST.get("data", "")
            #     if query == "":
            #         response['message'] = "no Query"
            #         return HttpResponse(json.dumps(response))
            #
            #     funnel = json.loads(query)
            #     try:
            #         raw_response = request_bypass.pass_funnel(funnel)
            #     except Exception as e:
            #         raise Exception("Invalid Query")
            #     response['data'] = request_bypass.get_plotdata_chart(raw_response)
            #     response['message'] = "OK"
            #     with open(data_path+'/%s/%s.dat'%(file_save,analysis_save), 'w') as jsonFile:
            #         json.dump(response, jsonFile)
            #     # return HttpResponse(json.dumps(response))
            #
            # elif mode == "simple-cohort":
            #     response['code'] = 200
            #     datasource = request.POST.get("datasource", "")
            #
            #     file_path = "dashboard/queries/RetentionTemplate.json"
            #     with open(file_path, "r") as cohort_file:
            #         cohort = json.load(cohort_file)
            #         cohort['birthSequence']['birthEvents'][0]['eventSelection'] = []
            #         events_data = request.POST.get("events", "")
            #         events = json.loads(events_data)
            #         for key in events:
            #             with open("dashboard/queries/event.json", "r") as event_file:
            #                     event = json.load(event_file)
            #                     event['fieldValue']['values'][0] = key
            #             cohort['birthSequence']['birthEvents'][0]['eventSelection'].append(event)
            #
            #     cohort['birthSequence']['birthEvents'][0]['cohortFields'][0]['field'] = request.POST.get("cohortField", "role")
            #     cohort['ageField']['field'] = request.POST.get("ageField", 'time')
            #     cohort['ageField']['range'][0] = '1|' + request.POST.get("time", "7")
            #     cohort['dataSource'] = datasource
            #     measure = request.POST.get("measure", "retention")
            #     cohort['measure'] = measure
            #     try:
            #         raw_response = request_bypass.pass_request(cohort)
            #     except Exception as e:
            #         raise Exception("Invalid Query")
            #     response['data'] = request_bypass.get_plotdata_chart(raw_response)
            #     response['message'] = "OK"
            #     with open(data_path+'/%s/%s.dat'%(file_save,analysis_save), 'w') as jsonFile:
            #         json.dump(response, jsonFile)
            #     # return HttpResponse(json.dumps(response))


            if mode == "cohort":
                response['code'] = 200
                query = request.POST.get("data", "")
                if query == "":
                    response['message'] = "no Query"
                    return HttpResponse(json.dumps(response))

                cohort = json.loads(query)
                # pprint.pprint(cohort)
                try:
                    raw_response = request_bypass.pass_request(cohort)
                except Exception as e:
                    raise Exception("Invalid Query")
                response['data'] = request_bypass.get_plotdata_chart(raw_response)
                response['message'] = "OK"
                with open(data_path+'/%s/%s.dat'%(file_save,analysis_save), 'w') as jsonFile:
                    json.dump(response, jsonFile)
                # return HttpResponse(json.dumps(response))
            elif mode == "loyal-cohort":
                response['code'] = 200
                query2 = request.POST.get("data2", "")
                if query2 == "":
                    response['message'] = "no create query"
                    return HttpResponse(json.dumps(response))

                loyal2 = json.loads(query2)
                request_bypass.removeCohort("loyal")
                result = request_bypass.pass_create_request(loyal2)

                query1 = request.POST.get("data1", "")
                if query1 == "":
                    response['message'] = "no loyal query"
                    return HttpResponse(json.dumps(response))

                loyal1 = json.loads(query1)
                try:
                    raw_response = request_bypass.pass_request(loyal1)
                except Exception as e:
                    raise Exception("Invalid Query")
                response['data'] = request_bypass.get_plotdata_chart(raw_response)

                with open(data_path+'/%s/%s.dat'%(file_save,analysis_save), 'w') as jsonFile:
                    json.dump(response, jsonFile)

                request_bypass.removeCohort("loyal")
                response['message'] = "OK"
                # return HttpResponse(json.dumps(response))

            elif mode == "funnel":
                response['code'] = 200
                query = request.POST.get("data", "")
                if query == "":
                    response['message'] = "no Query"
                    return HttpResponse(json.dumps(response))
                funnel = json.loads(query)
                try:
                    response['data'] = request_bypass.pass_funnel(funnel)
                except Exception as e:
                    raise Exception("Invalid Query")
                response['message'] = "OK"
                # with open('dashboard/data/last_loaded.dat', 'w') as jsonFile:
                #     json.dump(response, jsonFile)
                # return HttpResponse(json.dumps(response))

            elif mode == "loyal-funnel":
                response['code'] = 200
                query2 = request.POST.get("data2", "")
                if query2 == "":
                    response['message'] = "no create query"
                    return HttpResponse(json.dumps(response))

                loyal2 = json.loads(query2)
                request_bypass.removeCohort("loyal")
                result = request_bypass.pass_create_request(loyal2)

                query1 = request.POST.get("data1", "")
                if query1 == "":
                    response['message'] = "no loyal query"
                    # return HttpResponse(json.dumps(response))

                funnel = json.loads(query1)
                try:
                    response['data'] = request_bypass.pass_funnel(funnel)
                except Exception as e:
                    raise Exception("Invalid Query")
                # with open('dashboard/data/last_loaded.dat', 'w') as jsonFile:
                #     json.dump(response, jsonFile)

                request_bypass.removeCohort("loyal")
                response['message'] = "OK"
                # return HttpResponse(json.dumps(response))
            else:
                response['code'] = 500
                response['message'] = "Unsupported Mode"

            file = csv_file.objects.get(file_save=file_save)
            new_analysis = analysis(
                file_id=file,
                analysis_type=agg,
                analysis_name=analysis_name,
                analysis_save=analysis_save
            )
            new_analysis.save()

            return HttpResponse(json.dumps(response))

        except Exception as e:
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)
            response['code'] = 500
            response['message'] = "Internal Error: " + str(e)
            return HttpResponse(json.dumps(response))
        
