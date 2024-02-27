class Animal:
    def init(self, cantidad, gestacion, nombre_cientifico, nombre_comun, region, jaula):
        self.cantidad = cantidad
        self.gestacion = gestacion
        self.nombre_cientifico = nombre_cientifico
        self.nombre_comun = nombre_comun
        self.region = region
        self.jaula = jaula

    def mostrar_informacion(self):
        print("Nombre común:", self.nombre_comun)
        print("Nombre científico:", self.nombre_cientifico)
        print("Cantidad:", self.cantidad)
        print("Período de gestación:", self.gestacion)
        print("Región de procedencia:", self.region)
        print("Jaula:", self.jaula)


class Mamifero(Animal):
    def init(self, cantidad, gestacion, nombre_cientifico, nombre_comun, region, jaula):
        super().init(cantidad, gestacion, nombre_cientifico, nombre_comun, region, jaula)
        self.tipo = "Mamífero"


class Reptil(Animal):
    def init(self, cantidad, gestacion, nombre_cientifico, nombre_comun, region, jaula):
        super().init(cantidad, gestacion, nombre_cientifico, nombre_comun, region, jaula)
        self.tipo = "Reptil"


# Aquí puedes definir las clases para Aves, Peces y otras categorías de animales si es necesario

class Zoologico:
    def init(self):
        self.lista_animales = []

    def agregar_animal(self, animal):
        self.lista_animales.append(animal)

    def mostrar_todos_animales(self):
        for animal in self.lista_animales:
            animal.mostrar_informacion()

    def buscar_animal_por_nombre(self, nombre_comun):
        for animal in self.lista_animales:
            if animal.nombre_comun == nombre_comun:
                animal.mostrar_informacion()

    def eliminar_animal_por_nombre(self, nombre_comun):
        for animal in self.lista_animales:
            if animal.nombre_comun == nombre_comun:
                self.lista_animales.remove(animal)
                print(f"El animal {nombre_comun} ha sido eliminado.")
                return

# Crear una instancia del zoológico
zoo = Zoologico()

# Ejemplo de uso
mamifero1 = Mamifero(5, "6 meses", "Panthera leo", "León", "África", "Jaula 1")
zoo.agregar_animal(mamifero1)

reptil1 = Reptil(10, "3 meses", "Python regius", "Pitón bola", "América", "Jaula 2")
zoo.agregar_animal(reptil1)

# Mostrar todos los animales en el zoológico
print("Lista de animales en el zoológico:")
zoo.mostrar_todos_animales()

# Buscar un animal por su nombre común
print("\nBuscar animal por nombre común:")
zoo.buscar_animal_por_nombre("León")

# Eliminar un animal por su nombre común
zoo.eliminar_animal_por_nombre("Pitón bola")

# Mostrar la lista actualizada de animales
print("\nLista de animales en el zoológico después de eliminar:")
zoo.mostrar_todos_animales()
