# Interpreter loading and initialization

In the CAM system, **loading the interpreter into memory** consists of the following steps:

- Reading the interpreter settings file.
- Loading the list of registers from the interpreter settings file.
- Loading the parent interpreter into memory (loading of the parent interpreter repeats all the steps of loading the interpreter into memory in the same order).
- Loading the interpreter library into memory and getting the **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md)** interface (by calling the **NCT_GetInterface** function of the loaded library).
- Checking that the identifiers of the settings file and the library match (the library identifier is obtained by calling the **INCT_Interpreter.GetIdentifier** function), as well as the identifiers of the parent interpreter.
- Loading the list of registers from the library (calling the **INCT_Interpreter.GetRegisters** function).
- Loading the lists of registers of the parent interpreters.

As a result of loading the interpreter, the interpreter library and its parent libraries (if any) are loaded, and the resulting (base) list of registers is formed. The registers of the settings file take precedence over the registers of the library (i.e. override them), and the registers of descendant interpreters take precedence over the registers of parent interpreters if a register with the same name is present in both lists.

**Initialization of the interpreter** consists of the following steps:

- Initialization of the parent interpreters (initialization of the parent interpreter repeats all the steps of initializing the interpreter in the same order).
- The CAM system passes its interfaces to the library one after another (the **INCT_Interpreter.SetInterface** method of the interpreter library is called several times, according to the number of interfaces passed).
- Initialization of the library (calling the **INCT_Interpreter.Initialize** method).

As a result of initialization, the interpreter receives the CAM system objects that implement the interfaces for:

- access to the formed (base) list of registers **[INCT_SysState](../sprutcam-interfaces/basic-interfaces/register-list/register-list.md)**;
- managing the NC program text analysis settings **[INCT_Analyzer](../sprutcam-interfaces/managing-nc-program-analysis/managing-nc-program-analysis.md)**;
- access to the list of objects to interpret **[INCT_BlockExecArray](../sprutcam-interfaces/basic-interfaces/list-of-objects-to-interpret/list-of-objects-to-interpret.md)**;
- getting the equipment settings **[INCT_Equipment](../sprutcam-interfaces/basic-interfaces/equipment-parameters/equipment-parameters.md)**;
- forming the tool path in machine axes **[INCT_CLData](../sprutcam-interfaces/basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md)**;
- forming the tool path in geometric axes **[INCT_GeomCLData](../sprutcam-interfaces/basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md)**;
- interaction with the CAM system kernel that serves the interpreter **[INCT_Kernel](../sprutcam-interfaces/basic-interfaces/sprutcam-kernel-interface/cam-system-kernel-interface.md)**;
- the parent interpreter **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md)**.

Then the initialization method of the interpreter library is executed.
