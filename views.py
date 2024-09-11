from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'index.html'  # Le template que vous voulez rendre

    def get_context_data(self, **kwargs):
        # Appeler la méthode de la classe parente pour obtenir le contexte de base
        context = super().get_context_data(**kwargs)
        # Ajouter des données supplémentaires au contexte
        context['welcome_message'] = 'Bienvenue sur Learn and Films!'
        return context

