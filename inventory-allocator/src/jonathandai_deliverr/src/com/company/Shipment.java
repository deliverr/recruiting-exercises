package com.company;
import java.util.Map;
import java.util.HashMap;

/**
 * The Shipment class represents a shipment from one warehouse.
 * Example: {pwd: {apples: 5, oranges: 2}}
 *
 * @author  Jonathan Dai
 * @since   09-21-2019
 */

public class Shipment {
    private String _warehouseName;
    private Map<String, Integer> _shipment;

    /**
     * Creates an empty shipment from a given warehouse
     *
     * @param warehouseName
     */
    public Shipment(String warehouseName) {
        _warehouseName = warehouseName;
        _shipment = new HashMap<>();
    }
    /**
     * Creates a shipment from a given warehouse with a given shipment amount
     *
     * @param warehouseName
     * @param shipment
     */

    public Shipment(String warehouseName, Map<String, Integer> shipment) {
        _warehouseName = warehouseName;
        _shipment = shipment;
    }

    /**
     *
     * @return warehouse name
     */
    public String getWarehouseName() {
        return _warehouseName;
    }

    /**
     * Updates product and quantity for a shipment
     *
     * @param productName
     * @param quantity
     */
    public void addToShipment(String productName, int quantity) {
        _shipment.put(productName, _shipment.getOrDefault(productName, 0) + quantity);
    }

    /**
     *
     * @return formats and prints shipment receipt
     */
    @Override
    public String toString() {
        String shipmentQuantities = "";
        int item = 0;
        for (String products : _shipment.keySet()) {
            if(item != 0){
                shipmentQuantities += ", ";
            }
            shipmentQuantities = shipmentQuantities + products + ": " + _shipment.get(products);
            item++;
        }
        return String.format("Warehouse Name —- " + _warehouseName + "\n Shipment —- " + shipmentQuantities + "\n \n");
    }
}