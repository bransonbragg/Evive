from Solution.Solution import Solution
from Solution.Meals import Breakfast, Lunch, Dinner
from testing.MethodTest import TestMethods

sampleTests = ["Breakfast 1,2,3", "Breakfast 2,3,1", "Breakfast 1,2,3,3,3", 
               "Breakfast 1", "Lunch 1,2,3", "Lunch 1,2", "Lunch 1,1,2, 3", 
               "Lunch 1,2,2", "Lunch", "Dinner 1,2,3,4", "Dinner 1,2,3"]

sampleReturns = ["Eggs, Toast, Coffee", "Eggs, Toast, Coffee", "Eggs, Toast, Coffee(3)", 
                 "Unable to process: Side is missing", "Sandwich, Chips, Soda", 
                 "Sandwich, Chips, Water", "Unable to process: Sandwich cannot be ordered more than once", 
                 "Sandwich, Chips(2), Water", "Unable to process: Main is missing, side is missing", 
                 "Steak, Potatoes, Wine, Water, Cake", "Unable to process: Dessert is missing"]
    
additionalTests = ["Kachow 1,2,3", # valid meal names only
                   "Breakfast 4", # no dessert except at dinner
                   "Lunch 4", 
                   "Breakfast 1,2,3,4",
                   "Lunch 1,2,3,4", 
                   "Breakfast 1,1,2,3", # multiple main 
                   "Lunch 1,1,2,3",
                   "Dinner 1,1,2,3",
                   "breakfast 1,2,3", # case-sensitivity (implementation is case-sensitive)
                   "lunch 1,2,3",
                   "dinner 1,2,3",
                   "Breakfast 5,6,7,8,8,9" # valid numbers only
                   "Lunch 7,2345,3,4523,5"
                   "Dinner ,,,,,,,,,,,,,,,"
                   # handle large orders
                   "Breakfast 1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3"
                   "Lunch 1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3"
                   ]

additionalIntended = ["Unable to process: Meal selection is invalid", 
                      "Unable to process: Main is missing, side is missing",
                      "Unable to process: Main is missing, side is missing",
                      "Unable to process: Dessert can only be ordered at dinner",
                      "Unable to process: Dessert can only be ordered at dinner",
                      "Unable to process: Eggs cannot be ordered more than once",
                      "Unable to process: Sandwich cannot be ordered more than once",
                      "Unable to process: Dessert is missing",
                      "Unable to process: Meal selection is invalid",
                      "Unable to process: Meal selection is invalid",
                      "Unable to process: Meal selection is invalid",
                      "Unable to process: Main is missing",
                      "Eggs, Toast, Coffee(38)", "Sandwich, Chips(40), Soda"]
def test():
    # exectuting sample tests
    for i in range(len(sampleTests)):
        sample = sampleTests[i]
        Soln = Solution(sample)
        result = Soln.doOrder()
        assert(result == sampleReturns[i]) 
        
    # executing additional tests
    for i in range(len(additionalTests)):
        test = additionalTests[i]
        Soln = Solution(test)
        result = Soln.doOrder()
        assert(result == additionalIntended[i])
        
    # executing method tests
    
    print("All Tests Passed! :)")
        
if __name__ == '__main__':
    test()