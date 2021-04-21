const expect = require('chai').expect;
const allocator = require ('./inventory-allocator');

describe('Order Shipped using one warehouse', function() {
    it('should return the order shipping from one warehouse given one warehouse', function() {
        let shipments = { apple: 1};
        let warehouses = [{ name: "owd", inventory: { apple: 1 }}];
        let shipmentExpected = [ { owd: { apple: 1 } } ];

        let shipmentReturned = allocator.inventoryAllocator(shipments,warehouses);

        expect(shipmentReturned).to.deep.equal(shipmentExpected);
    })
})

describe('String containing a number passed instead of a number', function() {
    it('should return the order shipping from one warehouse given one warehouse', function() {
        let shipments = { apple: "4"};
        let warehouses = [{ name: "owd", inventory: { apple: "4" }}];;
        let shipmentExpected = [ { owd: { apple: 4 } } ];

        let shipmentReturned = allocator.inventoryAllocator(shipments,warehouses);

        expect(shipmentReturned).to.deep.equal(shipmentExpected);
    })
})

describe('Order Shipped using multiple warehouses', function() {
    it('should return the order shipping from multiple warehouse', function() {
        let shipments = { apple: 10 };
        let warehouses = [{ name: "owd", inventory: { apple: 5 } }, { name: "dm", inventory: { apple: 5 }}];
        let shipmentExpected = [{ dm: { apple: 5 }}, { owd: { apple: 5 } }];

        let shipmentReturned = allocator.inventoryAllocator(shipments,warehouses);

        expect(shipmentReturned).to.deep.equal(shipmentExpected);
    })
})

describe('Multiple items shipped from multiple warehouses', function() {
    it('should return the order shipping from multiple warehouse', function() {
        let shipments = { apple: 10, orange: 10};
        let warehouses = [{ name: "owd", inventory: { apple: 5, orange: 5 } }, { name: "dm", inventory: { apple: 5, orange: 5}}];
        let shipmentExpected = [{ dm: { apple: 5, orange: 5 }}, { owd: { apple: 5, orange: 5 } }];

        let shipmentReturned = allocator.inventoryAllocator(shipments,warehouses);

        expect(shipmentReturned).to.deep.equal(shipmentExpected);
    })
})

describe('Multiple items shipped from the first warehouse', function() {
    it('should return the order shipped from only the first warehouse', function() {
        let shipments = { apple: 10, orange: 10};
        let warehouses = [{ name: "owd", inventory: { apple: 20, orange: 20 } }, { name: "dm", inventory: { apple: 500, orange: 500}}];
        let shipmentExpected = [{ owd: { apple: 10, orange: 10 } }];

        let shipmentReturned = allocator.inventoryAllocator(shipments,warehouses);

        expect(shipmentReturned).to.deep.equal(shipmentExpected);
    })
})

describe('Multiple items shipped from the second warehouse', function() {
    it('should return the order shipped from only the second warehouse', function() {
        let shipments = { apple: 10, orange: 10};
        let warehouses = [{ name: "owd", inventory: { apple: 0, orange: 0 } }, { name: "dm", inventory: { apple: 500, orange: 500}}];
        let shipmentExpected = [{ dm: { apple: 10, orange: 10 } }];

        let shipmentReturned = allocator.inventoryAllocator(shipments,warehouses);

        expect(shipmentReturned).to.deep.equal(shipmentExpected);
    })
})

describe('First item shipped from the first warehouse second item shipped from second warehouse', function() {
    it('should return the order shipped from both warehouses', function() {
        let shipments = { apple: 10, orange: 10};
        let warehouses = [{ name: "owd", inventory: { apple: 10, orange: 0 } }, { name: "dm", inventory: { apple: 500, orange: 500}}];
        let shipmentExpected = [{ dm: { orange: 10 } }, { owd: { apple: 10 }}];

        let shipmentReturned = allocator.inventoryAllocator(shipments,warehouses);

        expect(shipmentReturned).to.deep.equal(shipmentExpected);
    })
})

describe('Order cannot be shiiped due to lack of inventory', function() {
    it('should return an empty array', function() {
        let shipments = { apple: 1};
        let warehouses = [{ name: "owd", inventory: { apple: 0 }}];
        let shipmentExpected = [];

        let shipmentReturned = allocator.inventoryAllocator(shipments,warehouses);

        expect(shipmentReturned).to.deep.equal(shipmentExpected);
    })
})

describe('Warehouse does not have a name', function() {
    it('should return an empty array', function() {
        let shipments = { apple: 1};
        let warehouses = [{ inventory: { apple: 30 }}];
        let shipmentExpected = [];

        let shipmentReturned = allocator.inventoryAllocator(shipments,warehouses);

        expect(shipmentReturned).to.deep.equal(shipmentExpected);
    })
})

describe('Negative numbers passed to the function', function() {
    it('should return an empty array', function() {
        let shipments = { apple: -33};
        let warehouses = [{ name: "owd", inventory: { apple: -23 }}];;
        let shipmentExpected = [];

        let shipmentReturned = allocator.inventoryAllocator(shipments,warehouses);

        expect(shipmentReturned).to.deep.equal(shipmentExpected);
    })
})

describe('Letter passed instead of a number', function() {
    it('should return an empty array', function() {
        let shipments = { apple: "e"};
        let warehouses = [{ name: "owd", inventory: { apple: "e" }}];;
        let shipmentExpected = [];

        let shipmentReturned = allocator.inventoryAllocator(shipments,warehouses);

        expect(shipmentReturned).to.deep.equal(shipmentExpected);
    })
})