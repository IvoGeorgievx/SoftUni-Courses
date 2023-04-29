from django.urls import path

from epfive.web.views import IndexView, RecipeCreateView, RecipeDetailsView, RecipeDeleteView, EditRecipeView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', RecipeCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', EditRecipeView.as_view(), name='edit'),
    path('delete/<int:pk>/', RecipeDeleteView.as_view(), name='delete'),
    path('details/<int:pk>/', RecipeDetailsView.as_view(), name='details'),

]