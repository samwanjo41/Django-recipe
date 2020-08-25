from django.urls import path
from . import views
from .views import RecipeUpdateView, RecipeDeleteView, RecipeDetailView, RecipeSearchListView

urlpatterns = [   
    path('', views.recipe, name='recipe'),
    path('create', views.createRecipe, name='create'),
    
    # path('update/<int:id>/', views.updateRecipe, name='update'),
    path('update/<int:pk>/', RecipeUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', RecipeDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', RecipeDetailView.as_view(), name='detail'),
    path('search', RecipeSearchListView.as_view(), name='search'),
]

