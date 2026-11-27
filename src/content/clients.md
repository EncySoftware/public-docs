---
title: "Workstation: configuration"
---

# Workstation: configuration

For the application on a workstation to get a license from the server, the workstation license
file is added to the workstation and the server address is specified. The supplier provides the
workstation license files together with the server license file.

## Configuring a workstation

1. Install the application, for example ENCY 3 or ENCY Tuner 3.
2. Open the [license manager](https://docs.encycam.com/ENCY/3/en/10025.html) of the application.
3. If the workstation license file is not in the list yet, click **Add**, select
   **I have license file** and choose the file. The license appears in the list with the
   **NetLock** protection type.
4. Select this license and click **Activate**.
5. In the **Server address** group, enter the **Hostname or Ip** of the server PC and the
   **Port** — the server's main port, 10100 by default. To find the server in the local network
   automatically, click **Find server**: the license manager polls the PCs of the network
   and fills in the address and port of the server it finds.
6. Click **Test connection** to make sure the server is reachable. If the server is not
   reachable, check the ports (see [Workstation: checking ports](ports-check.md)).
7. Click **Activate**.

On the next startup, the application connects to the server by itself and takes a seat (see
[Seat distribution](configuration.md#seat-distribution)).

## Where the server address is stored

The license manager saves the server address and port to the `stNLC.ini` file, a separate one
for each product and each of its versions, for example:

| Product | File |
|---|---|
| ENCY 3 | `C:\ProgramData\ENCY Software\ENCY\Version 3\stNLC.ini` |
| ENCY Tuner 3 | `C:\ProgramData\ENCY Software\ENCY Tuner\Version 3\stNLC.ini` |

These files are attached to a request to technical support (see
[The workstation does not see the network license](troubleshooting.md#the-workstation-does-not-see-the-network-license)).
