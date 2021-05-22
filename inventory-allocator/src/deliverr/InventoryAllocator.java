package deliverr;

import java.util.*;

public class InventoryAllocator {

    public List<Shipment> createShipments(Map<String, Integer> orders, List<Warehouse> warehouseList){

        List<Shipment> shipmentList = new ArrayList();

        if(orders == null || orders.size() == 0 || warehouseList.size() == 0 || warehouseList == null){
            return shipmentList;
        }

        for(Warehouse warehouse : warehouseList){
            Shipment shipment = new Shipment();
            shipment.setWarehouseName(warehouse.getName());


            for(String items: warehouse.inventoryDistribution.keySet()){
                if(orders.containsKey(items)){
                    if(orders.get(items) == warehouse.inventoryDistribution.get(items)){
                        shipment.shipmentDetails.put(items, orders.get(items));
                        orders.remove(items);
                        warehouse.inventoryDistribution.put(items, 0);
                    }else if(orders.get(items) < warehouse.inventoryDistribution.get(items)){
                        shipment.shipmentDetails.put(items, orders.get(items));
                        warehouse.inventoryDistribution.put(items, warehouse.inventoryDistribution.get(items)-orders.get(items));
                        orders.remove(items);
                    }else
                        if(warehouse.inventoryDistribution.get(items) != 0){
                            shipment.shipmentDetails.put(items, warehouse.inventoryDistribution.get(items));
                            orders.put(items, orders.get(items)-warehouse.inventoryDistribution.get(items));
                            warehouse.inventoryDistribution.put(items, 0);
                        }

                }
                //Break if all orders are fulfilled
                if(orders.size() == 0){
                    break;
                }
            }
            if(shipment.shipmentDetails.size() != 0){
                shipmentList.add(shipment);
            }

            if(orders.size() == 0){
                break;
            }
        }

        return shipmentList;
    }

}