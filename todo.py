from etat import Etat

class Todo:

    def __init__(self, nom, date, priorite=1):
        self.nom = nom
        self.date = date
        self.priorite = priorite
        self.etat = Etat.A_FAIRE

    def fait(self):
        self.etat = Etat.FAIT

    def __str__(self):
        return f"{self.nom}, {self.date}, {self.etat.name}"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.nom == other.nom and self.date == other.date and self.etat == other.etat
        return False