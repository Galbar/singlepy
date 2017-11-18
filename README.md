singlepy
========
[![Build Status](https://travis-ci.org/Galbar/singlepy.svg?branch=master)](https://travis-ci.org/Galbar/singlepy)
[![Coverage Status](https://coveralls.io/repos/github/Galbar/singlepy/badge.svg?branch=travis_integration)](https://coveralls.io/github/Galbar/singlepy?branch=travis_integration)

Small library that offers two simple to use singleton-pattern metaclasses:
 * Singleton
 * WeakSingleton

Install it using `pip`: `pip install singlepy`

Singleton
---------
Makes usage of the arguments passed to the class constructor to identify each unique instance of the class.
All instances, once created, will live until the end of the program.

### Example
```python
In [1]: from singlepy import Singleton

In [2]: class Number(metaclass=Singleton):
   ...:     def __init__(self, value):
   ...:         self.value = value
   ...:

In [3]: id(Number(1)) == id(Number(1))
Out[3]: True

In [4]: id(Number(1)) == id(Number(2))
Out[4]: False

In [5]: id(Number(2)) == id(Number(2))
Out[5]: True
```

WeakSingleton
---------
Makes usage of the arguments passed to the class constructor to identify each unique instance of the class.
Individual instances will be destroyed if there are no references to it.

### Example
```python
In [1]: from singlepy import WeakSingleton

In [2]: class Number(metaclass=WeakSingleton):
   ...:     def __init__(self, value):
   ...:         self.value = value
   ...:

In [3]: one = Number(1)

In [4]: id(one) == id(Number(1))
Out[4]: True

In [5]: two = Number(2)

In [6]: id(one) != id(two)
Out[6]: True

In [7]: id_one = id(one)

In [8]: del one

In [9]: id_two = id(two)

In [10]: two_two = Number(2)

In [11]: two_two is two
Out[11]: True

In [12]: del two

In [13]: two_two is Number(2)
Out[13]: True

In [14]: del two_two

In [15]: id_one == Number(1)
Out[15]: False

In [16]: id_two == Number(2)
Out[16]: False
```

Custom singleton key
--------------------
Imagine you have a class called Numbers, that stores a list of numbers:
```python
In [1]: class Numbers:
   ...:     def __init__(self, numbers):
   ...:         self._numbers = numbers
   ...:
   ...:     def sum(self):
   ...:         return sum(self._numbers)
   ...:
   ...:     def min(self):
   ...:         return min(self._numbers)
   ...:
   ...:     def max(self):
   ...:         return max(self._numbers)
   ...:

In [2]: Numbers([1, 2, 3, 4])
Out[2]: <__main__.Numbers at 0x10dfd5400>
```
And you want this class to be a singleton for the given set of numbers, no matter the order.
The classes Singleton and WeakSingleton offer a way to do this through `_make_singleton_key`:
```python
In [1]: from singlepy import Singleton
   ...: class Numbers(metaclass=Singleton):
   ...:     @staticmethod
   ...:     def _make_singleton_key(numbers):
   ...:         return str(list(sorted(numbers)))
   ...:
   ...:     ...

In [2]: id(Numbers([2, 3, 1, 4]))
Out[2]: 4535905696

In [3]: id(Numbers([1, 2, 3, 4]))
Out[3]: 4535905696

In [4]: id(Numbers([1, 2, 3]))
Out[4]: 4535654272
```

**Important**: `_make_singleton_key` must be a `staticmethod` and its return value must be hashable.
