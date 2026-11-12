# Statement of direct output into the block OUTPUT

This operator outputs the content of a string variable by separate block of NC-program.

**Format**

```
OUTPUT {<FileName$>}, S$
```

**Description**

`S$` – the identifier of a string variable. The literal constant or string expression may be the parameter of this operator.

Use optional `FileName$` parameter to specify the file where the system outputs the NC-block. If the parameter is omitted then the NC-block is output into the current file. If "*" is specified as a file name then the NC-block would be output into the main file, also the current file will be changed. If `FileName$` specifies the name of a file then corresponding tab will be created and the current file would be changed accordingly.

**Examples**

```
! The output of the first symbol into NC-code
OutPut "%"
Name$ = " John "
F$ = "Lord"
! The output of string into NC-program
OutPut "Programmer "+Name$+" "+F$
! The string "Programmer John Lord" will be written into NC-program
! Sample of usage the FormBlock and Output usage instead of OutBlock
FormBlock
Output OutStr$
! Two these statements work as OutBlock
```

**See also**

[The block output statement **OUTBLOCK**](block-output-statement-outblock.md)

[The block forming statement **FORMBLOCK**](block-forming-statement-formblock.md)
