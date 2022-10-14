from Solution.Meals import Breakfast, Lunch, Dinner

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
            return self._retString(Order)
        except:
            self.error = "Unable to process: " + self.error
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
            self.error = "Meal selection is invalid"
            raise Exception()
            
    def _validateOrder(self):
        if '1' not in self.items and '2' not in self.items:
            self.error = "Main is missing, side is missing"
        elif '1' not in self.items:
            self.error = "Main is missing"
        elif '2' not in self.items:
            self.error = "Side is missing"
        elif self.meal == "Dinner" and '4' not in self.items:
            self.error = "Dessert is missing"
        elif self.items.count('1') > 1:
            string = ""
            match self.meal:
                case "Breakfast":
                    string = "Eggs"
                case "Lunch":
                    string = "Sandwich"
                case "Dinner":
                    string = "Steak"
            self.error = string + " cannot be ordered more than once"
        elif self.meal != "Lunch" and self.items.count('2') > 1:
            string = ""
            match self.meal:
                case "Breakfast":
                    string = "Toast"
                case "Dinner":
                    string = "Potatoes"
            self.error = string + " cannot be ordered more than once"
        elif self.meal != "Breakfast" and '3' in self.items and self.items.count('3') > 1:
            string = ""
            match self.meal:
                case "Lunch":
                    string = "Soda"
                case "Dinner":
                    string = "Wine"
            self.error = string + " cannot be ordered more than once"
        elif self.meal != "Dinner" and '4' in self.items:
            self.error = "Dessert can only be ordered at dinner"
        elif self.meal == "Dinner" and '4' not in self.items:
            self.error = "Dessert is missing"
        elif self.meal == "Dinner" and self.items.count('4') > 1:
            self.error = "Dessert cannot be ordered more than once"
        if self.error:
            raise Exception()
        
    def _retString(self, Order):
        if not Order.drink:
            Order.drink = "Water"
        string = Order.main + ", " + Order.side + ", " + Order.drink
        if self.meal == "Dinner":
            string += ", " + Order.dessert
        return string
    