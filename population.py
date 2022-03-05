import os
import time as time
import django,random as rd




os.environ.setdefault("DJANGO_SETTINGS_MODULE","aituringtesttec.settings")

django.setup()

from cliente.models import Cliente,Pais,Category,City



vocals = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'z',
              'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z']
              




def generate_string(length):
    if length <= 0:
        return False

    random_string =  ''

    for i in range(length):
        decision = rd.choice(('vocals','consonants'))

        if random_string[-1:].lower() in vocals:
            decision = 'consonants'
        if random_string[-1:].lower() in consonants:
            decision = 'vocals'
        
        if decision == 'vocals':
            character = rd.choice(vocals)
        else:
            character = rd.choice(consonants)
        
        random_string += character
    
    return random_string

def generate_number():
    return rd.randint(1, 11)

def generate_category():
    categories=['Local', 'Nacional','Internacional']
    for category in categories:
        Category.objects.create(name_category=category)    
def generate_contry():
    contry=['Colombia', 'Mexico','Venezuela']
    for countries in contry:
        Pais.objects.create(name_pais=countries)    

def created_city():
    cityCOL = ['Bogota-Cundinamarcar', 'Cali-Valle','Medellín-Antioquia','Barranquilla-Atlántico','Cartagena-Bolívar','Cúcuta-Norte deSantander',
    'Bucaramanga-Santander','Ibagué-Tolima','Pereira-Risaralda','Santa Martha-Magdalena','Manizales-Caldas']
    cityMEX=['Ciudad de México-Distrito Federal','Ecatepec de Morelos-México','Naucalpan de Juárez-México','Tijuana-Baja California',
    'Nezahualcóyotl-México','Monterrey-Nuevo León','Guadalajara-Jalisco','Juárez-Chihuahua','León-Guanajuato','Zapopan-Jalisco','Puebla-Puebla']
    cityVEN=['Caracas-Distrito Federal','Ciudad Bolívar-Bolívar','Ciudad Guayana-Bolívar','San Cristóbal-Táchira','Barcelona-Anzoátegui',
    'Barquisimeto-Lara','Valencia-Carabobo','Maracaíbo-Zulia','Maturín-Monagas','Petare-Miranda','Maracay-Aragua',]

    for cities in cityCOL:
        City.objects.create(name_city=cities,pais_id=1)
    for cities in cityMEX:
        City.objects.create(name_city=cities,pais_id=2)
    for cities in cityVEN:
        City.objects.create(name_city=cities,pais_id=3)




def generate_city(contrynum):    
    # City.objects.filter(pais_id=1)
    if contrynum==1:
        return rd.randint(1, 11)
    elif contrynum ==2:
        return rd.randint(12, 22)
    else:
        return rd.randint(23, 33)
    


def generate_autor(count):
    for j in range(count):
        print(f'Generando cliente #{j} . . .')
        # random_user = generate_string(generate_number())
        num_random_contry=rd.randint(1, 3)
        random_name = generate_string(generate_number())
        random_category = rd.randint(1, 3)
        random_country = num_random_contry
        random_city = generate_city(num_random_contry)
        print(type(random_category))

        

        Cliente.objects.create(           
            name_cliente=random_name,
            pais_id=random_country,
            categoria_id=random_category,
            city_id=random_city,
        )


if __name__ == "__main__":
    print("Inicio de creación de población")
    print("Por favor espere . . . ")
    start = time.strftime("%c")
    print(f'Fecha y hora de inicio: {start}')
    # print(list(City.objects.filter(pais_id=3)))
    if len(list(Category.objects.all()))==0:
        generate_category()
    if len(list(Pais.objects.all()))==0:
        generate_contry()
    if len(list(City.objects.all()))==0:
        created_city()

    generate_autor(2)
    end = time.strftime("%c")
    print(f'Fecha y hora de finalización: {end}')


