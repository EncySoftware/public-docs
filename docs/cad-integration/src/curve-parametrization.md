# Curve parametrization

These methods change the parametrization of an already created curve (analytic or derived) by its identifier; no new object is created in the process.

| Method | Description |
|-------|----------|
| `SetCurveParametrization(CurveID: string; TMin, TMax: STFloat)` | Set new bounds for the parameter range of an existing curve. `CurveID` — curve identifier; `TMin`, `TMax` — new minimum and maximum parameter values. |
| `SetCurveDomain(ID: string; SrcTmin, SrcTmax, PrxTmin, PrxTmax: STFloat)` | Reparametrize the curve: define the correspondence between the old (`Src*`) and new (`Prx*`) parameter ranges. `ID` — curve identifier; `SrcTmin`, `SrcTmax` — old range bounds; `PrxTmin`, `PrxTmax` — new range bounds. |
