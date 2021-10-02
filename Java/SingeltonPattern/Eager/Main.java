package SingeltonPattern.Eager;

public class Main {

    public static void main(String[] args) {
        var order1=OrderService.getInstance();

        var order2= OrderService.getInstance();

        System.out.println(order1==order2);
        order1.placeOrder();
    }
}
