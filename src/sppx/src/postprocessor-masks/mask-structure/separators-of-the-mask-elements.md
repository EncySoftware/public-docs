# The separators of the mask elements

In general, the mask line consists of some elements. It is possible to insert the spaces between the elements. The spaces has not influence on the NC-program line.

To control the spaces between the words in the line it is possible to use the parameter **Spaces between commands**. If the parameter is checked then the spaces is added even if the separator is absent between the elements. For example:

- Mask:

```
" G[2] X[100.101]Y[234.89] Z[45.67]"
```

- NC code:

```
" G2 X100.101 Y243.890 Z045.670"
```

In the line, the space is added between the first and the second elements. The spaces quantity before the first between two and three, three and four is not changed.

If parameter **Spaces between commands** is off then all spaces between elements will be removed independently of it is quantity. For example:

- Mask:

```
G_INTERP[INTERP] X[CLD.X] Y[CLD.Y] Z[CLD.Z]
```

- NC code:

```
G1X-49.47Y-6.513Z.033
```

All spaces is removed from the NC-program line.

**See also**

[Mask structure](readme-mask-structure.md)
