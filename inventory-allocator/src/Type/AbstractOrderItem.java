package Type;

/**
 * Abstract class used to declare/implement OrderItem class
 * @author Arundathi Patil
 *
 */
public abstract class AbstractOrderItem {
	private AbstractItem item;
	private int quantity;
	
	public AbstractItem getItem() {
		return item;
	}
	public void setItem(AbstractItem item) {
		this.item = item;
	}
	public int getQuantity() {
		return quantity;
	}
	public void setQuantity(int quantity) {
		this.quantity = quantity;
	}
	
	

}
