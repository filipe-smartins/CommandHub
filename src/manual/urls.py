from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tipo/<int:tipo_id>/', views.tipo_detail, name='tipo_detail'),
    path('tipo/edit/<int:tipo_id>/', views.tipo_edit, name='tipo_edit'),
    path('tipo/delete/<int:tipo_id>/', views.tipo_delete, name='tipo_delete'),
    path('categoria/<int:categoria_id>/', views.categoria_detail, name='categoria_detail'),
    path('categoria/edit/<int:categoria_id>/', views.categoria_edit, name='categoria_edit'),
    path('categoria/delete/<int:categoria_id>/', views.categoria_delete, name='categoria_delete'),
    path('secao/<int:secao_id>/', views.secao_detail, name='secao_detail'),
    path('secao/edit/<int:secao_id>/', views.secao_edit, name='secao_edit'),
    path('secao/delete/<int:secao_id>/', views.secao_delete, name='secao_delete'),
    # Comando CRUD
    path('comando/edit/<int:comando_id>/', views.comando_edit, name='comando_edit'),
    path('comando/delete/<int:comando_id>/', views.comando_delete, name='comando_delete'),
    # Artigo CRUD
    path('artigo/edit/<int:artigo_id>/', views.artigo_edit, name='artigo_edit'),
    path('artigo/delete/<int:artigo_id>/', views.artigo_delete, name='artigo_delete'),
    path('tipo/add/', views.tipo_add, name='tipo_add'),
    path('categoria/add/<int:tipo_id>/', views.categoria_add, name='categoria_add'),
    path('secao/add/<int:categoria_id>/', views.secao_add, name='secao_add'),
]
