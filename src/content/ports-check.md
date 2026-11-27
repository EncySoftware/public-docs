---
title: "Workstation: checking ports"
---

# Workstation: checking ports

If the license manager does not connect to the server or the application does not get a license,
check from the workstation that the server ports are reachable.

## Main port

In PowerShell on the workstation, run:

```powershell
Test-NetConnection <server_address> -Port 10100
```

Replace `<server_address>` with the name or IP address of the server PC, and if the main
port has been changed, use its number (see [Ports and firewall](configuration.md#ports-and-firewall)).
For example:

```powershell
Test-NetConnection 192.168.0.1 -Port 10100
```

`TcpTestSucceeded : True` means the port is reachable and the server service accepts
connections. `False` means the server service is not running or the port is closed by a
firewall.

Windows 7 has no `Test-NetConnection` command. There, turn on the **Telnet Client** Windows
feature and run `telnet <server_address> 10100`: if the port is reachable, an empty window
opens; otherwise, a connection error is shown.

## Server web page

Open the page `http://<server_address>:10090` in a browser on the workstation. If the
**License modules** page opens, the server is reachable over the network, and the page shows
which products the license contains and how many seats are free (see
[Monitoring web pages](configuration.md#monitoring-web-pages)).

## If the port is not reachable

1. Make sure the server service is running and the monitor title shows the **Ok** state (see
   [Server state](installation.md#server-state)).
2. Check the firewall rules on the server PC: if necessary, add them with the
   **Add rules in the Windows Firewall** item of the monitor context menu (see
   [Windows firewall](configuration.md#windows-firewall)).
3. If there is a firewall between the workstation and the server, open the server ports on it
   (see [Network firewall](configuration.md#network-firewall)).
4. Check that the server address and port in the license manager of the workstation match the
   server settings (see [Workstation: configuration](clients.md)).
