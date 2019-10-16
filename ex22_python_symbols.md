Symbol | Name | What it does
--- | --- | ---
&nbsp; | Whitespace | Used as a word divider in scripts.[1]<br> Leading whitespace (spaces and tabs) at the beginning of a logical line is used to compute the indentation level of the line, which in turn is used to determine the grouping of statements.[2]
' | Single quote | String literals can be enclosed in matching single quotes. They can also be enclosed in matching groups of three single quotes (these are generally referred to as triple-quoted strings).[3]
" | Double quote | String literals can be enclosed in matching double quotes. They can also be enclosed in matching groups of three double quotes (these are generally referred to as triple-quoted strings).[3]
! | Exclamation mark | !=, not equal. This can also be written <>, but this is an obsolete usage kept for backwards compatibility only. New code should always use !=.[4]
. | Dot |
\# | Octothorpe, pound character, hash character | A comment starts with a hash character that is not part of a string literal, and ends at the end of the physical line.[5]
, | Comma |
: | Colon | Other languages use \{ \} or other method to indicate/use a code block. Python uses indentation after colons to indicate/use a code block.[6]
\+ | Plus | x + y, sum of x and y[7]<br>Python doesn't support ++[8]
\- | Minus | x - y,	difference of x and y[7]
\/ | Slash | x / y, quotient of x and y[7]
\* | Asterisk | x * y,	product of x and y[7]
% | Percent | The % does two things, depending on its arguments. It acts as the modulo operator, meaning when its arguments are numbers, it divides the first by the second and returns the remainder.If the first argument is a string, it formats it using the second argument.[9]
< | Less-than |
\> | Greater-than |
<= | Less-than-equal |
\>= | Greater-than-equal |
? | Question mark | It's not used in Python. Its occurrence outside string literals and comments is an unconditional error.[10]
= | Equal |
_ | Underscore | While the underscore is used for just snake-case variables and functions in most languages, but it has special meanings in Python.<br>There are 5 cases for using the underscore in Python:<br>1. For storing the value of last expression in interpreter.<br>2. For ignoring the specific values.<br>3. To give special meanings and functions to name of variables or functions.<br>4. To use as ‘Internationalization(i18n)’ or ‘Localization(l10n)’ functions.<br>5. To separate the digits of number literal value.[11]
( | Left parenthesis |
) | Right parenthesis |
\ | Backslash | The backslash character is used to escape characters that otherwise have a special meaning, such as newline, backslash itself, or the quote character.[3]
^ | Caret | x ^ y,	bitwise exclusive or of x and y[12]

[1]: https://en.wikipedia.org/wiki/Whitespace_character "Whitespace character - Wiki"
[2]: https://docs.python.org/2/reference/lexical_analysis.html#indentation "Indentation"
[3]: https://docs.python.org/2/reference/lexical_analysis.html#string-literals "String literals"
[4]: https://docs.python.org/2/library/stdtypes.html#comparisons "Comparisons"
[5]: https://docs.python.org/2/reference/lexical_analysis.html#comments "Comments"
[6]: https://www.daniweb.com/programming/software-development/threads/430094/i-don-t-understand-colons-in-python "I don't understand colons in Python"
[7]: https://docs.python.org/2/library/stdtypes.html#numeric-types-int-float-long-complex "Numeric Types — int, float, long, complex"
[8]: https://stackoverflow.com/questions/2632677/python-integer-incrementing-with "Python integer incrementing with ++"
[9]: https://stackoverflow.com/questions/961344/what-does-the-percentage-sign-mean-in-python "What does the percentage sign mean in Python"
[10]: https://docs.python.org/2/reference/lexical_analysis.html#delimiters "Delimiters"
[11]: https://hackernoon.com/understanding-the-underscore-of-python-309d1a029edc "Understanding the underscore(_) of Python"
[12]: https://docs.python.org/2/library/stdtypes.html#bitwise-operations-on-integer-types "Bitwise Operations on Integer Types"
