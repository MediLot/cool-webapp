from django.views          import View
from django.shortcuts      import render, redirect
import json
import os

from .                      import lang

class MVC( View ):
    def get(self, request):
        dirs = [ name for name in os.listdir('./cohana/') if os.path.isdir(os.path.join('./cohana/', name)) ]
        if len(dirs) == 0:
            return redirect('/error')

        template = 'mvc.html'
        return render(request, template)
