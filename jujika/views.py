# -----------------------------------------------------------------------------------------------
#
#       By:         Fredrick Stakem
#       Created:    8.9.16   
#
# -----------------------------------------------------------------------------------------------


# Libs
from django.shortcuts import render_to_response

def landing(request):
    print('MAIN')
    return render_to_response('landing.html')
