from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'sort'
urlpatterns = [
	path('', views.hello, name='hello'),
	path('mainpage/', views.mainpage, name='mainpage'),
	path('mainpage2/', views.mainpage2, name='mainpageend'),
	path('add_list/', views.add_list, name='add_list'),
	path('add_list_end/', views.add_list_end, name='add_list_end'),
	path('add_funcs/', views.add_funcs, name='add_funcs'),
	path('add_list_func/', views.add_list_func, name='add_list_func'),
	path('add_list_random/', views.add_list_random, name='add_list_random'),
	path('add_lists/', views.add_lists, name='add_lists'),
	path('add_lists_func/', views.add_lists_func, name='add_lists_func'),
	path('add_lists_random/', views.add_lists_random, name='add_lists_random'),
	path('modern_list/', views.modern_list, name='modern_list'),
	path('doubleTrack/', views.doubleTrack, name='doubleTrack'),
	path('doubleTrackShow/', views.doubleTrackShow, name='doubleTrackShow'),
	path('abstract/', views.abstract, name='abstract'),
	path('abstractShow/', views.abstractShow, name='abstractShow'),
	path('nish/', views.nish, name='nish'),
	path('nishShow/', views.nishShow, name='nishShow'),
	path('vosh/', views.vosh, name='vosh'),
	path('voshShow/', views.voshShow, name='voshShow'),
	path('ultrasort/', views.ultrasort, name='ultrasort'),
	path('ultrasortShow/', views.ultrasortShow, name='ultrasortShow'),
	path('mainpageend/', views.ultrasortShow, name='mainpageend'),
	path('sendEmail', views.sendEmail, name='sendEmail'),

]
