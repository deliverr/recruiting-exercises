package com.company;
import java.util.List;
import java.util.ArrayList;

/**
 * The InventoryAllocator class calculates the optimal way for an order to be fulfilled by an inventory distribution.
 * It will NOT update the inventory distribution or order to reflect the order being completed (keeps the data intact).
 *
 * @author  Jonathan Dai
 * @since   09-21-2019
 */

public class InventoryAllocator {
    /**
     *
     * @param order
     * @return list of most cost effective shipments fulfill order, [] if not enough inventory
     */
    public List<Shipment> allocateShipments(Order order, List<Warehouse> inventoryDistribution) {
        List<Shipment> ticket = new ArrayList<>();
        for(Warehouse w : inventoryDistribution) {
            Shipment ship = (w != null) ? w.processOrder(order) : null;
            if(ship != null) {
                // if this Warehouse has anything to ship, add it to the ticket
                ticket.add(ship);
            }
        }
        // if this order is completely allocated, return the ticket. otherwise, return an empty ArrayList
        return (order != null && order.isOrderAllocated()) ? ticket :  new ArrayList<>();
    }
}
