# G-code based program interpretation

Interpretation of the NC program text generated for operations consists of the following stages:

1. Before interpreting the NC program text of the first operation, the CAM system kernel [loads the interpreter into memory and initializes it](interpreter-loading-and-initialization/interpreter-loading-and-initialization.md).
2. For each operation, [the NC program text is translated and interpreted](translation-and-interpretation/translation-and-interpretation-g-code-based-program.md).
3. After interpreting the last operation, [the CAM system unloads the interpreter from memory](interpreter-unloading/interpreter-unloading.md).

How to use already developed interpreters to interpret the NC program text of other, similar controllers is described in the [Interpreter inheritance](interpreter-inheritance/interpreter-inheritance.md) article.

The list of interfaces used and implemented in the interpreter is given in the [List of used types](interfaces/list-of-used-interfaces.md) section.

How to manage logging of the NC program text interpretation is described in the [Log interaction with the interpreter](log-interaction-with-the-interpreter/log-interaction-with-the-interpreter.md) section.
