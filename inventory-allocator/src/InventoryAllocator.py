class InventoryAllocator:
    def allocate(self, order, warehouse):
        # avoid from crashing when meeting with empty input
        if order is None or warehouse is None:
            return []

        # initialize the return list
        res = []

        # by greedy, iterate all the warehouse by index
        for house in warehouse:
            house_name, house_inventory = house['name'], house['inventory']
            tmp = {}
            for item in order:
                # check whether each item in the order is being fullfiiled, or
                # the item is in the warehouse and make sure that item is actually in stock
                if order[item] > 0 and item in house_inventory and house_inventory[item] > 0:
                    # distribute value is the smaller value between the remaining number of the order
                    # and the number in warehouse
                    tmp[item] = min(order[item], house_inventory[item])
                    # update the remaining number in the order with order[item] - house_inventory[item], if the value
                    # is less than 0, set to 0
                    order[item] = max(0, order[item] - house_inventory[item])

            # if the there is item shipped from this warehouse, add to the result
            if tmp:
                res.append({house_name: tmp})

            # stop if all the items are fullfilled
            if not sum(order.values()):
                return res

        # if not fullfilled, return empty list
        return []



