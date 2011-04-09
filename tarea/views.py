from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from tarea.models import Tarea
from django.utils import simplejson

def crear(request):
    if request.method == "POST":
        tarea = Tarea.objects.create(descripcion=request.POST['descripcion'],
                                     lista_id=request.POST['lista'])
    else:
        raise Http404

    if request.is_ajax():
        result = {"id":tarea.id}
        return HttpResponse(simplejson.dumps(result), mimetype='application/json')
    else:
        return HttpResponseRedirect(reverse('lista', args=[tarea.lista.codigo,]))

@csrf_exempt
def cambiar_hecha(request, tarea_id):
    if request.method == "POST":
        tarea = Tarea.objects.get(id=tarea_id)
        tarea.hecha = not tarea.hecha
        tarea.save()
        return HttpResponse()
    else:
        raise Http404
