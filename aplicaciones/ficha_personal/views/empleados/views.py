from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from aplicaciones.ficha_personal.forms import EmpleadoForm, ContactoEmergenciasForm, InfoAcademicaForm,CapacitacionesForm
from aplicaciones.ficha_personal.models import Empleado, ContactoEmergencias, InfoAcademica, Capacitaciones

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
    listar_url = '/fichaPersonal/empleado'
    success_url = reverse_lazy('ficha_Personal:empleado')
    form_class = EmpleadoForm
    second_form_class = ContactoEmergenciasForm
    third_form_class = InfoAcademicaForm
    fourth_form_class = CapacitacionesForm

    def get_context_data(self, **kwargs):
        context = super(CrearEmpleado, self).get_context_data(**kwargs)
        context['listar_url'] = '/fichaPersonal/empleado'
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(self.request.GET)
        if 'form4' not in context:
            context['form4'] = self.fourth_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        form3 = self.third_form_class(request.POST)
        form4 = self.fourth_form_class(request.POST)
        if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
            solicitud = form.save(commit=False)
            solicitud.empleado = form2.save(commit=False)
            solicitud.empleado = form3.save(commit=False)
            solicitud.empleado = form4.save()
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3, form4=form4))

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['action_save'] = '/fichaPersonal/crearempleado/'
    #     context['titulo'] = 'CREAR EMPLEADO'
    #     context['url_anterior'] = '/fichaPersonal/empleado'
    #     context['listar_url'] = '/fichaPersonal/empleado'
    #     context['action'] = 'add'
    #     return context

# class ActualizarEmpleado(UpdateView):
#     model = Empleado
#     second_model = ContactoEmergencias
#     third_model = InfoAcademica
#     fourth_model = Capacitaciones
#     template_name = "Empleados/form.html"
#     success_url = reverse_lazy('ficha_Personal:empleado')
#     form_class = EmpleadoForm
#     second_form_class = ContactoEmergenciasForm
#     third_form_class = InfoAcademicaForm
#     fourth_form_class = CapacitacionesForm
#     #queryset = Cliente.objects.get(pk=request.GET.get("id"))
#
#     def get_context_data(self, **kwargs):
#         context = super(ActualizarEmpleado, self).get_context_data(**kwargs)
#         pk = self.kwargs.get('pk',0)
#         empleado = self.model.objects.get(id=pk)
#         contacEmer = self.second_model.objects.get(id=)
#         return context

class ActualizarEmpleado(UpdateView):
    model = Empleado
    template_name = "Empleados/editarEmpleado.html"
    success_url = reverse_lazy('ficha_Personal:empleado')
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



