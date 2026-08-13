# Troubleshooting

## The extension is not available

Confirm that CAM Agent was installed from the CAM Agent Extension Store, restart the host application, and check extension and host versions. If the Store is unavailable, do not install an unverified package; use the documented local workflow instead.

## The agent cannot read the project

Check the selected workspace, file permissions, and the active windowed or headless role. Reduce the request to a small readable file. A headless role cannot use UI-only context.

## The answer uses the wrong API

State whether the target is SPPX or .NET and provide the relevant existing source. For .NET, include the copied template's project files and installed SDK information. For SPPX, include the mask or program and the expected register behavior.

## Documentation is missing

Use the local `public-docs` checkout as a fallback and note its revision. It may not contain release-specific or private material. Verify version-sensitive details against the installed product and SDK.

## The generated code builds but output is wrong

Inspect the first differing NC block and trace it to the CLData command and handler. Check units, coordinate transforms, modal state, tool compensation, and omitted commands. Reproduce with the smallest input that shows the error, then run simulation before accepting a fix.

## RAG MCP is unavailable

This beta guide does not require a RAG MCP. Use local documentation and explicit files instead. Do not claim that an index, retrieval service, or automatic project graph exists unless it is installed and has been verified.
