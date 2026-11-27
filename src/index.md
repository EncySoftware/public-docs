---
title: "How the license server works"
---

# How the license server works

The license server distributes floating (network) licenses over the local network. The license
is stored on one PC — the server PC, while the applications run on workstations —
the users' PCs. An application can be started on any workstation of the network as long
as the server has a free seat: the number of application copies running at the same time is
limited by the number of seats in the license. The server and the application can also be
installed on the same PC.

1. The license server is installed on the server PC with the server license file. The
   license is protected by a hardware key or by software activation.
2. The application is installed on each workstation; the workstation license file is added in
   its license manager, and the server address is specified there.
3. On startup, the application takes a free seat on the server and releases it when it is
   closed.

## Products

One server serves all applications included in its license file:

| Product | Purpose |
|---|---|
| ENCY | CNC machine programming |
| ENCY Tuner | NC program tuning |
| Resource Manager | Enterprise resource management |
| MachineMaker | Building machine tool models |

The server is compatible with client applications of all versions, starting from V1.

## Workflow

1. [Preparing for installation](content/preparation.md) — PC requirements and what to
   prepare.
2. [Server PC: installation and activation](content/installation.md) — installing the server,
   the protection key, checking its state and activating a software license.
3. [Server PC: configuration](content/configuration.md) — the monitor, the **Settings**
   window, ports and firewall, license files, seat distribution and monitoring.
4. [Workstation: configuration](content/clients.md) — the workstation license file and the
   server address in the license manager.
5. [Workstation: checking ports](content/ports-check.md) — whether the server is reachable from
   the workstation.
6. [Troubleshooting](content/troubleshooting.md).
