from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from aplicaciones.ficha_personal.forms import InfoAcademicaForm
from aplicaciones.ficha_personal.models import InfoAcademica

class InfoAcademicaListView(ListView):
    template_name = "InformacionAcademica/listInfoAcademica.html"
    context_object_name = 'infoAcademica'
    model = InfoAcademica
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
        context['listar_url']= '/fichaPersonal/infoAcademica'
        context['crear_url'] = '/fichaPersonal/crearinfoAcademica'
        context['titulo'] = 'LISTADO DE INFORMACIÓN ACADÉMICA'
        context['query'] = self.request.GET.get("query") or ""
        return context

class RegistroInfoAcademicaListView(ListView):
    template_name = "InformacionAcademica/registroInfoAcademica.html"
    model = InfoAcademica
    context_object_name = 'infoAcademicas'
    paginate_by = 5
    #queryset = Cliente.objects.filter(estado=True)

    def get_queryset(self):
        #print("mira", type(self.kwargs['pk']), self.kwargs['pk'])
        return self.model.objects.filter(empleado__id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/fichaPersonal/infoAcademica'
        context['listar_url']= '/fichaPersonal/registroInfoAcademica'
        context['crear_url'] = '/fichaPersonal/crearInfoAcademica'
        context['titulo'] = 'REGISTRO DE INFORMACIÓN ACADÉMICA'
        context['query'] = self.request.GET.get("query") or ""
        return context

class CrearInfoAcademica(CreateView):
    model = InfoAcademica
    template_name = "InformacionAcademica/form.html"
    success_url = reverse_lazy('ficha_Personal:infoAcademica')
    form_class = InfoAcademicaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/fichaPersonal/crearInfoAcademica'
        context['titulo'] = 'CREAR INFORMACIÓN ACADÉMICA'
        context['url_anterior'] = '/fichaPersonal/registroInfoAcademica'
        context['listar_url'] = '/fichaPersonal/infoAcademica'
        context['action'] = 'add'
        return context

class ActualizarInfoAcademica(UpdateView):
    model = InfoAcademica
    template_name = "InformacionAcademica/form.html"
    success_url = reverse_lazy('ficha_Personal:actualizarInfoAcademica')
    form_class = InfoAcademicaForm
    #queryset = Cliente.objects.get(pk=request.GET.get("id"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ACTUALIZAR DE INFORMACIÓN ACADÉMICA'
        context['url_anterior'] = '/fichaPersonal/infoAcademica'
        context['listar_url'] = '/fichaPersonal/infoAcademica'
        return context


class EliminarInfoAcademica(DeleteView):
    model = InfoAcademica
    template_name = "InformacionAcademica/delete.html"
    success_url = reverse_lazy('ficha_Personal:deleteInfoAcademica')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ELMINAR DE INFORMACIÓN ACADÉMICA'
        context['url_anterior'] = '/fichaPersonal/infoAcademica'
        context['listar_url'] = '/fichaPersonal/infoAcademica'
        return context

