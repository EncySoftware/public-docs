# String functions

The following string functions are implemented:

- `CHR(x)` – returns the character for a specified ASCII value **x**.
- `ORD(Str)` – returns the ordinal value of the first character of the string **Str**.
- `LEN(Str)` – returns the length of the string **Str** (the number of characters in the string).
- `POS(Pat, Str)` – returns the index of the first occurrence of the string **Pat** in the **Str** string. Returns 0 if the **Pat** string is not found in the **Str** string.
- `NUM(Str)` – converts a string **Str** to a numeric representation; If the string is invalid, the function returns 0.
- `STR(n)` – converts number **n** into a string representation.
- `COPY(Str, n, m)` – returns a substring of **Str** containing **m** characters and starting at index **n**.
- `UPCASE(Str)` – returns a copy of the string **Str** in upper case.

- `REPLACE(<string variable>, <looked string>, <string for replace>)` [The replace statement of the substring in a string **REPLACE**](../../operators/replace-statement-of-the-substring-in-a-string-replace.md).

**Where**

- **Str**, **Pat** – expressions that evaluate into a string value (variables, literal constants, functions or expressions);
- **n**, **m** – numeric values.

**See also**

[Predefined variables and functions](readme-predefined-variables-and-functions.md)

[The replace statement of the substring in a string **REPLACE**](../../operators/replace-statement-of-the-substring-in-a-string-replace.md)
