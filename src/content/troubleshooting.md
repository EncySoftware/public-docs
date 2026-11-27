---
title: "Troubleshooting"
---

# Troubleshooting

## The server service does not start

If the **NetLock Service 4 x64** service stays in the Starting state in the Windows **Services**
console or stops:

1. Make sure that the **License files list** in the monitor's **Settings** window contains the
   server license file.
2. If the license is issued for a hardware key, make sure the key is connected and detected
   (see [Protection key not found](#protection-key-not-found)). If the license uses software
   protection, make sure it is activated (see
   [Software activation fails](#software-activation-fails)).
3. Make sure the server ports are not occupied by another program and a second server instance
   is not running (see [Port busy at startup](#port-busy-at-startup)).
4. Enable the server log (see [Log](configuration.md#log)), restart the service and look for
   errors in `*.log`.

## The workstation does not see the network license

1. Make sure the server is running: the **NetLock Service 4 x64** service is in the Running
   state, and the monitor title shows the **Ok** state (see
   [Server state](installation.md#server-state)).
2. Check that the server license includes the product and version of the workstation, for
   example ENCY Tuner 3 or ENCY 3: in the monitor or on the web page
   `http://<server_address>:10090`.
3. Check that the workstation license file has been added to the workstation, and that the
   server address and port in the license manager are correct (see
   [Workstation: configuration](clients.md)).
4. Check that the server ports are reachable from the workstation (see
   [Workstation: checking ports](ports-check.md)).

If the license is still not visible, send to technical support:

- a screenshot of the server monitor window with its full title;
- the `stNLC.ini` files from the workstation for every product that needs a network license;
- the application logs on the workstation from the folder
  `%APPDATA%\ENCY Software\<Product>\Version <N>\Log`, for example
  `%APPDATA%\ENCY Software\ENCY Tuner\Version <N>\Log`;
- the server log `*.log` if logging is enabled.

## No free seats

1. Open the **Busy licenses** window in the monitor or the page `http://<server_address>:10097`
   and see which clients occupy the seats.
2. If the list contains "stuck" clients — connected long ago but not working — disconnect them
   with the **Disconnect** button (see [Busy licenses](configuration.md#busy-licenses)).
3. Check whether more copies of the application are running than expected.

## Protection key not found

1. Make sure the USB key is connected to the server PC or, in a virtual machine, passed
   through to the guest OS; a Sentinel HASP HL key does not work in a virtual machine (see
   [Virtual machine](installation.md#virtual-machine)).
2. Install the key driver from the vendor's website.
3. Make sure the key type is supported by the server (see
   [License protection](installation.md#license-protection)).
4. Check a Guardant key with a utility from the **License server** → **Utils** folder of the
   **Start** menu, depending on the key model:

   - **Guardant Stealth 2**;
   - **Guardant Stealth 3**.

   The utility searches for connected keys and shows the result; if no key is found, it shows
   `Keys is not found.` The **Save key info** button saves the information about a found key to
   a file — attach it to your request to technical support.

## Software activation fails

1. Check the Internet connection of the server PC.
2. Check the login and password.
3. If activation over the Internet is not possible, activate the license by code (see
   [Activation by code](installation.md#activation-by-code)).
4. After moving the server to another PC or changing its hardware, the license must be
   reactivated — only through your dealer and with the dealer's consent (see
   [Reactivation](installation.md#reactivation)).
5. If the software license has stopped working, for example after the server PC was shut
   down incorrectly, restore it (see
   [Restoring a software license](installation.md#restoring-a-software-license)).

## The license has expired

When the license expires, the server stops issuing licenses, and the monitor title shows
"Time expired". Contact the supplier to renew the license. When you receive a new license file,
update the server license (see [Updating the license](configuration.md#updating-the-license)).

## Port busy at startup

The `Port is busy` message in the log means that the server port is already used by another
program. First make sure a second server instance is not running, then do one of the following:

- terminate the program that occupies the port;
- change the **Port number** in the **Settings** window and specify the new port on the
  workstations.

## The server uses 100% of the CPU

If the CPU load rises sharply after clients connect:

1. Make sure the latest server version is installed.
2. Check the server log `*.log` for errors.
3. If the problem persists, restart the server.
