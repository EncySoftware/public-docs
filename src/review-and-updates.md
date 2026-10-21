# Review, updates and visibility

## Moderation

A moderator reviews the first publication of each extension before it appears in the catalog.
While it waits, the card is marked **On moderation** and opens by its direct link, so you can
install it from the card and share the link with testers. It is not in the catalog and not on
the store feed of the CAM system.

The moderator checks the card, the declarations and the package against the store rules (see
[Store rules and your obligations](store-rules.md)), and sets the category if it is not set.
Review aims to finish within 10 business days of a complete submission. A rejection always comes
with a reason: the rule relied on, the facts, and what change would make the extension
publishable.

Follow the state on the website (see [Publication states](#publication-states)). Measures
against an already published extension come by email with a statement of reasons and can be
appealed (see [Store rules and your obligations](store-rules.md#enforcement-and-appeals)).

## Publication states

**My published** in your account lists your extensions with their version, publication date
and state:

- **on moderation** — a first publication waits for review.
- **rejected** — the reason is shown under the row and on the card. To resubmit, fix the
  extension and publish a new version.
- **accepted, not in the catalog yet** — the version is accepted but has not reached the feed.
- **published** — the extension is in the catalog.
- **hidden** — the extension is removed from the catalog.
- **building…** and **build failed** — for the GitHub route; a failed build shows the reason or
  links to the log and to the workflow run.

**Version not taken from the feed** under a row explains why a new version is missing from the
list. The **needs attention** filter shows the rows that require an action: failed builds,
rejections and extensions on moderation.

On the card itself, the same states appear as the **On moderation**, **Rejected** and
**Unlisted** marks.

## New versions

Increase the version and publish it the same way as the first one. A new version of an approved
extension appears in the catalog without waiting for a moderator, once the catalog indexes it,
usually within a few minutes. Users see the update on the **Extensions** tab of the CAM system.

Each version is still a submission under the store rules and can be reviewed after it appears.
A new version must not:

- add, remove or move a capability between reserved functionality areas without a new
  declaration;
- add a capability of a higher licence tier than the extension was published with;
- remove or weaken a licence check.

A published version cannot be replaced or removed. To fix a mistake, publish the next version.

Keep the extension working with supported releases of the CAM system, and tell the store team at
least 60 days before you stop maintaining it.

## What you can change without a new version

- **Category** — **Change the category** in **My published**.
- **Visibility** — hide the extension from the catalog or bring it back.
- **Repository** — the GitHub repository bound to the extension.

Everything else on the card — name, description, README, pictures, tags — comes from the
package and changes only with a new version.

## Hiding an extension

**Remove from the catalog** in **My published** hides the extension from search and the
catalog. The package stays on the feed, and installed copies keep working. You can bring the
extension back the same way.

If a moderator hid the extension, only a moderator can bring it back.

Extensions and versions cannot be deleted from the store. Users who already have the extension
keep their licences; after you leave the store, you keep providing them with security and
critical-defect fixes for 12 months (see
[Store rules and your obligations](store-rules.md#leaving-the-store)).
