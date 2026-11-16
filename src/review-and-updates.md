# Review, updates and visibility

## Moderation

A moderator reviews every version before it reaches the store feed: the first version of an
extension and each new one. Until the first version is approved, the extension is not in the
catalog, in search or on the store feed of the CAM system. To try your build meanwhile, install
it from your machine (see [Build and test locally](local-testing.md#install-your-build)).

The moderator checks the card, the declarations and the package against the store rules (see
[Store rules and your obligations](store-rules.md)), and sets the category if it is missing.
Review aims to finish within 10 business days of a complete submission.

A rejection comes with a reason: the rule relied on, the facts, and what change would make the
extension publishable. You see it in **My published**. To resubmit, fix the extension and publish
it again; the same version number is fine, since a rejected version never reached the feed. A
rejection can also be appealed (see [Store rules and your obligations](store-rules.md#enforcement-and-appeals)).

## New versions

Increase the version and publish it the same way as the first one. It goes to the moderator too,
and the catalog keeps the previous version until the new one is approved. Then users see the
update on the **Extensions** tab of the CAM system.

**Versions on their way** in **My published** shows where each version is: **Submitted**,
**Approved · signing**, **Published**, **Rejected** with the reason, or **Withdrawn**. While a
version waits for review, **Withdraw** takes it back.

Without a new declaration and review, a new version must not:

- add, remove or move a capability between reserved functionality Domains;
- add a capability of a higher licence tier than the extension was published with;
- remove or weaken a licence check.

A published version cannot be replaced or removed: to fix a mistake, publish the next version.
Security fixes can be reviewed faster on request.

Keep the extension working with supported releases of the CAM system, and tell the store team at
least 60 days before you stop maintaining it.

## My published

**Account settings** → **My published** lists your extensions — your own, your organization's
and those you collaborate on, each group under its own heading — with the version, the date of
publication, the state and the price.

| State | Meaning |
|---|---|
| **on moderation** | The first version waits for a moderator |
| **rejected** | The reason is shown under the row; publish a new version to resubmit |
| **accepted, not in the catalog yet** | Accepted, but not yet on the feed |
| **published** | In the catalog |
| **hidden** | You removed it from the catalog |
| **hidden by a moderator** | A moderator took it off the catalog; only a moderator can return it |
| **building…**, **build failed** | The GitHub route; a failed build names the step and links to the log and the run |

**Version not taken from the feed** under a row explains why a new version is missing.

**Refused at submission** at the top lists the versions the store refused on the spot, before
moderation: what the store said, when, and how many attempts. The same mark appears under the row
of the extension. Fix what the message says and publish again (see
[Troubleshooting](troubleshooting.md#store-messages)).

The **needs attention** filter shows the rows that wait on you: failed builds, refused submissions,
rejections and extensions on moderation.

Actions in a row:

- **Install in ENCY** — for a free extension in the catalog: installs it in your CAM system,
  starting it if needed.
- **Download .nupkg** — the package of the latest version, to install from a file or to take to a
  machine without internet.
- **Change the category**.
- **History** — every version of the extension, its steps and refused submissions.
- **Collaborators** — invite co-authors (see [Organizations and collaborators](organizations.md)).
- **Move into an organization** — for your own extension (see
  [Organizations and collaborators](organizations.md#move-your-extension-into-an-organization)).
- **Remove from the catalog** and **Return to the catalog** (see
  [Hiding an extension](#hiding-an-extension)).
- The **Price** cell opens the price window: plans, trial and free licences for ENCY resellers and
  the ENCY team (see [Selling and payouts](paid-extensions.md)).

Everything else on the card — name, description, README, pictures — comes from the package and
changes only with a new version. Tags and the icon can also be changed with the next publication
(see [Package requirements](package-requirements.md#where-the-card-comes-from)).

## Hiding an extension

**Remove from the catalog** hides the extension from the catalog and search; the card opens by its
direct link marked **Unlisted**. Installed copies keep working, and users keep their licences, but
nobody new can buy it or take a trial. **Return to the catalog** brings it back.

If a moderator hid the extension, only a moderator can bring it back. A harmful extension can be
taken down for good: it stops downloading and selling, and every licence issued for it, bought
ones included, stops working.

Extensions and versions cannot be deleted from the store. After you leave the store, users keep
their licences, and you keep providing them with security and critical-defect fixes for 12 months
(see [Store rules and your obligations](store-rules.md#leaving-the-store)).
