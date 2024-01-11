import java.util.Locale;
import java.util.Scanner;

public class EjerciciosBasicos {
    public static void main(String[] args) {

        Scanner sc=new Scanner (System.in).useLocale(Locale.ENGLISH);
        
        int num1,num2,resultado;
        String palabra;

        System.out.println("Dime un numero: ");
        num1 = sc.nextInt();

        System.out.println("Dime otro numero: ");
        num2 = sc.nextInt();

        sc.nextLine();

        System.out.println("Introduce la palabra: suma o resta ");
        palabra = sc.nextLine();


        if(palabra.equals("suma")){
            resultado = num1 + num2;
            System.out.println("El resultado de la suma de " + num1 + " y de " + num2 + " es: " + resultado);
        }
        else if (palabra.equals("resta")){
            resultado = num1 - num2;
            System.out.println("El resultado de la resta de " + num1 + " y de " + num2 + " es: " + resultado);
        }
    }
}
