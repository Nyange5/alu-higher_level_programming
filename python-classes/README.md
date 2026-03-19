Private attributes (__attr)

Protects internal state

Access via getter/setter for controlled read/write

Encapsulation

Getter/setter (@property) separates interface from implementation

Input validation

Always check types and values for critical attributes

Methods for functionality

area() → computation

my_print() → visualization

Default values and optional parameters

Makes classes flexible (size=0, position=(0,0))

Name mangling

Private attributes are internally renamed: __size → _Square__size

Explains why my_square.__size fails

Docstrings (optional but recommended)

Module/class/method docstrings describe purpose, aid help().

Progressive design

Start simple → add private attributes → validation → methods → additional attributes → formatted output
