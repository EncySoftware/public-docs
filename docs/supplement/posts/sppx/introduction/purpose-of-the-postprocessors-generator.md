# The purpose of the postprocessors generator

Postprocessors generator is an application for operating systems of the Windows family.

The purpose of the postprocessors generator is the generation of [the postprocessor adjustment files](files-set-of-the-postprocessors-generator.md) to various NC-systems. These files are used by the run-time postprocessor system for the concrete NC-program generation.

It is necessary to perform the following steps to develop the postprocessor adjustment file:

- [Define the data about the NC-machine and CNC-system](../common-organization-of-the-work/main-window/machine-parameters/defining-the-data-about-the-nc-machine-and-cnc-system.md);
- [Describe the structure and the format of the block](../common-organization-of-the-work/main-window/block-structure-and-format-definition-register-list-forming.md) (form the list of registers);
- Design masks or programs to process technological commands;
- Save the postprocessor's tuning file.

The generation of new tuning files and the editing of existing files is allowed.

In addition to the work with data about NC-machine and CNC-system, there is the possibility of [the examination of the technological commands files](../common-organization-of-the-work/main-window/work-with-the-files-of-technological-commands.md) and the [trial generation of NC-programs](../common-organization-of-the-work/main-window/test-nc-code-generation.md) in the environment of the postprocessors generator.
