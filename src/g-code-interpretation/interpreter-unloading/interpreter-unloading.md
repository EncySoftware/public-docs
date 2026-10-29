# Interpreter unloading

**Unloading the interpreter from memory** consists of the following steps:

- Releasing the **INCT_Interpreter** interface;
- Freeing the memory of all objects that the library created itself or received from the CAM system during operation (calling the **NCT_FreeMemory** function of the library);
- Unloading the interpreter library from memory;
- Unloading the parent interpreters from memory (if any).

As a result of unloading, the memory of the created objects is freed, and the interpreter library and its parent interpreters are unloaded from memory.
