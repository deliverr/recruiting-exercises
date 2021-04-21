/*
    This function takes an array of objects(shipments) 
    and an array with a name/inventory object containing an array similar to shipments(warehouses)
    and returns them in the order given fufilling the order.
    If the order isn't possible to fill it returns an empty array.
*/
function inventoryAllocator(shipments, warehouses){
    let result = [];
    let resultConstructor = [];
    for(let item in shipments){
        let shipmentAmount = shipments[item];
        for(let warehouseNumber = 0; warehouseNumber < warehouses.length; warehouseNumber++){
            //checks if there is any order to fill and if there is any of the specified item in the warehouse as well as checking if it has a name to not return undefined
            if(shipmentAmount > 0 && warehouses[warehouseNumber].inventory[item] > 0 && warehouses[warehouseNumber].hasOwnProperty("name")){
                if (warehouses[warehouseNumber].inventory[item] >= shipmentAmount){
                    //spreads the old name object into a new one adding the shipment amount results to the object and finishing the order for that item
                    resultConstructor[warehouses[warehouseNumber].name] =  {...resultConstructor[warehouses[warehouseNumber].name], [item] : parseInt(shipmentAmount)};
                    shipmentAmount -= shipmentAmount;
                } else if(shipmentAmount > warehouses[warehouseNumber].inventory[item]){
                    //spreads the old name object into a new one adding the warehouse amount to the object
                    resultConstructor[warehouses[warehouseNumber].name] = {...resultConstructor[warehouses[warehouseNumber].name], [item] : parseInt(warehouses[warehouseNumber].inventory[item])};
                    shipmentAmount -= warehouses[warehouseNumber].inventory[item];
                }
            }
        }
        if(shipmentAmount > 0){
            return [];
        }
    }
    for(let shipped in resultConstructor){
        result.unshift({ [shipped] : resultConstructor[shipped]})
    }
    return result;
};
module.exports = {inventoryAllocator};