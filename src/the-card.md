# The card and links

The card is what customers see: the component's name, picture, machine, controller, access and the
components it goes with. You fill it in the **New Asset** form — **Upload asset** in
**My published** — and change it later in the same form, opened with **Edit**.

## General

| Field | Notes |
|---|---|
| **Product Name** | A short name with the model, for example `Makino a81M`. |
| **Product** | The kind: Post Processor, Machine Schema, Interpreter or Digital Machine Kit. It decides which file the form takes and which groups it shows. |
| **Description** | Plain text; line breaks are kept. **✦ AI Description** writes one from the card's fields; **Hint** steers it, in up to 1000 characters. |
| **Product File** | The component itself (see [Components and archives](components-and-archives.md)). |
| **Product Images** | PNG, JPEG, GIF or BMP. The first one is the cover; drag the thumbnails to change the order. WebP is not accepted. |

## Machine and controller

- **Machine**: **Manufacturer**, **Series**, **Model**, **Machine Type** (Milling, Mill Turn, Turn,
  Wire EDM, Swiss, Additive, Gas/Plasma/Laser or Other), **Axes** (2 to 9) and **Units** (Metric,
  Inch or both).
- **Travel X**, **Travel Y**, **Travel Z** (mm) and **Equipment** — on machine schemas and kits.
  They are filled from the schema when you upload it, and you can correct them; the refresh button
  next to the travels reads them from the file again.
- **Controller**: **Manufacturer**, **Series** and **Model**, for example `Fanuc`, `30i`, `30i-B`.

Customers filter the catalog by these fields, so fill them in where the form does not insist:
a post processor with no controller is hard to find.

## Pricing & Software

- **Price**: **Generic**, **With Maintenance**, or **Paid** with an amount in €. What each one gives
  customers is in [Access, prices and licences](licences-and-prices.md).
- **ENCY ver**: the ENCY versions the component works with — **1**, **2**, **3**, one or several.
- **Experience**: how you tested it — **Not tested**, **Tested in simulation** or
  **Tested on real equipment**.

## Samples

Samples show what a component produces. Customers download them with a licence or a trial.

- **G&M Codes File** — the G and M codes the component supports: post processors, interpreters and
  kits.
- **NC File** — an example NC program: post processors and kits.

Machine schemas have no samples.

## What DMC fills in for you

- **Publisher** — your company's name, from your account. An account without a company can leave
  the card with no publisher, and the catalog's **Publisher** filter then misses the component: tell
  the DMC team (see [Contacts](references.md#contacts)).
- **Travels and Equipment** — from the machine schema.
- **Samples** — from the `<name>_g-and-m.zip` and `<name>_NCcode.nc` files that come with the post
  (see [Components and archives](components-and-archives.md#post-processor)). Only empty fields are
  filled: a sample you set is never replaced, and one you removed comes back only with a new archive
  that carries it.
- **Cover** — see [Covers](#covers).
- **Tested in ENCY** — from DMC's own check (see
  [Experience and Tested in ENCY](#experience-and-tested-in-ency)).

## Covers

The first picture in **Product Images** is the cover. Without one:

- A machine schema's or a kit's archive holds the picture ENCY saves beside the schema. A ZIP
  import puts it on the card by itself; in the form, click **Image from archive**.
- A post processor or an interpreter gets the control maker's logo: a post is made for a control,
  not for one machine.
- In a ZIP import with **Generate cover image** on, a component with neither gets an AI picture.

A machine schema or kit with a 3D model can also take a picture drawn from it,
**Image from 3D model**. **✦ AI Image** draws a cover when you ask for one.

## Experience and Tested in ENCY

Two fields say how a component was tested:

| Field | Values | Set by |
|---|---|---|
| **Experience** | Not tested, Tested in simulation, Tested on real equipment | You, in the form. |
| **Tested in ENCY** | Passed, Not tested | DMC's own check in ENCY, on machine schemas and kits (see [Review, updates and testing](review-and-updates.md#tested-in-ency)). You cannot set it. |

## Links to other components

A link joins two components that belong together, such as a post processor and the machine it was
made for. It shows on the cards of both, so you set it once, from either side. Links are saved with
the form.

| On a… | Fields |
|---|---|
| Machine Schema | **Suitable post processors**, **Suitable interpreters**, **Part of kits** |
| Post Processor or Interpreter | **Made for** — the machine schemas it was written for, where it is then recommended. **Part of kits**. |
| Digital Machine Kit | **Kit contents** — the components the kit holds. |

- **Part of kits** offers only your own kits: what a kit holds is the kit's to decide.
- DMC makes a Digital Machine Kit of a post processor and a machine schema of yours linked to each
  other, once both are published (see [Digital Machine Kits](kits.md#kits-dmc-makes-from-your-post-and-schema)).
- Besides your links, a machine schema's card shows **Auto-matched** post processors, found by
  control and machine type, and a post processor's card the machine schemas of the machine it
  names. You do not set them.

To link many components at once, use **Link…** in **My published** (see
[Publishing](publishing.md#many-components-at-once)).

## Fields needed to submit

A draft saves with a name alone. To go to review, a component needs five fields: **Product Name**,
the machine's **Manufacturer**, **Machine Type**, **Product File** and **Price**. When you save a
draft without them, the form marks them red and says what is still needed.
