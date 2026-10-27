# C# support in CAMAPI

## Support factory class

After the managed DLL is loaded into the main application's memory, it is analyzed for the presence of the namespace CAMAPI with the ExtensionFactory class inside. This class must implement the [IExtensionFactory](../../api/CAMAPI.Extensions.IExtensionFactory.yml). interface. The main application will interact with the loaded DLL through an object of this interface.

This interface provides method to create instances of extensions, so main application will call this method.
```
// ReSharper disable once CheckNamespace
namespace CAMAPI;

using Extensions;
using ResultStatus;

/// <summary>
/// Factory for creating extensions. Namespace and class name always should be CAMAPI.ExtensionFactory,
/// so CAMAPI will find it
/// </summary>
public class ExtensionFactory : IExtensionFactory
{
    /// <inheritdoc />
    public void OnLibraryRegistered(IExtensionFactoryContext context, out TResultStatus ret)
    {
        ret = default;
    }

    /// <inheritdoc />
    public void OnLibraryUnRegistered(IExtensionFactoryContext context, out TResultStatus ret)
    {
        ret = default;
    }
    
    /// <summary>
    /// Create new instance of our extension
    /// </summary>
    /// <param name="extensionIdent">
    /// Unique identifier, if out library has more than one extension. Should accord with
    /// value in settings json, describing this library
    /// </param>
    /// <param name="ret">Error to return it, because throw exception will not work</param>
    /// <returns>Instance of out extension</returns>
    public IExtension? Create(string extensionIdent, out TResultStatus ret)
    {
        try
        {
            // write your code to create new instance
        }
        catch (Exception e)
        {
            ret.Code = TResultStatusCode.rsError;
            ret.Description = e.Message;
        }
        return null;
    }
}

```

## Connecting the SDK

You have to include actual version of SDK as package reference.
```
<PackageReference Include="EncySoftware.CAMAPI.SDK.Net" Version="1.1.0" />
```