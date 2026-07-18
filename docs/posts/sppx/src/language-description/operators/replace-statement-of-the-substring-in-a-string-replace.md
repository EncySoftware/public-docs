# The replace statement of the substring in a string REPLACE



The statement is looking for the substring in a string and replace to the required.

**Format**

```
REPLACE (<string variable>, <looked string>, <string for replace>)
```

**Description**

This operator is looking for the **looked string** from the start of **string variable**. If **looked string** is found then it is replaced on the **string for replace** and the search is break. if the **looked string** is not found then replacement don't take the place.

**Example**

```
! Filling the source variable:
S$ = "GXX"
! Search and replace "XX" on "21":
REPLACE(S$, "XX", "21")
! The variable S$ has the "G21" value.
```
