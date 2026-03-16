0. Safe list printing

Print first x elements of a list.

Skip missing elements silently using try / except IndexError.

Return the number of elements actually printed.

1. Safe printing of an integer

Print a single integer using "{:d}".format().

Return True if value is an integer, False otherwise.

Use try / except to handle non-integer inputs.

2. Print and count integers

Print only integers from the first x elements of a list.

Skip non-integer values silently.

Return the count of integers printed.

Handle IndexError if x is bigger than the list.

3. Safe division of two integers

Divide a / b.

Handle division by zero using try / except ZeroDivisionError.

Print the result always in finally with "Inside result: {}".format(result).

Return the division result or None if division fails.

4. Divide two lists element-wise

Divide elements of two lists up to list_length.

If invalid type → print "wrong type" and use 0.

If division by zero → print "division by 0" and use 0.

If index out of range → print "out of range" and use 0.

Return a new list with all division results.

5. Raise exception

Write a function that raises a TypeError.

6. Raise exception with message

Write a function that raises a NameError with a custom message.
