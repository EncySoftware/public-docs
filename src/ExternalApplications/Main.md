# Interaction with external applications
Using CAMIPC, you can write an external application which:
- can run ENCY and then connect to it;
- can manage ENCY (open new project / calculate NC / edit operations list / etc);
- can open ENCY without any windows, so it will work faster;
- can open more than one ENCY and read information from all of them.
- can mimic the behaviour of user, for a example, it will press some buttons.

Right now, we are hardly working on expanding this list.

## Connecting
ENCY provides CAMIPC.Helper.Cam.dll, which can be used to connect to application. Connection methods:
- [In C#](ConnectInCSharp.md);
- [In Delphi](ConnectInDelphi.md);
- [In C++](ConnectInCpp.md).