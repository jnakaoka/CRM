from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import ClienteForm, ProdutoForm, VendaForm
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Cliente, Produto, Fornecedor, Venda
from .serializers import ClienteSerializer, ProdutoSerializer,  VendaSerializer, FornecedorSerializer
from django.db.models import Sum

# Create your views here.
def home(request):
    return HttpResponse("<h1>Bem-vindo ao CRM!</h1>")

def dashboard_view(request):
    # Coleta dados do banco
    total_clientes = Cliente.objects.count()
    total_produtos = Produto.objects.count()
    total_fornecedores = Fornecedor.objects.count()
    total_vendas = Venda.objects.count()

    # Opcional: total vendido (somando valores das vendas)
    total_valor_vendas = Venda.objects.aggregate(total=Sum('valor'))['total'] or 0

    return JsonResponse({
        'clientes': total_clientes,
        'produtos': total_produtos,
        'fornecedores': total_fornecedores,
        'vendas': total_vendas,
        'total_valor_vendas': total_valor_vendas,
    })

def home_redirect_view(request):
    return redirect('/dashboard/')

@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def cadastrar_cliente(request):
    if request.method == "POST":
        print("📥 Entrou no POST de cadastrar_cliente")
        print("📌 Recebendo POST:", request.data)  # LOG PARA DEPURAÇÃO
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            cliente = serializer.save()  # 🔥 Aqui o cliente é salvo!
            print("✅ Cliente salvo:", cliente)
            return Response(ClienteSerializer(cliente).data, status=201)
        
        print("❌ Erro na validação:", serializer.errors)
        return Response(serializer.errors, status=400)
        

    clientes = Cliente.objects.all()
    serializer = ClienteSerializer(clientes, many=True)
    return Response(serializer.data)

