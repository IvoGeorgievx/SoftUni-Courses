from django.shortcuts import render, redirect

from epfive.web.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from epfive.web.models import Recipe
from django.views import generic as views


class IndexView(views.View):
    def get(self, request):
        context = {
            'recipes': Recipe.objects.all()
        }
        return render(request, 'index.html', context)


class RecipeCreateView(views.CreateView):
    model = Recipe
    template_name = 'create.html'
    fields = '__all__'
    success_url = '/'


class RecipeDetailsView(views.DetailView):
    model = Recipe
    template_name = 'details.html'


class EditRecipeView(views.UpdateView):
    model = Recipe
    template_name = 'edit.html'
    fields = '__all__'
    success_url = '/'
# def edit(request, pk):
#     recipe = Recipe.objects.filter(pk=pk).get()
#     if request.method == 'GET':
#         form = EditRecipeForm(instance=recipe)
#     else:
#         form = EditRecipeForm(request.POST, instance=recipe)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     context = {
#         'form': form,
#         'recipe': recipe,
#     }
#     return render(request, 'edit.html', context)


class RecipeDeleteView(views.DeleteView):
    model = Recipe
    template_name = 'delete.html'
    success_url = '/'
