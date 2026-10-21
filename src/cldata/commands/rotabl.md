# ROTABL - Table rotation

> **Deprecated.** This command is obsolete - the current version of the CAM system does not generate it automatically. It is documented here for postprocessors that still handle legacy CLData.

## Command caption

How the command appears in the CLData command list:

```text
ROTABL ABS(0), A ab, CCLW(59)|CLW(60), PLANE XY(33)|YZ(37)|XZ(41)
```

**ROTABL** command passes positioning of the rotatable axis of the machine. This command is obsolete and is supported for backwards compatibility. Process the [MULTIGOTO](multigoto.md) command to handle rotatable axes.

## Access from sppx

Handler: `program Rotabl`

or

```text
ROTABL INCR(66), B ab, CCLW(59)|CLW(60), PLANE XY(33)|YZ(37)|XZ(41)
```

| Parameter | CLD array | CLD name | Description |
|---|---|---|---|
| ABS(0)<br>INCR(66) | CLD[1] | CLD.Incr | Rotation type: 0 (ABS) absolute, 66 (INCR) incremental |
| ab | CLD[2] | CLD.AB | Table rotation angle value or increment value |
| CCLW(59)<br>CLW(60) | CLD[3] | CLD.CCLW | Rotation direction: CCLW – counter clockwise; CLW – clockwise. |
| XY(33)<br>YZ(37)<br>XZ(41) | CLD[4] | CLD.Plane | Plane |

Use ISO.A, ISO.B, ISO.C to create similar ISO postprocessors with masks. The system fills these variables automatically with values of CLD array items:

| CLD parameters value | ISO value |
|---|---|
| CLD[4] = 33 CLD[1] = 0 CLD[3] = 59 | ISO.C = CLD[2] |
| CLD[4] = 33 CLD[1] = 0 CLD[3] = 60 | ISO.C = -CLD[2] |
| CLD[4] = 33 CLD[1] = 66 | ISO.C = CLD[2] |
| CLD[4] = 41 CLD[1] = 0 CLD[3] = 59 | ISO.B = CLD[2] |
| CLD[4] = 41 CLD[1] = 0 CLD[3] = 60 | ISO.B = -CLD[2] |
| CLD[4] = 41 CLD[1] = 66 | ISO.B = CLD[2] |
| CLD[4] = 37 CLD[1] = 0 CLD[3] = 59 | ISO.A = CLD[2] |
| CLD[4] = 37 CLD[1] = 0 CLD[3] = 60 | ISO.A = -CLD[2] |
| CLD[4] = 37 CLD[1] = 66 | ISO.A = CLD[2] |

Example (from the HAAS (SL30)_TurnMill postprocessor):

```pascal
program RoTabl
!  using RotAng,RotAngStep,RotPlan initialize in PARTNO
!  if cld[3] = 59 then sing = 1 else sign = -1
!  if cld[1] = 0 then RotAng = cld[2]*sign
!  if cld[1] = 66 then RotAngStep = cld[2]*sign
!  if cld[4] = 33 then RotPlan = 17        ! C-table rotationn plane XY
!  else if cld[4] = 37 then RotPlan = 18   ! B-table rotationn plane XZ
!  else if cld[4] = 41 then RotPlan = 19   ! A-table rotationn plane YZ
end
```

## See also
- [CLData access model](../cldata.md)
