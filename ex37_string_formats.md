String and Unicode objects have one unique built-in operation: the `%` operator (modulo). This is also known as the string formatting or interpolation operator. Given `format % values` (where format is a string or Unicode object), `%` conversion specifications in format are replaced with zero or more elements of values.[1]

String Format | What it does
--- | ---
%d | Signed integer decimal.
%i | Signed integer decimal.
%o | Signed octal value.
%u | Obsolete type - it is identical to 'd'.
%x | Signed hexadecimal (lowercase).
%X | Signed hexadecimal (uppercase).
%e | Floating point exponential format (lowercase).
%E | Floating point exponential format (uppercase).
%f | Floating point decimal format.
%F | Floating point decimal format.
%g | Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.
%G | Floating point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.
%c | Single character (accepts integer or single character string).
%r | String (converts any Python object using `repr()`).
%s | String (converts any Python object using `str()`).
%% | No argument is converted, results in a '%' character in the result.

repr()

> Return a string containing a printable representation of an object. This is the same value yielded by conversions (reverse quotes). It is sometimes useful to be able to access this operation as an ordinary function. For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to `eval()`, otherwise the representation is a string enclosed in angle brackets that contains the name of the type of the object together with additional information often including the name and address of the object. A class can control what this function returns for its instances by defining a `__repr__()` method.[2]

str()

> Return a string containing a nicely printable representation of an object. For strings, this returns the string itself. The difference with `repr(object)` is that `str(object)` does not always attempt to return a string that is acceptable to `eval()`; its goal is to return a printable string. If no argument is given, returns the empty string, ''.[3]

[1]: https://docs.python.org/2/library/stdtypes.html#string-formatting "String Formatting Operations"
[2]: https://docs.python.org/2/library/functions.html#func-repr "repr(object)"
[3]: https://docs.python.org/2/library/functions.html#str 'class str(object=")'
