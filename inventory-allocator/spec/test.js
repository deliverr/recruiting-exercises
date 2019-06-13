const assert = require('chai').assert;
const expect = require('chai').expect;
const InventoryAllocator = require('../src/inventoryAllocator');

const warehouses = [ 
  {
    name: 'first',
    inventory: { apple: 5, orange: 10 }
  }, 
  {
    name: 'second',
    inventory: { banana: 5, orange: 10 } 
  },
  {
    name: 'third',
    inventory: { carrots: 5, tomatoes: 10 }
  }, 
]
const inventory = new InventoryAllocator(warehouses);

describe('InventoryAllocator Class', () => {
  it('return an empty array for order of an item greater than total inventory', () => {
    assert.isEmpty(inventory.findCheapestShipment({ apple : 6 }));
  });

  it('return an empty array for order of an item not available in the total inventory', () => {
    assert.isEmpty(inventory.findCheapestShipment({ books : 6 }));
  });

  it('return cheapest shipment with an exact inventory match', () => {
    const shipment = inventory.findCheapestShipment({ apple : 5, tomatoes : 10 });

    expect(shipment).to.be.a('array');
    expect(shipment).to.have.lengthOf(2);
    expect(shipment[0]).to.have.property('first');
    expect(shipment[1]).to.have.property('third');
    expect(shipment[0].first.apple).to.equal(5);
    expect(shipment[1].third.tomatoes).to.equal(10);
  });

  it('update total inventory after an order has been placed', () => {
    expect(inventory.totalInventory.apple).to.equal(0);
    expect(inventory.totalInventory.tomatoes).to.equal(0);
  });

  it('should split an item across warehouses if that is the only way to completely ship an item', () => {
    const shipment = inventory.findCheapestShipment({ orange : 11 });

    expect(shipment).to.be.a('array');
    expect(shipment).to.have.lengthOf(2);
    expect(shipment[0]).to.have.property('first');
    expect(shipment[1]).to.have.property('second');
    expect(shipment[0].first.orange).to.equal(10);
    expect(shipment[1].second.orange).to.equal(1);
    expect(inventory.totalInventory.orange).to.equal(9);
  });

  it('should ship an item from the next warehouse if a cheaper one no longer contains the item', () => {
    const shipment = inventory.findCheapestShipment({ orange : 9 });

    expect(shipment).to.be.a('array');
    expect(shipment).to.have.lengthOf(1);
    expect(shipment[0]).to.have.property('second');
    expect(shipment[0].second.orange).to.equal(9);
    expect(inventory.totalInventory.orange).to.equal(0);

  });

  it('return an empty array for any order with items no longer available', () => {
    const shipment = inventory.findCheapestShipment({ 
      apple : 6,
      orange : 5, 
      carrots : 1 
    });

    assert.isEmpty(shipment);
  });
});