import java.util.HashMap;

//Result object contains name of the warehouse and a dictionary of items they got from that warehouse
public class Result {

    private String name;
    private HashMap<String, Integer>Items;

    public Result(String name, HashMap<String, Integer>items) {

        this.name = name;
        this.Items = items;
    }

    public String getName() {
        return this.name;
    }

    public HashMap<String, Integer> getItemList() {
        return this.Items;
    }
}
