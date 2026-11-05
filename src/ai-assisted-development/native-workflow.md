# Arbeitsablauf für native Interpreter

Ein nativer Interpreter ist eine Bibliothek `*.dll`, gebaut in Delphi, C++ oder einer anderen Sprache, die in Maschinencode kompiliert wird. Der Assistent übernimmt einen nativen Interpreter nur, wenn Sie ausdrücklich darum bitten oder einen bereits vorhandenen nativen Interpreter ändern; ein neuer Interpreter wird standardmäßig in C# erstellt — siehe [Arbeitsablauf .NET](dotnet-workflow.md).

Referenzinformationen zur Bibliothek finden Sie in den Abschnitten [Interpreter-Bibliothek](../interpreter-structure/interpreter-library/interpreter-library.md), [Interpreter-Einstellungsdatei](../interpreter-structure/interpreter-settings-file/interpreter-settings-file.md) und [Interpreter-Schnittstelle](../g-code-interpretation/interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md). Details für den Assistenten enthält der Skill `develop-native-interpreter`.

## Was der Assistent braucht

- Die Quellen des Interpreters und das Projekt, mit dem er gebaut wird — oder die ausdrückliche Bitte, einen neuen zu erstellen.
- Einen Compiler: RAD Studio für Delphi, einen C++-Compiler oder einen anderen.
- Die Schnittstellendeklarationen des SDK. Sie kommen als NuGet-Pakete aus derselben Quelle wie das SDK-Paket für C# (siehe [Produktversionen](dotnet-workflow.md#produktversionen)) und mit derselben Version: für Delphi `EncySoftware.NCInterpreterSDK.bpl.x64` (Module `IDL.<Name>.pas` und Pakete `*.bpl`, `*.dcp`), für C++ und andere Sprachen `EncySoftware.NCInterpreterSDK.tlb` (Typbibliotheken `*.tlb`, Header `*.h` und Beschreibungen `*.idl`). Beide Pakete ziehen je ein Paket pro Schnittstelle nach, jedes mit eigener Versionsnummer: `STNCInterpreter`, `STNCAnalyzer`, `STNCFormers`, `STNCCustomInterpreter` und `STNCConnect` (die Schutzschnittstelle, die ein geschützter Interpreter verwendet). Der Assistent übernimmt die Deklarationen aus ihnen, statt sie zu erfinden. Gibt es das Paket in der benötigten Version in der Quelle nicht, wenden Sie sich an den Support.
- Die Datei `*.snci`, mit der der Interpreter geladen wird.

## Was für die Bibliothek Pflicht ist

- Die Bibliothek exportiert zwei Funktionen: `NCT_GetInterface` und `NCT_FreeMemory`. Fehlt auch nur eine davon, lädt das Produkt die Bibliothek nicht.
- Die Zeichenkette, die `GetIdentifier` zurückgibt, ist gleich `LibraryID` in der Datei `*.snci`. Beide Kennungen, `LibraryID` und `ID`, sind eindeutig.
- Für aktuelle Produkte wird eine 64-Bit-Bibliothek gebaut, ihr Name steht in `LibraryFileName_x64`. Eine 32-Bit-Bibliothek, deren Name in `LibraryFileName_x32` steht, wird nur für ein 32-Bit-Produkt einer alten Version benötigt.
- Ein abgeleiteter Interpreter erhält den Eltern-Interpreter über `SetInterface` und ruft ihn nach den Regeln der [Vererbung von Interpretern](../g-code-interpretation/interpreter-inheritance/interpreter-inheritance.md) auf.

Register lassen sich sowohl in der Datei `*.snci` als auch in der Bibliothek selbst festlegen. Bequemer ist es, sie in der Bibliothek zusammen mit den Handlern zu deklarieren: Dann ist ein neues Wort eine Zeile in der Registerliste und ein Handler.

## Zyklus

1. Bauen Sie die Quellen ohne Änderungen und prüfen Sie, dass die Bibliothek geladen wird und Ihre NC-Programme simuliert. Speichern Sie das Ergebnis als Ausgangsstand.
2. Bevor Sie einen Fehler in der Simulation suchen, prüfen Sie den Export der Funktionen, die Bitbreite, die Kennungen und das Paar `*.snci` und `*.dll`: Der größte Teil von „funktioniert nicht“ beginnt hier.
3. Nehmen Sie eine kleine Änderung vor, bauen Sie, lassen Sie alle NC-Programme laufen und vergleichen Sie mit dem vorherigen Ergebnis — siehe [Prüfung und Bestätigung des Ergebnisses](review-and-verify.md).
4. Debuggen Sie mit dem Debugger Ihres Compilers, indem Sie sich an das CAM-System oder ENCY Tuner anhängen, und lesen Sie das [Protokoll der Interaktion mit dem Interpreter](../g-code-interpretation/log-interaction-with-the-interpreter/log-interaction-with-the-interpreter.md).

## Geschützter Interpreter

Ein Interpreter, der seine Daten über die Schutzschnittstelle prüft, ist im Abschnitt [Geschützte Interpreter](../interpreter-structure/protected-interpreters/protected-interpreters.md) beschrieben. Prüfen Sie ihn aus dem Container, in dem er ausgeliefert wird: Aus einem gewöhnlichen Ordner erhält er keine Schutzdaten. Ohne seine Daten muss ein geschützter Interpreter die Simulation verweigern. Wie er das meldet, entscheidet sein Autor: Der Assistent sorgt dafür, dass der Interpreter eine verständliche Meldung ausgibt, ein bereits vorhandener kann aber stillschweigend einen leeren Werkzeugweg liefern — prüfen Sie dann zuerst die Schutzdaten.

## Was Sie nicht tun sollten

- Ändern Sie den Kern und die Bibliotheken des Produkts nicht, um den Interpreter zum Laufen zu bringen.
- Betrachten Sie Besonderheiten der Implementierung in Delphi nicht als Teil der binären Schnittstelle: In C++ und anderen Sprachen gleichen Sie die Schnittstelle mit der Typbibliothek und mit einem funktionierenden Interpreter ab.
- Betrachten Sie die Arbeit nach dem Kompilieren nicht als abgeschlossen: Die Bibliothek muss geladen werden und Ihre Programme simulieren.
