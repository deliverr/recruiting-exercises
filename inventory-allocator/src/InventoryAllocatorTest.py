import unittest
from InventoryAllocator import InventoryAllocator


class InventoryAllocatorTest(unittest.TestCase):

    def setUp(self):
        self.allocator = InventoryAllocator()
        self.warehouseList = [
            {
                'name' : 'mis',
                'inventory' : {
                                'apple' : 5,
                                'banana' : 5,
                                'cherry' : 5
                                }
             },
             {
                 'name' : 'gph',
                 'inventory' : {}
             },
             {
                 'name' : 'vgh',
                 'inventory' : {
                                'grape' : 3,
                                'honeydew' : 3,
                                'jackfruit' : 3
                                }
             },
             {
                 'name' : 'mkh',
                 'inventory': {
                                'apple' : 0,
                                'grape' : 2,
                                'jackfruit' : 3
                                }
             },
             {
                 'name' : 'scr',
                 'inventory': {
                                'grape' : 5,
                                'kiwi' : 2
                                }
                 }
            
            ]


    def getWarehouse(self, requestedWH = ['mis', 'gph', 'vgh', 'mkh', 'scr']):
        selectedWarehouse = []

        if requestedWH == '':
            return self.warehouseList

        for w in self.warehouseList:
            if w['name'] in requestedWH:
                selectedWarehouse.append(w)

        return selectedWarehouse




    # 0 ORDER TEST

    # no order, no stock
    def testZeroOrderZeroStock(self):
        order = {}
        warehouses = self.getWarehouse('gph')

        result = self.allocator.fulfillOrder(order, warehouses)
        expected = []

        self.assertEqual(result, expected)

    # no order, stock available
    def testZeroOrderNonZeroStock(self):
        order = {}
        warehouses = self.getWarehouse('mis')

        result = self.allocator.fulfillOrder(order, warehouses)
        expected = []

        self.assertEqual(result, expected)

    # no order, all warehouse
    def testZeroOrderAllWarehouse(self):
        order = {}
        warehouses = self.getWarehouse()

        result = self.allocator.fulfillOrder(order, warehouses)
        expected = []


    # 1 ORDER TEST

    # item not sold
    def testOneOrderNoStock(self): 
        order = {'dragonfruit' : 3}
        warehouses = self.getWarehouse()

        result = self.allocator.fulfillOrder(order, warehouses)
        expected = []

        self.assertEqual(result, expected, ' Item not sold')

    # item listed, but 0 stock
    def testOneOrderZeroStock(self): 
        order = {'apple' : 3}
        warehouses = self.getWarehouse('mkh')

        result = self.allocator.fulfillOrder(order, warehouses)
        expected = []

        self.assertEqual(result, expected, 'Item out of stock')

    # not enough stock to fulfill order
    def testOneOrderLimitedStock(self):
        order = {'apple' : 10}
        warehouses = self.getWarehouse('mis')

        result = self.allocator.fulfillOrder(order, warehouses)
        expected = []

        self.assertEqual(result, expected, 'Not enough stock')

    # collective stock not enough to fulfill order
    def testOneOrderLimitedCombinedStock(self):
        order = {'grape' : 20 }
        warehouses = self.getWarehouse(['vgh', 'mkh', 'scr'])

        result = self.allocator.fulfillOrder(order, warehouses)
        expected = []

        self.assertEqual(result, expected, 'Not enough stock')

    # item ready
    def testOneOrderNonZeroStock(self):
        order = {'apple' : 3}
        warehouses = self.getWarehouse('mis')

        result = self.allocator.fulfillOrder(order, warehouses)
        expected = [{'mis' : {'apple' : 3} }]

        self.assertEqual(result, expected)

    # item ready on separate warehouses
    def testOneOrderCombinedStock(self):
        order = {'grape' : 10}
        warehouses = self.getWarehouse()

        result = self.allocator.fulfillOrder(order, warehouses)
        expected = [
             {'vgh' : {'grape' : 3}},
             {'mkh' : {'grape' : 2}},
             {'scr' : {'grape' : 5}}
              ]

        self.assertEqual(result, expected)




    # MULTI ORDER TEST, SAME WAREHOUSE
    
    # stock unavailable
    def testMultiOrderZeroStock(self):
        order = {'apple' : 3, 'banana' : 3, 'cherry' : 3}
        warehouses = self.getWarehouse('gph')

        result = self.allocator.fulfillOrder(order, warehouses)
        expected = []

        self.assertEqual(result, expected, 'Not enough stock')

    # only some order can be fulfilled
    def testMultiOrderLimitedStock(self):
        order = {'apple' : 3, 'banana' : 3, 'grape' : 3}
        warehouses = self.getWarehouse('mis')

        result = self.allocator.fulfillOrder(order, warehouses)
        expected = []

        self.assertEqual(result, expected, 'Not enough to complete all order')

    # one order is at stock 0
    def testMultiOrderOneWIthZeroStock(self):
        order = {'jackfruit' : 2, 'apple' : 2}
        warehouse = self.getWarehouse('mkh')

        result = self.allocator.fulfillOrder(order, warehouse)
        expected = []

        self.assertEqual(result, expected, 'One iten is at stock 0')

    # none of the item on that warehouse
    def testMultiOrderOtherWarehouse(self):
        order = {'jackfruit' : 5, 'grape' : 3, 'kiwi': 2}
        warehouses = self.getWarehouse('mis')

        result = self.allocator.fulfillOrder(order, warehouses)
        expected = []

        self.assertEqual(result, expected, 'Items not on this warehouse')

    # order fulfilled
    def testMultiOrderOneWarehouse(self):
        order = {'apple' : 3, 'banana' : 3, 'cherry' : 3}
        warehouses = self.getWarehouse('mis')

        result = self.allocator.fulfillOrder(order, warehouses)
        expected = [{
            'mis' : {
                    'apple' : 3,
                    'banana' : 3,
                    'cherry' : 3}
            }]

        self.assertEqual(result, expected)




    # MULTI ORDER TEST, MULTI WAREHOUSE

    # multi order, none of the item sold
    def testMultiOrderNoStock(self):
        order = {'table' : 3, 'chair' : 2, 'lamp' : 5}
        warehouses = self.getWarehouse()

        result = self.allocator.fulfillOrder(order, warehouses)
        expected = []

        self.assertEqual(result, expected, 'Items not sold')

    # multi order, only some can be fulfilled
    def testMultiOrderLimitedStock(self):
        order = {'apple' : 6, 'banana' : 2, 'grape' : 50}
        warehouses = self.getWarehouse()

        result = self.allocator.fulfillOrder(order, warehouses)
        expected = []

        self.assertEqual(result, expected, 'Not enough stock')

    # multi order, one at stock 0
    def testMultiOrderOneWithZeroStock(self):
        order = {'kiwi' : 2, 'grape' : 2, 'apple' : 2}
        warehouses = self.getWarehouse(['mkh', 'scr'])

        result = self.allocator.fulfillOrder(order, warehouses)
        expected = []

        self.assertEqual(result, expected, 'One of the items at stock 0')

    # multi order, none of them has enough stock
    def testMultiOrderAllLimitedStock(self):
        order = {'cherry' : 10, 'grape' : 20, 'apple' : 10, 'jackfruit' : 10}
        warehouses = self.getWarehouse()

        result = self.allocator.fulfillOrder(order, warehouses)
        expected = []

        self.assertEqual(result, expected, 'All not enough stock')

    # multi order, enough stock
    def testMultiOrderEnoughStock(self):
        order = {'apple' : 3, 'grape' : 6}
        warehouses = self.getWarehouse()

        result = self.allocator.fulfillOrder(order, warehouses)
        expected = [
            {
                'mis': {
                        'apple' : 3
                        }
            },
            {
                'vgh': {
                        'grape' : 3
                        }
            },
            {
                'mkh': {
                        'grape' : 2
                        }
            },
            {
                'scr': {
                        'grape' : 1
                        }
                }
            ]

    # multi order, one of each item, prioritize location with lower cost
    def testMultiOrderOneEach(self):
        order = {'apple' : 1, 'banana' : 1, 'cherry' : 1, 'grape' : 1, 'honeydew' : 1, 'jackfruit' : 1, 'kiwi' : 1}
        warehouses = self.getWarehouse()

        result = self.allocator.fulfillOrder(order, warehouses)
        expected = [
            {
                'mis': {
                        'apple' : 1,
                        'banana' : 1,
                        'cherry' : 1
                        }
            },
            {
                'vgh': {
                        'grape' : 1,
                        'honeydew' : 1,
                        'jackfruit' : 1
                        }
            },
            {
                'scr': {
                        'kiwi' : 1
                        }
                }
            ]

        self.assertEqual(result, expected, 'Ordered one of each')

    # multi order, everything in stock
    def testMultiOrderAllStock(self):
        order = {'apple' : 5, 'banana' : 5, 'cherry' : 5, 'grape' : 10, 'honeydew' : 3, 'jackfruit' : 6, 'kiwi' : 2}
        warehouses = self.getWarehouse()

        result = self.allocator.fulfillOrder(order, warehouses)
        expected = [
            {
                'mis': {
                        'apple' : 5,
                        'banana' : 5,
                        'cherry' : 5
                        }
            },
            {
                 'vgh': {
                        'grape' : 3,
                        'honeydew' : 3,
                        'jackfruit' : 3
                        }
            },
            {
                 'mkh': {
                        'grape' : 2,
                        'jackfruit' : 3
                        }
            },
            {
                 'scr': {
                        'grape' : 5,
                        'kiwi' : 2
                        }
                }
            ]

        self.assertEqual(result, expected, 'All stock ordered')


if __name__ == '__main__':
    unittest.main()