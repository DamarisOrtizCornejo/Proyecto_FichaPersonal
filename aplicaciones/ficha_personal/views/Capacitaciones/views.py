from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from aplicaciones.ficha_personal.forms import CapacitacionesForm
from aplicaciones.ficha_personal.models import Capacitaciones

class CapacitacionesListView(ListView):
    template_name = "Capacitaciones/listCapacitaciones.html"
    context_object_name = 'capacitacion'
    model = Capacitaciones
    paginate_by = 5
    #queryset = Cliente.objects.filter(estado=True)

    def get_queryset(self):
        query = self.request.GET.get("query")
        print(query)
        if query:
            return self.model.objects.filter(empleado__nombres=query)
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/fichaPersonal/fichaPersonal'
        context['listar_url']= '/fichaPersonal/capacitaciones'
        context['crear_url'] = '/fichaPersonal/crearCapacitaciones/'
        context['titulo'] = 'LISTADO DE CAPACITACIONES'
        context['query'] = self.request.GET.get("query") or ""
        return context

class RegistroCapacitacionesListView(ListView):
    template_name = "Capacitaciones/registroCapacitaciones.html"
    context_object_name = 'capacitaciones'
    model = Capacitaciones
    paginate_by = 5
    #queryset = Cliente.objects.filter(estado=True)

    def get_queryset(self):
        print("mira", type(self.kwargs['pk']), self.kwargs['pk'])
        return self.model.objects.filter(empleado__id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/fichaPersonal/capacitaciones'
        context['listar_url']= '/fichaPersonal/registroCapacitaciones'
        context['crear_url'] = '/fichaPersonal/crearcontactoEmergencias'
        context['titulo'] = 'REGISTRO DE CAPACITACIONES'
        context['query'] = self.request.GET.get("query") or ""
        return context

class CrearCapacitaciones(CreateView):
    model = Capacitaciones
    template_name = "Capacitaciones/form.html"
    success_url = reverse_lazy('ficha_Personal:capacitaciones')
    form_class = CapacitacionesForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/fichaPersonal/crearCapacitaciones'
        context['titulo'] = 'CREAR CAPACITACIONES'
        context['url_anterior'] = '/fichaPersonal/registroCapacitaciones'
        context['listar_url'] = '/fichaPersonal/capacitaciones'
        context['action'] = 'add'
        return context

class ActualizarCapacitaciones(UpdateView):
    model = Capacitaciones
    template_name = "Capacitaciones/form.html"
    success_url = reverse_lazy('ficha_Personal:actualizarCapacitaciones')
    form_class = CapacitacionesForm
    #queryset = Cliente.objects.get(pk=request.GET.get("id"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ACTUALIZAR DE CAPACITACIONES'
        context['url_anterior'] = '/fichaPersonal/capacitaciones'
        context['listar_url'] = '/fichaPersonal/capacitaciones'
        return context


class EliminarCapacitaciones(DeleteView):
    model = Capacitaciones
    template_name = "Capacitaciones/delete.html"
    success_url = reverse_lazy('ficha_Personal:deleteCapacitaciones')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ELMINAR DE CAPACITACIONES'
        context['url_anterior'] = '/fichaPersonal/capacitaciones'
        context['listar_url'] = '/fichaPersonal/capacitaciones'
        return context

