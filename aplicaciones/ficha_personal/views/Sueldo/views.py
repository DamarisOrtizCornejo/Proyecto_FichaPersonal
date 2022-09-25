from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from aplicaciones.ficha_personal.forms import SueldoForm
from aplicaciones.ficha_personal.models import Sueldo

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from aplicaciones.ficha_personal.forms import SueldoForm
from aplicaciones.ficha_personal.models import Sueldo

class SueldoListView(ListView):
    template_name = "Sueldo/listSueldo.html"
    context_object_name = 'sueldo'
    model = Sueldo
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
        context['listar_url']= '/fichaPersonal/sueldo'
        context['crear_url'] = '/fichaPersonal/crearSueldo'
        context['titulo'] = 'LISTADO DE SUELDO'
        context['query'] = self.request.GET.get("query") or ""
        return context

class RegistroSueldoListView(ListView):
    template_name = "Sueldo/registroSueldo.html"
    model = Sueldo
    context_object_name = 'sueldos'
    paginate_by = 5
    # queryset = ContactoEmergencias.objects.filter(id=1)

    def get_queryset(self):
        # print("mira",type(self.kwargs['pk']),self.kwargs['pk'])
        return self.model.objects.filter(empleado__id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/fichaPersonal/sueldo'
        context['listar_url']= '/fichaPersonal/registroSueldo'
        context['crear_url'] = '/fichaPersonal/crearSueldo'
        context['titulo'] = 'REGISTRO DE SUELDOS'
        context['query'] = self.request.GET.get("query") or ""
        return context

class CrearSueldo(CreateView):
    model = Sueldo
    template_name = "Sueldo/form.html"
    success_url = reverse_lazy('ficha_Personal:sueldo')
    form_class = SueldoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/fichaPersonal/crearSueldo'
        context['titulo'] = 'CREAR SUELDO'
        context['url_anterior'] = '/fichaPersonal/registroSueldo'
        context['listar_url'] = '/fichaPersonal/sueldo'
        context['action'] = 'add'
        return context

class ActualizarSueldo(UpdateView):
    model = Sueldo
    template_name = "Sueldo/form.html"
    # success_url = reverse_lazy('ficha_Personal:registroContactoEmergencia')
    success_url = reverse_lazy('ficha_Personal:sueldo')
    form_class = SueldoForm
    #queryset = Cliente.objects.get(pk=request.GET.get("id"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ACTUALIZAR DE SUELDO'
        context['url_anterior'] = '/fichaPersonal/sueldo'
        context['listar_url'] = '/fichaPersonal/sueldo'
        return context


class EliminarSueldo(DeleteView):
    model = Sueldo
    template_name = "Sueldo/delete.html"
    success_url = reverse_lazy('ficha_Personal:deleteSueldo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ELMINAR SUELDO'
        context['url_anterior'] = '/fichaPersonal/sueldo'
        context['listar_url'] = '/fichaPersonal/sueldo'
        return context

