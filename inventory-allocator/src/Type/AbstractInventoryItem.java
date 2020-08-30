package Type;

/**
 * Abstract class used to declare/implement InventoryItems class
 * @author Arundathi Patil
 *
 */
public abstract class AbstractInventoryItem {
	private int id;
	private AbstractItem item;
	private int quantity;
	
	/**
	 * method that returns item ID
	 * @return id
	 */
	public int getId() {
		return id;
	}
	
	/**
	 * method that sets item ID
	 * @return id
	 */
	public void setId(int id) {
		this.id = id;
	}
	
	/**
	 * method that returns item
	 * @return id
	 */
	public AbstractItem getItem() {
		return item;
	}
	
	/**
	 * method that sets item
	 * @return id
	 */
	public void setItem(AbstractItem item) {
		this.item = item;
	}
	
	/**
	 * method that returns item quantity
	 * @return id
	 */
	public int getQuantity() {
		return quantity;
	}
	
	/**
	 * method that sets item quantity
	 * @return id
	 */
	public void setQuantity(int quantity) {
		this.quantity = quantity;
	}
	
	

}
