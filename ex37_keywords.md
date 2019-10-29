Keywords | What it does
--- | ---
and | Boolean operator, this is a short-circuit operator, so it only evaluates the second argument if the first one is ture.[1]
del | This is used to delete the reference to an object. This is also used to delete items from a list or a dictionary.[2]
from | Generally used with import, this is used to import particular functionality from the module imported.[3]
not | Boolean operator, has a lower priority than non-Boolean operators.[1] It yields `True` if its argument is false, `False` otherwise.[4] 
while | This is used for looping in Python. The statements inside a `while` loop continue to execute until the condition for the `while` loop evaluates to `False` or a `break` statement is encountered.[2]
as | This is used to create an alias while importing a module. It means giving a different name (user-defined) to a module while importing it.[2]
elif | This is used for conditional branching or decision making. `elif` is short for else if.[2]
global | This is a declaration which holds for the entire current code block. It means that the listed identifiers are to be interpreted as globals. It would be impossible to assign to a global variable without `global`, although free variables may refer to globals without being declared global.[5]
or | Boolean operator, connect two Boolean expressions into one compound expression. At least one subexpressions must be true for the compound expression to be considered true, and it doesn’t matter which. If both subexpressions are false, then the expression is false.[6]
with | `with` statement is used to wrap the execution of a block of code within methods defined by the context manager. Context manager is a class that implements `__enter__` and `__exit__` methods. Use of `with` statement ensures that the `__exit__` method is called at the end of the nested block. This concept is similar to the use of `try ... finally` block.[2]
assert | Assert statements are a convenient way to insert debugging assertions into a program.[7]
else | `if`, `else`, `elif` are used for conditional branching or decision making.[2]
if | The `if` statement is used for conditional execution. It selects exactly one of the suites by evaluating the expressions one by one until one is found to be true; then that suite is executed (and no other part of the if statement is executed or evaluated). If all expressions are false, the suite of the `else` clause, if present, is executed.[8]
pass | `pass` is a null operation - when it is executed, nothing happens. It is useful as a placeholder when a statement is required syntactically, but no code needs to be executed.[9]
yield | `yield` is used inside a function like a `return` statement. But `yield` returns a generator.[2]
break | `break` and `continue` are used inside `for` and `while` loops to alter their normal behavior. `break` will end the smallest loop it is in and control flows to the statement immediately below the loop.[2]
except | Exception handlers are specified with the `try ... except` statement. Exceptions are identified by class instances. The `except` clause is selected depending on the class of the instance: it must reference the class of the instance or a base class thereof. The instance can be received by the handler and can carry additional information about the exceptional condition. Exceptions can also be identified by strings, in which case the `except` clause is selected by object identity. An arbitrary value can be raised along with the identifying string which can be passed to the handler.[10]
import | Import statements are executed in two steps: (1) find a module, and initialize it if necessary; (2) define a name or names in the local namespace (of the scope where the `import` statement occurs). The statement comes in two forms differing on whether it uses the `from` keyword. The first form (without `from`) repeats these steps for each identifier in the list. The form with `from` performs step (1) once, and then performs step (2) repeatedly.[11]
print | `print` evaluates each expression in turn and write the resulting object to standard output. If an object is not a string, it is first converted to a string using the rules of string conversions. The (resulting or original) string is then written. A `` `\n` `` character is written at the end, unless the `print` statement ends with a comma. This is the only action if the statement contains just the keyword `print`[12]
class | A class definition defines a class object. A class definition is an executable statement. It first evaluates the inheritance list, if present. Each item in the inheritance list should evaluate to a class object or class type which allows subclassing. The class's suite is then executed in a new execution frame, using a newly created local namespace and the orginal global namespace. (Usually, the suite contains only function definitions.) When the class's suite finishes execution, its execution frame is discarded but its local namespace is saved. A class object is then created using the inheriatance list for the base classes and the saved local namespace for the attribute dictionary. The class name is bound to this class object in the original local namespace.[13]
exec | This statement supports dynamic execution of Python code.[14]
in | The operators `in` and `not in` test for membership. `x in s` evaluates to `True` if x is a member of s, and `False` otherwise. `x not in s` returns the negation of `x in s`. All built-in sequences and set types support this as well as dictionary, for which `in` tests whether the dictionary has a given key. For container types such as list, tuple, set, frozenset, dict, or collections.deque, the expression `x in y` is equivalent to `any(x is e or x == e for e in y)`.[15] The secondary use of `in` is to traverse through a sequence in a `for` loop.[2	]
raise | The Python interpreter raises an exception when it detects a run-time error. A Python program can also explicitly raise an exception with the `raise` statement.[10]
continue | `break` and `continue` are used inside `for` and `while` loops to alter their normal behavior. `continue` causes to end the current iteration of the loop, but not the whole loop.[2]
finally | The `finally` clause of such a statement can be used to specify cleanup code which does not handle the exception, but is executed whether an exception occurred or not in the preceding code.[10]
is | The operators `is` and `is not` test for object identity: `x is y` is true if and only if x and y are the same object. `x is not y` yields the inverse truth value.[16]
return | `return` may only occur syntactically nested in a function definition, not within a nested class definition.[17]
def | `def` is used to define a user-defined function.[2]
for | The `for` statement is used to iterate over the elemetns of a sequence (such as a string, tuple or list) or other iterable object.[18]
lambda | Lambda expressions (sometimes called lambda forms) have the same syntactic position as expressions. They are a shorthand to create anonymous functions; the expression `lambda parameters: expression` yields a function object.[19]
try | The `try` statement specifies exception handlers and/or cleanup code for a group of statements.[20]

[1]: https://docs.python.org/2/library/stdtypes.html#boolean-operations-and-or-not "Boolean Operations — and, or, not"
[2]: https://www.programiz.com/python-programming/keyword-list "List of Keywords in Python"
[3]: https://www.geeksforgeeks.org/keywords-python-set-2/ "Keywords in Python | Set 2"
[4]: https://docs.python.org/2/reference/expressions.html#boolean-operations "Boolean operations"
[5]: https://docs.python.org/2/reference/simple_stmts.html#the-global-statement "The global statement"
[6]: https://realpython.com/python-or-operator/ "How to Use the Python or Operator"
[7]: https://docs.python.org/2/reference/simple_stmts.html#the-assert-statement "The assert statement"
[8]: https://docs.python.org/2/reference/compound_stmts.html#the-if-statement "The if statement"
[9]: https://docs.python.org/2/reference/simple_stmts.html#the-pass-statement "The pass statement"
[10]: https://docs.python.org/2/reference/executionmodel.html#exceptions "Exceptions"
[11]: https://docs.python.org/2/reference/simple_stmts.html#the-import-statement "The import statement"
[12]: https://docs.python.org/2/reference/simple_stmts.html#the-print-statement "The print statement"
[13]: https://docs.python.org/2/reference/compound_stmts.html#class-definitions "Class definitions"
[14]: https://docs.python.org/2/reference/simple_stmts.html#the-exec-statement "The exec statement"
[15]: https://docs.python.org/2/reference/expressions.html#in "Membership test operations"
[16]: https://docs.python.org/2/reference/expressions.html#is "Identity comparisons"
[17]: https://docs.python.org/2/reference/simple_stmts.html#the-return-statement "The return statement"
[18]: https://docs.python.org/2/reference/compound_stmts.html#the-for-statement "The for statement"
[19]: https://docs.python.org/2/reference/expressions.html#lambda "Lambdas"
[20]: https://docs.python.org/2/reference/compound_stmts.html#try "The try statement"
