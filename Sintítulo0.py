class Animal:
    def __init__( self, name, typo, sound ):
        self.typo  = typo
        self.sound = sound
        self.name  = name
    def __str__( self ):
        return "nombre: {} || tipo: {} || sónido: {}".format(self.name, self.typo, self.sound )+"\n"

   
class Vaca( Animal ):
    pass

toro = Vaca("toro","mamífero", "mujido" )

class Zorro( Animal ):
    pass

zorro_rojo = Animal("zorro rojo", "mamífero", "Gruñido")
print( toro, zorro_rojo )

class Cocodrilo(Animal):
    pass

caiman = Animal("caiman", "reptil","resoplido")
print(caiman)