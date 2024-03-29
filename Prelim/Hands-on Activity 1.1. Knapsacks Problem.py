# -*- coding: utf-8 -*-
"""G. Esperat Hands-on Activity 1.1 - Optimization and Knapsack Problem-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16pu-DWh8udXFWG5x_q1CnyNiu-f8DWeY

# Hands-on Activity 1.1 | Optimization and Knapsack Problem

#### Objective(s):

This activity aims to demonstrate how to apply  greedy and brute force algorithms to solve optimization problems

#### Intended Learning Outcomes (ILOs):
* Demonstrate how to solve knapsacks problems using greedy algorithm
* Demonstrate how to  solve knapsacks problems using brute force algorithm

#### Resources:
* Jupyter Notebook

#### Procedures:

1. Create a Food class that defines the following:
* name of the food
* value of the food
* calories of the food

2. Create the following methods inside the Food class:
* A method that returns the value of the food
* A method that returns the cost of the food
* A method that calculates the density of the food (Value / Cost)
* A method that returns a string to display the name, value and calories of the food
"""

class Food(object):
    def __init__(self, n, v, w):
        # Make the variables private
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.value)+ ', ' + str(self.calories) + '>'

"""3. Create a buildMenu method that builds the name, value and calories of the food

"""

def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],calories[i]))
    return menu

"""4. Create a method greedy to return total value and cost of added food based on the desired maximum cost"""

def greedy(items, maxCost, keyFunction):
    """Assumes items a list, maxCost >= 0,         keyFunction maps elements of items to numbers"""
    itemsCopy = sorted(items, key = keyFunction,
                       reverse = True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)

"""5. Create a testGreedy method to test the greedy method"""

def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print('   ', item)

def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits,          'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    print('\nUse greedy by cost to allocate', maxUnits,          'calories')
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
    print('\nUse greedy by density to allocate', maxUnits,          'calories')
    testGreedy(foods, maxUnits, Food.density)

"""6. Create arrays of food name, values and calories
7. Call the buildMenu to create menu for food
8. Use testGreedys method to pick food according to the desired calories
"""

names = ['wine', 'beer', 'pizza', 'burger', 'fries','cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 2000)

"""Task 1: Change the maxUnits to 100"""

#type your code here
testGreedys(foods, 100)

"""Task 2: Modify codes to add additional weight (criterion) to select food items."""

# type your code here
class Food(object):
    def __init__(self, n, v, w, vol):
        self.name = n
        self.value = v
        self.calories = w
        self.volume = vol
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def getVolume(self):
        return self.volume
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.value)+ ', ' + str(self.calories) + ', ' + str(self.volume) + '>'

def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits,          'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    print('\nUse greedy by cost to allocate', maxUnits,          'calories')
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
    print('\nUse greedy by density to allocate', maxUnits,          'calories')
    testGreedy(foods, maxUnits, Food.density)
    print('\nUse greedy by volume to allocate', maxUnits,          'calories')
    testGreedy(foods, maxUnits, Food.getVolume)

def buildMenu(names, values, calories, volumes):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],calories[i], volumes[i]))
    return menu

"""Task 3: Test your modified code to test the greedy algorithm to select food items with your additional weight."""

# type your code here
names = ['wine', 'beer', 'pizza', 'burger', 'fries','cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
volume = [1000, 750, 500, 400, 300, 750, 150, 250]

foods = buildMenu(names, values, calories, volume)
testGreedys(foods, 2000)

"""9. Create method to use  Bruteforce algorithm instead of greedy algorithm"""

class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.value)+ ', ' + str(self.calories) + '>'

def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the items of that solution"""
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        #Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake = maxVal(toConsider[1:],
                                     avail - nextItem.getCost())
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],calories[i]))
    return menu

def testMaxVal(foods, maxUnits, printItems = True):
    print('Use search tree to allocate', maxUnits,
          'calories')
    val, taken = maxVal(foods, maxUnits)
    print('Total costs of foods taken =', val)
    if printItems:
        for item in taken:
            print('   ', item)

names = ['wine', 'beer', 'pizza', 'burger', 'fries','cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
testMaxVal(foods, 2400)

"""**Conclusion:**

