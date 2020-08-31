import pytest

from Main import Main

""" TEST CASE 1 """
def test_simple():
    """
    Checks a simple case 
    """
    order = {"apple": 5}
    warehouses =  [
        { "name": "owd", "inventory": { "apple": 6} }, 
    ]
    main = Main(order, warehouses)
    shipment = main.find_cheapest_shipment()
    expected = {
        "owd" : { "apple": 5}
    }
    assert shipment == expected

""" TEST CASE 2 """
def test_inventory_not_enough():
    """
    Checks that the allocator returns an empty list when no sufficient quantity is found.
    """
    order = {"apple": 5}
    warehouses =  [
        { "name": "owd", "inventory": { "apple": 4} }, 
    ]
    main = Main(order, warehouses)
    shipment = main.find_cheapest_shipment()
    expected = {
    }
    assert shipment == expected

""" TEST CASE 3 """
def test_partial():
    """
    Checks if an order can be completed completely through a combination of warehouses
    """
    order = {"apple": 5}
    warehouses =  [
        { "name": "owd", "inventory": { "apple": 2} }, 
        { "name": "amazon", "inventory": { "apple": 3} }
    ]
    main = Main(order, warehouses)
    shipment = main.find_cheapest_shipment()
    expected = {
        "owd" : { "apple": 2},
        "amazon" : {"apple": 3}    
    }
    assert shipment == expected

""" TEST CASE 4 """
def test_multiple():
    """
    Checks if multiple orders could be shipped. 
    """
    order = {"apple": 5, "banana": 10}
    warehouses =  [
        { "name": "owd", "inventory": { "apple": 2, "banana": 10} }, 
        { "name": "amazon", "inventory": { "apple": 3} }
    ]
    main = Main(order, warehouses)
    shipment = main.find_cheapest_shipment()
    expected = {
        "owd" : { "apple": 2, "banana": 10},
        "amazon" : {"apple": 3}    
    }
    assert shipment == expected

""" TEST CASE 5 """
def test_priority_to_shipment():
    """
    Another tests for checking handling of multiple warehouses and orders. 
    """
    order = {"apple": 5, "banana": 10}
    warehouses =  [
        { "name": "owd", "inventory": { "apple": 2, "banana": 10} }, 
        { "name": "amazon", "inventory": { "apple": 3, "banana": 5} },
        { "name": "flipkart", "inventory": { "apple": 3, "banana": 5} },   
    ]
    main = Main(order, warehouses)
    shipment = main.find_cheapest_shipment()
    expected = {
        "owd" : { "apple": 2, "banana": 10},
        "amazon" : {"apple": 3}    
    }
    assert shipment == expected

""" TEST CASE 6 """
def test_cheapest_entire():
    """
    Checks if a complete warehouse is preferred over a cheaper partial options. 
    """
    order = {"banana": 2, "orange": 4,  "apple": 5}
    warehouses =  [
        { "name": "owd", "inventory": { "apple": 2, "orange": 4} }, 
        { "name": "amazon", "inventory": {"banana": 2, "apple": 3}},  
        { "name": "dm", "inventory": { "apple": 5, "banana": 2, "orange": 4}},
    ]
    main = Main(order, warehouses)
    shipment = main.find_cheapest_shipment()
    expected = {
        'dm': { "apple": 5, "banana": 2, "orange": 4}
    }
    assert shipment == expected

""" TEST CASE 7 """
def test_entire_partial_outside():
    """
    Another test case for functional testing. 
    """
    order = {"banana": 2, "orange": 4}
    warehouses =  [
        { "name": "owd", "inventory": { "apple": 2, "orange": 2} }, 
        { "name": "amazon", "inventory": {"banana": 2, "apple": 3}},  
        { "name": "dm", "inventory": { "apple": 5, "banana": 2, "orange": 2}},
    ]
    main = Main(order, warehouses)
    shipment = main.find_cheapest_shipment()
    expected = {
        'amazon': {'banana': 2}, 
        'owd': {'orange': 2},
        'dm': {'orange': 2}
    }
    assert shipment == expected

