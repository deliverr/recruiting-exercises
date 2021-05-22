package com.company;
import java.io.Serializable;
import java.util.Map;
import java.util.HashMap;
import java.util.Set;

/**
 * The Order class represents one order.
 * Example: {apples: 5, oranges: 2}
 *
 * @author  Jonathan Dai
 * @since   09-21-2019
 */

public class Order {
    Map<String, Integer> _order;

    /**
     * Creates new empty order
     */
    public Order() {
        _order = new HashMap<>();
    }

    /**
     * Creates new order with desired map
     *
     * @param order
     */
    public Order(Map<String, Integer> order) {
        _order = new HashMap<>();
        for(String key : order.keySet()) {
            int val = order.get(key);
            _order.put(key, val);
        }
    }

    public Set<String> getItems() {
        return _order.keySet();
    }

    public int getQuantity(String item) {
        return _order.get(item);
    }

    /**
     * Add product quantity to order
     *
     * @param productName
     * @param quantity
     */
    public void addToOrder(String productName, int quantity) {
        _order.put(productName, _order.getOrDefault(productName, 0) + quantity);
    }

    public void updateOrder(String productName, int newAmount) {
        _order.put(productName, newAmount);
    }

    public void setOrder(Map<String, Integer> newOrder) {
        _order = newOrder;
    }

    /**
     *
     * @returns if an order is completely allocated, meaning all the remaining quantities are 0
     */
    public boolean isOrderAllocated() {
        for(String s :_order.keySet()) {
            if(_order.get(s) != 0) {
                return false;
            }
        }
        return true;
    }
}
