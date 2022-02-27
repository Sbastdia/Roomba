class Robot():
    def __init__(self, nombre,tiempo,tiempolimite=55):
      self.nombre=nombre
      self.tiempo=tiempo
      self.tiempolimite=tiempolimite
    def tiempoLimpiezaEnMinutos(self,superficieALimpiar):
      return round(superficieALimpiar*self.tiempo)
    def hablar(self,tiempolimpieza):
      if tiempolimpieza > self.tiempolimite:
        return (self.nombre+" dice: ¡Me parece que esto va a tardar un poco!")
      else:
        return (self.nombre+" dice: Voy como una moto fiuuuuuuummmm")
        