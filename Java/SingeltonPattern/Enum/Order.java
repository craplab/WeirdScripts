package SingeltonPattern.Enum;

//This is the best way to implement sigelton pattern
//By default enum is thread safe and double check locking
public enum Order {
    INSTANCE;
    int value;

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}
