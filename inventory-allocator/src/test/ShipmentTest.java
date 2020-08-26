package test;

import main.Product;
import main.Shipment;
import org.junit.Test;
import java.util.*;

import static org.junit.Assert.*;

public class ShipmentTest {
    Shipment shipment = new Shipment("ocw", null);

    @Test
    public void name() {
        String name = "testName";
        assertNotEquals(shipment.getName(), name);
        shipment.setName(name);
        assertEquals(shipment.getName(),name);
    }

    @Test
    public void setShipment() {
        assertEquals(shipment.getShipmentList(), null);
        HashSet<Product> list = new HashSet<>();
        shipment.setShipmentList(list);
        assertNotEquals(shipment.getShipmentList(), null);
        assertEquals(shipment.getShipmentList(), list);

    }
}