package com.company.tests;
import com.company.InventoryAllocator;
import com.company.Order;
import com.company.Shipment;
import com.company.Warehouse;
import org.junit.Test;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
import static org.junit.Assert.*;

/**
 * The InventoryAllocatorTest class tests the InventoryAllocator class, mainly the allocateShipments() function.
 * The constructor provides a set of global Orders and Warehouses to test on.
 *
 * @author  Jonathan Dai
 * @since   09-21-2019
 */

public class InventoryAllocatorTest {
    InventoryAllocator allocator;

    // Orders
    Order null_order;
    Order empty_order;
    Order one_item_order;
    Order large_order;

    // Warehouses;
    Warehouse null_warehouse;
    Warehouse empty_warehouse;
    Warehouse small_warehouse;
    Warehouse medium_warehouse;
    Warehouse large_warehouse;

    /**
     * create a set of reusable Orders, Warehouses, and Inventory Distributions to use
     */
    public InventoryAllocatorTest () {
        allocator = new InventoryAllocator();

        // 0. Null order
        null_order = null;

        // 1. Empty order
        Map<String, Integer> empty_o = new HashMap<>();
        empty_order = new Order(empty_o);

        // 2. One item order
        Map<String, Integer> one_o = new HashMap<>();
        one_o.put("apple", 5);
        one_item_order = new Order(one_o);

        // 3. Large order
        Map<String, Integer> large_o = new HashMap<>();
        large_o.put("apple", 5);
        large_o.put("orange", 10);
        large_o.put("carrot", 9);
        large_o.put("tomato", 66);
        large_o.put("blueberry", 21);
        large_order = new Order(large_o);

        // 0. Null Warehouse
        null_warehouse = null;

        // 1. Empty Warehouse
        Map<String, Integer> empty_w = new HashMap<>();
        empty_warehouse = new Warehouse("empty_warehouse", empty_w);

        // 2. Small capacity Warehouse
        Map<String, Integer> small_w = new HashMap<>();
        small_w.put("apple", 5);
        small_warehouse = new Warehouse("small_warehouse", small_w);

        // 2. Medium capacity Warehouse
        Map<String, Integer> medium_v = new HashMap<>();
        medium_v.put("apple", 9);
        medium_v.put("orange", 4);
        medium_v.put("tomato", 20);
        medium_v.put("blueberry", 10);
        medium_warehouse = new Warehouse("medium_warehouse", medium_v);

        // 3. Large capacity Warehouse
        Map<String, Integer> large_v = new HashMap<>();
        large_v.put("apple", 10);
        large_v.put("tomato", 60);
        large_v.put("blueberry", 21);
        large_v.put("carrot", 15);
        large_v.put("orange", 9);
        large_v.put("mango", 100);
        large_warehouse = new Warehouse("large_warehouse", large_v);
    }

    /**
     * Allocate shipments for null inventory distribution and null Order.
     */

    @Test
    public void allocateShipments_nullOrderAndInventory_emptyList() {
        List<Warehouse> inventoryDistribution = new ArrayList<>();
        inventoryDistribution.add(null_warehouse);
        List<Shipment> actual = allocator.allocateShipments(null, inventoryDistribution);

        assertEquals(new ArrayList<>(), actual);
    }

    /**
     * Allocate shipments when the inventory distribution is not enough for the order, should return empty list.
     */
    @Test
    public void allocateShipments_notEnoughInventory_emptyList() {
        List<Warehouse> inventoryDistribution = new ArrayList<>();
        inventoryDistribution.add(small_warehouse);
        List<Shipment> actual = allocator.allocateShipments(large_order, inventoryDistribution);

        // Expect: empty list
        assertEquals(new ArrayList<>(), actual);
    }

    /**
     * Allocate shipments when the first warehouse can cover the order, return ticket with only one shipment.
     */
    @Test
    public void allocateShipments_oneWarehouse_oneItemTicket() {
        List<Warehouse> inventoryDistribution = new ArrayList<>();
        inventoryDistribution.add(small_warehouse);
        inventoryDistribution.add(large_warehouse);
        List<Shipment> shipments = allocator.allocateShipments(one_item_order ,inventoryDistribution);

        // Expect: [Name: small_warehouse, apple: 5]
        Map<String, Integer> exp = new HashMap<>();
        exp.put("apple", 5);
        Shipment expected = new Shipment("small_warehouse", exp);
        assertEquals(expected.toString(), printReceipt(shipments));
    }

    /**
     * Allocate shipments when the first warehouse cannot cover the order, overflows to multiple tickets.
     */
    @Test
    public void allocateShipments_multiWarehouse_multiItemTicket() {
        List<Warehouse> inventoryDistribution = new ArrayList<>();
        inventoryDistribution.add(small_warehouse);
        inventoryDistribution.add(medium_warehouse);
        inventoryDistribution.add(empty_warehouse);
        inventoryDistribution.add(null_warehouse);
        inventoryDistribution.add(large_warehouse);
        List<Shipment> shipments = allocator.allocateShipments(large_order ,inventoryDistribution);

        // Expect:
        Map<String, Integer> small = new HashMap<>();
        small.put("apple", 5);
        Shipment small_s = new Shipment("small_warehouse", small);

        Map<String, Integer> medium = new HashMap<>();
        medium.put("orange", 4);
        medium.put("tomato", 20);
        medium.put("blueberry", 10);
        Shipment medium_s = new Shipment("medium_warehouse", medium);

        Map<String, Integer> large = new HashMap<>();
        large.put("orange", 6);
        large.put("carrot", 9);
        large.put("tomato", 46);
        large.put("blueberry", 11);
        Shipment large_s = new Shipment("large_warehouse", large);

        List<Shipment> expected = new ArrayList<>();
        expected.add(small_s);
        expected.add(medium_s);
        expected.add(large_s);
//        System.out.println(printReceipt(shipments));
        assertEquals(printReceipt((expected)), printReceipt(shipments));
    }

    @Test
    public void allocateShipments_multiWarehouse_emptyList() {
        List<Warehouse> inventoryDistribution = new ArrayList<>();
        inventoryDistribution.add(small_warehouse);
        inventoryDistribution.add(medium_warehouse);
        List<Shipment> actual = allocator.allocateShipments(large_order ,inventoryDistribution);

        // Expect: empty list
        assertEquals(new ArrayList<>(), actual);
    }

    public String printReceipt(List<Shipment> shipments) {
        String actual = "";
        for (Shipment s : shipments) {
            actual = actual + s.toString();
        }
        return actual;
    }
}