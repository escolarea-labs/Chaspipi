import random
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from lista.models import Lista

def crear(request):
    if 'lista' not in request.session or request.session['lista'] is None:

        cod = ''
        lista = None

        while True:
            for i in range(10):
                cod += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')

            lista, creada = Lista.objects.get_or_create(codigo=cod)

            if creada:
                break

        request.session['lista'] = lista.codigo
    else:
        cod = request.session['lista']

    return HttpResponseRedirect(reverse('lista', args=[cod,]))

def mostrar(request, codigo):
    lista = Lista.objects.get(codigo=codigo)
    lista.save()
    return render_to_response('lista/mostar.html', {'lista':lista}, context_instance=RequestContext(request))
