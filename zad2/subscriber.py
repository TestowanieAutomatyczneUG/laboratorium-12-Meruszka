
class Subscriber:
    def __init__(self) -> None:
        self.lista = []
    
    def dodajOsobe(self, imie):
        if isinstance(imie, str):
            if imie not in self.lista:
                self.lista.append(imie)
                return True
        raise ValueError

    def usunOsobe(self, imie):
        if isinstance(imie, str):
            if imie in self.lista:
                self.lista.remove(imie)
                return True
        raise ValueError
    
    def wyslijWiadomosc(self, imie, tresc):
        if isinstance(imie, str) and isinstance(tresc, str):
                if imie in self.lista:
                    return True
        raise ValueError
    