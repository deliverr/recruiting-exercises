const { InventoryAllocator } = require("../src/InventoryAllocator");
const { expect } = require("chai");

describe('InventoryAllocator', () => {
  let inventoryAllocator;

  beforeEach(() => {
    inventoryAllocator = new InventoryAllocator();
  });

  describe('InventoryAllocator Constructor', () => {
    it ('Should exist', () => {
      expect(InventoryAllocator).to.exist;
    });

    it('Should be a function (ES6 classes are "special functions")', () => {
      expect(InventoryAllocator).to.be.a('function');
    });

    it('Should have order, inventoryDist, and bestShipment properties', () => {
      expect(inventoryAllocator).to.have.property('order');
      expect(inventoryAllocator).to.have.property('inventoryDist');
      expect(inventoryAllocator).to.have.property('bestShipment');
    });
  });

  describe('InventoryAllocator Methods', () => {
    it('Should have methods named "getOrder", "getInventoryDist", "getBestShipment", "setOrder", "setInventoryDist", "checkInventory", and "makeBestShipment"', () => {
      expect(inventoryAllocator.getOrder).to.be.a("function");
      expect(inventoryAllocator.getInventoryDist).to.be.a("function");
      expect(inventoryAllocator.getBestShipment).to.be.a("function");
      expect(inventoryAllocator.setOrder).to.be.a("function");
      expect(inventoryAllocator.setInventoryDist).to.be.a("function");
      expect(inventoryAllocator.checkInventory).to.be.a("function");
      expect(inventoryAllocator.makeBestShipment).to.be.a("function");
    });

    describe('getOrder', () => {
      it('Should return null if there is no order', () => {
        let order = {};
        inventoryAllocator.setOrder(order);
        expect(inventoryAllocator.getOrder().to.equal(null));
      });

      it('Should return the current order when the order has been set', () => {
        let order = { apple: 5, banana: 5, orange: 5 };
        inventoryAllocator.setOrder(order);
        expect(inventoryAllocator.getOrder().to.equal({ apple: 5, banana: 5, orange: 5 }));
      });
    });


  });
});
