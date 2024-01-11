import java.util.Locale;
import java.util.Scanner;

public class Ejbasicos5{
    public static void main(String[] args) {

        /*Solicita por teclado tres números. Si los dos primeros son mayores que el tercero, escribe "Mayores";
         si los dos son menores que el tercero, escribe "Menores"; para cualquier otro caso, escribe "¿Iguales?*/
        
        Scanner sc=new Scanner (System.in).useLocale(Locale.ENGLISH);

        int num1,num2,num3;

        System.out.println("Dime un numero: ");
        num1 = sc.nextInt();

        System.out.println("Dime otro numero: ");
        num2 = sc.nextInt();

        System.out.println("Dime otro numero: ");
        num3 = sc.nextInt();

        if(num1 > num3 && num2 > num3){
            System.out.println("Mayores");
        }
        else if(num1 < num3 && num2 < num3){
            System.out.println("Menores");
        }
        else{
            System.out.println("Iguales");
        }

    }
}