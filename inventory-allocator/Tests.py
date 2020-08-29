import pytest

from Main import Main

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

def test_inventory_not_enough():
    order = {"apple": 5}
    warehouses =  [
        { "name": "owd", "inventory": { "apple": 4} }, 
    ]
    main = Main(order, warehouses)
    shipment = main.find_cheapest_shipment()
    expected = {
    }
    assert shipment == expected

def test_partial():
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

def test_multiple():
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

def test_priority_to_shipment():
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

def test_cheapest_entire():
    """
    Tests whether a particular item can be found in the warehouse that is already being visited given the
    order in which the items were processed. 
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

def test_entire_partial_outside():
    """
    
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

def test_empty_order():
    """

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

def test_cheapest_takes_priority():
    """

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

def test_large_order():
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

def test_order_wout_certain_items():
    order = {"banana": 2, "orange": 25}
    warehouses =  [
        { "name": "owd", "inventory": { "apple": 2, "orange": 2} }, 
        { "name": "amazon", "inventory": {"banana": 2, "orange": 3}},  
        { "name": "dm", "inventory": { "apple": 5, "banana": 1, "orange": 4}},
    ]
    main = Main(order, warehouses)
    shipment = main.find_cheapest_shipment()
    expected = {"amazon": {"banana": 2}}
    assert shipment == expected



