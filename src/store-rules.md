# Store rules and your obligations

When you click **I Agree**, you accept the Developer Agreement and the documents incorporated into
it. This page summarises what they ask of an author. It is a guide, not a substitute: the
documents themselves are binding, the English text prevails, and the links are in
[External references](references.md#store-terms).

## The documents

| Document | What it governs |
|---|---|
| Developer Agreement | The contract: licences, warranties, liability, fees, termination |
| Publishing Policy | Content, technical and commercial rules for extensions |
| Schedule A — Reserved Functionality | The capabilities licensed separately, and whether third parties may publish in them |
| Schedule B — Technical Requirements | Packaging, entitlement checks, security, quality |
| Schedule C — Enforcement and Appeals | How decisions are taken, explained and appealed |
| Commercial Terms | Commission, prices, payouts, refunds, taxes for paid extensions |
| SDK Licence Terms | What the SDK may be used for |
| Trade Mark Guidelines | How to refer to the CAM system and its maker |

The documents may change, with notice by email and on the store website:

| Change | Notice |
|---|---|
| Most changes | At least 15 days |
| Commission | At least 60 days |
| A new area in Schedule A | At least 30 days |
| An area removed from Schedule A | Takes effect on publication |
| Required by law, or by an imminent security or fraud risk | Can take effect at once |

Changes do not apply backwards. A material change must be accepted before your next submission;
for other changes, publishing after the effective date counts as acceptance. You may terminate the
agreement during the notice period instead.

## Who may publish

- Companies and individuals may publish free extensions. Paid extensions are open to companies
  and to individuals acting for their trade, business or profession.
- Your details must be accurate and complete. Registration includes sanctions and export-control
  screening; developers established in or controlled from a sanctioned jurisdiction cannot
  publish.
- Whoever accepts the terms for a company confirms they may bind it.
- You must hold all rights to distribute the extension.
- Tell the store team within 15 days of any material change to your details, including a change
  of control of your business. Moving your extensions to another party — for example, from you to
  your company — needs the store's consent.

## What an extension must not do

- Infringe the rights of others, including the maker of the CAM system.
- Contain malware, spyware, cryptominers, backdoors or undisclosed code acting against the user.
- Circumvent, disable, weaken, emulate, replace or interfere with the licensing, activation,
  entitlement enforcement, signing or anti-tamper mechanisms of the CAM system, or help anyone do
  so.
- Collect or send user data beyond what its privacy disclosure states.
- Misrepresent its origin, functions or compatibility, or suggest that the maker of the CAM
  system produced, endorsed or certified it.
- Be non-functional, unmaintained, or a duplicate of another of your extensions without a real
  difference.
- Produce machine-control output that bypasses the validation, simulation and collision checks of
  the CAM system where it provides them.
- Download, install, load or update code from anywhere other than its own package published in the
  store.
- Break the law, including export-control, sanctions, competition and consumer-protection law.

## The store is the only channel

An extension — any software that loads into the CAM system through its SDK, API or extension
interfaces — may reach users only through the store. You must not distribute it in any other way,
or offer any other store, repository, installer, loader or update mechanism for such software, or
any means of bypassing signature verification.

Registered developers may load their own unpublished builds on their own machines while they
develop (see [Build and test locally](local-testing.md)); this must never become a way to hand
builds to users. To give an extension to a closed group only — an internal tool or a build for one
customer — ask the store team for a private listing.

The rule does not cover software that does not load into the CAM system, such as a standalone
application or a tool that exchanges files with it through import and export. The SDK itself,
however, may be used only for software distributed through the store, unless the store agrees in
writing.

## Free means free

A free extension must be free in substance. You must not charge for it or for any of its
functions — through licence keys or subscriptions sold outside the store, payments inside the
extension, or a separately sold component without which it does not do what its card says. Paid
services that unlock nothing, such as consulting, training or custom development, and voluntary
donations are allowed. To charge, sell the extension through the store (see
[Selling and payouts](paid-extensions.md)).

## Reserved functionality

Some capabilities of the CAM system are licensed to users separately. Schedule A lists them as
Domains: milling of each tier, turning, EDM, nesting, additive, robot programming, machine models,
Tuner, Hyper, direct import of native SolidWorks files, and others. The list is descriptive, not
exhaustive: a capability that the maker licenses separately is reserved even before it appears in
Schedule A.

- **Complementary extensions** — preparing inputs, processing outputs, automation, integration with
  other systems, post-processors, feature recognition, libraries, reports and similar — need no
  check and are welcome. Import of neutral formats such as STEP, IGES and Parasolid, and of native
  formats of other CAD systems, is open. A post-processor that turns 3-axis data into simultaneous
  multi-axis motion, however, falls into the Domain of that motion.
- **Gated extensions** provide a capability inside a Domain. Each such capability must run only for
  a user who holds the licence Schedule A names for that Domain, checked through the
  entitlement-verification API of the SDK at every load and before every run. A licence for a
  lower tier does not unlock a higher-tier capability, and a licence for one Domain does not unlock
  another. A gated extension is an addition for licensed users, not a way to avoid buying the
  module; it may be free or paid on top of the user's licence.
- **Closed Domains** take no third-party implementations: machining simulation and collision
  detection, NC output verification, licensing and anti-tamper, distribution and loading of
  components (the store, its payments and signature verification), and cloud accounts. Extensions
  that complement them remain welcome.

Every submission declares the Domains the extension works in (see
[Publishing](publishing.md#reserved-functionality)). Review checks what the extension actually
produces, not only the declaration.

Not sure whether your idea falls into a Domain? Ask the store team before you build. The written
answer comes within 20 business days and binds the store for 24 months, as long as your
description was complete and accurate and the extension is not changed, configured or marketed in
a way that would change the answer. Later changes to Schedule A do not reverse it.

## Technical requirements

Schedule B sets the technical rules that review checks:

- **No outside code.** The extension runs only code from its own package and updates only through
  the store. Downloading data — tool libraries, cutting data, configuration — is allowed if that
  data is not executed.
- **Network.** All communication goes over TLS 1.2 or newer, to endpoints you declare.
- **Credentials.** Tokens and passwords are kept only in the secure storage of the SDK.
- **Licence checks.** A gated extension checks the licence through the SDK; a successful check may
  be cached for up to 72 hours on that installation only. When a check fails, the user gets a clear
  message naming the licence needed, and functions that need no licence keep working.
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

When Schedule B changes in a way that requires changes to published extensions, you get at least
90 days to adapt.

## Names and trade marks

- Your card must clearly show you as the publisher.
- Do not build the product name of the CAM system into the name of your extension, company,
  domain or social handle in a way that suggests it comes from the maker: *Nesting Pro for*
  followed by the product name is fine; the product name followed by *Nesting Pro* is not.
- Do not use the logo of the CAM system in your icon or branding, and do not imply endorsement or
  certification without a written agreement.
- You may say truthfully that the extension works with the CAM system, and you must say which
  licence a gated extension needs.

If you are unsure about a name, ask the store team; naming questions are answered within 5
business days.

## Your obligations as a publisher

- **End-user terms.** Users get your extension under your own licence terms, which must not
  conflict with the store rules or with the user's licence of the CAM system; without your own
  terms, the Standard Extension EULA applies.
- **Privacy.** If the extension processes personal data, publish a privacy disclosure for it, for
  example in `readme.md`.
- **Support.** State on the card how users reach you and how fast you answer, and keep to it.
- **Maintenance.** Keep the extension working with supported releases, and tell the store team at
  least 60 days before you stop maintaining it.
- **Security.** Report a vulnerability, data breach or safety-relevant defect to the store's
  security address within 72 hours of discovery (see [Contacts](references.md#contacts)).

## Enforcement and appeals

If an extension breaks the rules, the store applies the least intrusive measure that addresses
the breach. Stages need not follow in order:

| Stage | Measure |
|---|---|
| 1 | Written notice with at least 30 days to fix |
| 2 | Removal from featured places and search promotion |
| 3 | No new installations; existing ones keep working |
| 4 | Removal from the store, with at least 30 days' notice |
| 5 | Termination of the agreement and closure of the account, with at least 30 days' notice |

- Every measure, and every refusal at review, comes with a statement of reasons: the rule, the
  facts, what change would fix it where one is possible, and how to appeal.
- New installations can be stopped at once, pending investigation, if the extension appears to
  circumvent licensing.
- The store acts immediately against malware, imminent security risks, licensing circumvention and
  other ways of installing components into the CAM system, and where the law or a credible
  infringement notice requires it; the reasons may follow afterwards.
- A decision is never based on an extension competing with the products of the CAM system maker
  or reducing its revenue.
- Three or more confirmed measures of stage 3 and above for similar breaches within 12 months may
  lead straight to removal or termination.
- You can appeal any decision within 30 days, free of charge. The appeal is acknowledged within 5
  business days and decided within 20 business days after that, by someone senior to the original
  decision-maker and not involved in it. An appeal against removal or termination filed within 10
  days stops the measure until the decision, except for immediate actions.
- Complaints about how the store treats you are acknowledged within 5 business days and answered
  within 20.

See [Contacts](references.md#contacts) for the addresses.

## Leaving the store

You may withdraw an extension from new distribution at any time (see
[Review, updates and visibility](review-and-updates.md#hiding-an-extension)) and terminate the
agreement with 30 days' notice. On termination:

- your extensions leave the store, and no new installations happen;
- licences users already have keep working, and for 12 months you keep providing them with
  security and critical-defect fixes, or help the store hand the extension over in an orderly way;
- what the store owes you is paid in the next payout, whatever the balance;
- your account stays open for 90 days so that you can export your data.
