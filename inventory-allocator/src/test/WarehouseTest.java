package test;

import main.Product;
import main.Warehouse;
import org.junit.Test;

import java.util.*;

import static org.junit.Assert.*;

public class WarehouseTest {

    private Warehouse warehouse = new Warehouse("Warehouse1", 2, null);

    @Test
    public void getInventory() {
        assertEquals(warehouse.getInventory(), null);

    }

    @Test
    public void setInventory() {
        List<Product> inventory = new ArrayList<>();
        warehouse.setInventory(inventory);
        assertEquals(warehouse.getInventory().size(), 0);
        inventory.add(new Product("Kiwi",1,"RandomWareHouse",5));
        assertFalse(warehouse.getInventory().size() == 0);
        assertFalse(warehouse.getInventory().equals(null));
    }

    @Test
    public void getName() {
        String name = "nameTest";
        warehouse.setName(name);
        assertFalse(warehouse.getName().equals("name"));
    }

    @Test
    public void setName() {
    }

    @Test
    public void getPriority() {
    }

    @Test
    public void setPriority() {
        int newPriority = 9;
        warehouse.setPriority(newPriority);
        assertEquals(warehouse.getPriority(), newPriority);
    }

}