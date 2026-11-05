# Liste der verwendeten Typen

Alle Typen, die für die Interaktion des CAM-Systems mit der Programmbibliothek des Interpreters nötig sind, sind in Typbibliotheken beschrieben. Woher die Pakete damit stammen und welche Version zu wählen ist, steht auf der Seite [Interpreter-Bibliothek](../../interpreter-structure/interpreter-library/interpreter-library.md).

Die folgenden TLB-Dateien enthalten die Beschreibung der Typen, die bei der Interaktion mit der Bibliothek des Interpreters verwendet werden:

**STNCInterpreter.tlb** - Hauptliste der Typen

**STNCAnalyzer.tlb** - Typen zur Steuerung der Analyse des NC-Programmtexts

**STNCFormers.tlb** - Typen zur Vereinfachung der Bildung des Werkzeugwegs (lineare Bewegungen, Kreisbogenbewegungen, Zyklen).

**STNCConnect.tlb** - Typen für den Schutz des Interpreters.

**STNCCustomInterpreter.tlb** - Typen für einen Interpreter mit eigenen Parametern.

Hauptliste der Typen (**STNCInterpreter.tlb**)

| Typen | Beschreibung der Typen |
| --- | --- |
| TNCExecObj<br>INCT_BlockExecObject<br>INCT_BlockExecArray | [Liste der zu interpretierenden Objekte](../cam-interfaces/basic-interfaces/list-of-objects-to-interpret/list-of-objects-to-interpret.md) |
| TNCSpindleCommand<br>INCT_BaseReg<br>INCT_SysState<br>INCT_SysState2<br>INCT_SpindleState | [Registerliste](../cam-interfaces/basic-interfaces/register-list/register-list.md) |
| TNCOperationGroup<br>INCT_Equipment<br>INCT_Equipment2<br>INCT_Equipment_Channels<br>INCT_Channel | [Parameter der Ausrüstung](../cam-interfaces/basic-interfaces/equipment-parameters/equipment-parameters.md) |
| TNC3DPoint<br>TNCFeedType<br>TNCPlaneType<br>TNCLengthCompensationMode<br>TNCRadiusCompensationMode<br>TNCGotoMode<br>TNCDrillingCycleType<br>TNCLatheCycleType<br>TNCSystemMeasure<br>TNCFeedrateMeasure<br>TNCThreadOrientation<br>TNCThreadLeadType<br>TNCTooltipMode<br>TNCEulerAnglesConvention<br>TNCFlipType<br>TNCMillingCycleType<br>TNCAddOriginFlipMode<br>TNCSPositioningMode<br>TNCOriginSolutionState<br>INCT_CLData<br>INCT_CLData2<br>INCT_CLData_CutTo5d<br>INCT_CLData_AutoAxesBrakes<br>INCT_CLData_Comment<br>INCT_CLData_BreakCommand<br>INCT_CLData_Insert<br>INCT_CLData_Print<br>INCT_CLData_Wait<br>INCT_CLData_LngID<br>INCT_AddOriginByShiftAndRotate<br>INCT_AddOriginByPhysicAxes<br>INCT_OriginSolver | [Bildung des Werkzeugwegs in Maschinenachsen](../cam-interfaces/basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md) |
| TNC3DMatrix<br>INCT_GeomCLData | [Bildung des Werkzeugwegs in geometrischen Achsen](../cam-interfaces/basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md) |
| TNCMessageType<br>INCT_Kernel<br>INCT_Kernel2 | [Schnittstelle des CAM-Systemkerns](../cam-interfaces/basic-interfaces/cam-kernel-interface/cam-system-kernel-interface.md) |
| TNCGetPartDirection<br>TNCGetPartOrigin<br>INCT_ProgramManager<br>INCT_ProgramManager2<br>INCT_Program<br>INCT_GetPartByUser | [Interaktion mit dem Text des NC-Programms](../cam-interfaces/basic-interfaces/nc-program-management/nc-program-management.md) |
| TNCSign<br>TNCPoint<br>TNCValueAvailType<br>INCT_RegisterValues<br>INCT_Register<br>INCT_RegisterList | [Liste der Interpreter-Register](interpreter-interfaces/list-of-interpreter-registers/list-of-interpreter-registers.md) |
| INCT_InterpreterState | [Bearbeitungszyklus beim Drehen](../cam-interfaces/toolpath-construction/turning-machining-cycle/turning-machining-cycle.md) |
| INCT_Interpreter | [Interpreter-Schnittstelle](interpreter-interfaces/interpreter-interface/interpreter-interface.md) |
| INCT_CLData_PocketCycleFormer | [Zyklus zum Fräsen kreisförmiger Taschen](../cam-interfaces/toolpath-construction/circular-pocket-milling-cycle/circular-pocket-milling-cycle.md) |

