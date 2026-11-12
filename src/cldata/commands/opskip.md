# OPSKIP - Optional skipping

> **Deprecated.** This command is obsolete - the current version of the CAM system does not generate it automatically. It is documented here for postprocessors that still handle legacy CLData.

## Command caption

How the command appears in the CLData command list:

```text
OPSKIP ON(71) | OFF(72)
```

**OPSKIP** command activates and deactivates the mode of forming frames of NC-program with optional skip mark. Commonly the symbol `/` is used to mark lines for optional skipping. Marked frames are processed by the CNC-system only if frame skipping option is turned off, otherwise they are ignored.

## Access from sppx

Handler: `program OpSkip`

| Parameter | CLD array | CLD name | Description |
|---|---|---|---|
| ON(71)<br>OFF(72) | CLD[1] | CLD.onoff | 71 (ON) – Activation of optional skipping, 72 (OFF) – Deactivation of optional skipping. |

Example (from the Sinumerik (840D) TurnMill postprocessor):

```pascal
program OpSkip  
   print "Not marketed "
end
```

## See also
- [CLData access model](../cldata.md)
