from abc import ABC, abstractmethod

class Veicolo:
    def __init__(self, modello, anno):
        self.modello = modello
        self.anno = anno

    def __str__(self):
        return f"{self.modello} ({self.anno})"

# Classe per le auto
class Auto(Veicolo):
    def __init__(self, modello, anno, targa):
        super().__init__(modello, anno)
        self.targa = targa

    def __str__(self):
        return f"Auto: {super().__str__()}, Targa: {self.targa}"

# Classe per le moto
class Moto(Veicolo):
    def __init__(self, modello, anno, cilindrata):
        super().__init__(modello, anno)
        self.cilindrata = cilindrata

    def __str__(self):
        return f"Moto: {super().__str__()}, Cilindrata: {self.cilindrata}cc"

# Classe base per le autofficine
class Autofficina(ABC):
    
    @abstractmethod
    def ripara(self, veicolo):
        pass
    

# Classe per l'officina delle auto
class OfficinaAuto(Autofficina):
    def ripara(self, veicolo):
        if isinstance(veicolo, Auto):
            return f"Riparazione in corso per l'auto {veicolo}"
        return "Questa officina ripara solo auto."

# Classe per l'officina delle moto
class OfficinaMoto(Autofficina):
    def ripara(self, veicolo):
        if isinstance(veicolo, Moto):
            return f"Riparazione in corso per la moto {veicolo}"
        return "Questa officina ripara solo moto."

# Classe gestore delle riparazioni
class App_Riparazioni:
    def __init__(self):
        self.officine = {"auto": OfficinaAuto(), "moto": OfficinaMoto()}

    def gestisci_riparazione(self, veicolo):
        if isinstance(veicolo, Auto):
            return self.officine["auto"].ripara(veicolo)
        elif isinstance(veicolo, Moto):
            return self.officine["moto"].ripara(veicolo)
        return "Tipo di veicolo non supportato per la riparazione."

# Esempio di utilizzo
def main():
    # Creazione dei veicoli
    auto1 = Auto("Fiat Panda", 2020, "AB123CD")
    moto1 = Moto("Yamaha MT-07", 2022, 689)

    # Creazione dell'oggetto gestore delle riparazioni
    app_riparazioni = App_Riparazioni()

    # Gestione delle riparazioni
    print(app_riparazioni.gestisci_riparazione(auto1))  # Officina per auto
    print(app_riparazioni.gestisci_riparazione(moto1))  # Officina per moto
    print(app_riparazioni.gestisci_riparazione(Veicolo("Generico", 2020)))  # Veicolo non supportato

# Avvio del programma
main()
