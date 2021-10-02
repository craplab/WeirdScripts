package SingeltonPattern.Lazy;

// locking of Singleton. Intention is to reduce cost
public class DoubleCheckedLocked {

    private static DoubleCheckedLocked ob;

    private DoubleCheckedLocked (){}

    public static DoubleCheckedLocked getInstance(){
        //first check
        if(ob==null){

            //Double check
            // locking critical section of code, the code which
            synchronized (DoubleCheckedLocked.class){
                if(ob==null){
                    ob = new DoubleCheckedLocked();
                }
            }

        }

        return ob;
    }
}
