from django.shortcuts import render,redirect,get_object_or_404
from bola.forms import CommunityForm
from bola.models import Community

def index(request):
    communities = Community.objects.all() # Consulta todas as linhas
    context = {"communities": communities} # Context é as variáveis que vão ser usadas no template
    return render(request,"bola/communities.html",context=context)

def community_create(request):
    if request.method == 'POST':
        form = CommunityForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            sobre = form.cleaned_data['sobre']
            community = Community(nome=nome,sobre=sobre)
            community.nome_tag_generator()
            community.save() # Salva no banco de dados
            return redirect(index) # Redireciona para outra view 
    form = CommunityForm()
    context = {"form":form}
    return render(request,"bola/community_create.html",context=context)

def community_edit(request,nome_tag):    
    if request.method == 'POST':
        form = CommunityForm(request.POST)
        if form.is_valid():
            community = get_object_or_404(Community, nome_tag=nome_tag)
            
            nome = form.cleaned_data['nome']
            sobre = form.cleaned_data['sobre']

            if nome != community.nome:
                community.nome = nome
                community.nome_tag_generator()

            community.nome = nome
            community.sobre = sobre

            community.save()
            return redirect(index)
    community = get_object_or_404(Community, nome_tag=nome_tag)
    form = CommunityForm(initial={'nome':community.nome,'sobre':community.sobre})
    context = {"form":form,"community":community}
    return render(request,"bola/community_edit.html",context=context)

def community_view(request, nome_tag):
    community = get_object_or_404(Community, nome_tag=nome_tag)
    context = {'community':community}
    return render(request,"bola/community.html",context=context)

def community_delete(request,nome_tag):
    community = get_object_or_404(Community, nome_tag=nome_tag)
    community.delete()
    return redirect(index)