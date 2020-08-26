package main;

import java.util.*;

import java.util.Objects;

public class Shipment {

    private String name;
    private HashSet<Product> shipmentList;

    public Shipment(String name, HashSet<Product> shipmentList) {
        this.name = name;
        this.shipmentList = shipmentList;
    }
    public Shipment(String name){
        this.name = name;
        this.shipmentList = new HashSet<>();
    }
    public Shipment(){}
    @Override
    public String toString() {
        return "{ " + name + " : { " +
                "" + this.shipmentList +
                '}';
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public HashSet<Product> getShipmentList() {
        return shipmentList;
    }
    public void addToShipmentList(Product currentProduct){
        this.shipmentList.add(currentProduct);
    }
    public void setShipmentList(HashSet<Product> shipmentList) {
        this.shipmentList = shipmentList;
    }


    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Shipment shipment = (Shipment) o;
        return Objects.equals(name, shipment.name) &&
                Objects.equals(shipmentList, shipment.shipmentList);
    }


    @Override
    public int hashCode() {
        return Objects.hash(name, shipmentList);
    }
}
