# Evive


<h1>Entry SE Test for Evive.</h1>   
  
<h2>Guide</h2>    
The <strong>Solution</strong> folder contains OOP implementation of the ordering system  <br>
-- **main.py** runs the program as outlined in the problem statement   <br>
-- **Solution.py** contains the Solution, Breakfast, Lunch, and Dinner classes <br>  
The **testing** folder  <br>
-- **testSuite.py** tests that the provided examples product correct output   <br>
-- -- I added additional tests and more can easily be added on to the additional_tests array  <br>
-- **MethodTest.py** contains unit tests for all of the class methods  v\<br>
<br>
Breakfast:  
  Main: 1. Eggs   
  Side: 2. Toast  
  Drink: 3. Coffee  
    
Lunch:  
  Main: 1. Sandwich  
  Side: 2. Chips  
  Drink: 3. Soda  
    
Dinner:  
  Main: 1. Steak  
  Side: 2. Potatoes  
  Drink: 3. Wine  
  Dessert: 4. Cake  
    
  
Rules:  
1. An order consists of a meal and collection of comma separated item Ids.  
2. The system should return the name of the items ordered  
3. The system should always return items in the following order: meal, side, drink  
4. If multiple items are ordered, the number of items should be indicated  
5. Each order must contain a main and a side  
6. If no drink is ordered, water should be returned  
7. At breakfast, multiple cups of coffee can be ordered  
8. At lunch, multiple sides can be ordered  
9. At dinner, dessert must be ordered  
10. At dinner, water is always provided   
   
Sample Input/Output  
In: Breakfast 1,2,3  
Out: Eggs, Toast, Coffee  
In: Breakfast 2,3,1  
Out: Eggs, Toast, Coffee  
In: Breakfast 1,2,3,3,3  
Out: Eggs, Toast, Coffee(3)  
In: Breakfast 1  
Out: Unable to process: Side is missing  
In: Lunch 1,2,3  
Out: Sandwich, Chips, Soda  
In: Lunch 1,2  
Out: Sandwich, Chips, Water  
In: Lunch 1,1,2, 3  
Out: Unable to process: Sandwich cannot be ordered more than once  
In: Lunch 1,2,2  
Out: Sandwich, Chips(2), Water  
In: Lunch  
Out: Unable to process: Main is missing, side is missing  
In: Dinner 1,2,3,4  
Out: Steak, Potatoes, Wine, Water, Cake  
In: Dinner 1,2,3  
Out: Unable to process: Dessert is missing  
