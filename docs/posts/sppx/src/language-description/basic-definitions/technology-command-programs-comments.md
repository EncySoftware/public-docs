# Technology command programs, comments

Postprocessor generates NC-program code using the files of technology commands (CLData). Briefly the process of postprocessing can be outlined as following:

1. A command is read from the file.
2. The command is analyzed, it's code and properties are determined and the built-in [CLD](predefined-variables-and-functions/miscellaneous-functions-and-variables.md) array and [predefined variables](predefined-variables-and-functions/readme-predefined-variables-and-functions.md) are initialized.
3. If a technology command program is enabled in the postprocessor and it's code is defined then it is called by the system. The technology command should contain the code to form the NC-program lines corresponding to the CLData.
4. If a mask is enabled and specified then the mask is used to form the NC-program code.

Technology command programs are coded on the task-oriented language and consist of mathematical expressions and functions, input/output operators, program flow control operators, subprogram call's, NC-program code output operators.

Technology command program starts with the [PROGRAM](../operators/processing-program-start-operator-program.md) keyword followed by the program name, the program ends with the **END** keyword. The name of the program is the same as the name of the CLData command which it processes. Technology command parameters are passed through the built-in [CLD](predefined-variables-and-functions/miscellaneous-functions-and-variables.md) array and special [Cmd](../../../../cldata/functions/current-command.md) operator. The detailed description of CLData commands and parameter values is found in the [Technology commands description](../../../../cldata/commands/commands.md) chapter.

Program code consists of operators and comments. It is possible to write multiple operators in a single line of code if you separate them with the `;` symbol. It is legal to carry operator code over a line if it's parts are logically incomplete.

Comments are useful to provide insight over some more complicated parts of your program. To place a comment type the `!` symbol and all the text after that symbol will be marked as a comment and thus ignored by the compiler. To comment/uncomment several lines, select the appropriate lines and press `Ctrl+!` or `Ctrl+/`.

It is also possible to comment out any part of the text by enclosing it in a pair of curly braces `{` - `}`. This way of commenting allows you to comment both an arbitrary part of a line and several consecutive lines, including lines commented out with the `!` symbol.

In the course of postprocessor execution the first technology program to be called is the **COMMON** program. Then the [PARTNO](../../../../cldata/commands/partno.md) program is executed, the [FINI](../../../../cldata/commands/fini.md) program is always the last.

The **COMMON** program is used to define global variables, that is all variables defined in the **COMMON** program are accessible in every part of the postprocessor. For their own needs, any program can use variables, not declared in **COMMON** and, therefore, are not publicly available. Such variables are called local.
