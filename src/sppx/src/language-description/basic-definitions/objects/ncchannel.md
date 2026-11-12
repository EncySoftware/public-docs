# NCChannel

The Channel object solves the problem of managing multiple channels simultaneously. Each channel manages its own isolated list of registers. The Activate procedure allows you to switch the currently active channel. The OutBlock, FormBlock, and Output procedures allow you to perform the appropriate functions for a channel without switching it to active mode.

## Parameters

- **FileName**: string
- **ChName**: string – channel name.

## Methods

- **Init** – object initialization.
- **Activate** – switching the channel to the current state.
- **OutBlock** – this statement forms the content of a block, corresponding to specified variable format, order, register format, and outputs the block into NC-program.
- **FormBlock** – this statement forms the block of NC-program according specified format, order and registers format. The block is formed in [OutStr$](../predefined-variables-and-functions/miscellaneous-functions-and-variables.md) variable without the output in the file of NC-program.
- **Output** – string output
- **IsActivCh** – is active channel, 1 - yes, 0 - no.
- **CloseFile** – fixing the state of the current file.

Registers access methods:

- **PutReg** – put value to register.
- **GetReg** – get value from register.
