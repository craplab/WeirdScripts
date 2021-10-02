package SingeltonPattern.Lazy;

public class OrderService {

    private static OrderService ob;

    private OrderService(){}

    //Synchronized keyword used for thread safe
    //This is not very much efficient
    public static synchronized OrderService getInstance(){
        if(ob==null){
           ob= new OrderService();
        }

        return ob;
    }



    public void placeOrder() {
        System.out.println("Place order method is invoked");
    }
}
