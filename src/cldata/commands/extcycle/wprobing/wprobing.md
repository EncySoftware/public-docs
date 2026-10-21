# EXTCYCLE WProbing - Probing cycle

`WProbing` is used for probing operations. It measures a part or tool based on one of the selected cycles using approach and return to the beginning of the cycle. Each cycle has its own toolpath, touch points and parameters on the basis of which further calculations are made.

`WProbing` stores parameters by code, and not by index, like other cycles of the `EXTCYCLE` command.

Below are examples of syntax for working:

Postprocessor (sppx):

```pascal
program ExtCycle
  if cld[1]=52 then begin ! Cycle call
    case cld[2] of
      500: begin ! All probing cycles
        case cmdPrm.Int[-2] of ! Probing cycle sub type
          11: begin ! My hole cycle P9814
            Output "G65 P9814 E" + cmdPrm.Flt[101] + " Q" + cmdPrm.Flt[102]
          end
          12: begin ! My boss cycle P9812
            Output "G65 P9812 E" + cmdPrm.Flt[101] + " Q" + cmdPrm.Flt[102]
          end
        end
      end
    end ! End of All probing cycles
  end
end
```

.NET postprocessor:

```csharp
public override void OnProbeExtCycle(ICLDExtCycleCommand cmd, CLDArray cld)
{
    if (!cmd.IsCall)
        return;
    switch (cmd.Prm.Int[-2]) // Cycle type
    {
        case 11: //My hole cycle P9814
            nc.WriteLine($"G65 P9814 E{cmd.Prm.Flt[101]} Q{cmd.Prm.Flt[102]}");
            break;
        case 12: //My boss cycle P9812
            nc.WriteLine($"G65 P9812 E{cmd.Prm.Flt[101]} Q{cmd.Prm.Flt[102]}");
            break;
    }
}
```

You can see a more detailed example of measurement cycles inside the distribution **Fanuc (30i)_Mill_DN.dll** postprocessor.

Subtype of probing cycles has "500" value.

cmd operator (parameters with a unique code) is described here.

## OnProbeExtCycle handler

Separate `OnProbeExtCycle` handler has been added for.net postprocessor which performs on EXTCYCLE CLData command for the probing cycles case (which SubCode is 500).

Declaration of `OnProbeExtCycle` handler:

```csharp
public virtual void OnProbeExtCycle(ICLDExtCycleCommand cmd, CLDArray cld)
```

## Parameters

| Type | Name | Description |
|---|---|---|
| ICLDExtCycleCommand | cmd | The current CLData command. |
| CLDArray | cld | The cld array of the command. |

More information about probing operations and cycles you can find in user manual.

## See also
- [Extended cycle (EXTCYCLE)](../extcycle.md)
- [CLData access model](../../../cldata.md)
