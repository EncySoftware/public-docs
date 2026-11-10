# Setting up the tools

The assistant does the setup itself. Your part is small: install an AI client, download the archive with the skills and give the assistant the instructions. The rest — putting the skills in place, checking the build and debugging tools, finding the installed CAM system — the assistant does by itself and reports the result. Only permissions and actions in program windows need you: permission to install missing programs; restarting the AI client if that is required; in the CAM system or ENCY Tuner — creating the interpreter in the **Create G-code interpreter** window, clicking the **Set ENCY file path** button in that window (in ENCY Tuner the button shows its own name), then signing out of Windows and signing in again, and turning on the log in the **System setup** window. The assistant will tell you about each of these actions when it comes to it.

## 1. Install an AI client

It is most convenient to work in Visual Studio Code: the interpreter is built and debugged in it as well (see [Interpreter debugging in Visual Studio Code](../dotnet/interpreter-debugging-in-visual-studio-code/interpreter-debugging-in-visual-studio-code.md)). A chat is an extension like any other: open the **Extensions** panel (`Ctrl+Shift+X`), find the one you need by name and install it. Any client will do, as long as you can allow it to read and edit files in the working folder and run commands there — for example, Kilo Code or Claude Code. Terminal-based clients have their own installation procedure.

You will need an account with an AI service provider — see [what it costs](index.md#what-it-costs).

A C# interpreter also needs [Visual Studio Code](https://code.visualstudio.com/Download) with the **C#** extension from Microsoft and the [.NET SDK](https://dotnet.microsoft.com/download) of the .NET version your product version runs on (see [Product versions](dotnet-workflow.md#product-versions)). You do not have to install them in advance: in step 3 the assistant checks what is missing and offers to install it — with your permission.

## 2. Download the skills

Download the [documentation archive](https://github.com/EncySoftware/public-docs/archive/refs/heads/Technical/Interpreters/en/v3.zip) and unpack it. All the content of the archive is in its root folder `public-docs-Technical-Interpreters-en-v3`, and the skills are in the `src/ai-assisted-development/skills/` folder inside it: six folders, each with a `SKILL.md` file.

## 3. Hand it over to the assistant

Open the working folder in Visual Studio Code (see [organizing the workspace](workspace.md)), open the chat, allow it to run commands in the working folder and give it the task. The skills are copied into your user folder (`%USERPROFILE%`), outside the working folder, so the client will ask for permission for that as well. Correct the paths (`<archive>` is the full path to the `public-docs-Technical-Interpreters-en-v3` folder of the unpacked archive) and paste:

```text
Set up the tools for interpreter development following the instructions in
<archive>\src\ai-assisted-development\advanced-setup.md
(the same page on the website: https://docs.encycam.com/technical/Interpreters/3/en/src/ai-assisted-development/advanced-setup.html)

Unpacked documentation archive: <archive>
The CAM system or ENCY Tuner is installed in: <installation folder>

Copy all the skills from the archive into this client's skills folder
for the user, not for the working folder,
check the .NET SDK and Visual Studio Code with the C# extension;
name whatever is missing and offer to install it.
Then tell me exactly what you changed and which skills you now see.
```

Clients pick up new skills in different ways: Claude Code — at once (if there was no skills folder before — after the `/reload-skills` command), Kilo Code — in a new session or after the `/reload` command, other clients — according to their documentation. If the client needs a restart, the assistant will tell you, since it cannot do that for you.

## 4. Check that everything worked

Two requests in the chat are enough. Both are safe: the assistant only reads and changes nothing.

**Checking the skills.** Write:

> Which skills for interpreter development do you see now, and which one will you start with?

A good answer lists six skills by their folder names and names `interpreter-development` first. If the assistant talks about "typical" skills or asks you to send files, the skills are not connected — go back to step 3 or to [advanced setup](advanced-setup.md).

**Checking program reading.** Put one or two real NC programs into the `programs` folder of the working folder and write:

> Read the NC programs in the `programs` folder and list which words occur in them and how they are spelled. Do not change anything.

A good answer is a list of words from your files: addresses, G- and M-functions, axis spellings such as `B90` and `B1=90`. If the answer contains words that are not in the programs, the assistant is reasoning from memory: point it to the files explicitly.

## 5. Updates

The skills are updated together with the documentation. When a new version is released, download the archive again and ask the assistant to replace the skill folders completely.

## If something does not work

[Troubleshooting](troubleshooting.md) collects typical symptoms. [Advanced setup](advanced-setup.md) gives the whole procedure in detail — it is the very page you gave to the assistant, so you can perform any step by hand and check what it did.
