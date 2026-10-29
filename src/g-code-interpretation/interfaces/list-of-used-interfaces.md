# Liste der verwendeten Typen

Alle Typen, die für die Interaktion des CAM-Systems mit der Programmbibliothek des Interpreters nötig sind, sind in der [Typbibliothek](https://docs.microsoft.com/en-us/windows/desktop/midl/com-dcom-and-type-libraries) beschrieben, die zum Lieferumfang des CAM-Systems gehört (Verzeichnis **TypeLibraries\\\*.tlb**).

Die folgenden TLB-Dateien enthalten die Beschreibung der Typen, die bei der Interaktion mit der Bibliothek des Interpreters verwendet werden:

**STNCInterpreter.tlb** - Hauptliste der Typen

**STNCAnalyzer.tlb** - Typen zur Steuerung der Analyse des NC-Programmtexts

**STNCFormers.tlb** - Typen zur Vereinfachung der Bildung des Werkzeugwegs (lineare Bewegungen, Kreisbogenbewegungen, Zyklen).

**STNCConnect.tlb** - Typen für den Schutz des Interpreters.

Hauptliste der Typen (**STNCInterpreter.tlb**)

| Typen | Beschreibung der Typen |
| --- | --- |
| TNCExecObj<br>INCT_BlockExecObject<br>INCT_BlockExecArray | [Liste der zu interpretierenden Objekte](../sprutcam-interfaces/basic-interfaces/list-of-objects-to-interpret/list-of-objects-to-interpret.md) |
| TNCSpindleCommand<br>INCT_BaseReg<br>INCT_SysState<br>INCT_SysState2<br>INCT_SpindleState | [Registerliste](../sprutcam-interfaces/basic-interfaces/register-list/register-list.md) |
| TNCOperationGroup<br>INCT_Equipment<br>INCT_Equipment2<br>INCT_Equipment_Channels<br>INCT_Channel | [Parameter der Ausrüstung](../sprutcam-interfaces/basic-interfaces/equipment-parameters/equipment-parameters.md) |
| TNC3DPoint<br>TNCFeedType<br>TNCPlaneType<br>TNCLengthCompensationMode<br>TNCRadiusCompensationMode<br>TNCGotoMode<br>TNCDrillingCycleType<br>TNCLatheCycleType<br>TNCSystemMeasure<br>TNCFeedrateMeasure<br>TNCThreadOrientation<br>TNCThreadLeadType<br>TNCTooltipMode<br>TNCEulerAnglesConvention<br>TNCFlipType<br>TNCMillingCycleType<br>TNCAddOriginFlipMode<br>TNCSPositioningMode<br>TNCOriginSolutionState<br>INCT_CLData<br>INCT_CLData2<br>INCT_CLData_CutTo5d<br>INCT_CLData_AutoAxesBrakes<br>INCT_CLData_Comment<br>INCT_CLData_BreakCommand<br>INCT_CLData_Insert<br>INCT_CLData_Print<br>INCT_CLData_Wait<br>INCT_CLData_LngID<br>INCT_AddOriginByShiftAndRotate<br>INCT_AddOriginByPhysicAxes<br>INCT_OriginSolver | [Bildung des Werkzeugwegs in Maschinenachsen](../sprutcam-interfaces/basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md) |
| TNC3DMatrix<br>INCT_GeomCLData | [Bildung des Werkzeugwegs in geometrischen Achsen](../sprutcam-interfaces/basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md) |
| TNCMessageType<br>INCT_Kernel<br>INCT_Kernel2 | [Schnittstelle des CAM-Systemkerns](../sprutcam-interfaces/basic-interfaces/sprutcam-kernel-interface/cam-system-kernel-interface.md) |
| TNCGetPartDirection<br>TNCGetPartOrigin<br>INCT_ProgramManager<br>INCT_ProgramManager2<br>INCT_Program<br>INCT_GetPartByUser | [Interaktion mit dem Text des NC-Programms](../sprutcam-interfaces/basic-interfaces/nc-program-management/nc-program-management.md) |
| TNCSign<br>TNCPoint<br>TNCValueAvailType<br>INCT_RegisterValues<br>INCT_Register<br>INCT_RegisterList | [Liste der Interpreter-Register](interpreter-interfaces/list-of-interpreter-registers/list-of-interpreter-registers.md) |
| INCT_Interpreter | [Interpreter-Schnittstelle](interpreter-interfaces/interpreter-interface/interpreter-interface.md) |
| INCT_CLData_PocketCycleFormer | [Zyklus zum Fräsen kreisförmiger Taschen](../sprutcam-interfaces/toolpath-construction/circular-pocket-milling-cycle/circular-pocket-milling-cycle.md) |

Typen zur Steuerung der Analyse des NC-Programmtexts (**STNCAnalyzer.tlb**)

| Typen | Beschreibung der Typen |
| --- | --- |
| INCT_Analyzer<br>INCT_Analyzer2<br>INCT_Comments<br>INCT_Brackets<br>INCT_Quotes<br>INCT_UnionLineChars<br>INCT_EndOfLineChars | [Verwaltung der NC-Programmanalyse](../sprutcam-interfaces/managing-nc-program-analysis/managing-nc-program-analysis.md) |

Typen zur Vereinfachung der Bildung des Werkzeugwegs mit Maschinenachsen (**STNCFormers.tlb**)

| Typen | Beschreibung der Typen |
| --- | --- |
| INCT_LinearMotionFormer<br>INCT_GeomLinearMotionFormer | [Lineare Bewegungen](../sprutcam-interfaces/toolpath-construction/linear-movements/linear-movements.md) |
| TNCCircularMode<br>TNCConstructArcMode<br>TNCAxisType<br>INCT_CircularMotionFormer | [Kreisbogenbewegungen](../sprutcam-interfaces/toolpath-construction/circular-movements/circular-movements.md) |
| TNCDCAxisIndexes<br>TNCDrillingCycleMoveType<br>INCT_DrillingCycleEvents<br>INCT_DrillingCycleFormer | [Bohrzyklus](../sprutcam-interfaces/toolpath-construction/drilling-cycle/drilling-cycle.md) |
| TNCShiftAxis<br>TNCShiftValues<br>TNCShiftPath<br>SetOfTNCShiftPath<br>INCT_DrillingCycleWithShiftFormer | [Bohrzyklus mit Verschiebung](../sprutcam-interfaces/toolpath-construction/drilling-cycle-with-shift/drilling-cycle-with-shift.md) |
| TNCStartLevelType<br>TNCDegressionType<br>TNCClearanceType<br>TNCRetractionType<br>INCT_PeckDrillingCycleEvents<br>INCT_PeckDrillingCycleFormer | [Bohrzyklus mit Spanbruch](../sprutcam-interfaces/toolpath-construction/drilling-cycle-with-chip-breaking/drilling-cycle-with-chip-breaking.md) |
| TNC2DPoint<br>TNCLCAxisIndexes<br>TNCLatheCycleMoveType<br>TNCGrooveDirection<br>INCT_LatheCycleEvents<br>INCT_LatheGroovingCycleFormer | [Drehzyklus Einstechen](../sprutcam-interfaces/toolpath-construction/turning-cycle-grooving/turning-cycle-grooving.md) |
| TNCThreadApproach<br>TNCThreadCuttingDirection<br>TNCThreadSequenceType<br>INCT_LatheThreadCuttingCycleEvents<br>INCT_LatheThreadCuttingCycleFormer<br>INCT_LatheThreadCuttingCycleFormer2 | [Gewindeschneiden mit Drehzyklus](../sprutcam-interfaces/toolpath-construction/turning-cycle-threading/turning-cycle-threading.md) |
| TNCLSRPointType<br>TNCCutDepthCalcMethod<br>TNCPassReturnMethod<br>TNCMachiningProcessing<br>TNCLatheMachiningType<br>TNCLatheMachiningDirection<br>TNCLatheStepType<br>TNCLatheStartPointMode<br>TNCLatheMachiningStyle<br>INCT_LatheStockRemovalCycleEvents<br>INCT_LatheStockRemovalCycleEvents2<br>INCT_LatheStockRemovalCycleEvents3<br>INCT_LatheCycleArcEvents<br>INCT_LatheStockRemovalCycleFormer<br>INCT_LatheStockRemovalCycleFormer2<br>INCT_InterpreterState | [Bearbeitungszyklus beim Drehen](../sprutcam-interfaces/toolpath-construction/turning-machining-cycle/turning-machining-cycle.md) |
| TNCMillingThreadType<br>TNCMillingCycleMoveType<br>INCT_MillingCycleEvents<br>INCT_ThreadMillingCycleFormer | [Gewindefräszyklus](../sprutcam-interfaces/toolpath-construction/thread-milling-cycle/thread-milling-cycle.md) |
| TNCFlatSpiralStepType<br>TNCSpiralDirection<br>TNCTypeOfProcessing<br>TNCPocketCycleMoveType<br>INCT_PocketCycleEvents<br>INCT_PocketCycleFormer | [Zyklus zum Fräsen kreisförmiger Taschen](../sprutcam-interfaces/toolpath-construction/circular-pocket-milling-cycle/circular-pocket-milling-cycle.md) |

Typen für den Schutz des Interpreters (**STNCConnect.tlb**)

| Typen | Beschreibung der Typen |
| --- | --- |
| INCT_Connect | [Schutz-Schnittstelle](interpreter-interfaces/protection-interface/protection-interface.md) |
