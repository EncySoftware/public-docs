# Deferred masks

Sometimes it is necessary to use the current parameters of the current command when other command is processed. There are two ways to solve this task. The first way is to save the parameters to the temporary variables and use it later in the required command. The second best way is the using of the deferred masks. The current parameters of these masks are saved and the mask execution is deferred to the required program execution. When the deferred mask is executed, the current parameters are replaced by the saved parameters.

The deferred mask must be in the braces `{` and `}`. Inside the braces necessarily to define one of the CLDATA commands. The mask is executed when this command appears. The lines before this command executed before command execution and the lines placed after the defined command are executed after the command execution. For example:

- Mask of command [SafPos](../../../cldata/commands/safpos.md):

```
{
G_INTERP[0] X[XT] Y[YT] Z[CLD.Z]
G_FUNC[28] X[CLD.X] Y[CLD.Y]
LoadTL
G_INTERP[1] G_FUNC[29] G_LENGTHCOMPENS[43] X[XT] Y[YT]
G_LENGTHCOMPENS[49] Z[ZT]
}
```

- Mask of command [LoadTL](../../../cldata/commands/loadtl.md):

```
H[CLD.N] T[CLD.N]
```

- Mask of command [AbsMov](../../../cldata/commands/goto.md):

```
X[CLD.X] Y[CLD.Y] Z[CLD.Z]
```

- CLData commands:

```
GOTO.abs X 20.0000,Y 20.0000,Z 20.0000
SAFPOS X 10.0000,Y 11.0000,Z 12.0000,N 0
LOADTL N 1,X 0.0000,Y 0.0000,Z 0.0000,D 1.0000,M 0,K 0,L 0.0000,
P 0.0000,A 0.0000,R 0.0000,PLANE XY(33),Dur 0.0000
```

- NC code:

```
X20.0000 Y20.0000 Z20.0000
G0 Z0.0000
G28 X0.0000 Y0.0000
H1 T1
G1 G29 G43 X20.0000 Y20.0000
G49 Z20.0000
```

In this case, when the [SafPos](../../../cldata/commands/safpos.md) command is executed then the deferred mask is created. The values of `CLD.X`, `CLD.Y`, `CLD.Z` of [SafPos](../../../cldata/commands/safpos.md) command are saved and the mask execution is deferred to the [LoadTL](../../../cldata/commands/loadtl.md) processing. Values of [XT](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [YT](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md), [ZT](../../language-description/basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md) is not saved because it is not the CLData command parameters. Before the [LoadTL](../../../cldata/commands/loadtl.md) processing the mask below is executed:

```
G_INTERP[0] X[XT] Y[YT] Z[CLD.Z]
G_FUNC[28] X[CLD.X] Y[CLD.Y]
```

After that, executed:

```
LoadTL: H[CLD.N] T[CLD.N]
```

Finally executed:

```
G_INTERP[1] G_FUNC[29] G_LENGTHCOMPENS[43] X[XT] Y[YT]
G_LENGTHCOMPENS[49] Z[ZT]
```

If write the **Keep** identifier before the right brace then deferred mask will be always performed then the required program is executed (It is [LoadTL](../../../cldata/commands/loadtl.md) in the previous sample). For example:

- Mask of command [SafPos](../../../cldata/commands/safpos.md):

```
{
G_INTERP[0] X[XT] Y[YT] Z[CLD.Z]
G_FUNC[28] X[CLD.X] Y[CLD.Y]
LoadTL
G_INTERP[1] G_FUNC[29] G_LENGTHCOMPENS[43] X[XT] Y[YT]
G_LENGTHCOMPENS[49] Z[ZT]
Keep
}
```

In this sample, the execution of the deferred mask will be performed every time when the [LoadTL](../../../cldata/commands/loadtl.md) is processed.

**See also**

[Mask structure](readme-mask-structure.md)
