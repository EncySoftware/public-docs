# List of used types

All types required for the interaction of the CAM system with the interpreter library are listed in the type libraries. Where to get the packages with them and which version to choose is described on the [Interpreter library](../../interpreter-structure/interpreter-library/interpreter-library.md) page.

The following TLB files contain descriptions of the types used for interaction with the interpreter library:

**STNCInterpreter.tlb** — the main list of types

**STNCAnalyzer.tlb** — types used to manage the NC program text analysis

**STNCFormers.tlb** — types used to simplify tool path construction (linear/circular movements, cycles).

**STNCConnect.tlb** — types used to protect the interpreter.

**STNCCustomInterpreter.tlb** — types for an interpreter with its own parameters.

The main list of types (**STNCInterpreter.tlb**)

| Types | Type description |
| --- | --- |
| TNCExecObj<br>INCT_BlockExecObject<br>INCT_BlockExecArray | [List of objects to interpret](../cam-interfaces/basic-interfaces/list-of-objects-to-interpret/list-of-objects-to-interpret.md) |
| TNCSpindleCommand<br>INCT_BaseReg<br>INCT_SysState<br>INCT_SysState2<br>INCT_SpindleState | [Register list](../cam-interfaces/basic-interfaces/register-list/register-list.md) |
| TNCOperationGroup<br>INCT_Equipment<br>INCT_Equipment2<br>INCT_Equipment_Channels<br>INCT_Channel | [Equipment parameters](../cam-interfaces/basic-interfaces/equipment-parameters/equipment-parameters.md) |
| TNC3DPoint<br>TNCFeedType<br>TNCPlaneType<br>TNCLengthCompensationMode<br>TNCRadiusCompensationMode<br>TNCGotoMode<br>TNCDrillingCycleType<br>TNCLatheCycleType<br>TNCSystemMeasure<br>TNCFeedrateMeasure<br>TNCThreadOrientation<br>TNCThreadLeadType<br>TNCTooltipMode<br>TNCEulerAnglesConvention<br>TNCFlipType<br>TNCMillingCycleType<br>TNCAddOriginFlipMode<br>TNCSPositioningMode<br>TNCOriginSolutionState<br>INCT_CLData<br>INCT_CLData2<br>INCT_CLData_CutTo5d<br>INCT_CLData_AutoAxesBrakes<br>INCT_CLData_Comment<br>INCT_CLData_BreakCommand<br>INCT_CLData_Insert<br>INCT_CLData_Print<br>INCT_CLData_Wait<br>INCT_CLData_LngID<br>INCT_AddOriginByShiftAndRotate<br>INCT_AddOriginByPhysicAxes<br>INCT_OriginSolver | [Forming the tool path in machine axes](../cam-interfaces/basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md) |
| INCT_CLData_PocketCycleFormer | [Circular pocket milling cycle](../cam-interfaces/toolpath-construction/circular-pocket-milling-cycle/circular-pocket-milling-cycle.md) |
| TNC3DMatrix<br>INCT_GeomCLData | [Forming the tool path in geometric axes](../cam-interfaces/basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md) |
| TNCMessageType<br>INCT_Kernel<br>INCT_Kernel2 | [CAM system kernel interface](../cam-interfaces/basic-interfaces/cam-kernel-interface/cam-system-kernel-interface.md) |
| TNCGetPartDirection<br>TNCGetPartOrigin<br>INCT_ProgramManager<br>INCT_ProgramManager2<br>INCT_Program<br>INCT_GetPartByUser | [NC program management](../cam-interfaces/basic-interfaces/nc-program-management/nc-program-management.md) |
| TNCSign<br>TNCPoint<br>TNCValueAvailType<br>INCT_RegisterValues<br>INCT_Register<br>INCT_RegisterList | [List of interpreter registers](interpreter-interfaces/list-of-interpreter-registers/list-of-interpreter-registers.md) |
| INCT_InterpreterState | [Turning stock removal cycle](../cam-interfaces/toolpath-construction/turning-machining-cycle/turning-machining-cycle.md) |
| INCT_Interpreter | [Interpreter interface](interpreter-interfaces/interpreter-interface/interpreter-interface.md) |

Types used to manage the NC program text analysis (**STNCAnalyzer.tlb**)

| Types | Type description |
| --- | --- |
| INCT_Analyzer<br>INCT_Analyzer2<br>INCT_Comments<br>INCT_Brackets<br>INCT_Quotes<br>INCT_UnionLineChars<br>INCT_EndOfLineChars | [Managing NC program text analysis](../cam-interfaces/managing-nc-program-analysis/managing-nc-program-analysis.md) |

Types used to simplify tool path construction (**STNCFormers.tlb**)

