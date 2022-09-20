import json
from decimal import Decimal

from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from aplicaciones.ventas.forms import VentaForm
from aplicaciones.ventas.models import Factura, Articulo, FacturaDetalle
from proyecto_administrativo.constantes import Opciones

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
    form_class = VentaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/venta/crear/'
        context['titulo'] = 'CREAR VENTA'
        context['url_anterior'] = '/venta/menu'
        context['listar_url'] = '/venta/consulta'
        context['action'] = 'add'
        context['articulos'] = Articulo.objects.filter(estado=True)
        context['iva'] = Opciones.iva
        return context

    def post(self,request,*args,**kwargs):
      try:
        data = json.loads(request.body)
        print(request.user.id)
        factura = Factura()
        factura.usuario_id=request.user.id
        factura.cliente_id=int(data['cliente'])
        factura.fecha=data['fecha']
        factura.forma_pago=data['forma_pago']
        factura.subtotal=float(data['subtotal'])
        factura.iva=float(data['iva'])
        factura.total=float(data['total'])
        print(factura)
        factura.save()
        items = data['articulos']
        # form = self.form_class(data)
        for item in items:
            #{id:1,precio:2}
            art = Articulo.objects.filter(id=int(item['id']))
            if art.exists():
                detalle = FacturaDetalle(
                    factura_id=factura.id,
                    articulo_id=int(item['id']),
                    cantidad=float(item['cantidad']),
                    precio=float(item['precio']),
                    subtotal=float(item['subtotal']),
                    iva=float(item['iva']),
                    total=float(item['total'])
                )
                detalle.save()
                articuloReal = art[0]
                articuloReal.stock = articuloReal.stock - Decimal(detalle.cantidad)
                articuloReal.save()
                data["error"] = "ok"
      except Exception as e:
          data["error"]=str(e)
          print(e)

      return JsonResponse(data,safe="false")
