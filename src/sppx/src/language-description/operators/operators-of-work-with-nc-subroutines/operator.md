# NCSUB.OUTPUTALL operator

Use `NCSUB.OUTPUTALL` to output all NC-subprograms. Like the [NCSUB.OUTPUT](operator-of-a-output-of-nc-subroutine.md) operator when called without parameters the `NCSUB.OUTPUTALL` operator translates all NC-subprogram CLData files, but unlike [NCSUB.OUTPUT](operator-of-a-output-of-nc-subroutine.md), `NCSUB.OUTPUTALL` can output all NC-subprograms into separate files.

**Syntax**

```
NCSUB.OUTPUTALL(<Mode>)
```

**Mode** – execution mode:

- 0 – works exactly like [NCSUB.OUTPUT](operator-of-a-output-of-nc-subroutine.md) without parameters;
- 1 – operator will save NC-subprogram texts in files named [NCSUB.NAME](operator-of-definition-of-a-name-of-nc-subroutine.md) for each subprogram respectively.

The files extension is defined by the postprocessor properties. NC-subprogram files will be saved into the folder of the main NC-program.

**See also**

[Operators of work with NC-subroutines](readme-operators-of-work-with-nc-subroutines.md)

[The operator of a output of NC-subroutine `NCSUB.OUTPUT`](operator-of-a-output-of-nc-subroutine.md)

[The operator of definition of a name of NC-subroutine `NCSUB.NAME`](operator-of-definition-of-a-name-of-nc-subroutine.md)
