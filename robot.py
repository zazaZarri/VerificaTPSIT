from componente import Componente

class Robot:
    def __init__(self, codice: str, modello: str, applicazione: str, peso_massimo_componenti_kg: float, stato: str) -> None:
        self.codice = codice
        self.modello = modello
        self.applicazione = applicazione
        self.peso_massimo_componenti_kg = peso_massimo_componenti_kg
        self.stato = stato
        self.componenti = []
        
        
    def aggiungi_componente(self, componente: Componente)->None:
        if componente.peso_kg >= self.peso_massimo_componenti_kg:
            raise ValueError("Erorre")
        self.componenti.append(componente)
        
    
    def peso_componenti(self)->float:
        pesoTot = 0
        for componente in self.componenti:
            pesoTot += componente.peso_kg
        return pesoTot
    
    def cerca_componente(self, codice: str) -> Componente:
        for componente in self.componenti:
            if componente.codice == codice:
                return componente
            
        return None
    
    
    def rimuovi_componente(self, codice: str) -> Componente:
        for componente in self.componenti:
            if componente.codice == codice:
                self.componenti.remove(componente)
                return componente
            
        return None
    
    def componenti_sotto_peso(self, peso_massimo: float)-> List:
        pesoMaxComponenti = []
        for componente in self.componenti:
            if componente.peso_kg <= peso_massimo:
                pesoMaxComponenti.append(componente)
                
        return pesoMaxComponenti
    
    
    
    
    
            