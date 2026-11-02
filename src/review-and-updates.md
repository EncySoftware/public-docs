# Review, updates and testing

## Moderation

The DMC team reviews every submission before it reaches the catalog, and accepts it (Published) or
rejects it (Rejected). DMC records no reason with a rejection: fix what you can see, or ask the DMC
team (see [Contacts](references.md#contacts)), and submit again.

Kits that DMC makes from your components, and the parts it makes from your kits, go through the
same review (see [Digital Machine Kits](kits.md)).

## Publication states

**My published** shows each component's status:

| Status | Who sees it | What it means |
|---|---|---|
| **Draft** | You and the DMC team | Work in progress. Every new component starts here. |
| **Pending Review** | You and the DMC team | Submitted and waiting for the DMC team. |
| **Published** | Everyone | In the catalog, and customers can get licences for it. |
| **Rejected** | You and the DMC team | Turned down. Fix it and submit it again from **Actions**. |
| **Disabled** | You and the DMC team | Taken out of the catalog. Licences already issued keep working. |
| **Archived** | You and the DMC team | Put away. **Unarchive** returns it to Draft. |

You move a component with its **Actions** menu; **Submit** and **Archive** are also at the bottom of
the form:

- Draft, Rejected or Disabled → **Submit** → Pending Review. For a rejected component, **Submit**
  is in **Actions** only.
- Pending Review → **Revoke** → Draft, to take it back before the review.
- Published → **Disable** → Disabled.
- Any status → **Archive** → Archived; **Unarchive** → Draft.
- **Delete** removes a component and its files for good — only if no licence was ever issued for
  it, not even a trial that has ended. Otherwise **Disable** or **Archive** it instead.

## Tested in ENCY

DMC tries every machine schema and Digital Machine Kit in ENCY by itself — after every new archive
(an upload, a replacement, a ZIP import), and the whole published catalog in turn. It fits ENCY's
test parts to the machine, calculates and simulates them; when every operation runs clean, the card
says **Tested in ENCY: Passed**.

- When the check does not pass, or cannot test that kind of machine yet, the card says
  **Not tested**. Why it did not pass is seen by the DMC team; ask them (see
  [Contacts](references.md#contacts)).
- A kit is tried by its machine schema.
- Post processors and interpreters are not tried, and their cards have no such row.
- Editing the card without a new archive does not repeat the check.

## Updating a published component

You can edit a published component at any time. The changes go live when you save, with no second
review.

That includes a new **Product File**, and every licence holder gets it: ENCY looks for updated
components each time it starts, downloads them and applies them after a restart. Try a new archive
in your ENCY before you upload it over a published one. A machine schema's new archive is also read
again — travels, equipment, 3D model — and tried in ENCY again.

DMC keeps the archives you replace, the last five of each component, and the DMC team sees every
replacement of a published one. If a new archive turns out wrong, upload a fixed one, or ask the DMC
team to put back an earlier one.

A component that is pending review, published or disabled must keep its file: removing it is
refused. Upload a replacement instead. To remove the file, take the component back to Draft first —
**Revoke** it while it waits for review — or archive it.
