# The variables

Variable – a named memory location used to refer data at that location. In other words, variable - the name, which may be due to a certain value.

Variables can have different types. The type of a variable defines the set of values that can be stored in the variable and the set of operations that can be performed on that variable. Variables in the Postprocessors generator can be one of the following types:

- **Integer** (integer number) – use Integer to represent an integer number. The Integer variable value range from -2147483648 to 2147483647.
- **Real** (real number) – use Real to store numbers with fractional values. The range of values that can be represented by the Real type variable is: 5.0*10^-324 .. 1.7*10^308. The Real type has 15-16 significant digits.
- **String** (character strings) – use String to store a sequence of up to ~2^31 characters.
- [Array](arrays.md) (arrays or vectors) – a complex type that represents a sequence of items of simple type values.

Variables can be local scope or global. Local scope variables are accessible only in the current program or subprogram. Global variables can be accessed in any program or sub of the postprocessor. To define a global variable define it in the special [COMMON](technology-command-programs-comments.md) program. All variables defined in the [COMMON](technology-command-programs-comments.md) program are global. It is allowed to declare several variables of the same type in one line.

The Postprocessor generator language allows definition of variables anywhere in the code of a program or a subprogram, but it is a good practice to define the variables used in the program at the program head. Use the following syntax to define a variable:

`Variable name 1`, {`Variable name 2`}: **Type of the variable**

Here:

- **Variable name** – a unique in the current scope identifier of the variable – an identifier must begin with an alphabetic character or an underscore (_) and cannot contain spaces; alphanumeric characters, digits, underscores, and symbols `@` and `$` are allowed after the first character. The identifiers are case insensitive. Reserved words, operator names, technology command program names and subprogram names cannot be used as identifiers.
- **Type of the variable** – one of the types: **Integer**, **Real**, **String**, [Array](arrays.md).

The following is an example of variable definition and usage.

**Example**

```
sub Sub1
  nn: Integer ! Integer type variable definition
  xx, yy, zz: Real ! Real type variables definition
  ss: String ! String type variable definition
  nn = 2 ! Variable value assignment
  xx = 7.43 ! Variable value assignment
  yy = 12.6 ! Variable value assignment
  rr = nn * sqr(xx^2 + yy^2) ! variables in expression
  ss = "Result = " ! Variable assignment
  print ss, rr ! debug output value of the variable
subend
```
