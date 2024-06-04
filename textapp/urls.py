from django.urls import path
from .views import index, add_text, edit_text, display_text

urlpatterns = [
    path('', index, name = 'index'),
    path('add_text/', add_text, name='add'),
    path('edit_text/<int:id>', edit_text, name = 'edit'),
    path('display_text/<int:id>', display_text, name='display'),
]
