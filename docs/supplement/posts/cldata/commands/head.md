# HEAD - Spindle head number

> **Deprecated.** This command is obsolete - the current version of the CAM system does not generate it automatically. It is documented here for postprocessors that still handle legacy CLData.

## Command caption

How the command appears in the CLData command list:

```text
HEAD BOTH(83)|N n
```

Use **HEAD** command to select active spindle head. The head number is passed as parameter.

## Access from sppx

Handler: `program Head`

| Parameter | CLD array | CLD name | Description |
|---|---|---|---|
| BOTH(83) n | CLD[1] | CLD.N | 83 (BOTH) – simultaneous operation of both heads, n – head number. |

## See also
- [CLData access model](../cldata.md)
