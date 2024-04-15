import os
import random as rd
import string
import time as time

import django

from faker import Faker

from cliente.models import Category, City, Cliente, Pais

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aituringtesttec.settings")

django.setup()

vowels = list("aeiouAEIOU")
consonants = [c for c in string.ascii_letters if c not in vowels]

fake_es = Faker("es_ES")


def generate_string():
    return fake_es.name()


def generate_number():
    return rd.randint(1, 11)


def generate_category():
    categories = ["Local", "Nacional", "Internacional"]
    for category in categories:
        Category.objects.create(name_category=category)


def generate_contry():
    country = ["Colombia", "Mexico", "Venezuela"]
    for countries in country:
        Pais.objects.create(name_pais=countries)


def created_city():
    cityCOL = [
        "Bogota-Cundinamarca",
        "Cali-Valle",
        "Medellín-Antioquia",
        "Barranquilla-Atlántico",
        "Cartagena-Bolívar",
        "Cúcuta-Norte deSantander",
        "Bucaramanga-Santander",
        "Ibagué-Tolima",
        "Pereira-Risaralda",
        "Santa Martha-Magdalena",
        "Manizales-Caldas",
    ]
    cityMEX = [
        "Ciudad de México-Distrito Federal",
        "Ecatepec de Morelos-México",
        "Naucalpan de Juárez-México",
        "Tijuana-Baja California",
        "Nezahualcóyotl-México",
        "Monterrey-Nuevo León",
        "Guadalajara-Jalisco",
        "Juárez-Chihuahua",
        "León-Guanajuato",
        "Zapopan-Jalisco",
        "Puebla-Puebla",
    ]
    cityVEN = [
        "Caracas-Distrito Federal",
        "Ciudad Bolívar-Bolívar",
        "Ciudad Guayana-Bolívar",
        "San Cristóbal-Táchira",
        "Barcelona-Anzoátegui",
        "Barquisimeto-Lara",
        "Valencia-Carabobo",
        "Maracaíbo-Zulia",
        "Maturín-Monagas",
        "Petare-Miranda",
        "Maracay-Aragua",
    ]

    for cities in cityCOL:
        City.objects.create(name_city=cities, pais_id=1)
    for cities in cityMEX:
        City.objects.create(name_city=cities, pais_id=2)
    for cities in cityVEN:
        City.objects.create(name_city=cities, pais_id=3)


def generate_city(country_id):
    # City.objects.filter(pais_id=1)
    if country_id == 1:
        return rd.randint(1, 11)
    elif country_id == 2:
        return rd.randint(12, 22)
    else:
        return rd.randint(23, 33)


def generate_autor(count):
    for j in range(count):
        print(f"Generando cliente #{j} . . .")
        # random_user = generate_string(generate_number())
        num_random_country = rd.randint(1, 3)
        random_name = generate_string()
        print(random_name)
        random_category = rd.randint(1, 3)
        random_country = num_random_country
        random_city = generate_city(num_random_country)
        # print(type(random_category))

        Cliente.objects.create(
            name_cliente=random_name,
            pais_id=random_country,
            categoria_id=random_category,
            city_id=random_city,
        )


def poblarMasivo(cantidad):
    if not list(Category.objects.all()):
        generate_category()
    if not list(Pais.objects.all()):
        generate_contry()
    if not list(City.objects.all()):
        created_city()
    while True:
        try:
            assert 1 <= cantidad <= 2000

            break
        except ValueError:
            print("Ingresa un valor entero--> ejemplo: 3")
        except AssertionError:
            print("Ingresa una valor entre 1 y 2000 ")

    generate_autor(cantidad)
    return
