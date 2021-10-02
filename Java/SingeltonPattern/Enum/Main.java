package SingeltonPattern.Enum;

public class Main {

    public static void main(String[] args) {
        Order order = Order.INSTANCE;

        order.setValue(25);
        System.out.println(order.getValue());

        
    }
}
