from veiculo.veiculo import Veiculo

class Moto:
    def __init__(self, tipo):
        self.tipo = tipo
        
        
    def __str__(self,):
        return f'O tipo da moto é {self.tipo}'