from veiculo.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, portas):
        self.portas = portas
        
    def __str__(self, mensagem):
        return f'O carro {self._modelo} da marca {self._marca} tem {self.portas} portas'
    