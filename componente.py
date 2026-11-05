class Componente:
    def  __init__(self, codice: str, nome: str, peso_kg: float) -> None:
        self._codice = codice
        self._nome = nome
        self._peso_kg = peso_kg
        
    
    @property
    def codice(self)-> str:
        return self._codice
    
    @codice.setter
    def codice(self, valore: str)->None:
        self._codice = valore
        
        
    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, valore: str)->None:
        self._nome = valore
        
        
    @property
    def peso_kg(self) -> float:
        return self._peso_kg
    
    @peso_kg.setter
    def peso_kg(self, valore: float)->None:
        self._peso_kg = valore
        
        