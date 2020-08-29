
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
`pip3 -r requirements.txt`

2. Run the command below to run all the tests. I have used the pytest module for testing of this project.  <br>
`pytest Tests.py`

## Improvements to the current algorithm