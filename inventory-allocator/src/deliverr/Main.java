package deliverr;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Main {
    public static void main(String[] args){

        InventoryAllocator ia = new InventoryAllocator();

        HashMap<String, Integer> orders = new HashMap<>();
        orders.put("apple", 10);
        orders.put("mango", 10);

        List<Warehouse> w = new ArrayList<>();

        HashMap<String, Integer> warehouseInventory1 = new HashMap<>();
        warehouseInventory1.put("apple", 3);
        warehouseInventory1.put("mango", 2);

        Warehouse w1 = new Warehouse("xyz", warehouseInventory1);

//        HashMap<String, Integer> warehouseInventory2 = new HashMap<>();
//        warehouseInventory2.put("apple", 1);
//        warehouseInventory2.put("mango", 2);
//
//        Warehouse w2 = new Warehouse("abc", warehouseInventory2);
//
//        HashMap<String, Integer> warehouseInventory3 = new HashMap<>();
//        warehouseInventory3.put("apple", 2);
//        warehouseInventory3.put("mango", 2);
//
//        Warehouse w3 = new Warehouse("owd", warehouseInventory3);

        w.add(w1);
//        w.add(w2);
//        w.add(w3);

        List<Shipment> shipment = ia.createShipments(orders, w);
        System.out.println(shipment);

    }
}