Typen zur Steuerung der Analyse des NC-Programmtexts (**STNCAnalyzer.tlb**)

| Typen | Beschreibung der Typen |
| --- | --- |
| INCT_Analyzer<br>INCT_Analyzer2<br>INCT_Comments<br>INCT_Brackets<br>INCT_Quotes<br>INCT_UnionLineChars<br>INCT_EndOfLineChars | [Verwaltung der NC-Programmanalyse](../cam-interfaces/managing-nc-program-analysis/managing-nc-program-analysis.md) |

Typen zur Vereinfachung der Bildung des Werkzeugwegs (**STNCFormers.tlb**)

| Typen | Beschreibung der Typen |
| --- | --- |
| INCT_LinearMotionFormer<br>INCT_GeomLinearMotionFormer | [Lineare Bewegungen](../cam-interfaces/toolpath-construction/linear-movements/linear-movements.md) |
| TNCCircularMode<br>TNCConstructArcMode<br>TNCAxisType<br>INCT_CircularMotionFormer | [Kreisbogenbewegungen](../cam-interfaces/toolpath-construction/circular-movements/circular-movements.md) |
| TNCDCAxisIndexes<br>TNCDrillingCycleMoveType<br>TNCReturnLevel<br>INCT_DrillingCycleEvents<br>INCT_DrillingCycleFormer | [Bohrzyklus](../cam-interfaces/toolpath-construction/drilling-cycle/drilling-cycle.md) |
| TNCDrillingCycleShiftType<br>TNCShiftAxis<br>TNCShiftValues<br>TNCShiftPath<br>SetOfTNCShiftPath<br>INCT_DrillingCycleWithShiftFormer | [Bohrzyklus mit Verschiebung](../cam-interfaces/toolpath-construction/drilling-cycle-with-shift/drilling-cycle-with-shift.md) |
| TNCStartLevelType<br>TNCDegressionType<br>TNCClearanceType<br>TNCRetractionType<br>INCT_PeckDrillingCycleEvents<br>INCT_PeckDrillingCycleFormer | [Bohrzyklus mit Spanbruch](../cam-interfaces/toolpath-construction/drilling-cycle-with-chip-breaking/drilling-cycle-with-chip-breaking.md) |
| TNC2DPoint<br>TNCLCAxisIndexes<br>TNCLatheCycleMoveType<br>TNCGrooveDirection<br>INCT_LatheCycleEvents<br>INCT_LatheGroovingCycleFormer | [Drehzyklus Einstechen](../cam-interfaces/toolpath-construction/turning-cycle-grooving/turning-cycle-grooving.md) |
| TNCThreadApproach<br>TNCThreadCuttingDirection<br>TNCThreadSequenceType<br>INCT_LatheThreadCuttingCycleEvents<br>INCT_LatheThreadCuttingCycleFormer<br>INCT_LatheThreadCuttingCycleFormer2 | [Gewindeschneiden mit Drehzyklus](../cam-interfaces/toolpath-construction/turning-cycle-threading/turning-cycle-threading.md) |
| TNCLSRPointType<br>TNCCutDepthCalcMethod<br>TNCPassReturnMethod<br>TNCMachiningProcessing<br>TNCLatheMachiningType<br>TNCLatheMachiningDirection<br>TNCLatheStepType<br>TNCLatheStartPointMode<br>TNCLatheMachiningStyle<br>INCT_LatheStockRemovalCycleEvents<br>INCT_LatheStockRemovalCycleEvents2<br>INCT_LatheStockRemovalCycleEvents3<br>INCT_LatheCycleArcEvents<br>INCT_LatheStockRemovalCycleFormer<br>INCT_LatheStockRemovalCycleFormer2 | [Bearbeitungszyklus beim Drehen](../cam-interfaces/toolpath-construction/turning-machining-cycle/turning-machining-cycle.md) |
| TNCMillingThreadType<br>TNCMillingCycleMoveType<br>INCT_MillingCycleEvents<br>INCT_ThreadMillingCycleFormer | [Gewindefräszyklus](../cam-interfaces/toolpath-construction/thread-milling-cycle/thread-milling-cycle.md) |
| TNCFlatSpiralStepType<br>TNCSpiralDirection<br>TNCTypeOfProcessing<br>TNCPocketCycleMoveType<br>INCT_PocketCycleEvents<br>INCT_PocketCycleFormer | [Zyklus zum Fräsen kreisförmiger Taschen](../cam-interfaces/toolpath-construction/circular-pocket-milling-cycle/circular-pocket-milling-cycle.md) |

