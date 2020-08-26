package main;

import java.util.ArrayList;
import java.util.List;

public class Warehouse {

    private String name;
    private int priority;
    private List<Product> inventory;

    public Warehouse(String name, int priority, List<Product> inventory) {
        this.name = name;
        this.priority = priority;
        this.inventory = inventory;
    }
    public Warehouse(){
        inventory = new ArrayList<>();
    }
    public Warehouse(String name, int priority){
        this.name = name;
        this.priority = priority;
        this.inventory = new ArrayList<>();
    }
    public void addToInventory(String name, int quantity){
        Product currentProduct = new Product(name, quantity);
        currentProduct.setPriority(this.priority);
        currentProduct.setWareHouseName(this.name);
        this.inventory.add(currentProduct);
    }
    public void addToInventory(Product currentProduct, int quantity){
        currentProduct.setPriority(this.priority);
        currentProduct.setWareHouseName(this.name);
        currentProduct.setQuantity(quantity);
        this.inventory.add(currentProduct);
    }
    public void addToInventory(Product currentProduct){
        currentProduct.setPriority(this.priority);
        this.inventory.add(currentProduct);
    }
    public List<Product> getInventory() {
        return inventory;
    }

    public void setInventory(List<Product> inventory) {
        this.inventory = inventory;
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
    @Override
    public String toString() {
        return "{" +
                "name : " + name +
                ", inventory: " + inventory +
                '}';
    }

}
