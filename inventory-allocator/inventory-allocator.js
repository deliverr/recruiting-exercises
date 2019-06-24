class InventoryAllocator {
  constructor(order = {}, warehouses = []) {
    this.warehouses = warehouses;
    this.order = Object.assign({}, order);
    this.allocatedInventories = [];
    this.setItemsRemaining();
  }

  setItemsRemaining() {
    this.itemsRemaining = Object.values(this.order).reduce((a, b) => a + b, 0);
  }

  setWarehouses(warehouses) {
    this.warehouses = warehouses;
  }

  setOrder(order) {
    this.order = Object.assign({}, order);
    this.setItemsRemaining();
  }

  getWarehouses() {
    return this.warehouses;
  }

  getOrder() {
    return this.order;
  }

  shopInventory(inventory) {
    const inventoryItems = new Set(Object.keys(inventory));
    const itemsFilled = {};

    Object.entries(this.order).forEach((orderEntry) => {
      const [orderItem, orderQuantity] = orderEntry;

      if (inventoryItems.has(orderItem)) {
        const inventoryQuantity = inventory[orderItem];
        let quantityTaken;

        // quantityTaken limited either buy warehouse supply or order quantity
        if (orderQuantity <= inventoryQuantity) {
          quantityTaken = orderQuantity;
          delete this.order[orderItem];
        } else {
          quantityTaken = inventoryQuantity;
          this.order[orderItem] = orderQuantity - inventoryQuantity;
        }

        // Account for orders with <= 0 quantity
        if (quantityTaken > 0) {
          itemsFilled[orderItem] = quantityTaken;
          this.itemsRemaining -= quantityTaken;
        }
      }
    });
    return itemsFilled;
  }

  allocateInventories() {
    for (let i = 0; i < this.warehouses.length; i++) {
      const { name, inventory } = this.warehouses[i];
      const inventoryItems = this.shopInventory(inventory);

      // If any item taken from current warehouse, add to warehouses used
      if (Object.keys(inventoryItems).length > 0) {
        this.allocatedInventories.push({ [name]: inventoryItems });
      }

      // Short circuit loop once order fulfilled
      if (this.itemsRemaining === 0) return this.allocatedInventories;
    }
    return [];
  }
}

module.exports.InventoryAllocator = InventoryAllocator;
