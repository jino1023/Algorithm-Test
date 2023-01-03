// 3003 Å·,Äý,·è,ºñ¼ó,³ªÀÌÆ®,Æù
import java.util.Scanner;
class Main {  
  public static void main(String args[]) { 
    Scanner in = new Scanner(System.in);

    int k = 1;
    int q = 1;
    int r = 2;
    int b = 2;
    int kn = 2;
    int p = 8;

    k = k - in.nextInt();
    q = q - in.nextInt();
    r = r - in.nextInt();
    b = b - in.nextInt();
    kn = kn - in.nextInt();
    p = p - in.nextInt();

    in.close();
    
    System.out.print(k+" ");
    System.out.print(q+" ");
    System.out.print(r+" ");
    System.out.print(b+" ");
    System.out.print(kn+" ");
    System.out.print(p);
  } 
}