import java.util.Locale;
import java.util.Scanner;

public class EjerciciosSwitch {
    public static void main(String[] args) {
        /*Solicita por teclado dos números y la palabra operación 
            (suma, resta, multiplicación, división).
                El programa debe realizar la operación correspondiente.
                    Modifícalo para que pueda funcionar tanto los datos 
                        introducidos por teclado como introduciendole 
                            argumentos al main.*/

        Scanner sc=new Scanner (System.in).useLocale(Locale.ENGLISH);

        
        int num1,num2;
        String operacion;

        if (args.length < 2){

            System.out.println("Introduce dos numeros: ");
            num1 = sc.nextInt();
            num2 = sc.nextInt();
        }else{
            num1 = Integer.parseInt(args[0]);
            num2 = Integer.parseInt(args[1]);
        }

        System.out.println("Introduce dos numeros: ");
        num1 = sc.nextInt();
        num2 = sc.nextInt();

        sc.nextLine();

        System.out.println("Introduce un operador: suma, resta, multiplicación o división");
        operacion = sc.nextLine();

        switch (operacion) {
            case "suma" -> System.out.println(num1 + num2);
            
            case "resta" -> System.out.println(num1 - num2);

            case "multiplicación" -> System.out.println(num1 * num2);

            case "división" -> System.out.println(num1 / num2);
        }

        }
}
