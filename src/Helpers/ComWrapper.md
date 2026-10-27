# Using ComWrapper

The CAM system core is written in a programming language where memory is released manually — as opposed to languages like C#, which rely on a Garbage Collector that frees memory automatically.

Therefore, when extensions written in .NET interact with the CAM system core, it is necessary to have a mechanism for explicitly releasing COM objects on demand. For this reason, the ComWrapper class was introduced to encapsulate all memory management logic for COM objects.

Problems solved by using the ComWrapper:
1. Accessing a COM object from multiple threads;
2. Proper memory cleanup after use, ensuring that the CAM system core can continue functioning correctly.

## Examples:
Get another COM-object:
```
using var ncMakerCom = activeProjectCom.InvokeAndWrap(project => project.NCMaker);
```

Execute method of COM-object:
```
applicationCom.Invoke(application =>
{
    application.MainWorkMode = TMainWorkMode.mwmModel;
});
```

Transfering ownership:
```
var curveCom2 = curveCom1.TransferOwnership();
```

## Conclusion
Using ComWrapper is mandatory, if your extension is written on .NET.