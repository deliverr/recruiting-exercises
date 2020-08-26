package main;

import java.util.Objects;

public class Product  implements Comparable {
    private String name;
    private int priority;
    private String wareHouseName;
    private int quantity;

    public Product(){

    }
    public Product(String name, int priority, String wareHouseName, int quantity) {
        this.name = name;
        this.priority = priority;
        this.wareHouseName = wareHouseName;
        this.quantity = quantity;
    }
    public Product(String name, int quantity){
        this.name = name;
        this.quantity = quantity;
    }
    @Override
    public String toString() {
        return "{ " +
                name +
                " : " + quantity +
                '}';
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }

    public String getWareHouseName() {
        return wareHouseName;
    }

    public void setWareHouseName(String wareHouseName) {
        this.wareHouseName = wareHouseName;
    }

    @Override
    public int compareTo(Object o) {
        if (this == (Product) o)
        return 0;
        return this.getPriority() - ((Product) o).getPriority();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Product product = (Product) o;
        return priority == product.priority &&
                Objects.equals(name, product.name) &&
                Objects.equals(wareHouseName, product.wareHouseName);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, priority, wareHouseName);
    }
}
