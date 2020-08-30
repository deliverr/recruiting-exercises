package Type;

import java.util.List;

/**
 * Abstract class used to declare/implement Order class
 * @author Arundathi Patil
 *
 */
public abstract class AbstractOrder {
	private int accountId;
	private List<AbstractOrderItem> orderItems;
	public int getAccountId() {
		return accountId;
	}
	public void setAccountId(int accountId) {
		this.accountId = accountId;
	}
	public List<AbstractOrderItem> getOrderItems() {
		return orderItems;
	}
	public void setOrderItems(List<AbstractOrderItem> orderItems) {
		this.orderItems = orderItems;
	}

	
}
