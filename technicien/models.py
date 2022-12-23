from django.db import models

# Create your models here.

class Informaticien(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="informaticien")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='informaticien')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        
        return self.nom
    
    
class Plombier(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="plombier")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='plombier')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom

class Enseignant(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="enseignant")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='Enseignants')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom

class Gestionnaire(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="gestionnaire")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='gestionnaire')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom

class Genie_civil(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="génie_civil")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='genie_civil')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom

class Comptable(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="comptable")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='comptable')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom

class Agriculture(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="agriculture")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='agriculture')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom
    

class Elevage(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="elevage")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='elevage')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom

class Maintenancier(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="maintenancier")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='maintenancier')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom

class Electricien(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="electricien")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='electriciens')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom
    
class Logisticien(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="logisticien")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='logisticiens')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom

class Maçon(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="maçon")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='maçon')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom

class Mecanicien(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="mécanicien")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='mecanicien')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom

class Cuisinier(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="cuisinier")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='cuisinier')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom

class Fille_et_garçon_salle(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="servante")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='fille_garçon_salle')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom

class Tolerie(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="tolérie")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='tolerie')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom

class Peintre(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="peintre")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='peintre')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom

class Manager(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="manager")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='manager')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom
    
class Menagere(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="ménagère")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='menagere')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom

class Veterinaire(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="vétérinaire")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='veterinaire')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom

class Developpeur(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="développeur")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='developpeur')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom

class Coiffure(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="coiffure")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='coiffure')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom

class Gardien(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="gardien")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='gardien')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom

class Infographe(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="infographie")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='infographe')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom
    
class Multimedia(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="multimédia")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='multimedia')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom

class Marketeur(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="markéteur")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='marketeur')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom

class Gardinier(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="gardinier")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='gardinier')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom

class Reparateur_phone(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="réparateur_phone")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='reparateur_phone')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom

class Reparateur_tele(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="réparateur_appareil_electronique")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='reparateur_tele')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom
    
class Installation_antenne(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="installation_antenne")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='installation_antenne')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom

class Chauffeur(models.Model):
    categorie = models.CharField(max_length=150, blank=True, default="chauffeur")
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    niveau = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='chauffeur')
    experience = models.TextField()
    travaux_effectue = models.TextField()
    Date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-Date_ajout']
        
    def __str__(self):
        return self.nom