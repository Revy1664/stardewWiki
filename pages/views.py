from django.views.generic import ListView, DetailView

from .models import Theme


class HomePageView(ListView):
	model = Theme
	template_name = "pages/index.html"
	context_object_name = "themes"


class ThemeDetailPageView(DetailView):
	model = Theme
	template_name = "pages/theme_detail.html"
	context_object_name = "theme"
