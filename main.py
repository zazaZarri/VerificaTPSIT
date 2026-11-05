from componente import Componente
from robot import Robot

class Main:
    def __init__ (self):
        self.robots = []
    
    def registra_robot(self, robot: Robot)->None:
        for rb in self.robots:
            if rb.codice == robot.codice:
                raise ValueError("Error")
                return None
        
        self.robots.append(robot)
        
        
    def cerca_robot(self, codice: str) -> Robot:
        for rb in self.robots:
            if rb.codice == codice:
                return Robot
            
        return None
    
    
    def riepilogo_robot(self)-> List:
        return self.robots
    
    
    
    
if __name__ == "__main__":
    main = Main()
    robot1 = Robot("QER", "Modello 2", "linux", 50, "OK")
    robot2 = Robot("QER2", "Modello 2", "linux", 50, "INCORSO")
    robot3 = Robot("QER3", "Modello 2", "linux", 50, "ROTTO")
    robot4 = Robot("QER4", "Modello 2", "linux", 50, "INIZIATO")
    componente1 = Componente("EER","BRACCIO",20)
    componente2 = Componente("EER2","BRACCIO",20)
    componente3 = Componente("EER3","BRACCIO",20)
    componente4 = Componente("EER4","BRACCIO",20)
    
    robot1.aggiungi_componente(componente1)
    robot1.aggiungi_componente(componente2)
    
    robot2.aggiungi_componente(componente2)
    robot2.aggiungi_componente(componente3)
    
    robot3.aggiungi_componente(componente3)
    robot3.aggiungi_componente(componente4)
    
    robot4.aggiungi_componente(componente1)
    robot4.aggiungi_componente(componente4)
    
    main.registra_robot(robot1)
    main.registra_robot(robot2)
    main.registra_robot(robot3)
    main.registra_robot(robot4)
    print(main.riepilogo_robot())
    
    print("funziona")
    print(main.cerca_robot("QER3"))
    
    print("non funziona")
    print(main.cerca_robot("EERQEWE"))
    
    
    print("non funziona componente")
    print(robot1.cerca_componente("eeeqweqwe"))
    
    robot1.rimuovi_componente("EER")
    print(robot1.cerca_componente("EER"))
    
    print(robot2.componenti_sotto_peso(1000))
    
    