from UnoAttack.Data.DECK.DECK import DECK

class HAND(DECK):

# ---------METODOS------------------------------------

    # ESTE METODO AGREGA UNA CARTA A LA MANO DE CARTAS DEL JUGADOR
    def AddCard(self, Card):
        Lista=list(self.Cards)
        Lista.append(Card)
        self.Cards=Lista

    # ESTE METODO SACA UNA CARTA A LA MANO DE CARTAS DEL JUGADOR
    def GetCard(self, position):
        Lista=list(self.Cards)
        Card= Lista.pop(position)
        self.Cards=tuple(Lista)
        return Card

    # ESTE METODO RETORNA TODAS LAS CARTAS DE LA MANO DEL JUGADOR QUE CUMPLAN UNA PROPIEDAD
    def GetCardsProperty(self, Property):
        Lista=list(self.Cards)
        Requests=[]
        for card in self.Cards:
            if (card.GetProperty().name == Property.name):
                Requests.append(card)
                Lista.remove(card)
        self.Cards=tuple(Lista)
        return Requests