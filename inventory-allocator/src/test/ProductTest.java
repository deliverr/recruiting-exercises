package test;

import main.Product;
import org.junit.Test;

import static junit.framework.TestCase.*;

public class ProductTest {

    private Product product = new Product("Banana",2,"WareHouse1",10);
    private Product product1 = new Product("Banana",2,"WareHouse1",10);

    @Test
    public void getQuantity() {
        int quantity = 10;
        product.setQuantity(quantity);
        assertEquals(product.getQuantity(), quantity);
    }
    @Test
    public void setQuantity() {
        int quantity = 1000;
        product.setQuantity(quantity);
        assertEquals(product.getQuantity(), quantity);
    }

    @Test
    public void getName() {
        String newName = "testingName";
        product.setName(newName);
        assertEquals(product.getName(),newName);
    }

    @Test
    public void setName() {
        String newName = "testingName";
        product.setName(newName);
        assertEquals(product.getName(),newName);
    }

    @Test
    public void getPriority() {
        int newpriority = 0;
        product.setPriority(newpriority);
        assertEquals(product.getPriority(),newpriority);
    }

    @Test
    public void compareTo() {
        assertTrue(this.product.compareTo(product1) == 0);
    }
    @Test
    public void equals() {
        assertTrue(this.product.equals(product1));
    }

}