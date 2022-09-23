from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from aplicaciones.ficha_personal.forms import ContactoEmergenciasForm
from aplicaciones.ficha_personal.models import ContactoEmergencias,Empleado

class ContactoEmergenciaListView(ListView):
    template_name = "ContactoEmergencia/listContactoEmergencia.html"
    context_object_name = 'contactoEmergencia'
    success_url = reverse_lazy('ficha_Personal:contactoEmergencia')
    model = ContactoEmergencias
    paginate_by = 3
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
        context['listar_url']= '/contactoEmergencia',
        context['crear_url'] = '/fichaPersonal/crearcontactoEmergencias/'
        context['titulo'] = 'LISTADO DE CONTACTO EMERGENCIAS'
        context['query'] = self.request.GET.get("query") or ""
        return context

class RegistroContactoEmergenciaListView(ListView):
    template_name = "ContactoEmergencia/registroContacto.html"
    model = ContactoEmergencias
    context_object_name = 'contactoEmergencias'
    paginate_by = 3
    # queryset = ContactoEmergencias.objects.filter(empleado__id=2)
    # queryset = ContactoEmergencias.objects.filter(id=1)
    # queryset = Empleado.objects.filter(id=1)

    # def get_queryset(self):
    #     if :
    #         return self.model2.objects.filter(id=Empleado)
    #     else:
    #         return self.model.objects.filter(empleado__id=ContactoEmergencias)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/fichaPersonal/contactoEmergencia'
        context['listar_url']= '/fichaPersonal/registroContactoEmergencias',
        context['crear_url'] = '/fichaPersonal/crearcontactoEmergencias/'
        context['titulo'] = 'REGISTRO DE CONTACTO EMERGENCIAS'
        context['query'] = self.request.GET.get("query") or ""
        return context

class CrearContactoEmergencia(CreateView):
    model = ContactoEmergencias
    template_name = "ContactoEmergencia/form.html"
    success_url = reverse_lazy('ficha_Personal:contactoEmergencia')
    form_class = ContactoEmergenciasForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/fichaPersonal/crearContactoEmergencia/'
        context['titulo'] = 'CREAR CONTACTO EMERGENCIA'
        context['url_anterior'] = '/fichaPersonal/registroContactoEmergencia'
        context['listar_url'] = '/fichaPersonal/contactoEmergencia'
        context['action'] = 'add'
        return context

class ActualizarContactoEmergencia(UpdateView):
    model = ContactoEmergencias
    template_name = "ContactoEmergencia/form.html"
    success_url = reverse_lazy('ficha_Personal:registroContactoEmergencia')
    form_class = ContactoEmergenciasForm
    #queryset = Cliente.objects.get(pk=request.GET.get("id"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ACTUALIZAR DE CONTACTO EMERGENCIA'
        context['url_anterior'] = '/fichaPersonal/contactoEmergencia'
        context['listar_url'] = '/fichaPersonal/contactoEmergencia'
        return context


class EliminarContactoEmergencia(DeleteView):
    model = ContactoEmergencias
    template_name = "ContactoEmergencia/delete.html"
    success_url = reverse_lazy('ficha_Personal:deleteContactoEmergencia')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ELMINAR DE CONTACTO EMERGENCIA'
        context['url_anterior'] = '/fichaPersonal/contactoEmergencia'
        context['listar_url'] = '/fichaPersonal/contactoEmergencia'
        return context

