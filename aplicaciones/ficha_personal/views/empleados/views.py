from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from aplicaciones.ficha_personal.forms import EmpleadoForm
from aplicaciones.ficha_personal.models import Empleado

class EmpleadoListView(ListView):
    template_name = "Empleados/listEmpleado.html"
    context_object_name = 'empleados'
    model = Empleado
    paginate_by = 3
    #queryset = Cliente.objects.filter(estado=True)

    def get_queryset(self):
        query = self.request.GET.get("query")
        print(query)
        if query:
            return self.model.objects.filter(nombres__icontains=query)
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/fichaPersonal/fichaPersonal'
        context['listar_url']= '/empleado',
        context['crear_url'] = '/fichaPersonal/crearempleado/'
        context['titulo'] = 'LISTADO DE EMPLEADOS'
        context['query'] = self.request.GET.get("query") or ""
        return context

class CrearEmpleado(CreateView):
    model = Empleado
    template_name = "Empleados/form.html"
    success_url = reverse_lazy('ficha_Personal:empleado')
    form_class = EmpleadoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/fichaPersonal/crearempleado/'
        context['titulo'] = 'CREAR EMPLEADO'
        context['url_anterior'] = '/fichaPersonal/empleado'
        context['listar_url'] = '/fichaPersonal/empleado'
        context['action'] = 'add'
        return context

class ActualizarEmpleado(UpdateView):
    model = Empleado
    template_name = "Empleados/form.html"
    success_url = reverse_lazy('ficha_Personal:actualizarempleado')
    form_class = EmpleadoForm
    #queryset = Cliente.objects.get(pk=request.GET.get("id"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ACTUALIZAR DE EMPLEADO'
        context['url_anterior'] = '/fichaPersonal/empleado'
        context['listar_url'] = '/fichaPersonal/empleado'
        return context


class EliminarEmpleado(DeleteView):
    model = Empleado
    template_name = "Empleados/delete.html"
    success_url = reverse_lazy('ficha_Personal:deleteempleado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ELMINAR DE EMPLEADO'
        context['url_anterior'] = '/fichaPersonal/empleado'
        context['listar_url'] = '/fichaPersonal/empleado'
        return context



