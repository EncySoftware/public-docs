---
title: "Preparing for installation"
---

# Preparing for installation

## PC requirements

- **OS:** 64-bit Windows 7, 8, 10, 11, Windows Server 2012 or later. License server 4 is
  available only as a 64-bit version.
- **Permissions:** administrator rights are required to install and remove the server.
- **Network:** a connection to the local network and a static IP address or a PC name by
  which workstations find the server. This PC must be running while users work with network
  licenses.
- **Ports:** the server accepts TCP connections on ports in the range 10090–11000 by
  default (see [Ports and firewall](configuration.md#ports-and-firewall)).

## What to prepare

1. The server license file (`*.license`) received from the supplier. It lists the seats: for
   which products, versions and configurations, and how many. The supplier provides the
   workstation license files together with it (see [Workstation: configuration](clients.md)).
2. The hardware key the license is issued for (see
   [License protection](installation.md#license-protection)), or the login and password of the
   personal account for software activation.
3. The license server 4 installer:
   [NetLockServer4_x64.exe](https://download.encycam.com/download/netlockserver/NetLockServer4_x64.exe).
4. If license server 3 is installed on the PC, uninstall it: in **Apps** in Windows
   Settings, uninstall **Netlock server 3**. Two license servers on one PC interfere with
   each other: they use the same services and service ports.

