# Change current NC-file operator

**ChangeNCFile** changes the current output NC-file. Thus following NC-code output operators which do not specify NC-file will write NC-blocks into the current NC-file.

**Syntax**

```
ChangeNCFile NewNCFileName$
```

**Description**

`NewNCFileName$` – expression that evaluates into string result.

**Example**

```
! Changing current NC-file sample
ChangeNCFile "File1.nc" ! changing the current NC-file
Output "NC block" ! this line will be output into the "File1.nc" file
```

**See also**

[The block output statement **OUTBLOCK**](block-output-statement-outblock.md)

[Statement of direct output into the block **OUTPUT**](statement-of-direct-output-into-the-block-output.md)
