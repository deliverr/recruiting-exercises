import unittest

class TestBestShipmentsSolution(unittest.TestCase):

    def testCase1(self):
        """
        Happy Case, exact inventory match!*
        Input: { apple: 1 }, [{ name: owd, inventory: { apple: 1 } }]
        Output: [{ owd: { apple: 1 } }]
        """
        order = { 'apple': 1 }
        inventory_distribution = [{ 'name': 'owd', 'inventory': { 'apple': 1 } }]
        output = [{ 'owd': { 'apple': 1 } }]
        self.assertEqual(output, BestShipmentsSolution().bestShipments(order, inventory_distribution))

    def testCase2(self):
        """
        Not enough inventory -> no allocations!
        Input: { apple: 1 }, [{ name: owd, inventory: { apple: 0 } }]
        Output: []
        """
        order = { 'apple': 1 }
        inventory_distribution = [{ 'name': 'owd', 'inventory': { 'apple': 0 } }]
        output = []
        self.assertEqual(output, BestShipmentsSolution().bestShipments(order, inventory_distribution))

    def testCase3(self):
        """
        Should split an item across warehouses if that is the only way to completely ship an item:
        Input: { apple: 10 }, [{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { apple: 5 }}]
        Output: [{ dm: { apple: 5 }}, { owd: { apple: 5 } }]
        """
        order = { 'apple': 10 }
        inventory_distribution = [{ 'name': 'owd', 'inventory': { 'apple': 5 } }, { 'name': 'dm', 'inventory': { 'apple': 5 }}]
        output = [{'dm': {'apple': 5}}, {'owd': {'apple': 5}}]
        self.assertEqual(output, BestShipmentsSolution().bestShipments(order, inventory_distribution))

class BestShipmentsSolution(object):
    def bestShipments(self, order, inventory_distribution):
        """
        :param order: dict
        :param inventory_distribution: List[dict]
        :return: List[dict]
        """
        output = []
        for house_id in range(len(inventory_distribution)):
            house_name = inventory_distribution[house_id]['name']
            house_inventory = inventory_distribution[house_id]['inventory']
            needs_from_the_house = {}
            order_item_list = order.keys()
            for item in order_item_list:
                if item in house_inventory:
                    # Update order
                    request_item_amount = order[item]
                    house_item_amount = house_inventory[item]
                    if house_item_amount >= request_item_amount:
                        needs_from_the_house[item] = request_item_amount
                        del order[item]
                    else:
                        needs_from_the_house[item] = house_item_amount
                        order[item] -= house_item_amount
            # Update output
            if len(needs_from_the_house) > 0:
                output.append({house_name: needs_from_the_house})
            # This means the order is empty now, so we can return output
            # In order to test our result, we sort the output here
            if len(order) == 0:
                return sorted(output)
        # There is not enough inventory
        return []

if __name__ == '__main__':
    unittest.main(verbosity = 2)




