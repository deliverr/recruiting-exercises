import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;


public class Solution {


    public ArrayList<Result> answer(HashMap<String, Integer>inputItems, ArrayList<Warehouse> warehouses) {

        ArrayList<Result> result = new ArrayList<>(); //store a list of results here

        HashMap<String, Integer> temp;
        temp = (HashMap<String, Integer>) inputItems.clone(); //make a copy of the input items list

        for (Warehouse i: warehouses) { //loop of list of warehouse

            boolean itemExist = false; //check if any items we need exists in this warehouse
            String currentName = i.getName(); //name of the current warehouse

            HashMap<String, Integer> currentList = new HashMap<>(); //store how items we can get from this warehouse

            for (Map.Entry<String, Integer> element: i.getInventory().entrySet()) { //loop through each items in the inventory

                //current item in the inventory
                String itemName = element.getKey();
                Integer itemCount = element.getValue();


                if (temp.containsKey(itemName) && itemCount > 0) {

                    itemExist = true;
                    Integer inputItemRemain = temp.get(itemName); // how many left for the item in the input
                    Integer currentTake = Math.min(itemCount, inputItemRemain); //determine how much we take here
                    currentList.put(itemName, currentTake); //put it in the current list so we can add it into the result

                    if(inputItemRemain == currentTake){
                        temp.remove(itemName); // if no more left, remove it from the inputItems
                    } else {
                        temp.put(itemName, (inputItemRemain - currentTake)); // else update how much is left
                    }

                }
            }
            if (itemExist) {  //only add result if there is something we need in this warehouse

                Result currentResult = new Result(currentName, currentList);
                result.add(currentResult);

            }

            if (temp.isEmpty()) { //if there's nothing left already, no need to search from other warehouses, just return result
                return result;
            }

        }


        return new ArrayList<>(); //means not enough inventory to empty the input list, return empty list

    }
}