Typen für den Schutz des Interpreters (**STNCConnect.tlb**)

| Typen | Beschreibung der Typen |
| --- | --- |
| INCT_Connect | [Schutz-Schnittstelle](interpreter-interfaces/protection-interface/protection-interface.md) |

Typen für einen Interpreter mit eigenen Parametern (**STNCCustomInterpreter.tlb**)

| Typen | Beschreibung der Typen |
| --- | --- |
| TCustomParameterType<br>INCT_CustomParameter<br>INCT_CustomParameters | Beschreibung der Parameter: Name (**Name**) und Typ (**ParamType**: `cpInt`, `cpFlt`, `cpStr`, `cpBol`, `cpArray`, `cpComplex`) jedes Parameters; Parameter der Typen `cpArray` und `cpComplex` haben untergeordnete Parameter (**Count**, **Childs**, **ChildsByName**) |
| INCT_CustomValue<br>INCT_CustomValues | Parameterwerte: Name (**Name**) und Wert (**Int**, **Flt**, **Str**); untergeordnete Werte: **Count**, **Childs**, **ChildsByName** |
| INCT_CustomInterpreter | Schnittstelle eines Interpreters mit eigenen Parametern (siehe unten) |

**INCT_CustomInterpreter** ist eine Schnittstelle, die das Objekt des Interpreters (dasselbe, das **NCT_GetInterface** zurückgibt) implementiert, wenn der Interpreter eigene Parameter hat. Die Parameterwerte stehen in einer Datei `*.sncix`: Die Datei verweist auf den Interpreter und enthält die Werte seiner Parameter, eine eigene Bibliothek hat sie nicht.

Die Datei `*.sncix` wird im Fenster **Dolmetscher-Konfigurator** erstellt. Das Fenster öffnet sich über den Eintrag **Interpreter-Konfigurator** in der Liste **Zubehör** des CAM-Systems oder über den Eintrag **Interpreter-Konfigurator** in ENCY Tuner. Wählen Sie im Fenster im Feld **Interpreter** die Datei des Interpreters, legen Sie die Parameterwerte fest und speichern Sie sie mit der Schaltfläche **Speichern als** in einer Datei `*.sncix`. Damit der Interpreter mit diesen Werten arbeitet, wählen Sie überall dort, wo die Interpreterdatei gewählt wird, die Datei `*.sncix` anstelle der Datei `*.snci`: Das Fenster zur Auswahl der Interpreterdatei bietet beide Dateitypen an.

| Methode oder Eigenschaft | Beschreibung |
| --- | --- |
| **Parameters** | Schreibgeschützte Eigenschaft, die **INCT_CustomParameters** zurückgibt, die Liste der Parameter des Interpreters. Anhand dieser Liste zeigt das Fenster **Dolmetscher-Konfigurator** die Parameter an und speichert ihre Werte in der Datei `*.sncix`. |
| **SetCustomValues**(Values: **INCT_CustomValues**) | Das CAM-System ruft die Methode nach dem Laden der Bibliothek des Interpreters und vor dem Lesen seiner Register auf und übergibt die Parameterwerte aus der Datei `*.sncix`. Wird der Interpreter über seine eigene Datei `*.snci` statt über eine Datei `*.sncix` gewählt, ist **Values** leer (nil / null). |

Ein Interpreter, dessen Objekt **INCT_CustomInterpreter** implementiert, kann kein Eltern-Interpreter sein: Das CAM-System bricht das Laden des abgeleiteten Interpreters mit einem Fehler ab.
