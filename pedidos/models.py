from django.db import models


class Pedido(models.Model):
    cliente_nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    pedido = models.TextField()
    pagamento = models.CharField(max_length=50)
    taxa_entrega = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    impresso = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cliente_nome