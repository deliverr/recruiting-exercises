module.exports = class InventoryAllocator {
  constructor(warehouses) {
    this.totalInventory = {};
    this.warehouses = warehouses;

    this.warehouses.forEach(warehouse => {
      this.addToTotalInventory(warehouse);
    });
  }

  addToTotalInventory(warehouse) {
    const inventoryDistribution = warehouse.inventory;
    
    for (let item in inventoryDistribution) {
      if (this.totalInventory[item]) {
        this.totalInventory[item] += inventoryDistribution[item];
      } else {
        this.totalInventory[item] = inventoryDistribution[item];
      }
    }
  }

  isValidQuantity(order) {
    for (let item in order) {
      if (order[item] > this.totalInventory[item]) return false;
    }
    return true;
  }
  
  findCheapestShipment(order) {
    if (!this.isValidQuantity(order)) return [];

    const finalShipment = [];
    const remaining = {};
    Object.assign(remaining, order);

    for (let i = 0; i < this.warehouses.length; i++) {
      if (Object.keys(remaining).length === 0) break;

      let warehouse = this.warehouses[i];
      let name = warehouse.name;
      let currentShipment = {};
      currentShipment[name] = {}

      for (let item in remaining) {
        if (warehouse.inventory[item] > 0) {
          if (warehouse.inventory[item] > remaining[item]) {

            currentShipment[name][item] = remaining[item];
            warehouse.inventory[item] -= remaining[item];
            this.totalInventory[item] -= remaining[item];
            delete remaining[item];

          } else {

            currentShipment[name][item] = warehouse.inventory[item];
            remaining[item] -= warehouse.inventory[item];
            this.totalInventory[item] -= warehouse.inventory[item];
            delete warehouse.inventory[item];

          }
          finalShipment.push(currentShipment);
        }
      }
    }
    return finalShipment; 
  }
}