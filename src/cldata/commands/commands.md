# Technology commands description

The list of CLData technology commands:

| Command | Code | Description |
|---|---|---|
| AXESBRAKE | 2012 | [Machine axes brakes control](axesbrake.md) |
| CIRCLE | 15000 | [Circle movement](circle.md) |
| CLAMP | 1074 | [Fixtures clamp/unclamp](clamp.md) |
| COMMENT | 1065 | [Commentaries](comment.md) |
| COOLNT | 1030 | [Cooling](coolnt.md) |
| CUTCOM | 1007 | [Tool compensation](cutcom.md) |
| CYCLE | 1054 | [Hole machining canned cycles](cycle/cycle.md) |
| DELAY | 1010 | [Delay](delay.md) |
| EDMMOVE | 16001 | [EDM movement](edmmove.md) |
| EFFECTOR | 2019 | [End effector activation (EFFECTOR)](effector.md) |
| EXTCYCLE | 1053 | [Extended cycle](extcycle/extcycle.md) |
| FEDRAT | 1009 | [Feedrate](fedrat.md) |
| FINI | 14000 | [Ending record](fini.md) |
| FROM | 5003 | [Original point](from.md) |
| GOHOME | 17 | [Return to original position](gohome.md) |
| GOTO.abs | 5005 | [Linear transition](goto.md) |
| HEAD | 1002 | [Spindle head number](head.md) |
| INSERT | 1046 | [Insertion](insert.md) |
| INTERPOLATION | 1047 | [Interpolation mode](interpolation.md) |
| LOADTL | 1055 | [Tool loading](loadtl.md) |
| MULTIARC | 9014 | [Multiaxis circle movement](multiarc.md) |
| MULTIGOTO | 9010 | [Multi coordinate movement](multigoto.md) |
| OPSKIP | 1012 | [Optional skipping](opskip.md) |
| OPSTOP | 2003 | [Auxiliary stop](opstop.md) |
| ORIGIN | 1027 | [Original coordinates](origin.md) |
| PALETA | 1001 | [Palette changing](paleta.md) |
| PARTNO | 1045 | [Part number](partno.md) |
| PhysicGOTO | 9013 | [Physical machine axes movement](physicgoto.md) |
| PLANE | 99 | [Working plane](plane.md) |
| POWER | 2018 | [Power adjustment (POWER)](power.md) |
| PPFUN | 1079 | [Postprocessor function](ppfun/ppfun.md) |
| PPRINT | 1044 | [Postprocessor printing](pprint.md) |
| RAPID | 2005 | [Rapid feedrate](rapid.md) |
| ROTABL | 1026 | [Table rotation](rotabl.md) |
| SAFPOS | 1094 | [Tool change point](safpos.md) |
| SELWORKPIECE | 2011 | [Active workpiece holder selection](selworkpiece.md) |
| SINGLETHREAD | 1037 | [Singlethread command](singlethread.md) |
| SPINDL | 1031 | [Spindle](spindle.md) |
| STOP | 2002 | [Stop](stop.md) |
| STRUCTURE | 2015 | [Structure command](structure.md) |
| SYNCAXES | 2016 | [Axes movement syncronization](syncaxes.md) |
| TAKEOVER | 2010 | [Workpiece takeover](takeover.md) |
| TLCONTACT | 2017 | [Tool contact command](tlcontact.md) |
| WAIT | 2014 | [Waiting for synchronization point](wait.md) |

Additional words:

| N | Word | Code | Description |
|---|---|---|---|
| 1 | BOTH | 83 | Both |
| 2 | BRKCHP | 288 | Chip breaking |
| 3 | CCLW | 59 | Counter clockwise |
| 4 | CLW | 60 | Clockwise |
| 5 | CUTS | 511 | Cuts |
| 6 | DEEP | 153 | Deep drilling |
| 7 | DEPTH | 510 | Depth |
| 8 | DRILL | 163 | Drill |
| 9 | DWELL | 279 | Dwell |
| 10 | FACE | 81 | G82 canned cycle |
| 11 | FINCUT | 512 | Final cut |
| 12 | INCR | 66 | Increment |
| 13 | LENGTH | 9 | Length |
| 14 | MMPM | 315 | Millimeters per minute |
| 15 | MMPR | 316 | Millimeters per revolution |
| 16 | MULTRD | 119 | Multi-start thread |
| 17 | OFF | 72 | Turn off |
| 18 | ON | 71 | Turn on |
| 19 | ORIENT | 246 | Orientation |
| 20 | TAP | 168 | Tapping |
| 21 | XYPLAN | 33 | XY plane |
| 22 | YZPLAN | 37 | YZ plane |
| 23 | ZXPLAN | 41 | ZX plane |
| 24 | R | 23 | Radius |
| 25 | RGT | 24 | Right tool positioning |
| 26 | LEFT | 8 | Left tool positioning |

## Global handlers (not CLData commands)

Handlers invoked outside the per-command dispatch - listed here so all postprocessor handlers can be found in one place:

| Handler | sppx | .NET | Description |
|---|---|---|---|
| [Output filter](filter.md) | `sub Filter` | `OnFilterString` | Runs on every NC-program line, whatever produced it. |

## See also
- [CLData](../cldata.md)
