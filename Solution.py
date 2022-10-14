class Solution:
    def __init__(self, query, meal=None, items=None, error=None):
        self.query = query
        self.meal, self.items, self.error = meal, items, error
        
    def doOrder(self):
        try:
            self._parse()
            self._validateOrder()
            match self.meal:
                case "Breakfast":
                    Order = Breakfast(self.items)
                case "Lunch":
                    Order = Lunch(self.items)
                case "Dinner":
                    Order = Dinner(self.items)
            for item in Order.items:
                Order.getItems(int(item))
            return self._returnString(Order)
        except:
            return self.error
            
    def _parse(self):
        if self.query.startswith("Breakfast"):
            self.meal = "Breakfast"
            self.items = self.query[10:].split(',')
        elif self.query.startswith("Lunch"):
            self.meal = "Lunch"
            self.items = self.query[6:].split(',')
        elif self.query.startswith("Dinner"):
            self.meal = "Dinner"
            self.items = self.query[7:].split(',')
        else:
            self.error = "Unable to process, meal selection is invalid"
            raise Exception()
            
    def _validateOrder(self):
        if '1' not in self.items and '2' not in self.items:
            self.error = "Unable to process: Main is missing, side is missing"
        elif '1' not in self.items:
            self.error = "Unable to process: Main is missing"
        elif '2' not in self.items:
            self.error = "Unable to process: Side is missing"
        elif self.meal == "Dinner" and '4' not in self.items:
            self.error = "Unable to process: Dessert is missing"
        elif self.items.count('1') > 1:
            string = ""
            match self.meal:
                case "Breakfast":
                    string = "Eggs"
                case "Lunch":
                    string = "Sandwich"
                case "Dinner":
                    string = "Steak"
            self.error = "Unable to process: " + string + " cannot be ordered more than once"
        elif self.meal != "Lunch" and self.items.count('2') > 1:
            string = ""
            match self.meal:
                case "Breakfast":
                    string = "Toast"
                case "Dinner":
                    string = "Potatoes"
            self.error = "Unable to process: " + string + " cannot be ordered more than once"
        elif self.meal != "Breakfast" and '3' in self.items and self.items.count('3') > 1:
            string = ""
            match self.meal:
                case "Lunch":
                    string = "Soda"
                case "Dinner":
                    string = "Wine"
            self.error = "Unable to process: " + string + " cannot be ordered more than once"
        elif self.meal != "Dinner" and '4' in self.items:
            self.error = "Unable to process: Dessert can only be ordered at dinner"
        elif self.meal == "Dinner" and '4' not in self.items:
            self.error = "Unable to process: Dessert is missing"
        elif self.meal == "Dinner" and self.items.count('4') > 1:
            self.error = "Unable to process: Dessert cannot be ordered more than once"
        if self.error:
            raise Exception()
            
    def _returnString(self, order):
        string = order.main + ", " + order.side + ", " + order.drink
        if self.meal == "Dinner":
            string += ", " + order.dessert
        return string
    
class Breakfast:
    def __init__(self, items, main="", side="", drink="", drinkCounter=0):
        self.items = items
        self.main, self.side, self.drink, self.drinkCounter = main, side, drink, drinkCounter
    def getItems(self, num):
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
    def __init__(self, items, main="", side="", drink="", sideCounter=0):
        self.items = items
        self.main, self.side, self.drink, self.sideCounter = main, side, drink, sideCounter
    def getItems(self, num):
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
    def __init__(self, items, main=None, side=None, drink="Water", dessert=None):
        self.items = items
        self.main, self.side, self.drink, self.dessert = main, side, drink, dessert
        
    def getItems(self, num):
        match num:
            case 1:
                self.main = "Steak"
            case 2:
                self.side = "Potatoes"
            case 3:
                self.drink = "Wine, " + self.drink
            case 4:
                self.dessert = "Cake"