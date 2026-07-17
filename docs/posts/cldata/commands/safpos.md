# SAFPOS - Tool change point

> **Deprecated.** This command is obsolete - the current version of the CAM system does not generate it automatically. It is documented here for postprocessors that still handle legacy CLData.

## Command caption

How the command appears in the CLData command list:

```text
SAFPOS X x, Y y, Z z, N n
```

**SAFPOS** command defines the coordinates of the point, where the tool center will be positioned for the change of tool ([LOADTL](loadtl.md) command), are defined. Tool change make in the current point as default.

## Access from sppx

Handler: `program SafPos`

| Parameter | CLD array | CLD name | Description |
|---|---|---|---|
| x<br>y<br>z | CLD[1]<br>CLD[2]<br>CLD[3] | CLD.X<br>CLD.Y<br>CLD.Z | Coordinates of point of tool change |
| N | CLD[4] | CLD.N | The number of point of tool change in the NC-machine |

## See also
- [CLData access model](../cldata.md)
