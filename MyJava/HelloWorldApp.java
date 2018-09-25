/**
 * The HelloWorldApp class implements an application that
 * simply prints "Hello World!" to standard output.
 * 
 */
class HelloWorldApp {


// This is the first method that Java calls when it
// starts the application. This method is public, so
// every other class can see the method. The method is
// static, so it isn't used as part of an object, but
// rather, called directly. The result is void, so this
// method doesn't return any data to the caller. The
// only argument, args, is a list of strings.

    public static void main(String[] args) {
        System.out.println("Hello World!"); // Display the string.
    }
}