""" TEST CASE 8 """
def test_empty_order():
    """
    Checks if an empty order returns an empty shipment 
    """
    order = {}
    warehouses =  [
        { "name": "owd", "inventory": { "apple": 2, "orange": 2} }, 
        { "name": "amazon", "inventory": {"banana": 2, "apple": 3}},  
        { "name": "dm", "inventory": { "apple": 5, "banana": 2, "orange": 2}},
    ]
    main = Main(order, warehouses)
    shipment = main.find_cheapest_shipment()
    expected = {}
    assert shipment == expected

""" TEST CASE 9 """
def test_cheapest_takes_priority():
    """
    Checks if a complete warehouse is preferred over a cheaper partial options. 
    """
    order = {"banana": 2, "orange": 5}
    warehouses =  [
        { "name": "owd", "inventory": { "apple": 2, "orange": 2} }, 
        { "name": "amazon", "inventory": {"banana": 2, "orange": 3}},  
        { "name": "dm", "inventory": { "apple": 5, "banana": 1, "orange": 5}},
    ]
    main = Main(order, warehouses)
    shipment = main.find_cheapest_shipment()
    expected = {
        'amazon': {'banana': 2}, 
        'dm': {'orange': 5}
    }
    assert shipment == expected

""" TEST CASE 10 """
def test_large_order():
    """
    Checks the handling of a very large order. 
    """
    order = {"banana": 2, "orange": 6, "guava": 30, "pineapple": 100, "strawberries": 400, 
    "raspberries": 20, "apple": 50, "grapes": 20}
    warehouses =  [
        { "name": "owd", "inventory": { "apple": 2, "orange": 2, "pineapple": 10}}, 
        { "name": "amazon", "inventory": {"banana": 1, "orange": 3}},  
        { "name": "dm", "inventory": { "apple": 20, "banana": 2, "orange": 5, "pineapple": 120}},
        { "name": "flipkart", "inventory": {"apple": 30, "strawberries": 40}},
        { "name": "wish", "inventory": {"guava": 10, "strawberries": 100}}, 
        { "name": "bigbasket", "inventory": {"raspberries": 25, "strawberries": 200}}, 
        { "name": "berkeley bowl", "inventory": {"strawberries": 100, "grapes": 20, "guava": 50}}
    ]
    main = Main(order, warehouses)
    shipment = main.find_cheapest_shipment()
    expected = {
        'dm': {'banana': 2, 'orange': 1, 'pineapple': 100, 'apple': 20}, 
        'owd': {'orange': 2, 'apple': 2}, 
        'amazon': {"orange": 3}, 
        'berkeley bowl': {"guava": 30, "grapes": 20, "strawberries": 60}, 
        'wish': {'strawberries': 100}, 
        'flipkart': {'strawberries': 40, "apple": 28}, 
        'bigbasket': {'strawberries': 200, 'raspberries': 20}
    }

    assert shipment == expected

""" TEST CASE 11 """
def test_order_wout_certain_items():
    """
    Checks that even if one item is not enough in inventory, an empty shipment is sent. 
    """
    order = {"banana": 2, "orange": 25}
    warehouses =  [
        { "name": "owd", "inventory": { "apple": 2, "orange": 2} }, 
        { "name": "amazon", "inventory": {"banana": 2, "orange": 3}},  
        { "name": "dm", "inventory": { "apple": 5, "banana": 1, "orange": 4}},
    ]
    main = Main(order, warehouses)
    shipment = main.find_cheapest_shipment()
    expected = {}
    assert shipment == expected

""" TEST CASE 12 """
def test_large_from_few_cheapest_orders():
    """
    Checks if large orders could be filled from few warehouses that can completely fulfill the order
    """
    order = {"banana": 2, "orange": 6, "guava": 30, "pineapple": 100, "strawberries": 400, 
    "raspberries": 25, "apple": 50, "grapes": 20}
    warehouses =  [
        { "name": "owd", "inventory": { "apple": 2, "orange": 2, "pineapple": 10}}, 
        { "name": "amazon", "inventory": {"banana": 1, "orange": 3, "guava": 25}},  
        { "name": "dm", "inventory": { "apple": 20, "banana": 1, "orange": 5, "pineapple": 90}},
        { "name": "flipkart", "inventory": {"apple": 30, "strawberries": 40}},
        { "name": "wish", "inventory": {"guava": 10, "strawberries": 100}}, 
        { "name": "bigbasket", "inventory": {"raspberries": 20, "strawberries": 200, "grapes": 5}}, 
        { "name": "berkeley bowl", "inventory": {"raspberries": 5, "strawberries": 100, "grapes": 15, "guava": 20}},
        { "name": "best_fruits", "inventory": {"banana": 2, "orange": 6, "guava": 30, "pineapple": 100}},
        { "name": "second_best_fruits", "inventory": {"strawberries": 400, "raspberries": 25, "apple": 50, "grapes": 20}}
    ]
    main = Main(order, warehouses)
    shipment = main.find_cheapest_shipment()
    expected = {
       'best_fruits': {"banana": 2, "orange": 6, "guava": 30, "pineapple": 100},
       'second_best_fruits': {"strawberries": 400, "raspberries": 25, "apple": 50, "grapes": 20}
    }
    assert shipment == expected

