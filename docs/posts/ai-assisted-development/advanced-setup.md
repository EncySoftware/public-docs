# Advanced setup

Advanced setup is for teams that need repeatable context and controlled automation. It does not add capabilities that are not provided by the installed tools.

## Automatic, then manual setup

Run the installed CAM Agent or AI client's automatic setup/check first. Then
perform the read-only connectivity smoke tests described in the VS Code page.
If setup does not cover a component, configure it manually from the installed
release documentation. Record the client, CAM Agent, MCP services, and tool
versions; do not assume that a successful setup check means a postprocessor is
correct.

## Local documentation fallback

Keep a read-only checkout of `public-docs` near the development workspace. Point the assistant or tool at the smallest relevant module, such as `docs/posts/cldata`, `docs/posts/sppx`, `docs/posts/dotnet`, or this module. Record the checkout revision when documentation is used for a release decision.

## Controlled context

Separate source, test projects, generated NC output, and machine configuration. Use allowlisted workspace folders and exclude credentials, customer archives, and unrelated repositories. Prefer reduced CLData fixtures over full projects.

## Headless automation

Run headless checks in a disposable workspace with fixed inputs and captured logs. Give the process the minimum file permissions it needs. Review generated diffs and NC output outside the automation step. Do not connect headless automation directly to a CNC controller.

## Service boundaries

Keep CLData MCP read-only and use it for CLData evidence. Use InP MCP only for
the InP capabilities it advertises. Postprocessor Tools and DotNet Posts are
the postprocessor-specific tools; neither replaces simulation or human review.

## Future retrieval services

A RAG MCP could later retrieve versioned CLData, SPPX, .NET, and machine documentation. That service is outside this beta's boundary: it is not described as available, authoritative, or safe by default, and it must not silently replace local evidence. Until it is implemented and validated, local public-docs content and installed product documentation remain the fallback sources.
