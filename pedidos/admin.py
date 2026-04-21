from django.contrib import admin
from .models import Pedido


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente_nome', 'pagamento', 'impresso', 'criado_em')