import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

public class Tests {

    InventoryAllocator inventoryAllocator = InventoryAllocator.getInstance();

    @Test
    public void emptyOrderNonEmptyWarehouse() {

        Order order = new Order();
        Warehouse warehouse = new Warehouse("Warehouse1");
        warehouse.addProduct("Potato", 100 );
        List<Warehouse> warehouses = new ArrayList<>();
        warehouses.add(warehouse);
        List<Shipment> expectedShipments = new ArrayList<>();
        List<Shipment> actualShipments = inventoryAllocator.allocateOrder(order, warehouses);

        assertEquals(expectedShipments, actualShipments);
    }

    @Test
    public void nonEmptyOrderEmptyWarehouse() throws BadInputException {
        Order order = new Order();
        order.addProduct("Potato",100);
        List <Warehouse> warehouses = new ArrayList<>();
        List<Shipment> expectedShipments = new ArrayList<>();
        List<Shipment> actualShipments = inventoryAllocator.allocateOrder(order, warehouses);
        assertEquals(expectedShipments, actualShipments);
    }

    @Test
    public void emptyOrderEmptyWarehouse() {
        Order order = new Order();
        List <Warehouse> warehouses = new ArrayList<>();
        List<Shipment> expectedShipments = new ArrayList<>();
        List<Shipment> actualShipments = inventoryAllocator.allocateOrder(order, warehouses);
        assertEquals(expectedShipments, actualShipments);
    }

    @Test
    public void fulfillableOrderWithOneProductAndOneWarehouse() throws BadInputException  {
        Order order = new Order();
        order.addProduct("Potato",100);
        Warehouse warehouse = new Warehouse("Warehouse1");
        warehouse.addProduct("Potato",150);
        warehouse.addProduct("Tomato", 1000);
        List <Warehouse> warehouses = new ArrayList<>();
        warehouses.add(warehouse);
        List<Shipment> expectedShipments = new ArrayList<>();
        Shipment shipment = new Shipment("Warehouse1");
        shipment.addProduct("Potato",100);
        expectedShipments.add(shipment);
        List<Shipment> actualShipments = inventoryAllocator.allocateOrder(order, warehouses);
        assertEquals(expectedShipments, actualShipments);
    }

    @Test
    public void fulfillableOrderWithMultipleProductsAndOneWarehouse() throws BadInputException {
        Order order = new Order();
        order.addProduct("Potato",100);
        order.addProduct("Tomato",200);
        Warehouse warehouse = new Warehouse("Warehouse1");
        warehouse.addProduct("Potato",150);
        warehouse.addProduct("Tomato", 1000);
        List <Warehouse> warehouses = new ArrayList<>();
        warehouses.add(warehouse);
        List<Shipment> expectedShipments = new ArrayList<>();
        Shipment shipment = new Shipment("Warehouse1");
        shipment.addProduct("Potato",100);
        shipment.addProduct("Tomato", 200);
        expectedShipments.add(shipment);
        List<Shipment> actualShipments = inventoryAllocator.allocateOrder(order, warehouses);
        assertEquals(expectedShipments, actualShipments);
    }


    @Test
    public void fulfillableOrderWithMultipleProductsAndMultipleWarehousesWithOneShipment() throws BadInputException {
        Order order = new Order();
        order.addProduct("Potato",100);
        order.addProduct("Tomato",200);
        Warehouse warehouse1 = new Warehouse("Warehouse1");
        warehouse1.addProduct("Potato",150);
        warehouse1.addProduct("Tomato", 1000);
        Warehouse warehouse2 = new Warehouse("Warehouse2");
        warehouse2.addProduct("Potato",500);
        warehouse2.addProduct("Tomato", 700);
        List <Warehouse> warehouses = new ArrayList<>();
        warehouses.add(warehouse1);
        warehouses.add(warehouse2);
        List<Shipment> expectedShipments = new ArrayList<>();
        Shipment shipment = new Shipment("Warehouse1");
        shipment.addProduct("Potato",100);
        shipment.addProduct("Tomato", 200);
        expectedShipments.add(shipment);
        List<Shipment> actualShipments = inventoryAllocator.allocateOrder(order, warehouses);
        assertEquals(expectedShipments, actualShipments);
    }


