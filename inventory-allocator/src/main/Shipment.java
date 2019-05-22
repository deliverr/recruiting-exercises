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
       // StringBuilder shipmentList = new StringBuilder();
       // int size = this.shipmentList.size();
        /*
        for(int i = 0; i < this.shipmentList.size() - 1; i++ ){
            Product eachShipment = this.shipmentList.get(i);
            shipmentList.append(eachShipment.getName()+" : "+eachShipment.getQuantity()+" , ");
        }
        shipmentList.append(this.shipmentList.get(size -1 ).getName()+" : "+this.shipmentList.get(size -1 ).getQuantity());
        */
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
