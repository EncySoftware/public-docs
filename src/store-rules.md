# Store rules and your obligations

When you click **I Agree** at registration, you accept the Developer Agreement and the documents
incorporated into it. This page summarises what they ask of an author. It is a guide, not a
substitute: the documents themselves are binding, the English text prevails, and the links are in
[External references](references.md#store-terms).

## The documents

| Document | What it governs |
|---|---|
| Developer Agreement | The contract: licences, warranties, liability, fees, termination |
| Publishing Policy | Content, technical and commercial rules for extensions |
| Schedule A — Reserved Functionality | The capabilities licensed separately, and whether third parties may publish in them |
| Schedule B — Technical Requirements | Packaging, signing, entitlement checks, security, quality |
| Schedule C — Enforcement and Appeals | How decisions are taken, explained and appealed |
| Commercial Terms | Commission, prices, payouts, refunds, taxes for paid extensions |
| SDK Licence Terms | What the SDK may be used for |
| Trade Mark Guidelines | How to refer to the CAM system and its maker |

The documents may change. You get at least 15 days' notice by email and on the store website.
A material change has to be accepted again before your next submission (see
[Getting started](getting-started.md#register-as-a-developer)).

## Who may publish

- Companies and individuals may publish free extensions. Paid extensions are open to companies
  and to individuals acting for their trade, business or profession.
- Your details must be accurate and complete; registration includes sanctions and export-control
  screening.
- You must hold all rights to distribute the extension.
- Tell the store team within 15 days of any material change to your details, including a change
  of control of your business.

## What an extension must not do

- Infringe the rights of others, including the maker of the CAM system.
- Contain malware, spyware, cryptominers, backdoors or undisclosed code acting against the user.
- Circumvent, weaken, emulate or interfere with the licensing, activation, signing or anti-tamper
  mechanisms of the CAM system.
- Collect or send user data beyond what its privacy disclosure states.
- Misrepresent its origin, functions or compatibility, or suggest that the maker of the CAM
  system produced, endorsed or certified it.
- Be non-functional, unmaintained, or a duplicate of another of your extensions without a real
  difference.
- Produce machine-control output that bypasses the validation, simulation and collision checks of
  the CAM system where it provides them.
- Download, install, load or update code from anywhere other than its own package published in the
  store.

## The store is the only channel

An extension — any software that loads into the CAM system through its SDK, API or extension
interfaces — may reach users only through the store. You must not distribute it in any other way,
or offer any other store, repository, installer, loader or update mechanism for such software, or
any means of bypassing signature verification.

Loading your own unpublished builds on your own machines while you develop is allowed (see
[Build and test locally](local-testing.md)). To give an extension to a closed group only — an
internal tool or a build for one customer — ask the store team for a private listing.

This rule does not restrict software that does not load into the CAM system, such as a standalone
application or a tool that exchanges files with it through its import and export.

## Free means free

A free extension must be free in substance. You must not charge for it or for any of its
functions — through licence keys or subscriptions sold outside the store, payments inside the
extension, or a separately sold component without which it does not do what its card says. Paid
services that unlock nothing, such as consulting, training or custom development, and voluntary
donations are allowed. To charge, publish the extension as paid (see
[Paid extensions](paid-extensions.md)).

## Reserved functionality

Some capabilities of the CAM system are licensed to users separately: milling of each tier,
turning, EDM, nesting, additive, robotics, machine models, separately licensed CAD import and
others. Schedule A lists them as Domains.

- **Complementary extensions** — preparing inputs, processing outputs, automation, integration with
  other systems, post-processors, feature recognition, libraries, reports and similar — need no
  check and are encouraged. Schedule A lists what is expressly open.
- **Gated extensions** provide a capability inside a Domain. Each such capability must run only for
  a user who holds the licence Schedule A names for that Domain, checked through the
  entitlement-verification API of the SDK at every load and before every run (Schedule B §B.4). The
  licence for a lower tier does not unlock a higher-tier capability. The extension must be offered
  as an addition for licensed users, not as a way to avoid buying the module.
- Some Domains are closed to third-party implementations: simulation and collision detection, NC
  output verification, licensing, distribution of extensions, and cloud accounts.

Every submission declares the Domains the extension operates in (see
[Publishing](publishing.md#reserved-functionality)). Review checks what the extension actually
produces, not only the declaration.

Not sure whether your idea falls into a Domain? Ask the store team before you build. The written
answer comes within 20 business days and binds the store for 24 months, as long as your
description was complete and the extension does not change.

## Technical requirements

Schedule B sets the technical rules that review checks:

- **No outside code.** The extension runs only code from its own package and updates only through
  the store. Downloading data — tool libraries, cutting data, configuration — is allowed if that
  data is not executed.
- **Network.** All communication goes over TLS 1.2 or newer, to endpoints you disclose.
- **Credentials.** Tokens and passwords are kept only through the secure storage of the SDK.
- **Components.** Third-party and open-source components are disclosed with their versions and kept
  free of known critical vulnerabilities. Their licences must not impose copyleft obligations on
  users or on the CAM system.
- **Quality.** The extension does not crash or hang the CAM system, adds no more than 500 ms to its
  start, releases resources when unloaded, lets the user cancel long operations, and does not
  change settings or files of the CAM system outside its own scope.
- **Machine output.** Machine-control output passes the validation pipeline of the CAM system where
  one exists, and is never presented as verified or collision-free on the extension's own
  authority.
- **Text.** User-facing text is available at least in English and is kept out of the code, so that
  it can be translated.
- **Compatibility.** The extension works on a supported release of the CAM system: the current one
  or one of the two preceding major releases.

## Names and trade marks

- Your card must clearly show you as the publisher.
- Do not build the product name of the CAM system into the name of your extension or company in a
  way that suggests it comes from the maker: a name like *Nesting Pro for* followed by the product
  name is fine; the product name followed by *Nesting Pro* is not.
- Do not use the logo of the CAM system in your icon or branding, and do not imply endorsement or
  certification without a written agreement.
- You may say truthfully that the extension works with the CAM system, and you must say which
  licence a gated extension needs.

If you are unsure about a name, ask the store team; naming questions are answered within 5
business days.

## Your obligations as a publisher

- **End-user terms.** Users get your extension under your own licence terms, shown to them; without
  your own terms, the standard extension EULA of the store applies.
- **Privacy.** If the extension processes personal data, publish a privacy disclosure for it, for
  example in `readme.md`.
- **Support.** Support users as your card promises.
- **Maintenance.** Keep the extension working with supported releases, and tell the store team at
  least 60 days before you stop maintaining it.
- **Security.** Report a vulnerability, data breach or safety-relevant defect to the store's
  security address within 72 hours of discovery (see [Contacts](references.md#contacts)).

## Enforcement and appeals

If an extension breaks the rules, the store applies the least intrusive measure that addresses
the breach:

| Stage | Measure |
|---|---|
| 1 | Written notice with at least 30 days to fix |
| 2 | Removal from featured places and search promotion |
| 3 | No new installations; existing ones keep working |
| 4 | Removal from the store, with at least 30 days' notice |
| 5 | Termination of the agreement and closure of the account, with at least 30 days' notice |

- Every measure comes with a statement of reasons by email: the rule, the facts, what change would
  fix it, and how to appeal.
- New installations can be stopped at once if the extension appears to circumvent licensing.
- For malware, imminent security risks, licensing circumvention or other ways of installing
  components into the CAM system, the store acts immediately.
- A decision is never based on an extension competing with the products of the CAM system maker.
- You can appeal within 30 days. An appeal against removal or termination filed within 10 days
  stops the measure until the decision, except for immediate actions. The appeal is decided by
  someone not involved in the original decision, within 20 business days.
- Complaints about any decision go to the store team and are answered within 20 business days.

See [Contacts](references.md#contacts) for the addresses.

## Leaving the store

You may withdraw an extension from new distribution at any time (see
[Review, updates and visibility](review-and-updates.md#hiding-an-extension)) and terminate the
agreement with 30 days' notice. Licences users already have keep working, and you keep providing
security and critical-defect fixes to them for 12 months.
