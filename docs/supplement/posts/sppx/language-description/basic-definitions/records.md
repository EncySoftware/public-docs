# Records

`Record` is a keyword used to describe variables - structures. The syntax for declaring a variable of type `Record` is:

```
RecVarName: Record
  RecFieldName1: Type1
  RecFieldName2: Type2
  .....
  RecFieldNameN: TypeN
End
```

**Where**

- RecVarName – name of variable;
- RecFieldName1...RecFieldNamen – variable field names;
- TypeX – record field type. It can be any simple type, record or static array of the above types.

**Example**

```
Rec1, Rec2: record
  X, Y, Z: real
  P: array [3,3] of integer;
  S1, S2: string
end
RR: array [10] of record
  X, Y, Z: real
end
Rec11: record
  field1: integer
  field2: array 10 of string
  field3: record
    nestedField1: real
    nestedField2: array 5 of integer
  end
end
```

## Using Records

Record fields are accessed by using the access operator: "."

In order to assign a value to the record field, you need to use the following expression:

```
<RecordName>.<FieldName1>{.<NestedFieldName2>...} = x
```

**Example**

```
Rec1.X = 1; Rec1.Y=2
Rec1.P[1,1] = 0
Rec1.S1 = "W100"
for i=1 to 10 do begin
   RR[i].X = i
   RR[i].Y = 0
   RR[i].Z = 50
end
rec3.field3.nestedField2[1]=33
```

You can use the value stored in the field as follows:

```
x = <RecordName>.<FieldName1>{.<NestedFieldName2>...}
```

**Example**

```
x1=Rec1.X; y1=Rec1.Y
z2=RR[2].Z
```
