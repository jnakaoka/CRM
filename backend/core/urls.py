from django.urls import path, re_path
from django.views.generic.base import TemplateView
from core import views


urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    re_path(r'^dashboard/?$', TemplateView.as_view(template_name="index.html")),

    # Clientes
    path('clientes/', views.cliente_list, name='cliente-list'),
    path('cadastrar-cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('deletar-cliente/<int:cliente_id>/', views.deletar_cliente, name='deletar_cliente'),
    path('atualizar-cliente/<int:cliente_id>/', views.atualizar_cliente, name='atualizar_cliente'),
    path('clientes/<int:cliente_id>/', views.cliente_detalhes, name='cliente-detalhes'),

    # Produtos
    path('produtos/', views.produto_list, name='produto-list'),
    path('cadastrar-produto/', views.cadastrar_produto, name='cadastrar_produto'),
    path('deletar-produto/<int:produto_id>/', views.deletar_produto, name='deletar_produto'),
    path('atualizar-produto/<int:produto_id>/', views.atualizar_produto, name='atualizar_produto'),
    path('produtos/<int:produto_id>/', views.produto_detalhes, name='produto-detalhes'),

    # Fornecedores
    path('fornecedores/', views.fornecedor_list, name='fornecedor-list'),
    path('cadastrar-fornecedor/', views.cadastrar_fornecedor, name='cadastrar_fornecedor'),
    path('deletar-fornecedor/<int:fornecedor_id>/', views.deletar_fornecedor, name='deletar_fornecedor'),
    path('atualizar-fornecedor/<int:fornecedor_id>/', views.atualizar_fornecedor, name='atualizar_fornecedor'),
    path('fornecedores/<int:fornecedor_id>/', views.fornecedor_detalhes, name='fornecedor-detalhes'),

    # Vendas
    path('vendas/', views.venda_list, name='venda-list'),
    path('cadastrar-venda/', views.cadastrar_venda, name='cadastrar_venda'),
    path('deletar-venda/<int:venda_id>/', views.deletar_venda, name='deletar_venda'),
    path('atualizar-venda/<int:venda_id>/', views.atualizar_venda, name='atualizar_venda'),
    path('vendas/<int:venda_id>/', views.venda_detalhes, name='venda-detalhes'),
    
    # path('api/token-auth/', obtain_auth_token, name='api_token_auth'),
    # path('api/login/', obtain_auth_token, name='api_login'),
    # # path('', views.home, name='home'),  # Definimos a rota principal "/"
    # path('dashboard/', dashboard_view, name='dashboard'),
    # path('', home_redirect_view),  # Redireciona a raiz para /dashboard/
    # # path('', RedirectView.as_view(url='/dashboard/', permanent=False)),  # redirecionando para a dashboard
    # path('api/clientes/', views.cliente_list, name='cliente-list'),
    # path('api/cadastrar-cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    # path('api/deletar-cliente/<int:cliente_id>/', views.deletar_cliente, name='deletar_cliente'),
    # path('api/atualizar-cliente/<int:cliente_id>/', views.atualizar_cliente, name='atualizar_cliente'),
    # path('api/clientes/<int:cliente_id>/', views.cliente_detalhes, name='cliente-detalhes'),  # ✅ Nova rota
    # path('produtos/', views.produto_list, name='produto-list'),
    # path('api/cadastrar-produtos/', views.cadastrar_produto, name='cadastrar_produto'),
    # path('api/deletar-produtos/<int:produto_id>/', views.deletar_produto, name='deletar_produto'),
    # path('api/atualizar-produtos/<int:produto_id>/', views.atualizar_produto, name='atualizar_produto'),
    # path('api/produtos/<int:produto_id>/', views.produto_detalhes, name='produto-detalhes'),  # ✅ Nova rota
    # path('fornecedores/', views.fornecedor_list, name='fornecedor-list'),
    # path('api/cadastrar-fornecedores/', views.cadastrar_fornecedor, name='cadastrar_fornecedor'),
    # path('api/deletar-fornecedores/<int:fornecedor_id>/', views.deletar_fornecedor, name='deletar_fornecedor'),
    # path('api/atualizar-fornecedores/<int:fornecedor_id>/', views.atualizar_fornecedor, name='atualizar_fornecedor'),
    # path('api/fornecedores/<int:fornecedor_id>/', views.fornecedor_detalhes, name='fornecedor-detalhes'),  # ✅ Nova rota
    # path('vendas/', views.venda_list, name='venda-list'),
    # re_path(r'^dashboard/?$', TemplateView.as_view(template_name="index.html")),
]
