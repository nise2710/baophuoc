from django.template import RequestContext
from django.shortcuts import render_to_response

def trangchu_index(request):
    context = RequestContext(request)
    context_dict = {}
    
    return render_to_response('trangchu/trangchu_index.html', context_dict, context)