""" TEST CASE 13 """
def test_all_partial():
    """

    Checks if all orders could be filled by combination of warehouses. 
    """
    order = {"apple": 6, "orange": 4, "banana": 4}
    warehouses =  [
        { "name": "owd", "inventory": { "apple": 2, "orange": 2} }, 
        { "name": "amazon", "inventory": {"banana": 2, "apple": 3}},  
        { "name": "dm", "inventory": { "apple": 5, "banana": 2, "orange": 2}},
    ]
    main = Main(order, warehouses)
    shipment = main.find_cheapest_shipment()
    expected = {
        'owd': {'apple': 2, 'orange': 2}, 
        'amazon': {'apple': 3, 'banana': 2}, 
        'dm': {'apple': 1, 'orange': 2, 'banana': 2}
    }
    assert shipment == expected

""" TEST CASE 14 """
def test_ordering_of_items_in_order_does_not_matter():
    """
    Uses order from Test Case 13, but checks if ordering of items matter. 
    """
    order = {"orange": 4, "banana": 4, "apple": 6}
    warehouses =  [
        { "name": "owd", "inventory": { "apple": 2, "orange": 2} }, 
        { "name": "amazon", "inventory": {"banana": 2, "apple": 3}},  
        { "name": "dm", "inventory": { "apple": 5, "banana": 2, "orange": 2}},
    ]
    main = Main(order, warehouses)
    shipment = main.find_cheapest_shipment()
    expected = {
        'owd': {'apple': 2, 'orange': 2}, 
        'amazon': {'apple': 3, 'banana': 2}, 
        'dm': {'apple': 1, 'orange': 2, 'banana': 2}
    }
    assert shipment == expected

""" TEST CASE 15 """
def test_ordering_of_warehouses_matters():
    """
    Uses order from Test Case 13, but checks if ordering of warehouses matter.
    """
    order = {"orange": 4, "banana": 4, "apple": 6}
    warehouses =  [
        { "name": "dm", "inventory": { "apple": 5, "banana": 2, "orange": 3}},
        { "name": "amazon", "inventory": {"banana": 2, "apple": 3}},  
        { "name": "owd", "inventory": { "apple": 2, "orange": 1}},
    ]
    main = Main(order, warehouses)
    shipment = main.find_cheapest_shipment()
    expected = {
        'owd': {'orange': 1}, 
        'amazon': {'apple': 1, 'banana': 2}, 
        'dm': {'apple': 5, 'orange': 3, 'banana': 2}
    }
    assert shipment == expected

""" TEST CASE 16 """
def test_reusing_the_warehouses():
    """
    Checks if existing warehouses could be used to prepare a new shipment
    """
    order = {"orange": 4, "banana": 4}
    warehouses =  [
        { "name": "dm", "inventory": { "apple": 5, "banana": 2, "orange": 3}},
        { "name": "amazon", "inventory": {"banana": 3, "apple": 3}},  
        { "name": "owd", "inventory": { "apple": 2, "orange": 3}},
    ]
    main = Main(order, warehouses)
    shipment = main.find_cheapest_shipment()
    expected = {
        'owd': {'orange': 1}, 
        'amazon': {'banana': 2}, 
        'dm': {'orange': 3, 'banana': 2}
    }
    assert shipment == expected
    new_order = {"apple": 5, "orange": 2, "banana": 1}
    new_shipment = main.use_existing_warehouses_for_order(new_order)
    new_shipment_expected = {
        'dm': {'apple': 5}, 
        'owd': {'orange': 2}, 
        'amazon': {'banana': 1}
    }
    assert new_shipment == new_shipment_expected






