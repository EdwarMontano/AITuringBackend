from django.db import models

# Create your models here.
class Category(models.Model):

    name_category=models.CharField('Categoría',max_length=200, blank = False, null =False)
    category_created=models.DateTimeField('Fecha de creación',auto_now_add=True)
    category_modifed=models.DateTimeField('Fecha de actualización',auto_now=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name_category']

    # def natural_key(self):
    #     return f'{self.nombre} {self.apellidos}'

    def __str__(self):
        return self.name_category

class Pais(models.Model):

    name_pais=models.CharField('País',max_length=100, blank = False, null =False)
    pais_created=models.DateTimeField('Fecha de creación',auto_now_add=True)
    pais_modifed=models.DateTimeField('Fecha de actualización',auto_now=True)

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'
        ordering = ['name_pais']

    # def natural_key(self):
    #     return f'{self.nombre} {self.apellidos}'

    def __str__(self):
        return self.name_pais

class City(models.Model):

    name_city=models.CharField('Ciudad',max_length=100, blank = False, null =False)
    pais=models.ForeignKey(Pais,on_delete=models.CASCADE)
    ciudad_created=models.DateTimeField('Fecha de creación',auto_now_add=True)
    ciudad_modifed=models.DateTimeField('Fecha de actualización',auto_now=True)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        # ordering = ['name_pais']

    # def natural_key(self):
    #     return f'{self.nombre} {self.apellidos}'

    def __str__(self):
        return self.name_city


class Cliente(models.Model):
    # id = models.AutoField(primary_key = True)
    name_cliente=models.CharField('Nombre',max_length=200, blank = False, null =False)
    categoria=models.ForeignKey(Category,on_delete=models.CASCADE)
    pais=models.ForeignKey(Pais,on_delete=models.CASCADE)
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    estado =models.BooleanField(default=True)
    user_created=models.DateTimeField('Fecha de creación',auto_now_add=True)
    user_modifed=models.DateTimeField('Fecha de actualización',auto_now=True)
         

    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['name_cliente']

    # def natural_key(self):
    #     return f'{self.nombre} {self.apellidos}'

    def __str__(self):
        return self.name_cliente
