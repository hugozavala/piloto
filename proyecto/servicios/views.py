from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import HistorialConformidad, Servicio


class IndexView(generic.ListView):
    template_name = 'servicios/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Servicio.objects.order_by('-codigo')[:600]


class DetailView(generic.DetailView):
    model = Servicio
    template_name = 'servicios/detail.html'


class ResultsView(generic.DetailView):
    model = Servicio
    template_name = 'servicios/results.html'


def vote(request, question_id):
  
    p = get_object_or_404(Servicio, pk=question_id)
    try:
        selected_historialconformidad = p.historialconformidad_set.get(pk=request.POST['historialconformidad'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'servicios/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_historialconformidad.votes += 1
        selected_historialconformidad.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('servicios:results', args=(p.id,)))

def ver_servicios(request):
	servicios = Servicio.objects.all().order_by('codigo')
	
	return render(request,'servicios/ver_servicios.html', { 'servicios':servicios })