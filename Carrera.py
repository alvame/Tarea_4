import random
from math import log, floor

class Vehiculo:
    distanciaCamion = 0
    distanciaTractor = 0
    distanciaSedan = 0
    distanciaBus = 0
    ciclosGlobales = 0
    gana = False

    def __init__(self):
        self.fuerzaMotor = 0

    def calcularFuerzaMotor(self):
        fuerzaMotor = random.uniform(0, 9)
        return int(fuerzaMotor)

class Camion(Vehiculo):
    def __init__(self):
        pass

    def avanceCamion(self):

        if Vehiculo.gana==False:
            fuerza = super().calcularFuerzaMotor()
            avanzar = floor(2 * (fuerza) + 1)
            Camion.distanciaCamion += avanzar

        if Camion.distanciaCamion >= 1000:
            Vehiculo.gana = True
            print('!!!!!El ganador es Camion!!!!!')

class Tractor(Vehiculo):
    def __init__(self):
        pass

    def avanceTractor(self):

        if Vehiculo.gana==False:
            fuerza = super().calcularFuerzaMotor()
            avanzar = floor(log(2) * fuerza)
            Tractor.distanciaTractor += avanzar

        if Tractor.distanciaTractor >= 1000:
            Vehiculo.gana = True
            print('!!!!!El ganador es Tractor!!!!')

class Sedan(Vehiculo):
    def __init__(self):
        pass

    def avanceSedan(self):

     if Vehiculo.gana== False:
        fuerza = super().calcularFuerzaMotor()
        avanzar = floor((3 * (fuerza)**2))
        Sedan.distanciaSedan += avanzar

     if sedan.distanciaSedan >= 1000:
            Vehiculo.gana = True
            print('!!!!!El ganador es Sedan!!!!!')


class Bus(Vehiculo):
    def __init__(self):
        pass

    def avanceBus(self):

        if Vehiculo.gana== False:
            fuerza = super().calcularFuerzaMotor()
            avanzar = floor((5 * (fuerza)))
            Bus.distanciaBus+= avanzar

        if Bus.distanciaBus >= 1000:
            Vehiculo.gana = True
            print('!!!!!El ganador es Bus!!!!!')


print("******Carrera de Vehiculos*******")

# creacion de objetos vehiculos
camion = Camion()
tractor = Tractor()
sedan = Sedan()
bus = Bus()

while Vehiculo.gana==False:
    camion.avanceCamion()
    tractor.avanceTractor()
    sedan.avanceSedan()
    bus.avanceBus()
    Vehiculo.ciclosGlobales += 1

print('Metros recorridos por Camion fue de: ' , Camion.distanciaCamion,'mts')
print('Metros recorridos por Tractor fue de: ' ,Tractor.distanciaTractor,'mts')
print('Metros recorridos por Sedan fue de: ' , Sedan.distanciaSedan,'mts')
print('Metros recorridos por Bus fue de: ' , Bus.distanciaBus,'mts')
print("Cantidad de ciclos globales fue de:", Vehiculo.ciclosGlobales)