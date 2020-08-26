import unittest
from inventory_allocator import InventoryAllocator


class TestInventoryAllocator(unittest.TestCase):
    def setUp(self):
        self.allocator = InventoryAllocator()

    def test_empty_order_empty_storage(self):
        self.assertEqual(self.allocator.allocate({}, []), [])

    def test_empty_order(self):
        order = {}
        storage = [{"name": "a", "inventory": {"apple": 5}}]
        self.assertEqual(self.allocator.allocate(order, storage), [])

        order = {"apple": 0}
        self.assertEqual(self.allocator.allocate(order, storage), [])

    def test_empty_storage(self):
        order = {"apple": 1}
        storage = []
        self.assertEqual(self.allocator.allocate(order, storage), [])

        storage = [{"name": "a", "inventory": {"apple": 0}}]
        self.assertEqual(self.allocator.allocate(order, storage), [])

    def test_exact_match(self):
        order = {"apple": 2, "orange": 1}
        storage = [{"name": "owd", "inventory": {"apple": 2, "orange": 1}}]
        self.assertEqual(self.allocator.allocate(
            order, storage), [{"owd": {"apple": 2, "orange": 1}}])

    def test_not_enough_inventory(self):
        order = {"apple": 2}
        storage = [{"name": "a", "inventory": {"apple": 0}}]
        self.assertEqual(self.allocator.allocate(order, storage), [])

        order = {"apple": 3}
        storage = [{"name": "a", "inventory": {"grape": 2}},
                   {"name": "b", "inventory": {"orange": 2}}]
        self.assertEqual(self.allocator.allocate(order, storage), [])

        order = {"apple": 3, "orange": 2}
        storage = [{"name": "a", "inventory": {"apple": 1, "orange": 1}},
                   {"name": "b", "inventory": {"apple": 1, "orange": 1}}]
        self.assertEqual(self.allocator.allocate(order, storage), [])

    def test_split_enough_inventory(self):
        order = {"apple": 5, "orange": 5}
        storage = [{"name": "a", "inventory": {"apple": 1, "orange": 5}},
                   {"name": "b", "inventory": {"apple": 6, "orange": 2}}]
        self.assertEqual(self.allocator.allocate(order, storage), [
                         {"a": {"apple": 1, "orange": 5}}, {"b": {"apple": 4}}])


if __name__ == '__main__':
    unittest.main()
