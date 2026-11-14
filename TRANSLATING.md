# How to prepare a documentation translation

The source documentation is in the public [EncySoftware/public-docs](https://github.com/EncySoftware/public-docs) repository, in the [CAM/en/v3](https://github.com/EncySoftware/public-docs/tree/CAM/en/v3) branch.

Git records the history of file changes. GitHub hosts repositories and provides tools for reviewing proposed changes. You do not need to know every Git feature to prepare a translation.

## What you will do

You will create a copy of the source branch, translate the Markdown files, and submit the result in one of these ways:

- push it to your own branch or fork;
- open a pull request (PR) in \`EncySoftware/public-docs\`.

We will review the translation. After approval, we will build and publish it on our host, where it will be publicly available.

## Prepare your computer

1. Create an account at [github.com](https://github.com/) and sign in.
2. Install [GitHub Desktop](https://desktop.github.com/). It provides buttons for the main Git actions, so you do not need to type commands.
3. Install a Markdown editor, for example [Visual Studio Code](https://code.visualstudio.com/). Any editor that saves files as UTF-8 will work.

## Get a copy of the documentation

### Option A: GitHub Desktop (recommended)

1. Open the [CAM/en/v3 branch](https://github.com/EncySoftware/public-docs/tree/CAM/en/v3) and click **Fork**. A fork is your personal copy of the repository on GitHub.
2. In GitHub Desktop, select **File → Clone repository**, open the **GitHub.com** tab, select your \`public-docs\` fork, and choose a folder on your computer.
3. If GitHub Desktop asks to enable Git LFS, accept. Git LFS is required for large attachments such as images.
4. Select \`CAM/en/v3\` in the branch list and click **Fetch origin**. Use this copy as the starting snapshot for your translation.

### Option B: Download a ZIP archive

On the branch page, click **Code → Download ZIP** and unpack the archive. This is suitable for viewing the source or making a small translation. For a complete translation and for submitting changes, use GitHub Desktop so that the change history and attachments are handled correctly.

## Translate the files

1. In GitHub Desktop, create a separate branch: **Current branch → New branch**. Use a clear name agreed with the documentation maintainers.
2. Open the local repository folder in your editor.
3. Translate the text in the Markdown (\`.md\`) files. Preserve:
   - the folder structure and file names;
   - links, anchors, parameter names, commands, numbers, and units;
   - images and other files in \`assets\`;
   - Markdown headings and their order.
4. Do not translate technical identifiers, API names, or values that must match the application interface. If an interface label is unclear, keep the product label and ask about it in the PR.
5. Save files as UTF-8. Do not add information that is absent from the source or remove conditions and examples.
6. Review the changed files in GitHub Desktop. Make sure that only translation files and required localized images are included.
7. Enter a short summary, for example \`Add documentation translation\`, and click **Commit to <branch name>**.

## Submit the translation

### Push to your branch or fork

In GitHub Desktop, click **Push origin**. The changes will appear in your branch on GitHub. This is useful when you plan to translate in stages or want to show the work to colleagues first.

### Create a pull request in \`public-docs\`

1. After you push the branch, GitHub may show **Compare & pull request**. Click it. If it does not appear, open the **Pull requests** tab in \`EncySoftware/public-docs\` and select **New pull request**.
2. Select the base branch specified by the documentation maintainers. If you are unsure which branch to use, send the link to your fork or branch to the maintainers before creating the PR.
3. In the title, describe the translation and its scope, for example \`Add documentation translation\`. In the description, include:
   - which sections are translated;
   - which files or images are still untranslated;
   - questions about terminology or interface labels.
4. Click **Create pull request**. Reply to review comments in the PR discussion. Changes pushed to the same branch are added to the PR automatically.

For the GitHub web workflow, see [Creating a pull request from a fork](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request-from-a-fork).

## What happens after submission

The documentation maintainers check the file structure, links, images, terminology, and translation completeness. They may ask for specific corrections. After the changes are approved, we run the build and publication; no additional action is required from you.

## Frequently asked questions

**Do I need to know Git commands?** No. GitHub Desktop is sufficient for the usual workflow.

**Can I translate only one section?** Yes. List the translated pages in the PR description.

**Can I send the files by email?** A fork and PR are preferred because they preserve the change history and review discussion. If this is impossible, send the maintainers a link to the archive and the name of the source branch.

**What if the source documentation changes?** Before continuing, fetch the latest changes from the source branch with **Fetch origin** and mention this in the PR. Do not overwrite other changes without agreement.
