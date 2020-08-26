class InventoryAllocator:

    def allocate_orders(self, order, inventory):
        res_list = []
        res = {}
        items = list(order.keys())
        for warehouse in inventory:
            name = warehouse['name']
            inventory = warehouse['inventory']
            for item in items:
                if item in inventory and order[item] != 0:
                    q = order[item]
                    q_in_stock = inventory[item]
                    if q_in_stock >= abs(q):
                        order[item] = 0
                        val = abs(q)
                    else:
                        order[item] = q_in_stock - abs(q)
                        val = abs(q_in_stock)

                    if name not in res:
                        res[name] = {}
                    res[name][item] = val

        quantities_left = list(order.values())
        order_fulfilled = all(x == 0 for x in quantities_left)
        if not order_fulfilled:
            return []
        if res:
            for k, v in res.items():
                res_list.append({k:v})
            return res_list
        return []