@api_view(["DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deletar_cliente(request, cliente_id):
    try:
        cliente = Cliente.objects.get(id=cliente_id)
        cliente.delete()
        return Response({"message": "Cliente excluído com sucesso!"}, status=204)
    except Cliente.DoesNotExist:
        return Response({"error": "Cliente não encontrado!"}, status=404)
    
@api_view(["PUT"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def atualizar_cliente(request, cliente_id):
    try:
        cliente = Cliente.objects.get(id=cliente_id)
    except Cliente.DoesNotExist:
        return Response({"error": "Cliente não encontrado!"}, status=404)

    serializer = ClienteSerializer(cliente, data=request.data, partial=True)  # Permite atualização parcial
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    
    return Response(serializer.errors, status=400)

@api_view(["GET", "PUT", "DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def cliente_detalhes(request, cliente_id):
    try:
        cliente = Cliente.objects.get(id=cliente_id)
    except Cliente.DoesNotExist:
        return Response({"erro": "Cliente não encontrado"}, status=404)

    if request.method == "GET":
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        cliente.delete()
        return Response({"mensagem": "Cliente deletado"}, status=204)

# def cliente_list(request):
#     clientes = list(Cliente.objects.values())
#     return JsonResponse(clientes, safe=False)

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def cliente_list(request):
    clientes = Cliente.objects.all()
    serializer = ClienteSerializer(clientes, many=True)
    return Response(serializer.data)

@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def cadastrar_produto(request):
    if request.method == "POST":
        print("📌 Recebendo POST:", request.data)  # LOG PARA DEPURAÇÃO
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            produto = serializer.save()  # 🔥 Aqui o cliente é salvo!
            print("✅ Produto salvo:", produto)
            return Response(ProdutoSerializer(produto).data, status=201)
        
        print("❌ Erro na validação:", serializer.errors)
        return Response(serializer.errors, status=400)
        

    produtos = Produto.objects.all()
    serializer = ProdutoSerializer(produtos, many=True)
    return Response(serializer.data)

@api_view(["DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deletar_produto(request, produto_id):
    try:
        produto = Produto.objects.get(id=produto_id)
        produto.delete()
        return Response({"message": "Produto excluído com sucesso!"}, status=204)
    except Produto.DoesNotExist:
        return Response({"error": "Produto não encontrado!"}, status=404)
    
@api_view(["PUT"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def atualizar_produto(request, produto_id):
    try:
        produto = Produto.objects.get(id=produto_id)
    except Produto.DoesNotExist:
        return Response({"error": "Cliente não encontrado!"}, status=404)

    serializer = ProdutoSerializer(produto, data=request.data, partial=True)  # Permite atualização parcial
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    
    return Response(serializer.errors, status=400)

@api_view(["GET", "PUT", "DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def produto_detalhes(request, produto_id):
    try:
        produto = Produto.objects.get(id=produto_id)
    except Produto.DoesNotExist:
        return Response({"erro": "Produto não encontrado"}, status=404)

    if request.method == "GET":
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        produto.delete()
        return Response({"mensagem": "Produto deletado"}, status=204)



# def produto_list(request): funciona mas estar semanticamente incorreto
#     produtos = list(Produto.objects.values())
#     return JsonResponse(produtos, safe=False)

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def produto_list(request):
    produtos = Produto.objects.all()
    serializer = ProdutoSerializer(produtos, many=True)
    return Response(serializer.data)

@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def cadastrar_fornecedor(request):
    if request.method == "POST":
        print("📌 Recebendo POST:", request.data)  # LOG PARA DEPURAÇÃO
        serializer = FornecedorSerializer(data=request.data)
        if serializer.is_valid():
            fornecedor = serializer.save()  # 🔥 Aqui o cliente é salvo!
            print("✅ Fornecedor salvo:", fornecedor)
            return Response(FornecedorSerializer(fornecedor).data, status=201)
        
        print("❌ Erro na validação:", serializer.errors)
        return Response(serializer.errors, status=400)
        

    fornecedores = Fornecedor.objects.all()
    serializer = FornecedorSerializer(fornecedores, many=True)
    return Response(serializer.data)

@api_view(["DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deletar_fornecedor(request, fornecedor_id):
    try:
        fornecedor = Fornecedor.objects.get(id=fornecedor_id)
        fornecedor.delete()
        return Response({"message": "Fornecedor excluído com sucesso!"}, status=204)
    except Fornecedor.DoesNotExist:
        return Response({"error": "Fornecedor não encontrado!"}, status=404)
    
@api_view(["PUT"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def atualizar_fornecedor(request, fornecedor_id):
    try:
        fornecedor = Fornecedor.objects.get(id=fornecedor_id)
    except Fornecedor.DoesNotExist:
        return Response({"error": "Fornecedor não encontrado!"}, status=404)

    serializer = FornecedorSerializer(fornecedor, data=request.data, partial=True)  # Permite atualização parcial
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    
    return Response(serializer.errors, status=400)

@api_view(["GET", "PUT", "DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def fornecedor_detalhes(request, fornecedor_id):
    try:
        fornecedor = Fornecedor.objects.get(id=fornecedor_id)
    except Fornecedor.DoesNotExist:
        return Response({"erro": "Fornecedor não encontrado"}, status=404)

    if request.method == "GET":
        serializer = FornecedorSerializer(fornecedor)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = FornecedorSerializer(fornecedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        fornecedor.delete()
        return Response({"mensagem": "Fornecedor deletado"}, status=204)
    
# def fornecedor_list(request):
#     fornecedores = list(Fornecedor.objects.values())
#     return JsonResponse(fornecedores, safe=False)

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def fornecedor_list(request):
    fornecedores = Fornecedor.objects.all()
    serializer = FornecedorSerializer(fornecedores, many=True)
    return Response(serializer.data)


@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def cadastrar_venda(request):
    if request.method == "POST":
        print("📌 Recebendo POST:", request.data)  # LOG PARA DEPURAÇÃO
        serializer = VendaSerializer(data=request.data)
        if serializer.is_valid():
            venda = serializer.save()  # 🔥 Aqui o cliente é salvo!
            print("✅ Venda salva:", venda)
            return Response(VendaSerializer(venda).data, status=201)
        
        print("❌ Erro na validação:", serializer.errors)
        return Response(serializer.errors, status=400)
        

    vendas = Venda.objects.all()
    serializer = VendaSerializer(vendas, many=True)
    return Response(serializer.data)

@api_view(["DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deletar_venda(request, venda_id):
    try:
        venda = Venda.objects.get(id=venda_id)
        venda.delete()
        return Response({"message": "Venda excluído com sucesso!"}, status=204)
    except Venda.DoesNotExist:
        return Response({"error": "Venda não encontrado!"}, status=404)
    
@api_view(["PUT"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def atualizar_venda(request, venda_id):
    try:
        venda = Venda.objects.get(id=venda_id)
    except Venda.DoesNotExist:
        return Response({"error": "Venda não encontrado!"}, status=404)

    serializer = VendaSerializer(venda, data=request.data, partial=True)  # Permite atualização parcial
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    
    return Response(serializer.errors, status=400)

@api_view(["GET", "PUT", "DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def venda_detalhes(request, venda_id):
    try:
        venda = Venda.objects.get(id=venda_id)
    except Venda.DoesNotExist:
        return Response({"erro": "Venda não encontrado"}, status=404)

    if request.method == "GET":
        serializer = VendaSerializer(venda)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = VendaSerializer(venda, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        venda.delete()
        return Response({"mensagem": "Venda deletada"}, status=204)
    
# def venda_list(request):
#     vendas = list(Venda.objects.values())
#     return JsonResponse(vendas, safe=False)

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def venda_list(request):
    vendas = Venda.objects.all()
    serializer = VendaSerializer(vendas, many=True)
    return Response(serializer.data)