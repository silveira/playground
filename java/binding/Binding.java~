class A {
	public String foo(){
		return "A.foo";
	}

	public static String bar(){
		return "A.bar";
	}
}

class B extends A{
	public String foo(){
		return "B.foo";
	}
	
	public static String bar(){
		return "B.bar";
	}
}

public class Binding {
	public static void main(String args[]) {
		A a = new A();
		B b = new B();
		A c = new B(); 

		System.out.println("Dynamic Binding / Late Binding");
		System.out.println(a.foo()); // A.foo
		System.out.println(b.foo()); // B.foo
		System.out.println(c.foo()); // B.foo

		System.out.println("\nStatic Binding");
		System.out.println(a.bar()); // A.bar
		System.out.println(b.bar()); // B.bar
		System.out.println(c.bar()); // A.bar
	}
}
