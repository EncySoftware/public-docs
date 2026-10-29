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

**Description of the native interpreter library functions in Delphi:**

```pascal
function NCT_GetInterface: INCT_Interpreter; stdcall;
procedure NCT_FreeMemory; stdcall;
```

**Description of the native interpreter library functions in C\+\+:**

```cpp
INCT_Interpreter __stdcall NCT_GetInterface();
void __stdcall NCT_FreeMemory();
```

All types required for interaction between the CAM system and the interpreter program library are given in the [type library](https://learn.microsoft.com/windows/win32/midl/com-dcom-and-type-libraries) included in the CAM system distribution (the **TypeLibraries\\\*.tlb** folder).

The following TLB files contain descriptions of the types used for interaction with the interpreter library:

- **STNCInterpreter.tlb** — main list of types;
- **STNCAnalyzer.tlb** — types used to manage NC program analysis;
- **STNCFormers.tlb** — types used to simplify tool path construction (linear/circular movements, cycles).

To connect the type library to your development environment, refer to the corresponding section of the development environment documentation.

> [!NOTE]
> **Registering the type library**
>
> To register the type library in Microsoft Visual Studio, try the following:
>
> Find the **tlbImp.exe** file on your computer. Run the command "**tlbimp.exe tlb-filename**". The command creates the "**tlb-filename.dll**" file (for example, "STNCAnalyzer.dll"). Add this dll file to your project via the "**Add Reference**" menu item.

The [Examples of interpreters with source codes](../interpreter-example/interpreter-example.md) page gives an example of the interpreter library source code, the 'dll' built from it, and an example of the settings file.
