import java.util.Locale;
import java.util.Scanner;

public class num1 {
    public static void main(String[] args) {

        Scanner sc=new Scanner (System.in).useLocale(Locale.ENGLISH);

        /*.- Numero natural: Solicita un número, si es menor que 0
        imprime que no es un número natural.


    .- Hora: Solicita una hora (hora,minutos,segundos) en una única línea, separada por espacios. 
        Si los datos son incorrectos, lanza un mensaje de error.



    .- Par: Solicita un número par, si el número introducido no es 
        un número par lanza un mensaje de error.



    .- Pasar a par: Solicita un número par, si el número introducido es impar súmale uno.



    .- Positivo: Solicita un número positivo, si el número introducido 
        no es un número positivo lanza un mensaje de error.
    */

        int numero = 0;
        int horas,minutos,segundos;
        int num1, num2;

        /*A la hora de ejecutar el código, añade dos números que pasarán como argumento del main.
        Gestiona que realemente introduce dos argumentos, ni más ni menos.
        Hay que imprimir por pantalla el número que sea mayor. 
        Gestiona para que, si el número de argumentos es incorrectos, los solicite desde teclado.*/

        if (args.length == 2) {
            
            num1 = Integer.parseInt(args[0]);
            num2 = Integer.parseInt(args[1]);
             
            if (num1 > num2)
                System.out.println("El número " + num1 + " es mayor que " + num2);
            else if (num1 < num2)
                System.out.println("El número " + num2 + " es mayor que " + num1);
            } else {
                System.out.println("Introduce 2 números separados por un espacio para saber cuál es el mayor: "
            );

            num1 = sc.nextInt();
            num2 = sc.nextInt();
          
         if (num1 > num2)
         System.out.println("El número " + num1 + " es mayor que " + num2);
         else if (num1 < num2)
         System.out.println("El número " + num2 + " es mayor que " + num1);
         else
         System.out.println("Los números son iguales. Son el: " + num1);
         }
        
        //EJERCICIO 1

        System.out.println("Introduce un numero: ");
        numero = sc.nextInt();

        if (numero < 0){
            System.out.println("No es un numero natural");
        }

        //EJERCICIO 2

        sc.nextLine();

        System.out.println("Introduce las horas: ");
        horas = sc.nextInt();

        System.out.println("Introduce los minutos: ");
        minutos = sc.nextInt();

        System.out.println("Introduce los segundos: ");
        segundos = sc.nextInt();


        if (horas > 60 || horas < 0){
            System.out.println("ERROR");
        }
        if(minutos > 60 || minutos < 0){
            System.out.println("ERROR");
        }
        if(segundos > 60 || segundos < 0){
            System.out.println("ERROR");
        }

        System.out.println("las horas son " + horas + " los minutos son " + minutos + " y los segundos son " + segundos);

        //EJERCICIO 3

        System.out.println("\nIntroduce un numero par: ");
        numero = sc.nextInt();

        if (numero % 2 != 0){
            System.out.println("ERROR");
        }

        //EJERCICIO 4

         System.out.println("\nIntroduce un numero par: ");
        numero = sc.nextInt();

        if (numero % 2 != 0){
            numero += 1; 
        }

        System.out.println("El numero es: " + numero);

        System.out.println("Introduce un numero: ");
        numero = sc.nextInt();

        if (numero < 0){
            System.out.println("ERROR");}

    }
}
