# Fehlerbehebung

## Der Assistent sieht die Skills nicht

Fragen Sie ihn, welche Skills er gerade hat. Wenn die sechs Skills für Interpreter nicht darunter sind, prüfen Sie, dass die Ordner der Skills in dem Ordner liegen, den Ihr Client tatsächlich liest, dass jeder eine Datei `SKILL.md` enthält und dass der Client sie übernommen hat: Claude Code sieht neue Skills sofort, und wenn es den Skills-Ordner vor dem Kopieren nicht gab, nach dem Befehl `/reload-skills`; Kilo Code in einer neuen Sitzung oder nach dem Befehl `/reload`; andere Clients laut ihrer Dokumentation, oft erst nach einem Neustart. Wo welcher Client nach Skills sucht, steht in der [erweiterten Einrichtung](advanced-setup.md#skills-in-verschiedenen-ki-clients).

## Der Assistent antwortet aus dem Gedächtnis statt aus den Programmen

Das passiert, wenn in der Anfrage keine Dateien genannt sind oder wenn für die Antwort keine Verweise auf die Daten verlangt werden. Nennen Sie Programme und Handbuch ausdrücklich, fragen Sie, aus welcher Datei und welchem Satz er das Wort genommen hat, und bitten Sie ihn, nach den Skills zu arbeiten — sie verlangen, zuerst die Programme zu lesen.

## Der Assistent meldet Erfolg, ohne etwas gestartet zu haben

Ein Build ist kein Ergebnis. Fragen Sie, welche Programme durchgelaufen sind, wo das Protokoll dieses Durchlaufs liegt und worin sich das Ergebnis vom vorherigen unterscheidet. Fehlt das, ist der Zustand **Nicht geprüft**, siehe [Prüfung und Bestätigung des Ergebnisses](review-and-verify.md).

## Der Interpreter wird nicht geladen

Lesen Sie zuerst, welche Datei im Feld **Interpreter file** auf der Registerkarte **Strategie** der Operationsparameter angegeben ist, und das Protokoll des CAM-Systems. Ist der Interpreter nicht geladen, wird jedes Wort des Programms ein Fehler sein.

Jeden Fehlschlag beim Laden eines Interpreters in C# beschreibt das CAM-System gleich — mit der Meldung „Externe Bibliothek unterstützt NCT-Schnittstelle nicht:“ und dem Pfad zur Bibliothek; dieselbe Meldung erscheint auch bei einer nativen Bibliothek ohne die nötigen Exporte. Die tatsächliche Ursache steht nicht in der Meldung. Meistens ist es eine der folgenden:

- neben der Datei `*.snci` liegt die darin genannte Bibliothek nicht oder es fehlen ihre Abhängigkeiten;
- die Bibliothek ist für eine andere .NET-Version gebaut, als diese Produktversion braucht;
- beim Erstellen des Interpreter-Objekts ist eine Ausnahme aufgetreten — meist beim Erstellen der Register.

Bitten Sie den Assistenten, die Dateien zu prüfen und das Interpreter-Objekt in einem kleinen Konsolenprogramm mit demselben SDK-Paket zu erstellen — so wird die tatsächliche Fehlermeldung sichtbar.

Prüfen Sie bei einem nativen Interpreter die Bitbreite der Bibliothek, den Export von `NCT_GetInterface` und `NCT_FreeMemory` und die Übereinstimmung von `GetIdentifier` mit `LibraryID` — siehe [Arbeitsablauf für native Interpreter](native-workflow.md).

## Zwei Interpreter werden verwechselt

Das CAM-System unterscheidet Interpreter anhand der Kennungen in der Datei `*.snci`. Ein kopierter Interpreter mit denselben `LibraryID` und `ID` ist vom Original nicht zu unterscheiden: Mal simuliert der eine, mal der andere. Geben Sie der Kopie neue Kennungen.

## Der Haltepunkt wird nicht ausgelöst

Prüfen Sie der Reihe nach: Neben der Bibliothek liegt eine Datei `*.pdb` (ein Build ohne Debug-Informationen macht jeden Haltepunkt „tot“); die Operation verwendet genau Ihren Interpreter; der Build vor dem Start war erfolgreich — öffnen Sie den Terminalbereich und lesen Sie sein Ergebnis; an das CAM-System wurde die Datei `*.snci` aus dem Ordner der Version übergeben, die Sie gestartet haben.

## Einstellungen aus InterpreterSettings.ini wirken nicht

In den Vorlagen gibt es bekannte Fehler beim Lesen von `InterpreterSettings.ini`: Die Datei wird unter Umständen gar nicht gelesen, und im Protokoll bleibt nur eine Informationszeile, die mit `Error reading settings file` beginnt. Ein nach Fehlern gefiltertes Protokoll zeigt sie nicht. Bitten Sie den Assistenten, die Vorlage zu prüfen, aus der der Interpreter erstellt wurde — der Skill `develop-dotnet-interpreter` listet diese Fehler und ihre Korrekturen auf.

## Eine Achse wird an der falschen Stelle oder gar nicht simuliert

Die Hilfsfunktion aus dem SDK-Paket, über die die .NET-Vorlagen die Achsen der Maschine finden, warnt einmal vor einem unbekannten Achsnamen und überspringt dessen Werte danach stillschweigend. Prüfen Sie, dass der Achsname im Programm mit der Adresse der Achse im Maschinenschema übereinstimmt und dass die Zuordnung der Namen für alle Schreibweisen aus der Wortliste funktioniert: `B90`, `B=90`, `B1=90`.

## Der zweite Kanal bewegt die Achsen des ersten oder wird nicht simuliert

Der Interpreter muss die Achsen bewegen, die ihm das CAM-System für den Kanal seines Programms übergibt: für den zweiten Kanal zum Beispiel `X2`, `Y2`, `Z2`. Bewegt der zweite Kanal die Achsen des ersten oder schrumpft sein Werkzeugweg auf einen Punkt, vergleichen Sie diese Achsen mit den Achsen, die der Interpreter an seine Bewegungsbefehle übergibt. Eine Abweichung ist ein Fehler des Interpreters oder seiner Datei `*.snci`, nicht des CAM-Systems.

Prüfen Sie die Synchronisation der Kanäle im CAM-System: Je nach Version und Lizenz simuliert ENCY Tuner die Kanäle unter Umständen nacheinander statt gleichzeitig, und dann halten die Wartepunkte nichts zurück.

## Leerer Werkzeugweg ohne Fehler

Häufige Ursachen:

- im Programm fehlt der Kopf, mit dem der Postprozessor es ausgibt: Ein Prüfprogramm, das nur aus den zu prüfenden Sätzen besteht, ergibt unter Umständen keine einzige Bewegung — bauen Sie es aus dem Kopf eines echten Programms derselben Operation;
- der Eltern-Interpreter ist nur für den Import des Werkzeugwegs bestimmt (in der [Liste der Interpreter](../appendix/list-of-interpreters/list-of-interpreters.md) steht bei solchen „Nur für den Import des Werkzeugwegs“);
- der Achsname im Programm stimmt nicht mit der Adresse der Achse im Maschinenschema überein (siehe den Abschnitt oben);
- ein geschützter Interpreter hat seine Schutzdaten nicht erhalten — zum Beispiel, weil er aus einem gewöhnlichen Ordner und nicht aus dem Container gestartet wurde — und ist so geschrieben, dass er dann stillschweigend nichts simuliert. Siehe [Geschützte Interpreter](../interpreter-structure/protected-interpreters/protected-interpreters.md).

## Das Ergebnis weicht von dem einer anderen Produktversion ab

Jede Version des CAM-Systems und von ENCY Tuner hat ihre eigene .NET-Version und ihre eigene Version des SDK-Pakets (siehe [Produktversionen](dotnet-workflow.md#produktversionen)). Prüfen Sie, in welcher Produktversion der Durchlauf lief und für welche die Bibliothek gebaut ist — siehe [Mehrere Produktversionen auf einem Computer](advanced-setup.md#mehrere-produktversionen-auf-einem-computer).

## Die Dokumentation, die der Assistent liest, ist veraltet

Eine lokale Kopie ist eine Momentaufnahme: Laden Sie das Archiv erneut herunter, wenn eine neue Version erscheint, und notieren Sie, auf welcher Version eine Lösung beruht. Versionsabhängige Details — die Version des SDK-Pakets, Namen von Schnittstellen — gleichen Sie mit dem installierten Produkt ab, nicht mit der Kopie.
