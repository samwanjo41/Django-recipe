from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Recipe
from .forms import CreateRecipeForm, UpdateRecipeForm
from django.views.generic.edit import UpdateView, DeleteView 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.db.models import Q


def recipe(request):
    recipe = Recipe.objects.all()
   
    context = {
        'recipe':recipe,
        
    }
    return render(request, 'recipe/recipe.html', context)

@login_required
def createRecipe(request):    
    if request.method == 'POST':  
        form = CreateRecipeForm(request.POST, request.FILES)      
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, f'Recipe Created')
            return redirect('recipe')
        else:
            messages.error(request, 'Recipe Not created')
    else:
        form = CreateRecipeForm()
    context = {
        'form':form,
        'title':'Create Recipe',
    }
    return render(request, 'recipe/create.html', context)

# def updateRecipe(request, id):
#     recipe = Recipe.objects.get(id = id)
#     if request.method == 'POST':
#         form = UpdateRecipeForm(request.POST, request.FILES, instance=recipe)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Recipe Updated')
#             return redirect('recipe')
#         else:
#              messages.error(request, 'Recipe Not updated')
#     else:
#         form = UpdateRecipeForm(request.POST, instance=recipe)
#     context = {
#         'title':'Update Recipe',
#         'recipe':recipe,
#         'form':form
#     }
#     return render(request, 'recipe/update.html', context)


class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ['title', 'description', 'image']
    template_name = 'recipe/update.html'


class RecipeDeleteView(DeleteView):
    model =  Recipe
    success_url = reverse_lazy('recipe')
    template_name = 'recipe/delete.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe/detail.html'

class RecipeSearchListView(ListView):
    model = Recipe
    template_name = 'recipe/search.html'
    context_object_name ='recipe'

    def get_queryset(self):
        query = self.request.GET.get('title')
        recipe = Recipe.objects.filter(
            Q(name_icontains=query))
        return recipe