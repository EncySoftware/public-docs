# Add-in XML file

Contains the Add-in's metadata, a description of the supported formats, and the names of the commands with which the Add-in wizard calls `<Translator>.exe`.

**Root structure.**

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Collection>
    <CADTranslators>
        <TranslatorName>Alibre</TranslatorName>
        <TranslatorComposition AddinConnected="-1" ToolbarConnected="-1"/>
        <IsExternal>-1</IsExternal>
        <WantAdmin>0</WantAdmin>
        <Enabled>0</Enabled>
        <HideWinow>-1</HideWinow>
        <TranslatorPath>C:\ProgramData\Company_name\Product_name\Product_version\AddIns\Alibre\AlibreTranslator.exe</TranslatorPath>
        <OutputExtension>IGS</OutputExtension>
        <InputExtensions>AD_PRT.AD_ASM</InputExtensions>
        <CommandLine>$(InFile) $(OutFile)</CommandLine>
        <CommandLineIsAppInst>IsInstalled</CommandLineIsAppInst>
        <CmdLnInstall>Install</CmdLnInstall>
        <CmdLnUnInstall>UnInstall</CmdLnUnInstall>
        <HostApplication>Alibre</HostApplication>
        <DeprecatedHostApplications>
            <Item>GeoMagic</Item>
        </DeprecatedHostApplications>        
        <MinimalVersion>v12</MinimalVersion>
        <CADPlatform>xAny</CADPlatform>
        <Description>
            <Item LangCode="1033">Addin and toolbar for Alibre Design™</Item>
            <Item LangCode="1049">Дополнение и панель инструментов для Alibre Design™</Item>
        </Description>
        <Copyright>Company name</Copyright>
        <HostCopyright>© Alibre, LLC</HostCopyright>
        <BuildInfo PackageID="" PackageVersion="" BuildNumber=""/>
    </CADTranslators>
</Collection>
```

**Tag descriptions.** Pay particular attention to `HostApplication` — its value is used by the Toolbar when transferring geometry to the CAM system.

| Tag name | Description | Value |
|----------|----------|----------|
| `TranslatorName` | The Add-in name shown in the Add-in wizard list. | — |
| `TranslatorComposition` | The `AddinConnected` and `ToolbarConnected` attributes indicate which import scenarios will be available. | `AddinConnected="-1"` — import from the CAM system is available (see [Importing a CAD file into the CAM system](import-cad-file.md)); `ToolbarConnected="-1"` — import from the CAD system is available (see [Importing from the CAD system into the CAM system](import-from-cad.md)). |
| `IsExternal` | Indicates that this is an external importer. | Must be equal to `-1`. |
| `WantAdmin` | Indicates whether the installer needs to be run with administrator rights. | `0` — False; `-1` — True. |
| `WantAdminForInstallation` | Indicates whether administrator rights are required for installation. | `0` — False; `-1` — True. |
| `Enabled` | Indicates the application's installation state. | Defaults to `0`. Set automatically. |
| `HideWinow` | Indicates whether the installer should be run in hidden mode. | `0` — False; `-1` — True. |
| `TranslatorPath` | Path to the Translator executable. | Empty by default. Set automatically. |
| `OutputExtension` | The file format into which the CAD system's geometry will be converted. | Specify the extension (for example, `SGF`, `IGS`, `STEP`). |
| `InputExtensions` | The file formats the Translator can import. When importing a file, the CAM system uses this tag to find the appropriate Add-in. | Usually the CAD system's native project extensions are specified here. Multiple extensions are separated by `.` (for example, `CDW.FRW.A3D`). |
| `CommandLine` | The command for import. Originally it was assumed the number of elements could vary, but in the end two were settled on. | Must be equal to `$(InFile) $(OutFile)`. |
| `CommandLineIsAppInst` | The command to check whether installation is possible. | Usually `IsInstalled`. |
| `CmdLnInstall` | The command to install the Add-in. | Usually `Install`. |
| `CmdLnUnInstall` | The command to uninstall the Add-in. | Usually `UnInstall`. |
| `HostApplication` | The CAD system's string identifier. Used by the Toolbar when transferring geometry to the CAM system — the CAM system uses it to find the registered Add-in. | Usually the value is duplicated from the `TranslatorName` tag. The key requirement is that it must be unique among the other Add-ins. |
| `DeprecatedHostApplications` | Old identifiers for backward compatibility with projects created in earlier versions of the CAM system. | A list of `<Item>` entries with the former `HostApplication` values. |
| `MinimalVersion` | The minimum CAD system version on which the Add-in can be installed. | A free-format string (for example, `v12`, `20+ x64`). |
| `CADPlatform` | Not used. | `xAny` by default. |
| `Description` | The description block shown in the Add-in wizard window. Split into sub-blocks with `LangCode` (locale, code page number) for display in different languages. | `<Item LangCode="1033">` — EN; `<Item LangCode="1049">` — RU. |
| `Copyright` | Copyright of the Add-in owner. | — |
| `HostCopyright` | Copyright of the CAD system. | — |
| `BuildInfo` | Build metadata (attributes `PackageID`, `PackageVersion`, `BuildNumber`). | Optional. |
