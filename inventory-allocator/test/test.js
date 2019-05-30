const { InventoryAllocator } = require("../src/InventoryAllocator");
const { expect } = require("chai");

describe('InventoryAllocator', () => {
  let inventoryAllocator;

  beforeEach(() => {
    let orderItems = {};
    let inventoryList = [];
    inventoryAllocator = new InventoryAllocator(orderItems, inventoryList);
  });

  describe('InventoryAllocator Constructor', () => {
    it ('Should exist', () => {
      expect(InventoryAllocator).to.exist;
    });

    it('Should have order and inventoryDist properties', () => {
      expect(inventoryAllocator).to.have.property('_order');
      expect(inventoryAllocator).to.have.property('_inventoryDist');
    });
  });

  describe('InventoryAllocator Methods', () => {
    describe('get order', () => {
      it('Should return null if there is no order', () => {
        let newOrder = null;
        inventoryAllocator.order = newOrder;
        expect(inventoryAllocator.order).to.equal(null);
      });

      it('Should return the current order when the order has been set', () => {
        let newOrder = { apple: 5, banana: 5, orange: 5 };
        inventoryAllocator.order = newOrder;
        expect(inventoryAllocator.order).to.equal(newOrder);
      });
    });

    describe('get inventoryDist', () => {
      it('Should return null if there is no inventory distribution', () => {
        let newInventoryDist = null;
        inventoryAllocator.inventoryDist = newInventoryDist;
        expect(inventoryAllocator.inventoryDist).to.equal(newInventoryDist);
      });

      it('Should return the inventory distribution when it has been set', () => {
        let newInventoryDist = [{ name: "owd", inventory: { apple: 5, orange: 10 } }, 
        { name: "dm", inventory: { banana: 5, orange: 10 } }];
        inventoryAllocator.inventoryDist = newInventoryDist;
        expect(inventoryAllocator.inventoryDist).to.equal(newInventoryDist);
      });
    });

    describe('set order', () => {
      it('Should set the order with the passed in new order', () => {
        let newOrder = { carrot: 5, broccoli: 10 };
        inventoryAllocator.order = newOrder;
        expect(inventoryAllocator.order).to.equal(newOrder);
      });
    });

    describe('set inventoryDist', () => {
      it('Should set the inventory distribution with the new inventory list', () => {
        let newInventoryDist = [{ name: "sams", inventory: { carrot: 5, pea: 10 } },
        { name: "kevins", inventory: { watermelon: 5, blueberry: 10 } }];
        inventoryAllocator.inventoryDist = newInventoryDist;
        expect(inventoryAllocator.inventoryDist).to.equal(newInventoryDist);
      });
    });
    
    describe('checkInventory', () => {
      it('Should return null if the warehouse does not have the inventory', () => {
        let newOrder = { strawberry: 5 };
        let newWarehouse = { name: "TJs", inventory: { strawberry: 0 } };
        expect(inventoryAllocator.checkInventory(newOrder, newWarehouse)).to.eql([]);
      });

      it('Should return an array of object(s) with the warehouse name as the key and the inventory as the value when the warehouse has the correct item and quantity', () => {
        let newOrder = { strawberry: 5 };
        let newWarehouse = { name: "TJs", inventory: { strawberry: 5 } };
        let newOrder2 = { apple: 5, banana: 5};
        let newWarehouse2 = { name: "Costco", inventory: { apple: 5, banana: 5 } };
        expect(
          inventoryAllocator.checkInventory(newOrder, newWarehouse)
        ).to.eql([{ TJs: { strawberry: 5 } }]);
        expect(
          inventoryAllocator.checkInventory(newOrder2, newWarehouse2)
        ).to.eql([{ Costco: { apple: 5 } }, { Costco: { banana: 5 } }]);
      });
    });
    
    describe('makeBestShipment', () => {
      it('Should return null if there is no order or no inventory distribution', () => {
        let newInventoryDist = [{
          name: "TJs",
          inventory: { strawberry: 5 }
        }];
        inventoryAllocator.order = null;
        inventoryAllocator.inventoryDist = newInventoryDist;
        expect(inventoryAllocator.makeBestShipment()).to.equal(null);
        let newOrder = { watermelon: 10};
        inventoryAllocator.order = newOrder;
        inventoryAllocator.inventoryDist = null;
        expect(inventoryAllocator.makeBestShipment()).to.equal(null);
      });

      it('Should return the exact inventory match if the inventory distribution has the exact order', () => {
        let newOrder = { carrot: 1 };
        let newInventoryDist = [{ 
          name: "TJs",
          inventory: { carrot: 1 }
        }];
        expect(
          inventoryAllocator.makeBestShipment(newOrder, newInventoryDist)
        ).to.eql([{ TJs: { carrot: 1 } }]);
      });

      it('Should return an empty array if there is not enough inventory', () => {
        let newOrder = { apple: 1 };
        let newInventoryDist = [{ name: "Costco", inventory: { apple: 0 } }];
        inventoryAllocator.order = newOrder;
        inventoryAllocator.inventoryDist = newInventoryDist;
        expect(inventoryAllocator.makeBestShipment()).to.eql([]);
      });

      it('Should split an item across warehouses if that is the only way to completely ship an item', () => {
        let newOrder = { apple: 10 };
        let newInventoryDist = [{ name: "TJs", inventory: { apple: 5 } }, { name: "Costco", inventory: { apple: 5 } }];
        inventoryAllocator.order = newOrder;
        inventoryAllocator.inventoryDist = newInventoryDist;
        expect(inventoryAllocator.makeBestShipment()).to.eql([{ TJs: { apple: 5 } }, { Costco: { apple: 5 } }]);
      });

      it('Should split multiple items across warehouses if that is the only way to completely ship the items', () => {
        let newOrder = { orange: 10, tangerine: 15 };
        let newInventoryDist = [
          { name: "TJs", inventory: { orange: 5, tangerine: 10 } },
          { name: "Costco", inventory: { orange: 5, tangerine: 5 } }
        ];
        inventoryAllocator.order = newOrder;
        inventoryAllocator.inventoryDist = newInventoryDist;
        expect(inventoryAllocator.makeBestShipment()).to.eql([
          { TJs: { orange: 5,} },
          { TJs: { tangerine: 10, } },
          { Costco: { orange: 5} },
          { Costco: { tangerine: 5 } }
        ]);
      });

      it('Should return the exact shipment when there is an excess amount in the inventory distribution', () => {
        let newOrder = { strawberry: 10, blueberry: 15 };
        let newInventoryDist = [
          { name: "TJs", inventory: { strawberry: 25, blueberry: 30 } },
        ];
        inventoryAllocator.order = newOrder;
        inventoryAllocator.inventoryDist = newInventoryDist;
        expect(inventoryAllocator.makeBestShipment()).to.eql([
          { TJs: { strawberry: 10 } },
          { TJs: { blueberry: 15 } }
        ]);
      });



    });

  });
});
