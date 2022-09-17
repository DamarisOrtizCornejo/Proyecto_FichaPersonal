from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from aplicaciones.ventas.forms import VentaForm
from aplicaciones.ventas.models import Factura, Articulo


class ConsultaVenta(ListView):
    template_name = 'venta/list.html'
    context_object_name = 'facturas'
    model = Factura
    paginate_by = 3
    def get_queryset(self):
        query = self.request.GET.get("query")
        print(query)
        if query:
            return self.model.objects.filter(cliente__nombres__icontains=query)
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/venta/menu/'
        context['listar_url']= '/venta/consulta/',
        context['crear_url'] = '/venta/crear/'
        context['titulo'] = 'LISTADO DE FACTURAS'
        context['query'] = self.request.GET.get("query") or ""
        return context

class CrearVenta(CreateView):
    template_name = 'venta/form_venta.html'
    model = Factura
    success_url = reverse_lazy('ventas:consultaventa')
    #form_class = VentaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/venta/crearventa/'
        context['titulo'] = 'CREAR VENTA'
        context['url_anterior'] = '/venta/menu'
        context['listar_url'] = '/venta/consulta'
        context['action'] = 'add'
        context['articulos'] = Articulo.objects.filter(estado=True)

        return context

    def post(self, request, *args, **kwargs):
        print(request)