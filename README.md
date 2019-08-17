# Inventory Allocator
by Carl Zhou

Written for this exercises:
https://github.com/deliverr/recruiting-exercises/blob/master/inventory-allocator/README.md

# Requirements:
Python 3

# Running the Code
```
(venv) A:\code\recruiting-exercises\inventory-allocator\src>python main.py
{ apple: 10 }, [{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { apple: 5 }}]
[{owd: {apple: 5}}, {dm: {apple: 5}}]
```

# Input Requirements:
Because the input string is missing double quotes", The spacing requirements between commas and brackets are strict.
In addition to that, the keys of the input cannot have \[ or \{ or \, or \:.
Unicode is supported.

# Testing
Test cases are written for logic and input. Security is not considered. This program may be vulnerable to deserialization vulnerabilities and DoS in Object deseriazliation.


# Running Tests
```
(venv) A:\code\recruiting-exercises\inventory-allocator\src>python inventory_allocator_tests.py
..................
----------------------------------------------------------------------
Ran 18 tests in 0.005s

OK
```
