from django.db import models
from PIL import Image
# Create your models here.

"""
Classe que permet conèixer la localitat del punt d'interès.
"""
class localitzacio(models.Model):
    ciutat = models.CharField(max_length=150)
    comarca = models.CharField(max_length=150)
    provincia = models.CharField(max_length=20)
    def __str__(self):
        return str(self.ciutat)+" ("+str(self.comarca)+"),"+str(self.provincia)
"""
Classe que representarà el punt en el mapa. Les altres informacion són per si es necessiten més tard al clicar al punt.
"""
class puntInteres(models.Model):
    latitud=models.FloatField()
    longitud=models.FloatField()
    actiu=models.BooleanField()
    superficie=models.FloatField()
    localitat=models.ForeignKey(localitzacio, on_delete=models.CASCADE)
    def __str__(self):
        return "{"+"latitud:\"" + str(self.latitud) + "\", longitud:\"" + str(self.longitud) + "\", actiu:\"" + str(self.actiu)+ "\", superficie:\"" + str(self.superficie) + "\", localitat:\"" + str(self.localitat)+"}";


"""
Classe que permet conèixer la categoria del local
"""
class categoriaLocal(models.Model):
    categoria = models.CharField(max_length=200)
    def __str__(self):
        return self.categoria

"""
Classe que serà el que donarà la informació del element que hi ha en el punt d'interès específic. 
En cas que el punt d'interès s'elimini, també s'esborrarà el local, en conseqüència, ja que sinó el sistema quedaria 
incosistent.
"""
class local(models.Model):
    localitzacio=models.ForeignKey(puntInteres, on_delete=models.CASCADE)
    nomLocal=models.CharField(max_length=500)
    estat_conservacio=models.IntegerField()
    categoria=models.ForeignKey(categoriaLocal, on_delete=models.CASCADE)
    anyConstruccio=models.IntegerField()
    descripcio=models.CharField(max_length=600)
    def __str__(self):
        return "{"+"nomLocal:\"" + str(self.nomLocal) + "\", puntuacio:\"" + str(self.estat_conservacio) + "\", categoria:\"" + str(self.categoria) + "\", anyConstruccio:\"" + str(self.anyConstruccio) + "\", descripcio:\"" + str(self.descripcio)+ "\", superficie:\""+"}";

'''
quan les imatges tenen molta qualitat, els bytes son tant grans que triga massa el servidor i peta la comunicacio amb la db
class imatges_locals(models.Model):
    imatge = models.BinaryField(blank=True)
    local=models.ForeignKey(local, on_delete=models.CASCADE)
    
'''

"""
Classe que representa la taula on s'emmagatzema la relació entre la fotografia i el local
"""
class imageLocal(models.Model):
    imatge=models.ImageField(upload_to='photo')
    local=models.ForeignKey(local, on_delete=models.CASCADE)

"""
Classe que representen les paraules més freqüents dints del sistema GIS
"""
class paraulesClauGIS(models.Model):
    paraula=models.CharField(max_length=600)
    idioma=models.CharField(max_length=30)
    def __str__(self):
        return self.paraula