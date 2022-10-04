from django.urls import path

from .views import HomePageView, ThemeDetailPageView


urlpatterns = [
	path("", HomePageView.as_view(), name="home"),
	path("<slug:slug>", ThemeDetailPageView.as_view(), name="theme_detail"),
]