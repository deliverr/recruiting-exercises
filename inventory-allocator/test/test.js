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

    it('Should be a function (ES6 classes are "special functions")', () => {
      expect(InventoryAllocator).to.be.a('function');
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
        let order = { strawberry: 5 };
        let warehouse = { name: "TJs", inventory: { strawberry: 0 } };
        expect(inventoryAllocator.checkInventory(order, warehouse)).to.equal(null);
      });

      it('Should return an array of object(s) with the warehouse name as the key and the inventory as the value when the warehouse has the correct item and quantity', () => {
        let order = { strawberry: 5 };
        let warehouse = { name: "TJs", inventory: { strawberry: 5 } };
        let order2 = { apple: 5, banana: 5};
        let warehouse2 = { name: "Costco", inventory: { apple: 5, banana: 5 } };
        expect(
          inventoryAllocator.checkInventory(order, warehouse)
        ).to.eql([{ TJs: { strawberry: 5 } }]);
        expect(
          inventoryAllocator.checkInventory(order2, warehouse2)
        ).to.eql([{ Costco: { apple: 5 } }, { Costco: { banana: 5 } }]);
      });

      
    });
    


  });
});
