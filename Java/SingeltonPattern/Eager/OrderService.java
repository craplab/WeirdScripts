package SingeltonPattern.Eager;

public class OrderService {

    private static OrderService ob = new OrderService();

    private OrderService(){}

    public static OrderService getInstance(){
        return ob;
    }

    public void placeOrder() {
        System.out.println("Place order method is invoked");
    }
}
