"""
URL configuration for crm_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token-auth/', obtain_auth_token),
    path('api/login/', obtain_auth_token, name='api_login'),
    path('api/', include('core.urls')),  # Inclui todas as rotas da app core
    path('', include('core.urls')),     # Para rotas como /dashboard/
    path('', views.home_redirect_view),  # Redireciona a raiz para /dashboard/
    # path('api/token-auth/', obtain_auth_token, name='api_token_auth'),
    # path('api/login/', obtain_auth_token, name='api_login'),
    # path('admin/', admin.site.urls),
    # #path('', views.home, name='home'),  # Definimos a rota principal "/"
    # path('dashboard/', views.dashboard_view, name='dashboard'),
    # path('', views.home_redirect_view),  # Redireciona a raiz para /dashboard/
    # # path('', RedirectView.as_view(url='/dashboard/', permanent=False)),  # redirecionando para a dashboard
    # path('api/', include('core.urls')),  # Incluindo as rotas da app core
    # path('api/clientes/', views.cliente_list, name='cliente-list'),
    # path('api/cadastrar-cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    # path('api/deletar-cliente/<int:cliente_id>/', views.deletar_cliente, name='deletar_cliente'),
    # path('api/atualizar-cliente/<int:cliente_id>/', views.atualizar_cliente, name='atualizar_cliente'),
    # path('api/clientes/<int:cliente_id>/', views.cliente_detalhes, name='cliente-detalhes'),  # ✅ Nova rota
    # path('produtos/', views.produto_list, name='produto-list'),
    # path('api/cadastrar-produtos/', views.cadastrar_cliente, name='cadastrar_produto'),
    # path('api/deletar-produtos/<int:produto_id>/', views.deletar_cliente, name='deletar_produto'),
    # path('api/atualizar-produtos/<int:produto_id>/', views.atualizar_cliente, name='atualizar_produto'),
    # path('api/produtos/<int:produto_id>/', views.cliente_detalhes, name='produto-detalhes'),  # ✅ Nova rota
    # path('fornecedores/', views.produto_list, name='fornecedor-list'),
    # path('api/cadastrar-fornecedores/', views.cadastrar_cliente, name='cadastrar_fornecedor'),
    # path('api/deletar-fornecedores/<int:fornecedor_id>/', views.deletar_cliente, name='deletar_fornecedor'),
    # path('api/atualizar-fornecedores/<int:fornecedor_id>/', views.atualizar_cliente, name='atualizar_fornecedor'),
    # path('api/fornecedores/<int:fornecedor_id>/', views.cliente_detalhes, name='fornecedor-detalhes'),  # ✅ Nova rota
    # path('vendas/', views.venda_list, name='venda-list'),
    # path('csrf/', views.get_csrf_token, name='get-csrf-token'),
]
