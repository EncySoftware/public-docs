# The statement to form the block by mask MASK



The **Mask** statement forms the block of NC-code by mask string. According to the rules and output the string to the NC-program.

**Format**

```
MASK (<mask string>) {, OutBlock | FormBlock {, Poll}}
```

**Description**

The statement masks form the NC code line according to the rules that is described in the mask string.

Options OutBlock and FormBlock are mutually exclusive.

**Poll** option corresponds to the **Poll all registers** switch. See [Mask switches](../../postprocessor-masks/mask-management/mask-switches.md) topic for details.

- **OutBlock** corresponds to **Out Block** switch;
- **FormBlock** starts [OutStr$](../basic-definitions/predefined-variables-and-functions/miscellaneous-functions-and-variables.md) forming mode similar to [FORMBLOCK](block-forming-statement-formblock.md), without output to NC-text.

**Example**

```
! Form the NC code lines by mask
MASK(M[30]), OutBlock
MASK(% N[Off] ), OutBlock
MASK(G_INTERP[INTERP]X[CLD.X]Y[CLD.Y]Z[CLD.Z]), OutBlock, Poll
! Form NC-line in OutStr$ variable
MASK(G_INTERP[INTERP]X[CLD.X]Y[CLD.Y]Z[CLD.Z]), FormBlock, Poll
! OutStr$ holds formed NC-line
Output OutStr$
```
