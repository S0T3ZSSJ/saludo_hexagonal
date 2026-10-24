
from principal.domain.persona import Persona
from principal.application.ports.saludar_use_case import SaludarUseCase

class SaludarService(SaludarUseCase):

    def saludar(self, nombre):
        persona = Persona(nombre)
        return persona.saludar()
