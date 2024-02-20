interface Person
{
    public void id();
    public void name();
}
class Student implements Person
{
   public void id()
    {
        System.out.print("1\n");
        
    }
 public void name()
  {
      System.out.print("aswin "); 
}
public static void main(String args[])
{
    Person o=new Student();
    o.id();
    o.name();
}}
