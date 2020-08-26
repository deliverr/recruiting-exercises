package main;

import java.util.*;

public class InventoryAllocator {

    public InventoryAllocator() {
    }

    // Given an inventory distribution
    // Pre-Computation for products(in inventory) and their corresponding location ordered by priority(cheapest first)
    //
    public HashMap<String, PriorityQueue<Product>> getProductByPriority(List<Warehouse> inventoryDistribution) {

        HashMap<String, PriorityQueue<Product>> productsByPriority = new HashMap<>();

        if (inventoryDistribution == null || inventoryDistribution.size() < 1) {
            return productsByPriority;
        }

        for (int i = 0; i < inventoryDistribution.size(); i++) {

            Warehouse eachWarehouse = inventoryDistribution.get(i);
            String currentWarehouseName = eachWarehouse.getName();
            List<Product> currentWarehouseProductList = eachWarehouse.getInventory();

            int currentWarehousePriority = eachWarehouse.getPriority();

            for (Product product : currentWarehouseProductList) {

                PriorityQueue<Product> currentProductQueue = productsByPriority.getOrDefault(product.getName(), new PriorityQueue<>());

                product.setPriority(currentWarehousePriority);
                product.setWareHouseName(currentWarehouseName);
                currentProductQueue.add(product);
                productsByPriority.put(product.getName(), currentProductQueue);
            }
        }

        return productsByPriority;
    }

    // Given a  list of inventory Distribution and order map, return the best way to ship the orders from warehouses
    public List<Shipment> getCheapestShipments(List<Warehouse> inventoryDistribution, HashMap<String, Integer> order) {

        List<Shipment> shipmentsList = new ArrayList<>();

        // Not enough inventory
        if (inventoryDistribution == null || inventoryDistribution.size() < 1) {
            return shipmentsList;
        }

        HashMap<String, PriorityQueue<Product>> productsByPriority = getProductByPriority(inventoryDistribution);
        HashMap<String, HashSet<Product>> shipments = new HashMap<>();

        for (Map.Entry<String, Integer> eachOrder : order.entrySet()) {

            String productNameFromOrder = eachOrder.getKey();
            int productQuantityFromOrder = eachOrder.getValue();
            PriorityQueue<Product> productsQueue = productsByPriority.getOrDefault(productNameFromOrder, null);

            if (productsQueue == null) {
                return shipmentsList;
            }

            while (!productsQueue.isEmpty() && productQuantityFromOrder > 0) {

                Product productWithHigherPriority = productsQueue.peek();
                int productWithHigherPriorityQuantity = productWithHigherPriority.getQuantity();
                String warehouseName = productWithHigherPriority.getWareHouseName();
                HashSet<Product> shipmentListCurrentWarehouse = shipments.getOrDefault(warehouseName, new HashSet<>());

                if (productWithHigherPriorityQuantity <= productQuantityFromOrder) {

                    productQuantityFromOrder -= productWithHigherPriorityQuantity;
                    productsQueue.poll();
                    shipmentListCurrentWarehouse.add(productWithHigherPriority);
                    shipments.put(warehouseName, shipmentListCurrentWarehouse);

                } else {
                    productsQueue.peek().setQuantity(productWithHigherPriorityQuantity - productQuantityFromOrder);
                    Product top = new Product(productWithHigherPriority.getName(), productWithHigherPriority.getPriority(),
                            productWithHigherPriority.getWareHouseName(), productWithHigherPriority.getQuantity());
                    // quantity is the whole order since there are more into inventory right now.
                    top.setQuantity(productQuantityFromOrder);
                    shipmentListCurrentWarehouse.add(top);
                    shipments.put(warehouseName, shipmentListCurrentWarehouse);
                    productQuantityFromOrder = 0;
                }
            }
            // Not enough inventory, reset the shipment list and return it
            if (productQuantityFromOrder > 0) {

                shipmentsList.clear();
                return shipmentsList;
            }
        }
        // Now that we have the Shipments in HashMap, create their list now
        for (Map.Entry<String, HashSet<Product>> each : shipments.entrySet()) {
            shipmentsList.add(new Shipment(each.getKey(), each.getValue()));
        }

        return shipmentsList;
    }

}
