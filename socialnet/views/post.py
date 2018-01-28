# -----------------------------------------------------------------------------------------------
#
#       By:         Fredrick Stakem
#       Created:    8.9.16   
#
# -----------------------------------------------------------------------------------------------


# Libs
from django.shortcuts import render_to_response


def posts(request, user_name):
    return render_to_response('posts.html')

def post(request, user_name, id):
    return render_to_response('post.html')

