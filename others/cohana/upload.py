#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@version:0.1
@author:Cai Qingpeng
@file: upload.py
@time: 2020/5/8 6:15 PM
'''

from .views import *


def upload_1(request):
    result = {}
    if request.method == "GET":
        return render(request, "upload_1.html", result)
    elif request.method == "POST":
        csv_file = request.FILES["csv_file"]
        file_name = request.POST.get("name")

        rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        raw_save = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        f = open(upload_path + raw_save + ".csv", 'wb')
        for chunk in csv_file.chunks():
            f.write(chunk)
        f.close()

        rawdata = pd.read_csv(upload_path + raw_save + ".csv")
        columns = rawdata.columns
        columns = [i.strip() for i in columns if i != '' and i != '\r']
        rawdata.columns = columns
        # print(columns)
        csv_save = raw_save + "_" + rand_str
        print(csv_save)
        rawdata.to_csv(upload_path + csv_save + ".csv", index=False)
        os.remove(upload_path + raw_save + ".csv")

        result['columns'] = columns
        result['options'] = fieldTypes

        request.session['columns'] = columns
        request.session['csv_name'] = file_name
        request.session['csv_save'] = csv_save

        return render(request, "upload_2.html", result)

def upload_2(request):
    result = {}
    if request.method == "GET":
        return render(request, "upload_2.html", result)
    elif request.method == "POST":
        # print(request.POST.get("name"))
        # print(request.session['columns'])

        sub_path = data_path+"/%s"%request.session['csv_save']
        if not os.path.exists(sub_path):
            os.mkdir(sub_path)
        with open(sub_path+'/table.yaml', 'w') as f:
            fields = []
            for field in request.session['columns']:
                fields.append({
                    "name": field.replace('\r', ''),
                    "fieldType": fieldTypes[request.POST.get(field)]['type'],
                    "dataType": fieldTypes[request.POST.get(field)]['datatype'],
                })
            f.write(yaml.dump({'fields': fields, 'charset': 'utf-8'}, default_flow_style=False))

        subprocess.call([BASE_DIR + '/utils/preprocess.sh', request.session['csv_save']])

        user = user_info.objects.get(user_name=request.session['user'])
        new_file = csv_file(
            user_id=user,
            file_name = request.session['csv_name'],
            file_save = request.session['csv_save'],
        )
        new_file.save()

        return redirect("/database/")