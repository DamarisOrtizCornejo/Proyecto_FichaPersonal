from django.views.generic.base import TemplateView

class FichaPersonalTemplateView(TemplateView):
    template_name = 'fichaPersonal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "fichaPersonal"
        context['url_anterior'] = "/"
        return context