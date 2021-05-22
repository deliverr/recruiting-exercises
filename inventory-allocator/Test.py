import unittest
import random
from BestShipment import Test




class test(unittest.TestCase):
    #simple test for one warehouse (gurantees to have the storage!) from original repository
    def test_orderShippedOneWarehouse1(self):
        order = {'apple': 1}
        inventory = [{'name': 'owd', 'inventory': {'apple': 1}}]
        output = [{'owd': {'apple': 1}}]
        self.assertEqual(output, Test.findBestShipment(order, inventory))

    #more general test for one warehouse with guranteed storage
    #the order number is some x and the inventory number is some n such that x < n
    #in this case the amount to ship is clearly x (we do this per item)
    def test_orderShippedOneWarehouseGeneral(self):
        appleOrderNumber = random.randint(1, 1000)
        orangeOrderNumber = random.randint(1, 1000)
        appleInventoryNumber = random.randint(appleOrderNumber, 10000)
        orangeInventoryNumber = random.randint(orangeOrderNumber, 10000)
        order = {'apple': appleOrderNumber, 'orange': orangeOrderNumber}
        inventory = [{'name': 'owd', 'inventory': {'apple': appleInventoryNumber, 'orange': orangeInventoryNumber}}]
        output = [{'owd': {'apple': appleOrderNumber, 'orange': orangeOrderNumber}}]
        self.assertEqual(output, Test.findBestShipment(order, inventory))

    #simple test for multiple warehouses (from original repository)
    def test_orderShippedMultipleWarehouse1(self):
        order = {'apple': 10}
        inventory = [{'name': 'owd', 'inventory': {'apple': 5}}, {'name': 'dm', 'inventory': {'apple': 5}}]
        output = [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]
        self.assertEqual(output, Test.findBestShipment(order, inventory))

    #more eneral test for multiple warehouses (in this case 2) with guranteed storage
    #if the ordered number is some x, then the total inventory number is some n >= x.
    #then the inventory for the storae is n1, n2 such that n1 + n2 = n
    #we also assume n1 < x so the case is more interesting
    #in this case we will have the shippping, n1, x - n1 (we do this per item)
    def test_orderShippedMultipleWarehouseGeneral(self):
        appleOrderNumber = random.randint(2, 1000)
        orangeOrderNumber = random.randint(2, 1000)
        totalAppleInventoryNumber = random.randint(appleOrderNumber, 10000)
        totalOrangeInventoryNumber = random.randint(orangeOrderNumber, 10000)
        appleInventoryNumber1 = random.randint(1, appleOrderNumber-1)
        orangeInventoryNumber1 = random.randint(1, orangeOrderNumber-1)
        appleInventoryNumber2 = totalAppleInventoryNumber - appleInventoryNumber1
        orangeInventoryNumber2 = totalOrangeInventoryNumber - orangeInventoryNumber1
        order = {'apple': appleOrderNumber, 'orange': orangeOrderNumber}
        inventory = [{'name': 'owd', 'inventory': {'apple': appleInventoryNumber1, 'orange': orangeInventoryNumber1}}, {'name': 'dm', 'inventory': {'apple': appleInventoryNumber2, 'orange': orangeInventoryNumber2}}]
        output = [{'owd': {'apple': appleInventoryNumber1, 'orange': orangeInventoryNumber1}}, {'dm': {'apple': appleOrderNumber - appleInventoryNumber1, 'orange': orangeOrderNumber-orangeInventoryNumber1}}]
        self.assertEqual(output, Test.findBestShipment(order, inventory))

    #simple test of cannotBeShipped from repository
    def test_cannotBeShipped1(self):
        order = {'apple': 1}
        inventory = [{'name': 'owd', 'inventory': {'apple': 0}}]
        output = []
        self.assertEqual(output, Test.findBestShipment(order, inventory))

    #simple test of cannotBeShipped from repository
    def test_cannotBeShipeed2(self):
        order = {'apple': 2}
        inventory = [{'name': 'owd', 'inventory': {'apple': 1}}]
        output = []
        self.assertEqual(output, Test.findBestShipment(order, inventory))

    #tests the simple case where we have enough inventory for some items but not all
    def test_cannotBeShipped3(self):
        order = {'apple': 10, 'banana': 9, 'orange': 9}
        inventory = [{'name': '1', 'inventory': {'apple': 11, 'banana': 12, 'orange': 8}}]
        output = []
        self.assertEqual(output, Test.findBestShipment(order, inventory))

    #tests the case where we have enough inventory for some items but not all (this times multiple storages). I got lazy with the names so its going to be 1, 2, 3 and so on
    def test_cannotBeShipped4(self):
        order = {'apple': 10, 'banana': 9, 'orange': 9}
        inventory = [{'name': '1', 'inventory': {'apple': 11}}, {'name': '2', 'inventory': {'apple': 10, 'orange': 12}}, {'name': '3', 'inventory': {'banana': 2}}]
        output = []
        self.assertEqual(output, Test.findBestShipment(order, inventory))

    #tests what happens if the ordered items do not exist yet
    def test_cannotBeshipped5(self):
        order = {'apple': 10}
        inventory = [{'name': 'a', 'inventory': {'banana': 1}}]
        output = []
        self.assertEqual(output, Test.findBestShipment(order, inventory))

    #tests what happens if inventories ceased to exist
    def test_cannotBeShipped6(self):
        order = {'apple': 1}
        inventory = []
        output = []
        self.assertEqual(output, Test.findBestShipment(order, inventory))

    #tests what happens if something glitches and sends an empty order
    def test_cannotBeShipped7(self):
        order = {}
        inventory = [{'name': 'a', 'inventory': {'banana': 1}}]
        output = []
        self.assertEqual(output, Test.findBestShipment(order, inventory))



if __name__ == '__main__':
    unittest.main()