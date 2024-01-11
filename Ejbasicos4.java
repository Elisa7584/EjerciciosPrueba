import java.util.Locale;
import java.util.Scanner;

public class Ejbasicos4 {
    public static void main(String[] args) {
        /*Solicita por teclado un día de la semana y un número. Si el número coincide con su día de la semana o el día introducido es viernes escribe "¡Has ganado!*/

        Scanner sc=new Scanner (System.in).useLocale(Locale.ENGLISH);

        int numero,diaSemana;

        System.out.println("Dime un dia de la semana: ");
        diaSemana = sc.nextInt();

        System.out.println("Introduce un número: ");
        numero = sc.nextInt();

        if(diaSemana == numero || diaSemana == 7){
                System.out.println("¡Has ganado!");
        }
        else{
            System.out.println("Has perdido...");
        }
    }
}
