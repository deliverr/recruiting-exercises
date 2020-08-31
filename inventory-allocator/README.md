
# Inventory Allocator Solution

## Introduction:
Hi! I am Priyans Nishithkumar Desai. I am a junior at UC Berkeley, studying Computer Science with a minor in Data Science. I am really passionate about algorithms, software engineering and have got a recent interest in machine learning too. 

This repository contains my solution to the Inventory Allocation Problem given by Deliverr Inc. as part of their coding assessment. I have created this readme to make it easier to understand my thinking behind the design of the solution, how to run tests and some other ideas on improving the current algorithm. 

## Design:
1. Inventory.py - This is a class for the Inventory Management of the Warehouse. 
2. Item.py - Every item in the order or the inventory of a warehouse is an instance of this class. 
3. Main.py - Driver class for running the entire inventory allocation. 
4. Order.py - This is the class that handles the processing of a particular order. 
5. Tests.py - Contains all the tests for this project. 
6. Warehouse.py - The class for handling the warehouse and its management. 

## Running the tests:

1. Install the requirements using pip <br>
```bash
pip3 -r requirements.txt
```

2. Run the command below to run all the tests. I have used the pytest module for testing of this project.  <br>
```bash
pytest Tests.py
```

## Running a new order:

1. Navigate to place_order.py

2. The place_order.py contains the following code. Change the order and available warehouses as per your need. 
```python
from Main import Main
 
# Describes the order to be placed
order = {"apple": 5}
print("Order Received: {}".format(order))

# Describes the available warehouses
warehouses =  [
        { "name": "owd", "inventory": { "apple": 6} }, 
]

# Initializes the driver class for the inventory allocator
print("Order placed...")
main = Main(order, warehouses)

# Prepares the shipment
print("Preparing the shipment...")
shipment = main.find_cheapest_shipment()

# Prints the shipment
print("Shipment: {}".format(shipment))
```
## Improvement for the existing algorithm:

1. So, if we were to assume that the order in which items were to be purchased, then we can maintain a current shipments list and for next order items give priority to those warehouses already existing in that shipment. The pseudo code for that algorithm is (DISCLAIMER: This is super raw. But, explains my thought process and my in-notebook writing practice for algorithms. If you are interested in studying a python version of this improvement, have a look at extra/order_alternative.py from this directory. Note again this is a raw version too and may have errors. If you are interested in running that file, replace lines 30 - 169 in Order.py with this file's contents. But there might be errors.) : <br>
```
-->Iterate through all order_items
	-->If there are warehouse in the current shipment:
		-->Check if there is a warehouse from the shipment  that can completely fulfill the order
		-->If not, are there any warehouses in the shipment that can partially fulfill this order. 
			-->If only a certain quantity can be fulfilled, then check in remaining warehouses for a warehouse to 	 fulfill the remaining the quantity or a warehouse that can completely fulfill the order of the item
			    --> For the remaining quantity, if only one warehouse is needed
					--> Check its cost as compared to a warehouse from the remaining warehouses that can completely fulfill an order if that exists
			    --> If there are multiple warehouses from remaining warehouses, then check if a warehouse from the remaining warehouses can completely fulfill your order. 
			    	--> If Yes, then discard the combination of warehouses
			    	--> If No, use the combination. 

	--> If nothing in shipment:
		Proceed Normally for finding a complete warehouse or combination. 
```


2. Some kind of priority can also be set into the costs of having multiple items from one warehouse compared to the rest, to be able to come up with a better alternative. 

3. Some kind of optimization modelling could be applied. 