class InventoryAllocator:
    """
    Computes the best way an order can be shipped (called shipments) 
    given inventory across a set of warehouses (called inventory distribution)
    """ 
    def solution(self, order, inventory_dist):
        """
        input order: a map of items that are being ordered and how many of 
                    them are ordered
        input inventory_dist: a list of objects with warehouse name and inventory 
                    amounts (inventory distribution) for these items ordered by 
                    price.
        return: list of wearhouses and corresponding amounts of items from each
        
        # EXAMPLE OF USAGE
        >>>IA = InventoryAllocator()
        >>>IA.solution({ apple: 10 }, [{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { apple: 5 }}])
        [{ dm: { apple: 5 }}, { owd: { apple: 5 } }]) 
        >>>
        """
        result = []

        # initialize current checkout basket
        basket = {item: 0 for item in order.keys()}

        # make a linear pass over all the available stores until we fulfill the order.
        # greedily buy from cheaper stores, assuming earlier stores cost less.
        for store in inventory_dist:
            name = store['name']
            store_basket = {}
            to_remove = []
            for item in basket.keys():
                # see if store has curr item
                num_in_store = store['inventory'].get(item, -1)
                if num_in_store != -1:
                    num_need = order[item] - basket[item]
                    if num_in_store > 0 and num_need > 0:
                        # if the store has enough of item, remove item from checkout basket
                        # and add to store_basket
                        if num_in_store >= num_need:
                            store_basket[item] = num_need
                            to_remove.append(item)
                        # if the store has less than what is needed, update curr basket count
                        # and add to store_basket
                        else:
                            basket[item] += num_in_store
                            store_basket[item] = num_in_store
            # if we ordered from this store, add the basket to result
            if store_basket:
                result.append({name: store_basket})
            # remove items from basket if we've fulfilled that order
            for i in to_remove:
                del basket[i]
            # if our basket is empty return result
            if len(basket) == 0:
                return result
        return []