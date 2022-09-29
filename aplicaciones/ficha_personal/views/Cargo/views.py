from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from aplicaciones.ficha_personal.forms import CargoForm
from aplicaciones.ficha_personal.models import Cargo

class CargoListView(ListView):
    template_name = "Cargo/listCargos.html"
    context_object_name = 'cargo'
    model = Cargo
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
        context['listar_url']= '/fichaPersonal/cargo'
        context['crear_url'] = '/fichaPersonal/crearcargo/'
        context['titulo'] = 'LISTADO DE CARGOS'
        context['query'] = self.request.GET.get("query") or ""
        return context

class CrearCargo(CreateView):
    model = Cargo
    template_name = "Cargo/formCargo.html"
    success_url = reverse_lazy('ficha_Personal:cargo')
    form_class = CargoForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/fichaPersonal/crearcargo/'
        context['titulo'] = 'CREAR CARGO'
        context['url_anterior'] = '/fichaPersonal/cargo'
        context['listar_url'] = '/fichaPersonal/cargo'
        context['action'] = 'add'
        return context


class ActualizarCargo(UpdateView):
    model = Cargo
    template_name = "Cargo/formCargo.html"
    success_url = reverse_lazy('ficha_Personal:cargo')
    form_class = CargoForm
    #queryset = Cliente.objects.get(pk=request.GET.get("id"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ACTUALIZAR CARGO'
        context['url_anterior'] = '/fichaPersonal/cargo'
        context['listar_url'] = '/fichaPersonal/cargo'
        return context


class EliminarCargo(DeleteView):
    model = Cargo
    template_name = "Cargo/eliminar_cargo.html"
    success_url = reverse_lazy('ficha_Personal:cargo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ELMINAR CARGO'
        context['url_anterior'] = '/fichaPersonal/cargo'
        context['listar_url'] = '/fichaPersonal/cargo'
        return context
