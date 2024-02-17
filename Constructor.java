public class Main
{
int salary;
Main()
{
salary=30000;
}
public static void main(String args[])
{
Main obj=new Main();
if(obj.salary<20000)
{
System.out.print("eligible for scholarship");
}
else
{
System.out.print("you are not eligible ");
}
}
}
