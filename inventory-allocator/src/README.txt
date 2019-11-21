
### File descriptions

Warehouse.java
    Creates each warehouse with a unique name and inventory distribution.
    Used in creating a LinkedList of warehouses for the input.
InventoryAllocator.java
    Computes the best way an order can be shipped through the ship() method,
    given the inventory across the warehouses.
InventoryAllocatorTest.java
    Contains unit tests for the problem. Tests examples given in the problem
    description, as well as general cases and other edge cases.

### Running tests

Compile JAVA classes with:
javac ClassName.java

Run java class file with:
java ClassName

### Results should be displayed as: 

Input: {banana=30, orange=6, apple=5}, [{ name: sf, inventory: {apple=0} }, { name: ny,
inventory: {orange=0} }, { name: la, inventory: {banana=31, orange=6, apple=5} }]
Output: [{ name: la, inventory: {banana=30, orange=6, apple=5} }]

Input: {banana=5, orange=5, apple=5}, [{ name: owd, inventory: {orange=10, apple=5} },
{ name: dm, inventory: {banana=5, orange=10} }]
Output: [{ name: owd, inventory: {orange=5, apple=5} }, { name: dm, inventory: {banana=5} }]

Input: {apple=1}, [{ name: owd, inventory: {apple=1} }]
Output: [{ name: owd, inventory: {apple=1} }]

Input: {apple=10}, [{ name: owd, inventory: {apple=5} }, { name: dm, inventory: {apple=5} }]
Output: [{ name: owd, inventory: {apple=5} }, { name: dm, inventory: {apple=5} }]

Input: {banana=5, orange=20, apple=5, watermelon=15, mango=5}, [{ name: sf, inventory: {orange=7,
apple=10, watermelon=7} }, { name: ny, inventory: {banana=5, orange=10, mango=5} }, { name: la, inventory:
{banana=5, orange=15, mango=5} }, { name: dc, inventory: {watermelon=9} }]
Output: [{ name: sf, inventory: {orange=7, apple=5, watermelon=7} }, { name: ny, inventory: {banana=5,
orange=10, mango=5} }, { name: la, inventory: {orange=3} }, { name: dc, inventory: {watermelon=8} }]

Input: {banana=5, orange=5, apple=5}, [{ name: ny, inventory: {orange=10, apple=5,
cabbage=10} }, { name: sf, inventory: {banana=5, orange=10, sweet potato=10} }]
Output: [{ name: ny, inventory: {orange=5, apple=5} }, { name: sf, inventory: {banana=5} }]

Input: {apple=10}, [{ name: owd, inventory: {apple=5} }, { name: dm, inventory: {apple=5} },
{ name: ny, inventory: {apple=5} }]
Output: [{ name: owd, inventory: {apple=5} }, { name: dm, inventory: {apple=5} }]

Input: {apple=1}, [{ name: owd, inventory: {apple=0} }]
Output: []
