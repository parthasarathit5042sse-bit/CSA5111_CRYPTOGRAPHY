import java.util.*;
public class first{
    static void encrypted(String text,int key){
        String result="";
        for(char ch:text.toCharArray()){
            // if(Character.isUpperCase(ch)){
            if(ch>='A'&&ch<='Z'){

            ch=(char)((ch-'A'+key)%26+'A');
        }
        // else if(Character.isLowerCase(ch)){
        if(ch>='a'&&ch<='z'){
            ch=(char)((ch-'a'+key)%26+'a');
        }
        result=result+ch;
        }
        System.out.print("Encrypted: "+result);

    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the Text: ");
        String text=sc.nextLine();
        System.out.println();
        System.out.print("Enter the key: ");
        int key=sc.nextInt();
        System.out.println();
       encrypted(text,key);
    }
}