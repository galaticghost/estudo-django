from django.shortcuts import render,redirect
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
            community.save() # Salva no banco de dados
            return redirect(index) # Redireciona para outra view 
    form = CommunityForm()
    context = {"form":form}
    return render(request,"bola/community_create.html",context=context)

def community(request, nome):
    test = Community.objects.filter(nome=nome)
    context = {'community':test}
    return render(request,"bola/community.html",context=context)