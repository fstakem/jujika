# -----------------------------------------------------------------------------------------------
#
#       By:         Fredrick Stakem
#       Created:    8.9.16   
#
# -----------------------------------------------------------------------------------------------


# Libs
from django.shortcuts import render_to_response


def photos(request, user_name):
    return render_to_response('photos.html')

