# PALETA - Palette changing

> **Deprecated.** This command is obsolete - the current version of the CAM system does not generate it automatically. It is documented here for postprocessors that still handle legacy CLData.

## Command caption

How the command appears in the CLData command list:

```text
PALETA N n
```

Use **PALETA** command to form NC-program frames that control palette change. The new palette number is passed as the command parameter.

## Access from sppx

Handler: `program Paleta`

| Parameter | CLD array | CLD name | Description |
|---|---|---|---|
| n | CLD[1] | CLD.N | Palette number |

## See also
- [CLData access model](../cldata.md)
