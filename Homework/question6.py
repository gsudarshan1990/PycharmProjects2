#What is Django in python?
#Django is an open purpose framework used for the web applications in the backend


from django.http import HttpResponse

def small_function(request):
    return HttpResponse('Hello')