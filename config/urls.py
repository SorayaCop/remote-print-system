from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from pedidos.views import novo_pedido, proximo_pedido, marcar_impresso

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", LoginView.as_view(template_name="pedidos/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("", novo_pedido, name="novo_pedido"),
    path("api/proximo-pedido/", proximo_pedido, name="proximo_pedido"),
    path("api/marcar-impresso/", marcar_impresso, name="marcar_impresso"),
]