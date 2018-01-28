# -----------------------------------------------------------------------------------------------
#
#       By:         Fredrick Stakem
#       Created:    8.9.16   
#
# -----------------------------------------------------------------------------------------------


# Libs
from django.shortcuts import render_to_response


def landing(request, user_name):
    print(user_name)
    return render_to_response('user_landing.html')

def about_me(request, user_name):
    return render_to_response('about_me.html')

def links(request, user_name):
    return render_to_response('links.html')

def resume(request, user_name):
    return render_to_response('resume.html')
