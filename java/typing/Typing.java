class A {
	public String foo(){
		return "A";
	}
}

class B extends A{
	public String foo(){
		return "B";
	}
}

public class Typing {
	public static void main(String args[]) {
		A a = new A();
		B b = new B();
		A c = new B(); 

		System.out.println(a.foo());
		System.out.println(b.foo());
		System.out.println(c.foo());
	}
}
