from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from aplicaciones.ficha_personal.forms import DatosMedicosForm
from aplicaciones.ficha_personal.models import DatosMedicos