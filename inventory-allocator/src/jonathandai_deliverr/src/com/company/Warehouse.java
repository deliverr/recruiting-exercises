package com.company;
import java.util.Map;
import java.util.HashMap;

/**
 * The Warehouse class represents an instance of one warehouse and its inventory.
 * Example: {name: pwd, inventory: {apples: 5, oranges: 2}}
 *
 * @author  Jonathan Dai
 * @since   09-21-2019
 */

public class Warehouse {
    private String _name;
    private Map<String, Integer> _inventory;

    /**
     * Creates a Warehouse with a given name and an empty inventory
     *
     * @param name
     */
    public Warehouse(String name) {
        _name = name;
        _inventory = new HashMap<>();
    }

    /**
     * Creates a warehouse with a given name and inventory
     *
     * @param name
     * @param inventory
     */
    public Warehouse(String name, Map<String, Integer> inventory) {
        _name = name;
        _inventory = inventory;
    }

    /**
     *
     * @return name of the warehouse
     */
    public String getName() {
        return _name;
    }

    /**
     *
     * @param newName name to set
     */
    public void setName(String newName) {
        _name = newName;
    }

    /**
     *
     * @return inventory of the warehouse
     */
    public Map<String, Integer> getInventory() {
        return _inventory;
    }

    /**
     * Add product quantity to inventory
     *
     * @param productName
     * @param quantity
     */
    public void addToInventory(String productName, int quantity) {
        _inventory.put(productName, _inventory.getOrDefault(productName, 0) + quantity);
    }

    public Shipment processOrder(Order order) {
        Map<String, Integer> itemsToShip = new HashMap<>();
        Order orderTracker = new Order(order._order);
        for(String item: order.getItems()) {
            // If the order quantity is 0 or if the inventory does not have any of that item, go to next item.
            if(order.getQuantity(item) <= 0 || _inventory.getOrDefault(item, 0) <= 0) {
                continue;
            }
            // Update items to ship with either the whole order, or however much the inventory has left (if the whole order cannot be completed)
            itemsToShip.put(item, Math.min(order.getQuantity(item), _inventory.get(item)));
            // Update the order tracker with either the leftover amount this order needs, or 0 if the order was completed
            orderTracker.updateOrder(item, Math.max(order.getQuantity(item) - _inventory.get(item), 0));
        }

        if(itemsToShip.isEmpty()) {
            // If there are no items to ship from this warehouse, return null
            return null;
        }
        else {
            // Update the order to reflect the items shipped
            order.setOrder(orderTracker._order);
            // Create a new shipment object for this warehouse with the appropriate items to ship
            return new Shipment(_name, itemsToShip);
        }
    }
}

