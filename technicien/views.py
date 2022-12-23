from django.shortcuts import render
from .models import*
from django.core.paginator import Paginator
# Create your views here.

def informaticien(request):
    total = Informaticien.objects.count()
    technicien = Informaticien.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien,
        'total': total
    }
    return render(request, 'techniciens/informaticien.html', context)

def detail(request, myid):
    technicien = Informaticien.objects.get(id=myid)
    context = {
        'technicien':technicien
    }
    return render(request, 'detail.html', context)
    
    

def plombier(request):
    technicien = Plombier.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/plombier.html', context)

def plombier_detail(request, myid):
    technicien = Plombier.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)
    
    

def enseignant(request):
    technicien = Enseignant.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/enseignants.html', context)

def enseignant_detail(request, myid):
    technicien = Enseignant.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)
    
    

def gestionnaire(request):
    technicien = Gestionnaire.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/gestionnaire.html', context)

def gestionnaire_detail(request, myid):
    technicien = Gestionnaire.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)
    
    

def genie_civil(request):
    technicien = Genie_civil.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/genie_civil.html', context)
def genie_civil_detail(request, myid):
    technicien = Genie_civil.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)
    

def comptable(request):
    technicien = Comptable.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/comptable.html', context)
def comptable_detail(request, myid):
    technicien = Comptable.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)
    
    

def agriculture(request):
    technicien = Agriculture.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request,'techniciens/agriculture.html', context)

def agriculture_detail(request, myid):
    technicien = Agriculture.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)



def elevage(request):
    technicien = Elevage.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/elevage.html', context)
def elevage_detail(request, myid):
    technicien = Elevage.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)


def maintenancier(request):
    technicien = Maintenancier.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/maintenancier.html', context)
def maintenancier_detail(request, myid):
    technicien = Maintenancier.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)
    
    

def electricien(request):
    technicien = Electricien.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/electricien.html', context)
def electricien_detail(request, myid):
    technicien = Electricien.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)



def logisticien(request):
    technicien = Logisticien.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/logisticien.html', context)
def logisticien_detail(request, myid):
    technicien = Logisticien.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)
    
    

def maçon(request):
    technicien = Maçon.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/maçon.html', context)
def maçon_detail(request, myid):
    technicien = Maçon.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)
    
    

def mecanicien(request):
    technicien = Mecanicien.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/mecanicien.html', context)
def mecanicien_detail(request, myid):
    technicien = Mecanicien.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)
    
    

def cuisinier(request):
    technicien = Cuisinier.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/cuisinier.html', context)
def cuisinier_detail(request, myid):
    technicien = Cuisinier.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)
    
    

def fille_et_garçon_salle(request):
    technicien = Fille_et_garçon_salle.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/fille_garçon.html', context)
def servante_detail(request, myid):
    technicien = Fille_et_garçon_salle.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)
    
    
    

def tolerie(request):
    technicien = Tolerie.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/tolerie.html', context)
def tolerie_detail(request, myid):
    technicien = Tolerie.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)
    
    

def peintre(request):
    technicien = Peintre.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/peintre.html', context)
def peintre_detail(request, myid):
    technicien = Peintre.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)




def manager(request):
    technicien = Manager.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/manager.html', context)
def manager_detail(request, myid):
    technicien = Manager.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)




def menagere(request):
    technicien = Menagere.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/menagere.html', context)
def menagere_detail(request, myid):
    technicien = Menagere.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)



def veterinaire(request):
    technicien = Veterinaire.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/veterinaire.html', context)
def veterinaire_detail(request, myid):
    technicien = Veterinaire.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)




def developpeur(request):
    technicien = Developpeur.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/developpeur.html', context)
def developpeur_detail(request, myid):
    technicien = Developpeur.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)




def coiffure(request):
    technicien = Coiffure.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/coiffure.html', context)
def coiffure_detail(request, myid):
    technicien = Coiffure.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)




def gardien(request):
    technicien = Gardien.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/gardien.html', context)
def gardien_detail(request, myid):
    technicien = Gardien.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)




def infographie(request):
    technicien = Infographe.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/infographe.html', context)
def infographie_detail(request, myid):
    technicien = Infographe.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)




def multimedia(request):
    technicien = Multimedia.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/multimedia.html', context)
def multimedia_detail(request, myid):
    technicien = Multimedia.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)



def marketeur(request):
    technicien = Marketeur.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/marketeur.html', context)
def marketeur_detail(request, myid):
    technicien = Marketeur.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)





def gardinier(request):
    technicien = Gardinier.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/gardinier.html', context)
def gardinier_detail(request, myid):
    technicien = Gardinier.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)



def reparateur_phone(request):
    technicien = Reparateur_phone.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/phone.html', context)
def phone_detail(request, myid):
    technicien = Reparateur_phone.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)




def reparateur_tele(request):
    technicien = Reparateur_tele.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/tele.html', context)
def tele_detail(request, myid):
    technicien = Reparateur_tele.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)



def installation_antenne(request):
    technicien = Installation_antenne.objects.all()
    paginator = Paginator(technicien,12)
    page = request.GET.get('page')
    technicien = paginator.get_page(page)
    context = {
        'technicien' : technicien
    }
    return render(request, 'techniciens/antenne.html', context)
def antenne_detail(request, myid):
    technicien = Installation_antenne.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)




def chauffeur(request):
    techniciens = Chauffeur.objects.all()
    paginator = Paginator(techniciens,12)
    page = request.GET.get('page')
    techniciens = paginator.get_page(page)
    context = {
        'technicien' : techniciens
    }
    return render(request, 'techniciens/chauffeur.html', context)
def chauffeur_detail(request, myid):
    technicien = Chauffeur.objects.get(id=myid)
    context = {
        
        'technicien':technicien
    }
    return render(request, 'detail.html', context)
