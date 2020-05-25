from django.shortcuts       import render, redirect
from django.views           import View

from razer.models import *
import shutil, os, yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
upload_path = "upload/"
data_path = "cohana/"

class Database(View):
    def get(self, request):
        result = {}
        user = user_info.objects.get(user_name=request.session['user'])
        files = csv_file.objects.filter(user_id=user)
        if files.exists():
            result['files'] = {}
            for index, file in enumerate(files):
                result['files'][index] = {
                    "index": index + 1,
                    "file_name": file.file_name,
                    "file_save": file.file_save,
                    "file_date": file.file_save[:4] + "/" + file.file_save[4:6] + "/" + file.file_save[6:8]
                }
        return render(request, "database.html", result)

    def post( self,request ):
        result = {}
        file_operation = request.POST.get('file_operation')
        file_save = request.POST.get('file_save')

        if file_operation == "delete":
            if csv_file.objects.filter(file_save=file_save).exists():
                csv_file.objects.filter(file_save=file_save).delete()
                shutil.rmtree(data_path + file_save)
                os.remove(upload_path + file_save + ".csv")

            return redirect("/database")
        else:
            request.session['file_save'] = file_save

            columns = []
            with open(data_path + '/%s/table.yaml' % file_save, 'r') as f:
                data = yaml.load(f.read())
                for col in data['fields']:
                    columns.append(col['name'])

            request.session['columns'] = columns

            return redirect('/figure_design/')