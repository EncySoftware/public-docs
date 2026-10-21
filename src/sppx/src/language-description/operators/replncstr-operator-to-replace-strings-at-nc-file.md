# ReplNCStr operator to replace strings at NC-file



ReplNCStr operator replaces all From$ strings to To$ strings in the File$ file (or in all files, if the File$ is not specified or it is an empty string "").

**Format**

```
ReplNCStr(<From$>, <To$>{, <File$>})
```

**Description**

`From$`, `To$`, `File$` – string expressions.

**Example**

```
! Replace all "placeholder" strings to "world!" in all NC-files
Output "hello, placeholder" ! NC-file: hello, placeholder
ReplNCStr("placeholder", "world!", "") ! NC-file: hello, world!
! Replace one string of NC-file on two strings:
! Hello -> Hello,
! World!
Output "Hello"
ReplNCStr("Hello", "Hello," + Chr(13) + Chr(10) + "World!")
```
