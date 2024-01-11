import java.util.Locale;
import java.util.Scanner;

public class Ejbasicos3 {
    public static void main(String[] args) {

        /*Solicita por teclado dos numeros. Escribe "Has ganado" si el segundo número menos el primero da un valor positivo*/

        Scanner sc = new Scanner (System.in).useLocale(Locale.ENGLISH);
        
        int num1,num2,resultado;

        System.out.println("Dime un numero: ");
        num1 = sc.nextInt();

        System.out.println("Dime otro numero: ");
        num2 = sc.nextInt();

        resultado = num2 - num1;

        if(resultado > 0){
            System.out.println("Has ganado");
        }
        else{
            System.out.println("Has perdido");
        }


    }
}