    @Test
    public void fulfillableOrderWithMultipleProductsAndMultipleWarehousesWithMultipleShipments() throws BadInputException {
        Order order = new Order();
        order.addProduct("Potato",500);
        order.addProduct("Tomato",1200);
        Warehouse warehouse1 = new Warehouse("Warehouse1");
        warehouse1.addProduct("Potato",150);
        warehouse1.addProduct("Tomato", 1000);
        Warehouse warehouse2 = new Warehouse("Warehouse2");
        warehouse2.addProduct("Potato",500);
        warehouse2.addProduct("Tomato", 700);
        List <Warehouse> warehouses = new ArrayList<>();
        warehouses.add(warehouse1);
        warehouses.add(new Warehouse("EmptyWarehouse"));
        warehouses.add(warehouse2);
        List<Shipment> expectedShipments = new ArrayList<>();
        Shipment shipment1 = new Shipment("Warehouse1");
        shipment1.addProduct("Potato",150);
        shipment1.addProduct("Tomato", 1000);
        Shipment shipment2 = new Shipment("Warehouse2");
        shipment2.addProduct("Potato",350);
        shipment2.addProduct("Tomato", 200);
        expectedShipments.add(shipment1);
        expectedShipments.add(shipment2);
        List<Shipment> actualShipments = inventoryAllocator.allocateOrder(order, warehouses);
        assertEquals(expectedShipments, actualShipments);
    }

    @Test
    public void unfulfillableOrderWithOneProductAndOneWarehouse() throws BadInputException {
        Order order = new Order();
        order.addProduct("Potato",500);
        Warehouse warehouse = new Warehouse("Warehouse");
        warehouse.addProduct("Potato",150);
        List <Warehouse> warehouses = new ArrayList<>();
        warehouses.add(warehouse);
        List<Shipment> expectedShipments = new ArrayList<>();
        List<Shipment> actualShipments = inventoryAllocator.allocateOrder(order, warehouses);
        assertEquals(expectedShipments, actualShipments);
    }



    @Test
    public void unfulfillableOrderWithMultipleProductsAndOneWarehouse() throws BadInputException {
        Order order = new Order();
        order.addProduct("Potato",100);
        order.addProduct("Tomato",1200);
        Warehouse warehouse = new Warehouse("Warehouse1");
        warehouse.addProduct("Potato",150);
        warehouse.addProduct("Tomato", 1000);
        List <Warehouse> warehouses = new ArrayList<>();
        warehouses.add(warehouse);
        List<Shipment> expectedShipments = new ArrayList<>();
        List<Shipment> actualShipments = inventoryAllocator.allocateOrder(order, warehouses);
        assertEquals(expectedShipments, actualShipments);
    }

    @Test
    public void unfulfillableOrderWithMultipleProductsAndMultipleWarehouses() throws BadInputException {
        Order order = new Order();
        order.addProduct("Potato",100);
        order.addProduct("Tomato",1800);
        Warehouse warehouse1 = new Warehouse("Warehouse1");
        warehouse1.addProduct("Potato",150);
        warehouse1.addProduct("Tomato", 1000);
        Warehouse warehouse2 = new Warehouse("Warehouse2");
        warehouse2.addProduct("Potato",500);
        warehouse2.addProduct("Tomato", 700);
        List <Warehouse> warehouses = new ArrayList<>();
        warehouses.add(warehouse1);
        warehouses.add(warehouse2);
        List<Shipment> expectedShipments = new ArrayList<>();
        List<Shipment> actualShipments = inventoryAllocator.allocateOrder(order, warehouses);
        assertEquals(expectedShipments, actualShipments);
    }
}