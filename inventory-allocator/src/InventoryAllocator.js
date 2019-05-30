class InventoryAllocator {
  constructor(orderItems, inventoryList) {
    this._order = orderItems;
    this._inventoryDist = inventoryList;
  }

  get order() {
    return this._order;
  }

  get inventoryDist() {
    return this._inventoryDist;
  }

  set order(newOrder) {
    this._order = newOrder;
  }

  set inventoryDist(newInventoryDist) {
    this._inventoryDist = newInventoryDist;
  }

  checkInventory(order, warehouse) {
    let result = [];
    let inventory = warehouse.inventory;
    // let copyOrder = order;

    for (let item in inventory) {
      let quantity = inventory[item];
      if (quantity === 0) continue;

      if (item in order) {
        let shipment = {};
        let itemAmount = {};
        // let orderAmt = order[item];

        if (quantity === order[item]) {
          itemAmount[item] = quantity;
          delete order[item];
        } else if (quantity < order[item]) {
          let difference = order[item] - quantity;
          itemAmount[item] = quantity;
          order[item] = difference;
        } else {
          itemAmount[item] = order[item];
          delete order[item];
        }

        shipment[warehouse.name] = itemAmount;
        result.push(shipment);
      }
    }

    return result.length < 1 ? null : result;
  }

  makeBestShipment(order = this.order(), inventoryDist = this.inventoryDist()) {
    if (!order || !inventoryDist) return null;
    let result = [];

    for (let i = 0; i < inventoryDist.length; i++) {
      let warehouse = inventoryDist[i];
      let shipment = this.checkInventory(order, warehouse);
      result = result.concat(shipment);
    }

    return result;
  }
}


exports.InventoryAllocator = InventoryAllocator;