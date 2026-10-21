# Arrays

An array represents an indexed collection of elements of the same type. The array is characterized by its name, the type of stored items, the size (number of stored items) and the numbering of elements. An array can be viewed as a table:

| Array item index | Array item value |
|---|---|
| 1 | Value1 |
| 2 | Value2 |
| ... | ... |
| N | ValueN |

In the table above N – an array size (number of items in the array). There is no limitation to the maximum array size, although using exceptionally large arrays is not recommended. All arrays are indexed from 1 up to array size.

Postprocessor language supports both one-dimensional and two-dimensional arrays. Array items can be of any simple type: ([Integer](variables.md)), ([Real](variables.md)), ([String](variables.md)) or ([Record](records.md)).

Arrays can be used anywhere where simple variables of the same base type are legal. To access array item you need to specify array name and item index, index can be any numeric expression that doesn't violate the range bounds:

```
<ArrayIdentifier>[<ItemIndex>, {<ItemIndex>}]
```

To define an array variable use the following syntax:

**Array variable name**: array **Array size** of **Array base type**

**Where**

- **Array variable name** – any legal [identifier](set-of-symbols.md);
- **Array size** – positive integer number;
- **Array base type** – one of simple types ([Integer](variables.md), [Real](variables.md) or [String](variables.md)).

To define two-dimensional array use next syntax:

**Array variable name**: array [**First array size**, **Second array size**] of **Array base type**

**Example**

```
V: array 10 of Real ! Definition of an array of 10 real items
V[5] = 10.67 ! Assigning value to the fifth array item
i = 7
! Using array in expressions
i = 7
V[10] = 15*sqr((sin(V[i]))^2 + (cos(V[i+1]))^2)
```

```
V: array [3, 3] of Real ! Definition of two-dimensional array

for i = 1 to 3 do for j = 1 to 3 do V[i, j] = i*10+j
```

An array with hardcoded number of elements is called a static array. An array whose size can change along the course of program execution is called dynamic array. To define a dynamic array omit the array size in the array definition. Dynamic arrays are indexed from 1. The size of dynamic array is set to the maximum item index that was accessed.

The following is an example of string array definition and usage.

**Example**

```
ArrayS: array of string ! Array definition
! Fill array items
ArrayS[1] = "Hello," ! There is no need to specify
ArrayS[2] = " World" ! the number of items
ArrayS[3] = "!" ! the memory is allocated automatically
! Array use
output ArrayS[1] + ArrayS[2] + ArrayS[3]
```
