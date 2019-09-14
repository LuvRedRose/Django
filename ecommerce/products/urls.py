from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from.views import index, AddProduct, DeleteProduct, UpdateProduct

app_name = 'products'

urlpatterns = [
    path('delete/<int:delete_id>', DeleteProduct, name='delete'),
    path('update/<int:update_id>', UpdateProduct, name='update'),
    path('add/', AddProduct, name='add'),
    path('', index, name='index'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
