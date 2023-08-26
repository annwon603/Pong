public class even_odd{
    public static void test(int x){
        if(x%2==0){
            System.out.println(x+" is even");
        }
        else{
            System.out.println(x+" is odd");
        }
    }
    public static void main(String[] args) {
        test(2);
        test(40);
        test(3);
    }
}