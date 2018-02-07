'''
Your own custom Python Module!
Did you know that you can actually create your own custom python module similar to the Underscore library in JavaScript? That may be hard to believe, as the things you've learned might seem simple (again, we try to make it look simple... (-: ), but in truth, you know how to create significant Python modules of your own. To create a custom Python module, you will simply add methods to a Python class!

You will create the following methods from the underscore library as methods of the "_" object. Pay attention to what you have to change, in terms of parameters for each method as well as implementation.

class Underscore(object):
    def map(self):
        # your code here
    def reduce(self):
        # your code here
    def find(self):
        # your code here
    def filter(self):
        # your code
    def reject(self):
        # your code

# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above

In the code above, you just created your own custom Python module/library that others can use! How can others use the methods in your library? By calling the properties stored in the class you defined (e.g. _.map(), _. reduce(), _.find(), etc).

Your assignment is to implement the 5 methods above using delegating callbacks. You will have to modify the 5 methods to take in an array and a callback. Use what you learned in the previous chapter about callbacks to complete the assignment.

One important concept that we want you to learn through this assignment is how to pass data to and from callbacks. You pass data to a callback with a parameter and you pass data from the callback back to the parent function with a return. While you are going through this assignment pay close attention to this relationship.

To understand what each method does, please refer to the underscore library. Note that your method does not have to be as robust as underscore's; you just need to get the base functionality working. Therefore for most methods you will only have the list and a lambda as parameters, and for the lambda you will pass in each element and potentially a "memo" also known as a "collector".

Note that some of these functions already exist in Python. We want you to explore how you might implement these yourself. Be aware that these tools exist to help work in a design idiom known as "functional programming". It's not something that we cover here, but is a topic you may want to explore on your own. It is mainly used in data science in recent years.
'''

class Underscore(object):
    def map(self, arg, f):
        results = []
        for k, v in enumerate(arg):
            if(isinstance(v,int)):
                results.append(f(arg[v-1]))
            else:
                results.append(f(arg[v], k))
        return sorted(results)
    def reduce(self, arg, f):
        sum = 0
        for i in range(0, len(arg)):
            sum = f(sum, arg[i])
        return sum
    def find(self, arg, f):
        for val in arg:
            if f(val):
                return val
        return 'undefined'
    def filter(self, arg, f):
        results = []
        for i in arg:
            if f(i):
                results.append(i)
        return results
    def reject(self, arg, f):
        results = []
        for i in arg:
            if not f(i):
                results.append(i)
        return results

_ = Underscore()

evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print evens

sumReduce = _.reduce([1, 2, 3], lambda memo, num: memo + num)
print sumReduce

map1 = _.map([1, 2, 3], lambda num: num * 3)
print map1
# => [3, 6, 9]

map2 = _.map({'one': 1, 'two': 2, 'three': 3}, lambda num, key: num * 3 )
print map2
# => [3, 6, 9]

find1 = _.find([1, 2, 3, 4, 5, 6], lambda num: num % 2 == 0 )
print find1

find2 = _.find(["hello", "world", "hows", "are", "you"], lambda val: val == "how" )
print find2

reject = _.reject([1, 2, 3, 4, 5, 6], lambda num: num % 2 == 0 )
print reject
