class Breakfast:
    def __init__(self):
        self.main, self.side, self.drink, self.drinkCounter = "", "", "", 0
    def _setItem(self, num):
        match num:
            case 1:
                self.main = "Eggs"
            case 2:
                self.side = "Toast"
            case 3:
                self.drinkCounter += 1
                self.drink = "Coffee"
                if self.drinkCounter > 1:
                    self.drink += '(' + str(self.drinkCounter) + ')'

class Lunch:
    def __init__(self):
        self.main, self.side, self.drink, self.sideCounter = "", "", "", 0
    def _setItem(self, num):
        match num:
            case 1:
                self.main = "Sandwich"
            case 2:
                self.side = "Chips"
                self.sideCounter += 1
                if self.sideCounter > 1:
                    self.side += '(' + str(self.sideCounter) + ')'
            case 3:
                self.drink = "Soda"
    
class Dinner:
    def __init__(self, drink="Water"):
        self.main, self.side, self.dessert, self.drink = "", "", "", drink
    def _setItem(self, num):
        match num:
            case 1:
                self.main = "Steak"
            case 2:
                self.side = "Potatoes"
            case 3:
                self.drink = "Wine, " + self.drink
            case 4:
                self.dessert = "Cake"