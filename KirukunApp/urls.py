from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('shorten', views.shorten, name='shorten'),
	path('<str:uuid>', views.go, name='go'),
	re_path(r'(?P<re>[/\w]+)', views.dump, name='dump')
]