In this activity, the knapsack problem, is a classic example of optimization, using both greedy and brute force algorithms. The greedy algorithm prioritized items based on their value-to-weight ratio, offering a fast but sometimes suboptimal solution. While, the brute force algorithm exhaustively explored all possibilities, guaranteeing the optimal solution but becoming computationally expensive for larger problems. the optimization techniques like approximation algorithms to balance efficiency. Overall, this activity provided a valuable hands-on introduction to knapsack problems.

#### Supplementary Activity:

* Choose a real-world problem that solves knapsacks problem
* Use the greedy and brute force algorithm to solve knapsacks problem

#### Supplementary Activity:

The real-world problem that I chose was a liI chose was a list of Interns with their corresponding salary and hours required to receive the salary.


The idea that I used knapsacks problem is the interns that has the least required hours and high salary.

In conclusion, the results of the greedy and brute force algorithm solves the problem since most of the results has the least hours and high salary.
"""

class Interns(object):
    def __init__(self, n, s, h):
        self.name = n
        self.salary = s
        self.hours = h

    def getName(self):
        return self.name

    def getSalary(self):
        return self.salary

    def getHours(self):
        return self.hours

    def density(self):
        return self.salary/self.hours

    def __str__(self):
        return self.name + ' <' + str(self.salary) + ', ' + str(self.hours) + '>'

def buildMenu(names, salary, hours):
    menu = []
    for i in range(len(salary)):
        menu.append(Interns(names[i], salary[i],hours[i]))
    return menu

def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the items of that solution"""
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getSalary() > avail:
        #Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake = maxVal(toConsider[1:],
                                     avail - nextItem.getSalary())
        withVal += nextItem.getSalary()
        #Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def testMaxVal(foods, maxUnits, printItems = True):
    print('Use search tree to allocate', maxUnits,
          'salaries')
    val, taken = maxVal(foods, maxUnits)
    print('Total salary of Interns taken =', val)
    if printItems:
        for item in taken:
            print('   ', item)

# Data
InternsName = ['Interns1', 'Interns2','Interns3','Interns4','Interns5','Interns6','Interns7','Interns8','Interns9','Interns10']
hours = [3,1,8,7,5,9,8,1,5,2]
salaries = [500,800,300,900,400,900,200,400,600,700]

Interns = buildMenu(InternsName, salaries, hours)

testMaxVal(Interns, 1000)

class Interns(object):
    def __init__(self, n, s, h):
        self.name = n
        self.salary = s
        self.hours = h

    def getName(self):
        return self.name

    def getSalary(self):
        return self.salary

    def getHours(self):
        return self.hours

    def density(self):
        return self.salary/self.hours

    def __str__(self):
        return self.name + ' <' + str(self.salary) + ', ' + str(self.hours) + '>'

def buildMenu(names, salaries, hours):
    menu = []
    for i in range(len(names)):
        menu.append(Interns(names[i], salaries[i], hours[i]))
    return menu

def greedy(items, maxSalary, keyFunction):
    itemsCopy = sorted(items, key = keyFunction,
                       reverse = True)
    result = []
    totalValue, totalSalary = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalSalary+itemsCopy[i].getSalary()) <= maxSalary:
            result.append(itemsCopy[i])
            totalSalary += itemsCopy[i].getSalary()
            totalValue += itemsCopy[i].getSalary()
    return (result, totalValue)

def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print('   ', item)

def testGreedys(interns, maxUnits):
    print('Use greedy by hours to allocate', maxUnits, 'hours')
    total_salary = sum(intern.getSalary() for intern in interns)
    print('Total salary for all interns:', total_salary)
    # Implement your greedy algorithm based on hours allocation

# Call the function with the list of interns
testGreedys(Interns, 1000)

InternsName = ['Interns1', 'Interns2','Interns3','Interns4','Interns5','Interns','Interns7','Interns8','Interns9','Interns10']
hours = [3,1,8,7,5,9,8,1,5,2]
salaries = [500,800,300,900,400,900,200,400,600,700]

Interns = buildMenu(InternsName, salaries, hours)
testGreedys(Interns, 1000)