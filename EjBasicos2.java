import java.util.Locale;
import java.util.Scanner;

public class EjBasicos2{
    public static void main(String[] args) {

       Scanner sc = new Scanner (System.in).useLocale(Locale.ENGLISH);
        
        int num1,num2;

        System.out.println("Dime un numero: ");
        num1 = sc.nextInt();

        System.out.println("Dime otro numero: ");
        num2 = sc.nextInt();

        if (num1 > num2){
            System.out.println("El primer numero es mayor");
        }
        else if (num1 < num2){
            System.out.println("El primer numero es menor");
        }

    }
}