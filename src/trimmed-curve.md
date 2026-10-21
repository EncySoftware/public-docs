# Trimmed curve

A portion of the source curve between two boundaries. The boundaries are specified in one of two ways — by parameter values or by points:

`CreateTrimmedCurve(ID: string; SourceCurveID: string; t1, t2: STFloat)` — trim by parameter values.

- `ID` — identifier of the entity being created;
- `SourceCurveID` — identifier of the source curve;
- `t1`, `t2` — the start and end parameter values.

`CreateTrimmedCurve2(ID: string; SourceCurveID: string; p1, p2: TST3DPoint)` — trim by two points.

- `ID` — identifier of the entity being created;
- `SourceCurveID` — identifier of the source curve;
- `p1`, `p2` — the start and end points.
