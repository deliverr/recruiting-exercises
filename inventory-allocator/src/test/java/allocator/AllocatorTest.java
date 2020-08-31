package allocator;

import org.junit.Test;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static org.hamcrest.CoreMatchers.equalTo;
import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.MatcherAssert.assertThat;

public class AllocatorTest {

    @Test
    public void testProduceCheapestShipment() {
        Allocator allocator = new Allocator();

        // Order is empty
        Map<String, Integer> order = new HashMap<>();
        List<Warehouse> warehouses = List.of(new Warehouse("owd", Map.of("apple", 1)));
        assertThat(allocator.produceCheapestShipment(order, warehouses), is(equalTo(List.of())));

        // There is no warehouse
        order = new HashMap<>(Map.of("apple", 1));
        warehouses = List.of();
        assertThat(allocator.produceCheapestShipment(order, warehouses), is(equalTo(List.of())));

        order = new HashMap<>();
        warehouses = List.of();
        assertThat(allocator.produceCheapestShipment(order, warehouses), is(equalTo(List.of())));

        // Order can be shipped using one warehouse
        order = new HashMap<>(Map.of("apple", 1));
        warehouses = List.of(new Warehouse("owd", Map.of("apple", 1)));
        assertThat(
                allocator.produceCheapestShipment(order, warehouses),
                is(equalTo(List.of(new Shipment("owd", Map.of("apple", 1)))))
        );

        // Order can be shipped using multiple warehouses
        order = new HashMap<>(Map.of("apple", 10));
        warehouses = List.of(
                new Warehouse("owd", Map.of("apple", 5)),
                new Warehouse("dm", Map.of("apple", 5))
        );
        assertThat(
                allocator.produceCheapestShipment(order, warehouses),
                is(equalTo(List.of(
                        new Shipment("owd", Map.of("apple", 5)),
                        new Shipment("dm", Map.of("apple", 5))
                )))
        );

        order = new HashMap<>(Map.of("apple", 5, "banana", 5, "orange", 5));
        warehouses = List.of(
                new Warehouse("owd", Map.of("apple", 5, "orange", 10)),
                new Warehouse("dm", Map.of("banana", 5, "orange", 10))
        );
        assertThat(
                allocator.produceCheapestShipment(order, warehouses),
                is(equalTo(List.of(
                        new Shipment("owd", Map.of("apple", 5, "orange", 5)),
                        new Shipment("dm", Map.of("banana", 5))
                )))
        );

        order = new HashMap<>(Map.of("apple", 13, "banana", 7, "orange", 12));
        warehouses = List.of(
                new Warehouse("owd", Map.of("apple", 2, "orange", 10, "kiwi", 3)),
                new Warehouse("dm", Map.of("banana", 3, "apple", 2)),
                new Warehouse("foo", Map.of("orange", 3, "apple", 8, "banana", 1)),
                new Warehouse("bash", Map.of("apple", 2, "banana", 4))
        );
        assertThat(
                allocator.produceCheapestShipment(order, warehouses),
                is(equalTo(List.of(
                        new Shipment("owd", Map.of("apple", 2, "orange", 10)),
                        new Shipment("dm", Map.of("banana", 3, "apple", 2)),
                        new Shipment("foo", Map.of("orange", 2, "apple", 8, "banana", 1)),
                        new Shipment("bash", Map.of("apple", 1, "banana", 3))
                )))
        );

        // Order cannot be shipped because there is not enough inventory
        order = new HashMap<>(Map.of("apple", 1));
        warehouses = List.of(new Warehouse("owd", Map.of("apple", 0)));
        assertThat(allocator.produceCheapestShipment(order, warehouses), is(equalTo(List.of())));

        order = new HashMap<>(Map.of("apple", 2));
        warehouses = List.of(new Warehouse("owd", Map.of("apple", 1)));
        assertThat(allocator.produceCheapestShipment(order, warehouses), is(equalTo(List.of())));

        order = new HashMap<>(Map.of("apple", 3));
        warehouses = List.of(
                new Warehouse("owd", Map.of("apple", 2)),
                new Warehouse("dm", Map.of("banana", 3))
        );
        assertThat(allocator.produceCheapestShipment(order, warehouses), is(equalTo(List.of())));

        order = new HashMap<>(Map.of("apple", 3, "banana", 3));
        warehouses = List.of(
                new Warehouse("owd", Map.of("apple", 2)),
                new Warehouse("dm", Map.of("banana", 3))
        );
        assertThat(allocator.produceCheapestShipment(order, warehouses), is(equalTo(List.of())));

        // Order can be shipped by multiple warehouses, but one is enough
        order = new HashMap<>(Map.of("apple", 1, "banana", 3));
        warehouses = List.of(
                new Warehouse("owd", Map.of("apple", 2, "banana", 4)),
                new Warehouse("dm", Map.of("apple", 3, "banana", 1))
        );
        assertThat(
                allocator.produceCheapestShipment(order, warehouses),
                is(equalTo(List.of(new Shipment("owd", Map.of("apple", 1, "banana", 3)))))
        );

        // Shipping out of one warehouse is cheaper than shipping from multiple warehouses
        order = new HashMap<>(Map.of("apple", 1, "banana", 3));
        warehouses = List.of(
                new Warehouse("owd", Map.of("apple", 3, "banana", 1)),
                new Warehouse("dm", Map.of("banana", 2)),
                new Warehouse("foo", Map.of("banana", 100))
        );
        assertThat(
                allocator.produceCheapestShipment(order, warehouses),
                is(equalTo(List.of(
                        new Shipment("owd", Map.of("apple", 1)),
                        new Shipment("foo", Map.of("banana", 3))
                )))
        );

        order = new HashMap<>(Map.of("apple", 13, "banana", 7, "orange", 12));
        warehouses = List.of(
                new Warehouse("owd", Map.of("apple", 2, "orange", 10, "banana", 3)),
                new Warehouse("dm", Map.of("banana", 3, "apple", 2)),
                new Warehouse("foo", Map.of("orange", 3, "apple", 8, "banana", 1)),
                new Warehouse("bash", Map.of("apple", 2, "banana", 20))
        );
        assertThat(
                allocator.produceCheapestShipment(order, warehouses),
                is(equalTo(List.of(
                        new Shipment("owd", Map.of("apple", 2, "orange", 10)),
                        new Shipment("dm", Map.of("apple", 2)),
                        new Shipment("foo", Map.of("orange", 2, "apple", 8)),
                        new Shipment("bash", Map.of("apple", 1, "banana", 7))
                )))
        );
    }
}
