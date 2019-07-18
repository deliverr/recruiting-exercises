package deliverr;

import java.util.HashMap;
import java.util.Map;

public class Shipment {

    String warehouseName;
    Map<String, Integer> shipmentDetails = new HashMap<>();


    public void setWarehouseName(String warehouseName) {
        this.warehouseName = warehouseName;
    }


    @Override
    public String toString() {
        return "{" +
                "" + warehouseName +
                ": " + shipmentDetails +
                '}';
    }
}