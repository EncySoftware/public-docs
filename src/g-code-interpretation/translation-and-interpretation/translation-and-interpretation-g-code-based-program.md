# G-code based program Translation and Interpretation

**Interpretation of the NC program text.**

Until the NC program blocks run out or the interpreter library sets the end-of-program flag (the **INCT_Interpreter.EndOfProgram** method), the CAM system reads the NC program blocks and performs the following steps for each block:

- Translation of the NC program block (analysis of the block for familiar constructions — objects to interpret);
- If the block translation has produced at least one object in the list of objects to interpret of the current block (i.e. the list of objects to interpret **[INCT_BlockExecArray](../sprutcam-interfaces/basic-interfaces/list-of-objects-to-interpret/list-of-objects-to-interpret.md)** is not empty), each object from the **[INCT_BlockExecArray](../sprutcam-interfaces/basic-interfaces/list-of-objects-to-interpret/list-of-objects-to-interpret.md)** list is interpreted in turn;
- The list of objects to interpret of the current block is cleared.

**Translation of the NC program block.**

Until the block characters run out, the CAM system performs the following steps:

- The unprocessed part of the block is passed to the interpreter library (i.e. at the first step the whole block is passed). In response, the CAM system expects to receive the number of characters **from the beginning of the passed string** that the interpreter has recognized as a separate word or another construction it understands (the **INCT_Interpreter.TransLine** method). The recognized characters are considered processed and are removed from the block. This step is repeated while the interpreter recognizes meaningful constructions (words) at the beginning of the rest of the block, i.e. returns to the CAM system a number of recognized characters greater than zero, or until the block ends.
- As soon as the interpreter fails to recognize a meaningful construction at the beginning of the rest of the block, the CAM system tries to determine the register and its value by the algorithm described in [this article](algorithm-for-determining-register-and-values-in-g-code-block/algorithm-for-determining-register-and-values-in-g-code-block.md).
- If the register has been determined, it is added to the end of the list of objects to interpret of the current block (**[INCT_BlockExecArray](../sprutcam-interfaces/basic-interfaces/list-of-objects-to-interpret/list-of-objects-to-interpret.md)**, with the **register** flag). Otherwise the read and unrecognized part of the block is skipped, but it is also considered processed and is removed from the beginning of the rest of the block;

**Note.**

To recognize meaningful constructions of the block, we recommend using, wherever possible, the CAM system mechanism for determining registers and values ([Algorithm for determining the register and values in the G-code block](algorithm-for-determining-register-and-values-in-g-code-block/algorithm-for-determining-register-and-values-in-g-code-block.md)), and processing in the interpreter (in the **INCT_Interpreter.TransLine** method) only those constructions that the CAM system mechanism cannot recognize or recognizes inefficiently. In this case the routine work of determining typical constructions is done by the CAM system kernel, and the interpreter handles rare cases of meaningful constructions that do not fit the general rules of the algorithm.

**Note.**

After the interpreter has recognized a word or a meaningful construction, it can store the information about it itself (using its own internal data structures) or use the list of objects to interpret of the current block (**[INCT_BlockExecArray](../sprutcam-interfaces/basic-interfaces/list-of-objects-to-interpret/list-of-objects-to-interpret.md)**), i.e. add its own item with the **object** or **register** flag to the list. We recommend the second option: in this case the order of objects in the block is preserved regardless of how the object was determined — by the CAM system kernel or by the interpreter.

**Interpretation of the objects in the list of objects to interpret** consists of the following steps:

- Before the list of objects is interpreted, the **INCT_Interpreter.BeforeInterprete** method is called; it informs the interpreter that interpretation of the current block begins;
- For each item of the list, if its **IsUsed** flag is not set and the end-of-translation flag (**INCT_Interpreter.EndOfProgram**) is not set, the **INCT_Interpreter.Interprete** method is executed. Then the **IsUsed** flag is set for the interpreted item of the list;
- After the whole list of objects has been interpreted, the **INCT_Interpreter.AfterInterprete** method is called; it informs the interpreter that interpretation of the current block is complete;

**Note.**

When executing the **INCT_Interpreter.Interprete** method, the interpreter must determine the type of the passed object and add the corresponding command to the list of CLDATA commands.

For example, if the object passed **for the Fanuc controller** is a register with the address **F** (feed), you need to execute the **[INCT_CLData](../sprutcam-interfaces/basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md).OutFeed** method and pass the register value as the parameter.
