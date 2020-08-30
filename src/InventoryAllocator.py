class InventoryAllocator:
    
    #initialize orders and warehouse for inventory allocation
    def __init__(self, orders, warehouse):
        '''
        orders: parameter, represents the order that is used for search in inventories
        warehouse: paramer, represents the list of all available warehouses 
        '''
        self.__warehouse = warehouse
        self.__orders = orders
       
    #test the validation of the orders
    def isOrderValid(self):  
        #if order has no values inside, it is false -> no proceed
        if len(self.__orders) == 0:
            return False
        else:
            #iterate orders' items to test its validation on keys and values
            for keys, values in self.__orders.items():
                # if orders' key is an empty, it is false -> no proceed 
                if self.__orders.get('') :
                    return False 
                #if its keys has the string type but it is not an empty string, and its values are integer and also not empty integer
                #then continue looping through all the values 
                if isinstance(keys,str) and keys != '' and isinstance(values, int) and values != 0 :
                    continue
                #this is false when the conditions above do not match, then returns false -> no further proceed
                else:
                    return False
            #when the conditions are met, return true as a result
            return True 
    
    #test the validation of warehouses' inventory
    def isInventoryValid(self):
        #if the list of warehouses is empty, returns values False -> no proceed
        if len(self.__warehouse) == 0: 
            return False
        #while, the list of warehouses is not empty, need to test out their validity
        else:
            #Before testing warehouses's validity, need to make sure the orders are also true and valid
            if self.isOrderValid() == True:
                #Iterating through all the warehouses in the list
                for indexWarehouses, warehouseItem in enumerate(self.__warehouse): 
                    
                    #if the each item in the warehouse list is empty, immediately return false
                    if len(warehouseItem) == 0:
                        return False
                    else:
                        #otherwise,convert the values in warehouse list into another separate list for easier access to each values' content
                        #eg: {"name":"owa", "inventory":{"apple":5, "orange":7"}} -> [('name','owa'),('inventory', {"apple":5, "orange":7})]
                        listwarehouseItem = list(warehouseItem.items())
                       
                        #iterating within the range of the new list of warehouses
                        for i in range(len(listwarehouseItem)): 
                            
                            #for each content inside the range of values in the list, need to test for their validity
                            for j in range(len(listwarehouseItem[i])):
                                                         
                                bval = True
                                #Here, testing for the validation of each values' content begins here with conditions
                                # from line 75-line 85, I use redundant code (which is bad) that I could have easily called for the previous
                                #method isOrderValid() to test the validation of the amount of inventory (eg: {'apple':5,'pears' 3})
                                #but since the testing for the method is using the orders' values, I decided to create the similar way of testing the validation 
                                if len(listwarehouseItem[1][1]) == 0:
                                    bval=False
                                else:
                                    for keys, values in listwarehouseItem[1][1].items():
                                        if listwarehouseItem[1][1].get('') :
                                            bval= False 
            
                                        if isinstance(keys,str) and keys != '' and isinstance(values, int) :
                                            continue
                                        else:
                                            bval= False                           
                                #if each values' content (originally was a key in list), is not string and not empty then pass, and move to the next index 
                                if isinstance(listwarehouseItem[i][j],str) and (listwarehouseItem[i][j] != ''): 
                                    pass
                                #if there is a value's content that is a dict type, and the value of dict content is valid -> break out of the loop to test for the next validation in the next item of the list (inventory)
                                elif isinstance(listwarehouseItem[i][j],dict) and bval == True:
                                    break
                                #otherwise, the above conditions are not met -> immediately return false
                                else: 
                                    return False
                #if the testing of inventory is valid, return true as a result              
                return True
            else:
                #return false when the the value of orders is not valid
                return False
    
    #helper function
    #get associated warehouse's name with its inventory as a dictionary
    #this method is used along with the find_cheapest_shipments() method for my second experimentation
    def get_warehousename_and_inventory(self,dictItem): 
        
        
        dictItemsValues = [] #holds all values of inventory
        dictwHouseValues = [] #holds all values of warehouse's names
        '''
        - append all values into dictItemsValues list
        - append all warehouse's name into dictwHouseValues list
        - initialize a new dictionary to combine associated warehouse's name with its inventory
        - return the dictionary combinewHouseAndIven as the result
        '''
        for values in dictItem.values():
            if isinstance(values, dict) :
                dictItemsValues.append(values)
            else:
                dictwHouseValues.append(values)
                
        
        combinewHouseAndInven = {}
        for i in range(len(dictwHouseValues)):
            combinewHouseAndInven[dictwHouseValues[i]] = dictItemsValues[i]
        
        return combinewHouseAndInven #->eg: {'owa':{'apple':5},'dwa':{'orange':3}}
    
    #this method is used for finding the minimum shipments for optimal result
    #the logic of this method below is gathered from dynamic progamming strategy
    def find_cheapest_shipment(self):
        
        '''
           1.initialize newshipmentItem as an empty dictionary to hold of all the list of matching warehouses when the item is found
           2.initialize newshipmentResult as an empty list to hold newshipmentItem and this is used as the returned result
           3.initialize combineValues as an empty dictionary to hold the result of merged warehouses with their associated inventory
        '''  
        newshipmentResult=[] 
        newshipmentItem ={}
        combineValues = {}    
        
        #iterate through the result of combineValues to get all the associated warehouses
        for items in self.__warehouse:
            combineValues.update(self.get_warehousename_and_inventory(items))
        
        #from line 136 to line 153, only valids if the inventory values are valid as well    
        if self.isInventoryValid() == True:
            # iterate through the items of all orders
            for ordersKey, ordersVal in self.__orders.items():
                #iterate through the items of all warehouses
                for cKey,cValue in combineValues.items():
                    #iterate through the dictionary inventory values for each warehouse
                    for key, Invenval in cValue.items():
                        #if the product is found in the list of inventory, proceeds to the next line
                        if ordersKey == key: 
                            #if the order's amount is less or equal to the quantity from a product in inventory
                            #insert the warehouse into the dictionary newshipmentItem (container)
                            #Then insert newshipmentItem dict into the newShipmentResult list as the final returned result
                            if Invenval >= ordersVal: 
                                newshipmentItem[cKey] = cValue
                                newshipmentResult.append(newshipmentItem)                                
                                return newshipmentResult 
                            #if the order's amount is larger than the quantity from a product in inventory
                            #insert the warehouse into the dictionary newshipmentItem (container)
                            #substract the order's value amount from inventory quantity to search if there is more warehouse that can fullfil the order
                            #break out the loop to go the next warehouse
                            elif Invenval < ordersVal and Invenval != 0:  
                                newshipmentItem[cKey] = cValue                                   
                                ordersVal -= Invenval
                                break
                            #the condition is triggered when the orders cannot be fulfilled
                            else:
                                break
                        #if the product is not found in the list of inventory, break out of the loop, go to the next warehouse
                        else:
                            break
                    continue
        else:
            return False
        return newshipmentResult  #returned list of all cheapest shipments        
    


                    