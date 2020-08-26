class InventoryAllocator():
    def allocate(self, order, storage):
        result = []

        if order == None or len(order) == 0:
            return result
        if storage == None or len(storage) == 0:
            return result

        total = 0
        for item in order:
            total += order[item]

        for warehouse in storage:
            if total == 0:
                break
            name = warehouse["name"]
            inventory = warehouse["inventory"]
            for item in order:
                if order[item] == 0:
                    continue
                if item in inventory and inventory[item] > 0:
                    if result == [] or name not in result[-1]:
                        result.append({name: {}})
                    if inventory[item] >= order[item]:
                        total -= order[item]
                        result[-1][name][item] = order[item]
                        order[item] = 0
                    else:
                        total -= inventory[item]
                        result[-1][name][item] = inventory[item]
                        order[item] -= inventory[item]

        if total > 0:
            return []

        return result
