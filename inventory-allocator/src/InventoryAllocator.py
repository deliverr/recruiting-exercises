class InventoryAllocator:
    def cheapestShipment(self,order, warehouses):

        #check if orders is empty
        if not order:
            return []

        answer = []

        #check if we can ship the orders from one warehouse completely (as in FAQs, this way is cheapest)
        for warehouse in warehouses:
            name = warehouse['name']
            item_list = warehouse['inventory']

            #set a flag as if the current warehouse can prepare the whole shipment
            flag = True
            for item in order:
                #if the current warehouse cannot prepare the whole order, we move on to next warehouse
                if item not in item_list or order[item] > item_list[item]:
                    flag = False
                    break

            if flag:
                #to maintain the stock of warehouse when increase the scabability of this problem in real life
                for item in order:
                    item_list[item] -= order[item]
                return [{name : order}]

        #In case we have to ship from multiple warehouses
        shipment = {}
        for warehouse in warehouses:
            name = warehouse['name']
            item_list = warehouse['inventory']


            shipment[name] = {}
            for item in order:
                #if this item from the order is empty
                if not order[item]:
                    continue
                #else we check if the current warehouse has the item or can prepare part of the item
                if item in item_list and item_list[item]:
                    #we update the order and current warehouse's stock
                    possible_item = min(order[item],item_list[item])
                    order[item] -= possible_item
                    item_list[item] -= possible_item
                    shipment[name][item] = possible_item

        for item in order:
            if order[item]:
                return []
        #get the answer of shipment list
        for name in shipment:
            #only at warehouse if they help prepare part of the order
            if shipment[name]:
                answer.append({name:shipment[name]})
        return answer
