# Interpretation of the NC-code

Interpretation is the process of converting the NC program text, its words and blocks, into [CLDATA technological commands](https://docs.encycam.com/Inp/2/en/10088.html) that form the tool path. During interpretation, the CAM system uses the interpreter selected for the machine and:

- reads the NC program blocks one by one;
- using the register information received from the interpreter, extracts words (or semantic constructs) from the NC program block or lets the interpreter extract the words itself;
- passes the words to the interpreter in the order in which they appear in the block;
- the interpreter, taking into account the features of the machine, converts the NC program words into CLDATA technological commands that form the restored tool path.

The interpreter is described in the [Interpreter structure](../interpreter-structure/interpreter-structure.md) section.

The interaction of the CAM system with the interpreter to obtain the secondary (restored) tool path is described in the [G-code based program interpretation](../g-code-interpretation/g-code-based-program-interpretation.md) section.
