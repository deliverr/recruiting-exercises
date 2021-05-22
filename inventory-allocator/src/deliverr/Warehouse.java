package deliverr;

import java.util.Map;

public class Warehouse {

    String name;
    Map<String, Integer> inventoryDistribution;

    public Warehouse(String name, Map<String, Integer> inventoryDistribution) {
        this.name = name;
        this.inventoryDistribution = inventoryDistribution;
    }

    public String getName() {
        return name;
    }


}