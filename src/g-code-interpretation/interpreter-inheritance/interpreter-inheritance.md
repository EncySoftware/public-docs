# Interpreter inheritance

The inheritance mechanism is intended for reusing already developed interpreters to translate and interpret NC programs with a similar but different syntax. How much an NC program must differ from the original one to justify a descendant rather than a new interpreter is up to the developer.

The purpose of a descendant interpreter is to translate and interpret the differences in the NC program and to pass control to the parent interpreter for translating and interpreting the similar parts of the NC program text.

A descendant interpreter is implemented differently from [an ordinary interpreter](../../../index.md) in the following:

1. The **ParentID** and **ParentFileName** fields are filled in the [interpreter settings file](../../interpreter-structure/interpreter-settings-file/interpreter-settings-file.md) (SNCI).
2. If necessary, existing registers are overridden or new ones are added. This can be done by adding the changes to the list of registers of the SNCI file or to the list of registers returned by the **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).GetRegisters** function of the descendant interpreter [library](../../interpreter-structure/interpreter-library/interpreter-library.md).
3. The descendant interpreter [library](../../interpreter-structure/interpreter-library/interpreter-library.md) is implemented. In the library, the descendant calls or does not call the functions and methods of the parent interpreter library, depending on the algorithms it uses to translate and interpret the NC program text. The parent interpreter interface (**[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md)**) is passed to the descendant during initialization.

An interpreter can inherit from only one parent. The number of descendant interpreters of one parent and the depth of inheritance are not limited.

**Register inheritance.**

The registers of descendant interpreters override the registers of parent interpreters. Register inheritance is implemented so that the resulting list (the [list of base registers](../sprutcam-interfaces/basic-interfaces/register-list/register-list.md)) is filled in the following order:

1. The list of registers is loaded from the settings file of the **descendant interpreter**.
2. The list of registers is loaded from the library of the **descendant interpreter** (**[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).GetRegisters**). If a register with the same name already exists in the list of base registers, it is not loaded.
3. The list of registers is loaded from the settings file of the **parent interpreter**. If a register with the same name already exists in the list of base registers, it is not loaded.
4. The list of registers is loaded from the library of the **parent interpreter**. If a register with the same name already exists in the list of base registers, it is not loaded.
5. The list of registers is loaded from the settings file of the **parent of the parent interpreter**. If a register with the same name already exists in the list of base registers, it is not loaded.
6. The list of registers is loaded from the library of the **parent of the parent interpreter**. If a register with the same name already exists in the list of base registers, it is not loaded.
7. And so on, up to the very first parent.

**Library inheritance.**

When the [parent interpreter library is initialized](../interpreter-loading-and-initialization/interpreter-loading-and-initialization.md), a number of methods and functions are called by the CAM system kernel, so the descendant does not need to call them:

1. **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).GetIdentifier.**
2. **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).GetRegisters.**
3. **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).SetInterface.**
4. **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).Initialize.**

The descendant calls or does not call the other functions and methods of the parent interpreter library, depending on the algorithms it uses to translate and interpret the NC program text. To let the descendant call the parent methods, the parent interpreter interface is passed to it, among others, when the [descendant interpreter library is initialized](../interpreter-loading-and-initialization/interpreter-loading-and-initialization.md) (the **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).SetInterface** function).

Below are recommendations for calling the functions and methods of the parent interpreter from a descendant interpreter.

1. **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).TransLine** - call the parent **TransLine** if analyzing the NC program line did not shorten the original line. Pass all the parameters returned by the parent method (**ProcessedChars, NextLine, BreakLine**) to the output parameters of the descendant method.
2. **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).DefineRegister** - call the parent **DefineRegister** if the descendant has not determined the register by its address. Pass the **Index** parameter and the result returned by the parent function to the output parameter and the result of the descendant function.
3. **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).BeforeInterprete** - always call the parent **BeforeInterprete**.
4. **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).Interprete** - call the parent **Interprete** if the descendant does not interpret the object to interpret.
5. **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).AfterInterprete** - always call the parent **AfterInterprete**.
6. **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).EndOfProgram** - always call the parent **EndOfProgram** if the descendant has not determined the end of the NC program. Return the result of the parent function as the result of the descendant function.

The page [Examples of interpreters with source codes](../../interpreter-structure/interpreter-example/interpreter-example.md) gives an example of the source code of a descendant interpreter library, the 'dll' built from it, and an example of the settings file.
