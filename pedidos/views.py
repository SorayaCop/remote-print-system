from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Pedido
import json


@login_required
def novo_pedido(request):
    if request.method == "POST":
        cliente_nome = request.POST.get("cliente_nome", "").strip()
        endereco = request.POST.get("endereco", "").strip()
        pedido = request.POST.get("pedido", "").strip()
        pagamento = request.POST.get("pagamento", "").strip()
        taxa_entrega = request.POST.get("taxa_entrega", "0").replace(",", ".")
        total = request.POST.get("total", "0").replace(",", ".")

        if cliente_nome and endereco and pedido and pagamento:
            Pedido.objects.create(
                cliente_nome=cliente_nome,
                endereco=endereco,
                pedido=pedido,
                pagamento=pagamento,
                taxa_entrega=taxa_entrega,
                total=total,
            )
            return render(request, "pedidos/sucesso.html")

    return render(request, "pedidos/novo_pedido.html")


def proximo_pedido(request):
    pedido = Pedido.objects.filter(impresso=False).order_by("criado_em").first()

    if not pedido:
        return JsonResponse({"pedido": None})

    return JsonResponse({
        "id": pedido.id,
        "cliente_nome": pedido.cliente_nome,
        "endereco": pedido.endereco,
        "pedido": pedido.pedido,
        "pagamento": pedido.pagamento,
        "taxa_entrega": str(pedido.taxa_entrega),
        "total": str(pedido.total),
    })


@csrf_exempt
def marcar_impresso(request):
    if request.method != "POST":
        return JsonResponse({"ok": False, "erro": "Método não permitido"}, status=405)

    try:
        dados = json.loads(request.body)
        pedido_id = dados.get("id")

        pedido = Pedido.objects.get(id=pedido_id)
        pedido.impresso = True
        pedido.save()

        return JsonResponse({"ok": True})

    except Pedido.DoesNotExist:
        return JsonResponse({"ok": False, "erro": "Pedido não encontrado"}, status=404)

    except Exception as e:
        return JsonResponse({"ok": False, "erro": str(e)}, status=400)