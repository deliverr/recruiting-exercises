
class InventoryAllocatory {
  constructor() {
    this.order = {};
    this.inventoryDist = [];
  }

  getOrder() {
    return this.order;
  }

  getInventoryDist() {
    return this.inventoryDist;
  }

  setOrder(order) {
    this.order = order;
  }
  
  setInventoryDist(inventoryDist) {
    this.inventoryDist = inventoryDist;
  }
  
  checkInventory(order, warehouse) {
    let result = [];
    let inventory = warehouse.inventory;
    let copyOrder = order;

    for (let item in inventory) {
      let quantity = inventory[item];
      if (quantity === 0) continue;

      if (item in copyOrder) {
        let shipment = {};
        let itemAmount = {};

        if (quantity === copyOrder[item]) {
          itemAmount[item] = quantity;
          delete copyOrder[item];
        } else if (quantity < copyOrder[item]) {
          let difference = copyOrder[item] - quantity;
          itemAmount[item] = quantity;
          copyOrder[item] = difference;
        } else {
          itemAmount[item] = copyOrder[item];
          delete copyOrder[item];
        }

        shipment[warehouse.name] = itemAmount;
        result.push(shipment);
      }
    }

    return result;
  }

  makeCheapestShipment(order, inventoryDist) {
    let result = [];

    for (let i = 0; i < inventoryDist.length; i++) {
      let warehouse = inventoryDist[i];
      let shipment = this.checkInventory(order, warehouse);
      result = result.concat(shipment);
    }

    return result;
  }

}