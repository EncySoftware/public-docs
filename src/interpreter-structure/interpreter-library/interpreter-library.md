# Interpreter library

The interpreter program library is a dynamic link library ([DLL](https://learn.microsoft.com/troubleshoot/windows-client/deployment/dynamic-link-library)). Regardless of the platform the library is implemented for (.NET/native), the library must export two functions:

**NCT_GetInterface** — returns to the CAM system an object implementing the interface for interaction between the CAM system kernel and the program library ([**INCT_Interpreter**](../../g-code-interpretation/interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md));

**NCT_FreeMemory** — frees memory from all objects created by the library itself or received from the CAM system during operation.

**Example of a class describing the interpreter library functions in C# (assembly for the .NET platform):**

```csharp
namespace sample
{
    public class Interpreter : MarshalByRefObject
    {
        public static INCT_Interpreter NCT_GetInterface()
        {
            /* implementation */
        }
        public static void NCT_FreeMemory()
        {
            /* implementation */
        }
    }
}
```

In a .NET assembly these functions can be either static or instance methods: the CAM system creates an object of the class specified by the **NetNamespaceClass** tag of the [interpreter settings file](../interpreter-settings-file/interpreter-settings-file.md), calls its **NCT_GetInterface** and, when the library is unloaded, **NCT_FreeMemory**. Therefore the class must have a public parameterless constructor.

**Description of the native interpreter library functions in Delphi:**

```pascal
function NCT_GetInterface: INCT_Interpreter; stdcall;
procedure NCT_FreeMemory; stdcall;
```

**Description of the native interpreter library functions in C\+\+:**

```cpp
void __stdcall NCT_GetInterface(INCT_Interpreter** Result);
void __stdcall NCT_FreeMemory();
```

The CAM system declares **NCT_GetInterface** as a Delphi function returning an interface. Such a result is not returned in a register but through a hidden parameter: the CAM system passes the address to which the library must write the pointer to the **INCT_Interpreter** object.

All types required for interaction between the CAM system and the interpreter program library are given in the [type libraries](https://learn.microsoft.com/windows/win32/midl/com-dcom-and-type-libraries). They are distributed as NuGet packages published on nuget.org (see [Product versions](../../ai-assisted-development/dotnet-workflow.md#product-versions)); use packages of the same major version as the SDK package the product is built with: for C++ and other languages — the `EncySoftware.NCInterpreterSDK.tlb` package (`*.tlb`, `*.h` and `*.idl` files), for Delphi — `EncySoftware.NCInterpreterSDK.bpl.x64` (`IDL.<Name>.pas` units). Both packages pull in one package per type library.

The following TLB files contain descriptions of the types used for interaction with the interpreter library:

- **STNCInterpreter.tlb** — main list of types;
- **STNCAnalyzer.tlb** — types used to manage NC program analysis;
- **STNCFormers.tlb** — types used to simplify tool path construction (linear/circular movements, cycles);
- **STNCConnect.tlb** — types used to protect the interpreter (see [Protected interpreters](../protected-interpreters/protected-interpreters.md));
- **STNCCustomInterpreter.tlb** — types for an interpreter with its own parameters (see [List of used types](../../g-code-interpretation/interfaces/list-of-used-interfaces.md)).

To connect the type library to your development environment, refer to the corresponding section of the development environment documentation.

> [!NOTE]
> **Registering the type library**
>
> To register the type library in Microsoft Visual Studio, try the following:
>
> Find the **tlbImp.exe** file on your computer. Run the command "**tlbimp.exe tlb-filename**". The command creates the "**tlb-filename.dll**" file (for example, "STNCAnalyzer.dll"). Add this dll file to your project via the "**Add Reference**" menu item.

The [Examples of interpreters with source codes](../interpreter-example/interpreter-example.md) page gives an example of the interpreter library source code, the 'dll' built from it, and an example of the settings file.
