from django.urls import path
from .views import*

app_name = 'techniciens'
urlpatterns = [
    
    path('technicien/informaticien', informaticien, name="informaticien"),
    path('technicien/informaticien/<int:myid>', detail, name="detail"),
    
    path('technicien/plombier',plombier , name="plombier"),
    path('technicien/plombier/<int:myid>', plombier_detail, name="detail"),
    
    path('technicien/enseignant',enseignant , name="enseignant"),
    path('technicien/enseignant/<int:myid>', enseignant_detail, name="detail"),
    
    path('technicien/gestionnaire',gestionnaire , name="gestionnaire"),
    path('technicien/gestionnaire/<int:myid>', gestionnaire_detail, name="detail"),
    
    path('technicien/génie_civil',genie_civil , name="genie_civil"),
    path('technicien/genie_civil/<int:myid>', genie_civil_detail, name="detail"),
    
    path('technicien/comptable',comptable , name="comptable"),
    path('technicien/comptable/<int:myid>', comptable_detail, name="detail"),
    
    path('technicien/agriculture',agriculture , name="comptable"),
    path('technicien/agriculture/<int:myid>', agriculture_detail, name="detail"),
    
    path('technicien/elevage',elevage , name="elevage"),
    path('technicien/elevage/<int:myid>', elevage_detail, name="detail"),
    
    path('technicien/maintenancier',maintenancier , name="maintenancier"),
    path('technicien/maintenancier/<int:myid>', maintenancier_detail, name="detail"),
    
    path('technicien/electricien',electricien , name="electricien"),
    path('technicien/electricien/<int:myid>', electricien_detail, name="detail"),
    
    path('technicien/logisticien',logisticien , name="logisticien"),
    path('technicien/logisticien/<int:myid>', logisticien_detail, name="detail"),
    
    path('technicien/maçon',maçon , name="maçon"),
    path('technicien/maçon/<int:myid>', maçon_detail, name="detail"),
    
    path('technicien/mécanicien',mecanicien , name="mecanicien"),
    path('technicien/mecanicien/<int:myid>', mecanicien_detail, name="detail"),
    
    path('technicien/cuisinier',cuisinier , name="cuisinier"),
    path('technicien/cuisinier/<int:myid>', cuisinier_detail, name="detail"),
    
    path('technicien/servante',fille_et_garçon_salle , name="servante"),
    path('technicien/servante/<int:myid>', servante_detail, name="detail"),
    
    path('technicien/tolérie',tolerie , name="tolerie"),
    path('technicien/tolérie/<int:myid>', tolerie_detail, name="detail"),
    
    path('technicien/peintre',peintre , name="peintre"),
    path('technicien/peintre/<int:myid>',peintre_detail, name="detail"),
    
    path('technicien/manager',manager , name="manager"),
    path('technicien/manager/<int:myid>', manager_detail, name="detail"),
    
    path('technicien/ménagère',menagere , name="menagere"),
    path('technicien/menagere/<int:myid>', menagere_detail, name="detail"),
    
    path('technicien/vétérinaire',veterinaire , name="veterinaire"),
    path('technicien/veterinaire/<int:myid>', veterinaire_detail, name="detail"),
    
    path('technicien/développeur',developpeur , name="developpeur"),
    path('technicien/developpeur/<int:myid>', developpeur_detail, name="detail"),
    
    path('technicien/coiffure',coiffure , name="coiffure"),
    path('technicien/coiffure/<int:myid>', coiffure_detail, name="detail"),
    
    path('technicien/gardien',gardien , name="gardien"),
    path('technicien/gardien/<int:myid>', gardien_detail, name="detail"),
    
    path('technicien/infographie',infographie , name="infographie"),
    path('technicien/infographie/<int:myid>', infographie_detail, name="detail"),
    
    path('technicien/multimédia',multimedia , name="multimedia"),
    path('technicien/multimedia/<int:myid>', multimedia_detail, name="detail"),
    
    path('technicien/markéteur',marketeur , name="marketeur"),
    path('technicien/marketeur/<int:myid>', marketeur_detail, name="detail"),
    
    path('technicien/gardinier',gardinier , name="gardinier"),
    path('technicien/gardinier/<int:myid>', gardinier_detail, name="detail"),
    
    path('technicien/réparateur_phone',reparateur_phone , name="phone"),
    path('technicien/réparateur_phone/<int:myid>', phone_detail, name="detail"),
    
    path('technicien/réparateur_appareil_electronique',reparateur_tele , name="tele"),
    path('technicien/réparateur_appareil_electronique/<int:myid>', tele_detail, name="detail"),
    
    path('technicien/installation_antenne',installation_antenne , name="antenne"),
    path('technicien/installation_antenne/<int:myid>', antenne_detail, name="detail"),
    
    path('technicien/chauffeur',chauffeur , name="chauffeur"),
    path('technicien/chauffeur/<int:myid>', chauffeur_detail, name="detail"),
      
]
