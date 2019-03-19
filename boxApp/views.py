from django.http import HttpResponse
from django.template import loader



def index(request):
    template = loader.get_template('boxApp/index.html')
    context = None
    return HttpResponse(template.render(context, request))
#fdfdfgdgr