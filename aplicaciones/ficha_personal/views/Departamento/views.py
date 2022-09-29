from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from aplicaciones.ficha_personal.forms import DepartamentoForm
from aplicaciones.ficha_personal.models import Departamento

class DepartamentoListView(ListView):
    template_name = "Departamento/listDepartamentos.html"
    context_object_name = 'departamentos'
    model = Departamento
    paginate_by = 5
    #queryset = Cliente.objects.filter(estado=True)

    def get_queryset(self):
        query = self.request.GET.get("query")
        print(query)
        if query:
            return self.model.objects.filter(descripcion__icontains=query)
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/fichaPersonal/fichaPersonal'
        context['listar_url']= '/fichaPersonal/departamento'
        context['crear_url'] = '/fichaPersonal/creardepartamento/'
        context['titulo'] = 'LISTADO DE DEPARTAMENTOS'
        context['query'] = self.request.GET.get("query") or ""
        return context

class CrearDepartamento(CreateView):
    model = Departamento
    template_name = "Departamento/formDepartamento.html"
    success_url = reverse_lazy('ficha_Personal:departamento')
    form_class = DepartamentoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/fichaPersonal/creardepartamento/'
        context['titulo'] = 'CREAR DEPARTAMENTO'
        context['url_anterior'] = '/fichaPersonal/departamento'
        context['listar_url'] = '/fichaPersonal/departamento'
        context['action'] = 'add'
        return context

class ActualizarDepartamento(UpdateView):
    model = Departamento
    template_name = "Departamento/formDepartamento.html"
    success_url = reverse_lazy('ficha_Personal:departamento')
    form_class = DepartamentoForm
    #queryset = Cliente.objects.get(pk=request.GET.get("id"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ACTUALIZAR DEPARTAMENTO'
        context['url_anterior'] = '/fichaPersonal/departamento'
        context['listar_url'] = '/fichaPersonal/departamento'
        return context


class EliminarDepartamento(DeleteView):
    model = Departamento
    template_name = "Departamento/eliminar_departamento.html"
    success_url = reverse_lazy('ficha_Personal:departamento')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ELMINAR DEPARTAMENTO'
        context['url_anterior'] = '/fichaPersonal/departamento'
        context['listar_url'] = '/fichaPersonal/departamento'
        return context
