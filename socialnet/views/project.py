# -----------------------------------------------------------------------------------------------
#
#       By:         Fredrick Stakem
#       Created:    8.9.16   
#
# -----------------------------------------------------------------------------------------------


# Libs
from django.shortcuts import render_to_response


def projects(request, user_name):
    return render_to_response('projects.html')

def project(request, user_name, id):
    return render_to_response('project.html')

