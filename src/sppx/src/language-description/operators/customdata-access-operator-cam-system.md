# CustomData access operator CAM system

Use **CustomData** operator to access CustomData of a CAM system project.

**Syntax**

```
S$ = CustomData(ItemName$)
```

**Description**

`ItemName$` – expression that evaluates to string.

CustomData operator returns the value of custom data item named ItemName$ set by the user in the CAM system project.

**Example**

```
! Output user data into NC-program:
Output CustomData("UserData")
```
