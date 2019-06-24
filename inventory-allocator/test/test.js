const { InventoryAllocator } = require('../inventory-allocator');
const { expect } = require('chai');

describe('InventoryAllocator', () => {
  beforeEach(() => {
    inventoryAllocator = new InventoryAllocator();
  });

  describe('InventoryAllocator Constructor', () => {
    it('Should exist', () => {
      expect(InventoryAllocator).to.exist;
    });
  });

  describe('InventoryAllocator Methods', () => {
    describe('set and get order', () => {
      it('Should set and get order properly', () => {
        const newOrder = { apples: 5, bananas: 5 };
        inventoryAllocator.setOrder(newOrder);
        expect(inventoryAllocator.getOrder()).to.deep.equal(newOrder);
      });
    });

    describe('set and get warehouse', () => {
      it('Should set and get order properly', () => {
        const warehouses = [{ name: 'owd', inventory: { apples: 5, oranges: 10 } }, { name: 'dm', inventory: { bananas: 5, oranges: 10 } }];
        inventoryAllocator.setWarehouses(warehouses);
        expect(inventoryAllocator.getWarehouses()).to.deep.equal(warehouses);
      });
    });

    describe('set and get items remaining', () => {
      it('Should set and get order properly', () => {
        const newOrder = { apples: 5, bananas: 5 };
        inventoryAllocator.setOrder(newOrder);
        const solution = 10;
        expect(inventoryAllocator.getItemsRemaining()).to.deep.equal(solution);
      });
    });

    describe('set and get items remaining', () => {
      it('Should set and get order with negative and zero quantities properly', () => {
        const newOrder = {
          apples: 5, bananas: 5, mangoes: 0, peaches: -5,
        };
        inventoryAllocator.setOrder(newOrder);
        const solution = 10;
        expect(inventoryAllocator.getItemsRemaining()).to.deep.equal(solution);
      });
    });

    describe('#allocateInventories', () => {
      it('Should allocate single inventories properly', () => {
        const order = { apples: 1 };
        const warehouses = [{ name: 'owd', inventory: { apples: 5, oranges: 10 } }, { name: 'dm', inventory: { bananas: 5, oranges: 10 } }];
        const solution = [{ owd: { apples: 1 } }];
        inventoryAllocator.setWarehouses(warehouses);
        inventoryAllocator.setOrder(order);
        expect(inventoryAllocator.allocateInventories()).to.deep.equal(solution);
      });
    });

    describe('#allocateInventories', () => {
      it('Should allocate insufficient inventories properly', () => {
        const order = { apples: 1 };
        const warehouses = [{ name: 'owd', inventory: { apples: 0 } }];
        const solution = [];
        inventoryAllocator.setWarehouses(warehouses);
        inventoryAllocator.setOrder(order);
        expect(inventoryAllocator.allocateInventories()).to.deep.equal(solution);
      });
    });

    describe('#allocateInventories', () => {
      it('Should allocate split inventories properly', () => {
        const order = { apples: 10 };
        const warehouses = [{ name: 'owd', inventory: { apples: 5 } }, { name: 'dm', inventory: { apples: 5 } }];
        const solution = [{ owd: { apples: 5 } }, { dm: { apples: 5 } }];
        inventoryAllocator.setWarehouses(warehouses);
        inventoryAllocator.setOrder(order);
        expect(inventoryAllocator.allocateInventories()).to.deep.equal(solution);
      });
    });

    describe('#allocateInventories', () => {
      it('Should allocate multiple split inventories properly', () => {
        const order = { apples: 3, watch: 2 };
        const warehouses = [{ name: 'w1', inventory: { apples: 1, watch: 1 } },
          { name: 'w2', inventory: { apples: 1 } },
          { name: 'w3', inventory: { apples: 1, watch: 2 } }];
        const solution = [{ w1: { apples: 1, watch: 1 } }, { w2: { apples: 1 } }, { w3: { apples: 1, watch: 1 } }];
        inventoryAllocator.setWarehouses(warehouses);
        inventoryAllocator.setOrder(order);
        expect(inventoryAllocator.allocateInventories()).to.deep.equal(solution);
      });
    });

    describe('#allocateInventories', () => {
      it('Should allocate inventories properly with zero quantity orders', () => {
        const order = { apples: 0, watch: 2 };
        const warehouses = [{ name: 'w1', inventory: { apples: 1, watch: 1 } },
          { name: 'w2', inventory: { apples: 1 } },
          { name: 'w3', inventory: { apples: 1, watch: 2 } }];
        const solution = [{ w1: { watch: 1 } }, { w3: { watch: 1 } }];
        inventoryAllocator.setWarehouses(warehouses);
        inventoryAllocator.setOrder(order);
        expect(inventoryAllocator.allocateInventories()).to.deep.equal(solution);
      });
    });

    describe('#allocateInventories', () => {
      it('Should allocate inventories properly, with negative quantity orders', () => {
        const order = { apples: -1, watch: 2 };
        const warehouses = [{ name: 'w1', inventory: { apples: 1, watch: 1 } },
          { name: 'w2', inventory: { apples: 1 } },
          { name: 'w3', inventory: { apples: 1, watch: 2 } }];
        const solution = [{ w1: { watch: 1 } }, { w3: { watch: 1 } }];
        inventoryAllocator.setWarehouses(warehouses);
        inventoryAllocator.setOrder(order);
        expect(inventoryAllocator.allocateInventories()).to.deep.equal(solution);
      });
    });

    describe('#allocateInventories', () => {
      it('Should allocate multiple split inventories properly', () => {
        const order = { apples: 4, oranges: 2, mangoes: 15 };

        const warehouses = [{ name: 'w1', inventory: { apples: 3, watch: 1, oranges: 1 } },
          { name: 'w2', inventory: { apples: 1, oranges: 1, mangoes: 10 } },
          { name: 'w3', inventory: { apples: 1, watch: 2, mangoes: 5 } }];

        const solution = [{ w1: { apples: 3, oranges: 1 } },
          { w2: { apples: 1, oranges: 1, mangoes: 10 } },
          { w3: { mangoes: 5 } }];

        inventoryAllocator.setWarehouses(warehouses);
        inventoryAllocator.setOrder(order);
        expect(inventoryAllocator.allocateInventories()).to.deep.equal(solution);
      });
    });
  });
});
