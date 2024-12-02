from abc import ABC, abstractmethod


class Professore:
    def __init__(self, nome, materia):
        self.nome = nome
        self.materia = materia

    def insegna(self):
        return f"{self.nome} insegna {self.materia.nome}"

# Classe astratta per Materia
class Materia(ABC):
    @abstractmethod
    def __init__(self, nome):
        self.nome = nome

# Classe per Materia di Matematica
class Matematica(Materia):
    def __init__(self, nome="Matematica"):
        super().__init__(nome)

# Classe per Materia di Storia
class Storia(Materia):
    def __init__(self, nome="Storia"):
        super().__init__(nome)

# Classe astratta per Numero di Studenti
class NumeroStudenti(ABC):
    @abstractmethod
    def __init__(self, numero):
        self.numero = numero

# Classe per numero fisso di studenti
class NumeroStudentiFisso(NumeroStudenti):
    def __init__(self, numero=3):
        super().__init__(numero)

# Classe per numero variabile di studenti
class NumeroStudentiVariabile(NumeroStudenti):
    def __init__(self, numero):
        super().__init__(numero)

# Classe per Studente
class Studente:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

# Classe Aula che gestisce gli studenti
class Aula:
    def __init__(self, materia, numero_studenti):
        self.materia = materia
        self.numero_studenti = numero_studenti
        self.studenti = []

    def aggiungi_studenti(self, studenti):
        if len(studenti) == self.numero_studenti.numero:
            self.studenti.extend(studenti)
            return f"Studenti aggiunti all'aula di {self.materia.nome}"
        else:
            return f"Numero di studenti non corrispondente. L'aula ha bisogno di {self.numero_studenti.numero} studenti."

    def mostra_studenti(self):
        return [str(studente) for studente in self.studenti]



# Test
materia_matematica = Matematica()
materia_storia = Storia()


numero_studenti_fisso = NumeroStudentiFisso()
numero_studenti_variabile = NumeroStudentiVariabile(3)

professore = Professore("Prof. Marco", materia_matematica)

studente1 = Studente("Giuseppe")
studente2 = Studente("Anna")
studente3 = Studente("Andrea")

aula_matematica = Aula(materia_matematica, numero_studenti_fisso)
aula_storia = Aula(materia_storia, numero_studenti_variabile)

aula_matematica.aggiungi_studenti([studente1, studente2, studente3])
aula_storia.aggiungi_studenti([studente1, studente2, studente3])

print(professore.insegna())
print(f"Studenti in aula di Matematica: {aula_matematica.mostra_studenti()}")
print(f"Studenti in aula di Storia: {aula_storia.mostra_studenti()}")

   

    
   
