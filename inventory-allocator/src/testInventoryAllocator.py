import unittest
from inventory_allocator import InventoryAllocator

class TestInventoryAllocator(unittest.TestCase):

    def setUp(self):
        self.ia = InventoryAllocator()
        self.itemPool = ['book', 'car', 'pen', 'bottle', 'phone']

    """
    Returns an order of items of the same quantity.
    """
    def makeOrder(self, items, quantity):
        newOrder = {}
        for i in range(len(items)):
            newOrder[items[i]] = quantity
        return newOrder

    """
    Returns an inventory of the given items of the same quantity for the given inventory name.
    """
    def makeInventory(self, name, items, quantity):
        newInventory = {}
        newInventory['name'] = name
        newInventory['inventory'] = {}
        for i in range(len(items)):
            newInventory['inventory'][items[i]] = quantity
        return newInventory

    """
    Returns an allocation of the given items of the given quantities for the given inventory name.
    """
    def makeAllocation(self, name, items, quantities):
        newAllocation = {name: {}}
        for i in range(len(items)):
            newAllocation[name][items[i]] = quantities[i]
        return newAllocation

    ################################################################################
    ## Tests for empty order.
    ################################################################################

    def testEmptyOrderEmptyInventories(self):
        order = {}
        inventories = []
        self.assertEqual(self.ia.allocate_orders(order, inventories), [])

    def testEmptyOrderSomeInventories(self):
        order = {}
        inventories = [self.makeInventory('tor', self.itemPool, 4)]
        self.assertEqual(self.ia.allocate_orders(order, inventories), [])


    ################################################################################
    ## Tests for one item order.
    ################################################################################

    def testOneOrderEmptyInventories(self):
        order = self.makeOrder(self.itemPool[0:1], 5)
        inventories = []
        self.assertEqual(self.ia.allocate_orders(order, inventories), [])

    ################################################################################

    """
    Not enough quantity.
    """
    def testOneOrderOneInsufficientInventory1(self):
        order = self.makeOrder(self.itemPool[0:1], 5)
        inventories = [self.makeInventory('tor', self.itemPool[0:3], 4)]
        self.assertEqual(self.ia.allocate_orders(order, inventories), [], 'Not enough quantity.')

    """
    Item not in stock.
    """
    def testOneOrderOneInsufficientInventory2(self):
        order = self.makeOrder(self.itemPool[0:1], 5)
        inventories = [self.makeInventory('tor', self.itemPool[3:4], 5)]
        self.assertEqual(self.ia.allocate_orders(order, inventories), [], 'Item not in stock.')

    """
    Special case: item in stock but 0 quantity.
    """
    def testOneOrderOneInsufficientInventory3(self):
        order = self.makeOrder(self.itemPool[0:1], 5)
        inventories = [self.makeInventory('tor', self.itemPool[0:4], 0)]
        self.assertEqual(self.ia.allocate_orders(order, inventories), [], 'Special case: item in stock but 0 quantity.')

    """
    Item not in stock.
    """
    def testOneOrderMultipleInsufficientInventory1(self):
        order = self.makeOrder(self.itemPool[0:1], 5)
        inventories = [self.makeInventory('tor', self.itemPool[3:4], 5), self.makeInventory('usa', self.itemPool[1:4], 5),
                       self.makeInventory('can', [self.itemPool[4]], 5)]
        self.assertEqual(self.ia.allocate_orders(order, inventories), [], 'Item not in stock.')

    """
    Not enough quantity.
    """
    def testOneOrderMultipleInsufficientInventory2(self):
        order = self.makeOrder(self.itemPool[0:1], 5)
        inventories = [self.makeInventory('tor', self.itemPool[3:4], 5), self.makeInventory('usa', self.itemPool[0:4], 2),
                       self.makeInventory('can', [self.itemPool[0]], 2)]
        self.assertEqual(self.ia.allocate_orders(order, inventories), [], 'Not enough quantity.')

    ################################################################################

    def testOneOrderOneSufficientInventory(self):
        order = self.makeOrder(self.itemPool[0:1], 5)
        inventories = [self.makeInventory('tor', self.itemPool[0:3], 6)]
        self.assertEqual(self.ia.allocate_orders(order, inventories), [self.makeAllocation('tor', self.itemPool[0:1], [5])])


    ################################################################################
    ## Tests for multiple items order.
    ################################################################################

    def testMultipleOrderEmptyInventories(self):
        order = self.makeOrder(self.itemPool[0:3], 5)
        inventories = []
        self.assertEqual(self.ia.allocate_orders(order, inventories), [])

    ################################################################################

    """
    One of the items not in stock.
    """
    def testMultipleOrderOneInsufficientInventory1(self):
        order = self.makeOrder(self.itemPool[0:3], 5)
        inventories = [self.makeInventory('tor', self.itemPool[3:4], 6)]
        self.assertEqual(self.ia.allocate_orders(order, inventories), [], 'One of the items not in stock.')

    """
    Not enough quantity.
    """
    def testMultipleOrderOneInsufficientInventory2(self):
        order = self.makeOrder(self.itemPool[0:3], 5)
        inventories = [self.makeInventory('tor', self.itemPool[0:4], 2)]
        self.assertEqual(self.ia.allocate_orders(order, inventories), [], 'Not enough quantity.')

    """
    Special case: 0 quantity.
    """
    def testMultipleOrderOneInsufficientInventory3(self):
        order = self.makeOrder(self.itemPool[0:3], 5)
        inventories = [self.makeInventory('tor', self.itemPool[0:4], 0)]
        self.assertEqual(self.ia.allocate_orders(order, inventories), [], 'Special case: 0 quantity.')

    """
    Some items not in stock, enough quantities for the rest.
    """
    def testMultipleOrderOneInsufficientInventory4(self):
        order = self.makeOrder(self.itemPool[0:3], 5)
        inventories = [self.makeInventory('tor', self.itemPool[2:4], 6)]
        self.assertEqual(self.ia.allocate_orders(order, inventories), [], 'Some items not in stock, enough quantities for the rest.')

    """
    Items not in stock.
    """
    def testMultipleOrderMultipleInsufficientInventory1(self):
        order = self.makeOrder(self.itemPool[0:3], 5)
        inventories = [self.makeInventory('tor', self.itemPool[3:], 6), self.makeInventory('usa', self.itemPool[3:4], 2),
                       self.makeInventory('can', self.itemPool[4:], 6)]
        self.assertEqual(self.ia.allocate_orders(order, inventories), [], 'Items not in stock.')

    """
    Not enough quantity.
    """
    def testMultipleOrderMultipleInsufficientInventory2(self):
        order = self.makeOrder(self.itemPool[0:3], 5)
        inventories = [self.makeInventory('tor', self.itemPool[:], 1), self.makeInventory('usa', self.itemPool[2:], 1),
                       self.makeInventory('can', self.itemPool[2:], 1)]
        self.assertEqual(self.ia.allocate_orders(order, inventories), [], 'Not enough quantity.')

    """
    Enough quantities for some items, not for the rest.
    """
    def testMultipleOrderMultipleInsufficientInventory3(self):
        order = self.makeOrder(self.itemPool[0:3], 5)
        inventories = [self.makeInventory('tor', self.itemPool[:], 2), self.makeInventory('usa', self.itemPool[2:], 3),
                       self.makeInventory('can', self.itemPool[1:], 1)]
        self.assertEqual(self.ia.allocate_orders(order, inventories), [], 'Enough quantities for some items, not for the rest.')

    ################################################################################

    def testMultipleOrderOneSufficientInventory(self):
        order = self.makeOrder(self.itemPool[0:3], 5)
        inventories = [self.makeInventory('tor', self.itemPool[0:3], 6)]
        self.assertEqual(self.ia.allocate_orders(order, inventories), [self.makeAllocation('tor', self.itemPool[0:3], [5, 5, 5, 5])])

    """
    One inventory has all the items needed.
    """
    def testMultipleOrderMultipleSufficientInventory1(self):
        order = self.makeOrder(self.itemPool[0:3], 5)
        inventories = [self.makeInventory('tor', self.itemPool[3:], 5), self.makeInventory('usa', self.itemPool[:], 5),
                       self.makeInventory('can', [self.itemPool[4]], 4)]
        self.assertEqual(self.ia.allocate_orders(order, inventories), [self.makeAllocation('usa', self.itemPool[0:3], [5, 5, 5])],
                         'One inventory has all the items needed.')



if __name__ == '__main__':
    unittest.main()