| Types | Type description |
| --- | --- |
| INCT_LinearMotionFormer<br>INCT_GeomLinearMotionFormer | [Linear movements](../cam-interfaces/toolpath-construction/linear-movements/linear-movements.md) |
| TNCCircularMode<br>TNCConstructArcMode<br>TNCAxisType<br>INCT_CircularMotionFormer | [Circular movements](../cam-interfaces/toolpath-construction/circular-movements/circular-movements.md) |
| TNCDCAxisIndexes<br>TNCDrillingCycleMoveType<br>TNCReturnLevel<br>INCT_DrillingCycleEvents<br>INCT_DrillingCycleFormer | [Drilling cycle](../cam-interfaces/toolpath-construction/drilling-cycle/drilling-cycle.md) |
| TNCDrillingCycleShiftType<br>TNCShiftAxis<br>TNCShiftValues<br>TNCShiftPath<br>SetOfTNCShiftPath<br>INCT_DrillingCycleWithShiftFormer | [Drilling cycle with shift](../cam-interfaces/toolpath-construction/drilling-cycle-with-shift/drilling-cycle-with-shift.md) |
| TNCStartLevelType<br>TNCDegressionType<br>TNCClearanceType<br>TNCRetractionType<br>INCT_PeckDrillingCycleEvents<br>INCT_PeckDrillingCycleFormer | [Drilling cycle with chip breaking](../cam-interfaces/toolpath-construction/drilling-cycle-with-chip-breaking/drilling-cycle-with-chip-breaking.md) |
| TNC2DPoint<br>TNCLCAxisIndexes<br>TNCLatheCycleMoveType<br>TNCGrooveDirection<br>INCT_LatheCycleEvents<br>INCT_LatheGroovingCycleFormer | [Turning grooving cycle](../cam-interfaces/toolpath-construction/turning-cycle-grooving/turning-cycle-grooving.md) |
| TNCThreadApproach<br>TNCThreadCuttingDirection<br>TNCThreadSequenceType<br>INCT_LatheThreadCuttingCycleEvents<br>INCT_LatheThreadCuttingCycleFormer<br>INCT_LatheThreadCuttingCycleFormer2 | [Turning threading cycle](../cam-interfaces/toolpath-construction/turning-cycle-threading/turning-cycle-threading.md) |
| TNCLSRPointType<br>TNCCutDepthCalcMethod<br>TNCPassReturnMethod<br>TNCMachiningProcessing<br>TNCLatheMachiningType<br>TNCLatheMachiningDirection<br>TNCLatheStepType<br>TNCLatheStartPointMode<br>TNCLatheMachiningStyle<br>INCT_LatheCycleArcEvents<br>INCT_LatheStockRemovalCycleEvents<br>INCT_LatheStockRemovalCycleEvents2<br>INCT_LatheStockRemovalCycleEvents3<br>INCT_LatheStockRemovalCycleFormer<br>INCT_LatheStockRemovalCycleFormer2 | [Turning stock removal cycle](../cam-interfaces/toolpath-construction/turning-machining-cycle/turning-machining-cycle.md) |
| TNCMillingThreadType<br>TNCMillingCycleMoveType<br>INCT_MillingCycleEvents<br>INCT_ThreadMillingCycleFormer | [Thread milling cycle](../cam-interfaces/toolpath-construction/thread-milling-cycle/thread-milling-cycle.md) |
| TNCFlatSpiralStepType<br>TNCSpiralDirection<br>TNCTypeOfProcessing<br>TNCPocketCycleMoveType<br>INCT_PocketCycleEvents<br>INCT_PocketCycleFormer | [Circular pocket milling cycle](../cam-interfaces/toolpath-construction/circular-pocket-milling-cycle/circular-pocket-milling-cycle.md) |

Types used to protect the interpreter (**STNCConnect.tlb**)

| Types | Type description |
| --- | --- |
| INCT_Connect | [Protection interface](interpreter-interfaces/protection-interface/protection-interface.md) |

Types for an interpreter with its own parameters (**STNCCustomInterpreter.tlb**)

| Types | Type description |
| --- | --- |
| TCustomParameterType<br>INCT_CustomParameter<br>INCT_CustomParameters | Description of the parameters: the name (**Name**) and type (**ParamType**: `cpInt`, `cpFlt`, `cpStr`, `cpBol`, `cpArray`, `cpComplex`) of each parameter; parameters of the `cpArray` and `cpComplex` types have nested parameters (**Count**, **Childs**, **ChildsByName**) |
| INCT_CustomValue<br>INCT_CustomValues | Parameter values: the name (**Name**) and value (**Int**, **Flt**, **Str**); nested values: **Count**, **Childs**, **ChildsByName** |
| INCT_CustomInterpreter | Interface of an interpreter with its own parameters (see below) |

**INCT_CustomInterpreter** is an interface that the interpreter object (the one returned by **NCT_GetInterface**) implements if the interpreter has its own parameters. The parameter values are stored in a `*.sncix` file: the file refers to the interpreter and stores the values of its parameters; it has no library of its own.

The `*.sncix` file is created in the **Interpreter configurator** window. The window opens with the **Interpreter configurator** item in the **Utilities** list of the CAM system or with the **Interpreter configurator** item in ENCY Tuner. In the window, select the interpreter file in the **Interpreter** field, set the parameter values and save them to a `*.sncix` file with the **Save as** button. For the interpreter to work with these values, select the `*.sncix` file instead of the `*.snci` file wherever the interpreter file is selected: the interpreter file selection window accepts both file types.

| Method or property | Description |
| --- | --- |
| **Parameters** | Read-only property that returns **INCT_CustomParameters**, the list of the interpreter's parameters. The **Interpreter configurator** window uses it to show the parameters and save their values to the `*.sncix` file. |
| **SetCustomValues**(Values: **INCT_CustomValues**) | The CAM system calls the method after loading the interpreter library, before reading its registers, and passes the parameter values from the `*.sncix` file. If the interpreter is selected by its own `*.snci` file rather than a `*.sncix` file, **Values** is empty (nil / null). |

An interpreter whose object implements **INCT_CustomInterpreter** cannot be a parent interpreter: the CAM system stops loading the descendant with an error.
