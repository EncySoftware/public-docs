# Troubleshooting

## DMC messages

| Message begins with | What to do |
|---|---|
| Saved. Still needed for Submit / Please fill in / Missing required fields | Fill in the fields it names. A submission needs **Product Name**, the machine's **Manufacturer**, **Machine Type**, **Product File** and **Price** (see [The card and links](the-card.md#fields-needed-to-submit)). |
| A submitted or published component must keep its Product File | Upload a replacement instead of removing the file. To remove it, take the component back to Draft first — **Revoke** it while it waits for review — or archive it. |
| This component was changed while you were editing it | Someone saved it after you opened the form. Close the form, open it again and repeat your change. |
| WebP pictures are not supported | Save the picture as PNG or JPEG and upload it again. |
| No image found inside the component archive | The archive holds no picture. Upload one to **Product Images**. |
| Cannot delete product with active licenses | A licence was issued for it, perhaps only a trial that has ended. **Disable** or **Archive** it instead; the licence holders keep it. |
| Queued — another import is running | One ZIP import of yours runs at a time. This one starts when the other finishes. |
| This kit's archive is built from its post and schema | DMC made the kit from your post processor and machine schema (see [Digital Machine Kits](kits.md#kits-dmc-makes-from-your-post-and-schema)). Upload the new archive to the post or the schema; the kit follows. |
| This post's archive is taken from its kit / This schema's archive is taken from its kit | DMC made the part from your kit (see [Digital Machine Kits](kits.md#parts-dmc-makes-from-your-kit)). Upload the new archive to the kit; the parts follow. |

## In the catalog and in ENCY

**A component is not in the catalog.** Only published components are. A submission waits for the
DMC team; check its status in **My published** (see
[Review, updates and testing](review-and-updates.md#publication-states)).

**A ZIP import skipped a folder.** It held no file DMC recognises (see
[Components and archives](components-and-archives.md#how-zip-import-tells-them-apart)).

**A licence holder still has the old archive.** ENCY looks for updated components when it starts
and applies them after a restart. Ask them to restart ENCY.

**A machine schema says Not tested.** Its check has not passed, has not reached it yet, or cannot
test this kind of machine yet (see [Review, updates and testing](review-and-updates.md#tested-in-ency)).
The DMC team can tell you which.

## Not sure

Ask the DMC team before you publish — about a name, a price, a component that does not fit any kind
above. See [Contacts](references.md#contacts) for the address.
