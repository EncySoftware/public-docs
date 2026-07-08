# CAMInfo.ini file

The `CAMInfo.ini` file contains the current settings of the CAM system that are used by Add-ins. The file is created automatically during a scan by the Add-ins Wizard in the directory of each Add-in. If necessary, the list can be extended with new parameters.

**Example CAMInfo.ini file:**

```ini
[CAM]
CAMName=<Product_name> <Product_version>
CompanyName=<Company_name>
CompanyURL=<company_website>
CAMPath=C:\Program Files\<Company_name>\<Product_name>\Bin64\<CAM>.exe
CAMLinearMeasure=lmMillimetre
CAMCfgPath=C:\Users\<User>\AppData\Roaming\<Company_name>\<Product_name>\<Product_version>
LanguageID=1049
CompanyLocalizedName=<Company_name>
```

**Parameter descriptions.**

| Parameter | Description |
|----------|----------|
| `CAMName` | The official name of the installed product. |
| `CompanyName` | The official company name. Since different companies are used for different markets, it is better to use `CompanyLocalizedName`. |
| `CompanyURL` | Link to the website. |
| `CAMPath` | Path to the CAM system's executable file. |
| `CAMLinearMeasure` | The current units of measurement. Possible values: `lmMillimetre`, `lmCentimetre`, `lmDecimetre`, `lmMetre`, `lmInch`, `lmFoot`. |
| `CAMCfgPath` | Path to the settings file. |
| `LanguageID` | The current encoding number used in the CAM system (LCID). |
| `CompanyLocalizedName` | The localized company name. |
