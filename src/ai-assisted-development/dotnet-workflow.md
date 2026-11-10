# Arbeitsablauf .NET

Ein Interpreter in C# ist ein .NET-Projekt, das auf das SDK-Paket für Interpreter verweist und zu einer Bibliothek `*.dll` gebaut wird; daneben liegt die Einstellungsdatei `*.snci`. Das CAM-System oder ENCY Tuner lädt die Bibliothek und ruft sie bei der Simulation von NC-Programmen auf. Das ist der Standardweg: Der Assistent wählt ihn für jeden neuen Interpreter, sofern Sie nichts anderes verlangt haben.

Wie Sie einen Interpreter aus einer Vorlage erstellen, beschreibt der Abschnitt [Entwicklung eines eigenen Interpreters in (.NET) C#](../dotnet/developing-a-custom-interpreter-in-net-csharp.md), wie Sie ihn im Debugger starten, das [Debuggen des Interpreters in Visual Studio Code](../dotnet/interpreter-debugging-in-visual-studio-code/interpreter-debugging-in-visual-studio-code.md). Details für den Assistenten enthält der Skill `develop-dotnet-interpreter`.

## Womit beginnen

Meistens nicht bei null. Gibt es einen Interpreter für dieselbe oder eine ähnliche Steuerung, dessen Verhalten an echten Programmen geprüft ist, kopieren Sie ihn und passen Sie ihn an. Die Kopie braucht neue Kennungen: die GUID, die `GetIdentifier` zurückgibt (sie ist zugleich `LibraryID` in der Datei `*.snci`), und die GUID im Feld `ID`. Zwei Interpreter mit gleichen Kennungen kann das CAM-System nicht unterscheiden.

Wird ein neuer benötigt, erstellen Sie ihn mit dem Eintrag **Interpreter erstellen** in der Liste **Zubehör** des CAM-Systems oder mit dem Eintrag **Interpreter-Verwaltung** in ENCY Tuner — beide öffnen dasselbe Fenster **Erstellen Sie einen G-Code-Interpreter** (das Erstellungswerkzeug für Interpreter). Die Vorlage, aus der der Interpreter erstellt wird, ist auf eine Familie von Steuerungen ausgelegt; der Assistent prüft und korrigiert, was das Erstellungswerkzeug nicht selbst erledigt: Er füllt `ID` in der Datei `*.snci` aus, setzt die veröffentlichte Version des SDK-Pakets und entfernt Handler für Wörter, die auf Ihrer Steuerung etwas anderes bedeuten. Bei einem abgeleiteten Interpreter korrigiert er auch den Verweis auf den Eltern-Interpreter: `ParentID` muss mit der `ID` des Eltern-Interpreters übereinstimmen, und `ParentFileName` muss dessen Datei `*.snci` nennen.

Ein Interpreter kann einen anderen erben — siehe [Vererbung von Interpretern](../g-code-interpretation/interpreter-inheritance/interpreter-inheritance.md). Bevor Sie einen mitgelieferten Interpreter als Eltern-Interpreter nehmen, prüfen Sie seinen Zweck in der [Liste der Interpreter](../appendix/list-of-interpreters/list-of-interpreters.md): Bei einigen steht „Nur für den Import des Werkzeugwegs“ — sie verknüpfen die Sätze des NC-Programms nicht mit Bewegungen.

Beginnen Sie in jedem Fall mit einem bekannten Zustand:

1. Stellen Sie den Interpreter unter Versionskontrolle, bevor Sie irgendetwas ändern.
2. Bauen Sie ihn ohne Änderungen. Lässt er sich so nicht bauen, ist jede weitere Diagnose sinnlos.
3. Lassen Sie alle Ihre NC-Programme durch ihn laufen und speichern Sie das Ergebnis als Ausgangsstand für den Vergleich.

## Produktversionen

Jede Produktversion hat ihre eigene .NET-Version: Version 3 des CAM-Systems und von ENCY Tuner läuft unter .NET 10, Version 2 unter .NET 8.

Der Interpreter verweist auf das Paket `EncySoftware.NCInterpreterSDK.Net`. Seine Version bestimmt der Assistent so:

1. Er liest, mit welcher Paketversion das installierte Produkt gebaut ist: aus der Datei `Bin64\STNCInterpreterSDKProject.stbuildresult.json`, Abschnitt `build_results.versions`. Eine Installation von ENCY Tuner hat diese Datei möglicherweise nicht; dann wird die Version aus dem CAM-System derselben Version genommen (ENCY 3 für ENCY Tuner 3, ENCY 2 für ENCY Tuner 2). Hat ENCY Tuner die Datei, legt die Nummer darin der Build von ENCY Tuner fest, der die SDK-Pakete nicht veröffentlicht; ein Paket mit genau dieser Nummer gibt es in der Paketquelle daher möglicherweise nicht.
2. Er setzt die neueste **veröffentlichte** Version des Pakets (ohne Endungen wie `-dev` oder `-rc`) mit derselben Hauptversionsnummer, die nicht neuer ist als die Version aus Schritt 1. Für ENCY Tuner ist das die Nummer aus seiner Datei oder, wenn es die Datei nicht gibt, aus der Datei des CAM-Systems derselben Version. Die Nummer aus der Datei von ENCY Tuner ist nur eine Obergrenze.

Die veröffentlichten Pakete liegen auf nuget.org. Diese Paketquelle ist im .NET SDK standardmäßig eingerichtet; ein Befehl zum Hinzufügen ist nicht nötig. Die Version, mit der ein Nightly- oder Testbuild des Produkts gebaut wurde, kann der Kunde nicht herunterladen; deshalb gehört sie nicht in ein Projekt, das Ihren Computer verlässt.

Soll der Interpreter in mehreren Produktversionen arbeiten, wird ein Projekt für jede davon gebaut; prüfen müssen Sie ihn in jeder.

## Zyklus

1. Formulieren Sie die Aufgabe als sichtbaren Unterschied in der Simulation: welches Programm, welcher Satz, was geschehen soll.
2. Bitten Sie den Assistenten, die Stelle zu finden, an der der Interpreter dieses Wort liest, und zu erklären, was er jetzt tut.
3. Entscheiden Sie gemeinsam mit ihm, um welche Art von Änderung es sich handelt:
   - **Variation** — ein anderer Achsname, eine M-Funktion der Maschine, ein Wort ohne Einfluss auf den Werkzeugweg. Ihr Platz ist die Datei `InterpreterSettings.ini` neben der Bibliothek, nicht der Code: Dann löst den nächsten solchen Fall ein Supportingenieur ohne Build. Beim ersten Mal wird der Einstellungsschlüssel in den Code eingebaut, danach ist es eine Einstellung;
   - **neues Verhalten** — ein Zyklus, ein Frame, ein Vorschubmodus. Das ist eine Änderung im Code, in der Datei der Rolle, zu der sie gehört;
   - **Einschränkung des Kerns oder des SDK** — der benötigte Aufruf fehlt. Der Assistent beschreibt die Umgehung und ihre Grenzen und hält fest, was im Produkt geändert werden müsste.
4. Nehmen Sie eine kleine Änderung vor und bauen Sie das Projekt. Build-Warnungen sind Informationen über Ihre Änderung, kein Rauschen.
5. Lassen Sie alle NC-Programme laufen und vergleichen Sie mit dem vorherigen Ergebnis — siehe [Prüfung und Bestätigung des Ergebnisses](review-and-verify.md).

## Debuggen

Die Taste `F5` in Visual Studio Code baut den Interpreter und startet die im Bereich **Run and Debug** gewählte Konfiguration: **Launch CAM** startet das CAM-System, **Launch Tuner** startet ENCY Tuner; der Haltepunkt wird ausgelöst, wenn ein NC-Programm simuliert wird. Schalten Sie vor dem Debuggen das Protokoll ein, wie in der [erweiterten Einrichtung](advanced-setup.md#werkzeuge-zum-bauen-und-debuggen) beschrieben — sonst stehen im Protokoll weder Meldungen des Kerns über gelesene Wörter noch die Zeilen, die der Interpreter schreibt.

Um ein Programm zu simulieren, erstellen Sie eine G-Code basierte Operation, fügen Sie den Programmtext ein, wählen Sie den Interpreter im Feld **Interpreter file** auf der Registerkarte **Strategie** der Operationsparameter und berechnen Sie die Operation.

Lassen Sie Build und Debugging so, wie die Vorlage sie eingerichtet hat: Ein Kollege muss den Ordner öffnen, `F5` drücken und am Haltepunkt anhalten können. Der Assistent ersetzt sie nicht durch eigene Skripte und Umgebungsvariablen.

## Was im Code zu prüfen ist

- Die Änderungen enthalten das, worum gebeten wurde, und nichts weiter: keine Neuformatierung, keine fremden Umschreibungen.
- Zeilenenden und Kodierung der Vorlagendateien sind erhalten — sonst zeigt der Verlauf jede Zeile als geändert.
- Zahlen im Programm werden unabhängig von der Windows-Sprache gelesen: Der Punkt ist immer das Dezimaltrennzeichen.
- Der Zustand des Interpreters wird in seinem Objekt gehalten, nicht in statischen Feldern: Das CAM-System erstellt bei jeder Berechnung einer Operation eine neue Instanz, getrennte für den Eltern-Interpreter und für die Kontur eines Zyklus, und ein statisches Feld ist ihnen nicht gemeinsam; ENCY Tuner dagegen hält eine Instanz je Kanal — von der ersten Operation des Kanals bis zur letzten —, und der modale Zustand und ein statisches Feld gehen von Operation zu Operation über: Ein `G0` vom Ende einer Operation gilt zum Beispiel noch am Anfang der nächsten.
- Ein Wort, das der Interpreter nicht simuliert, verschwindet nicht stillschweigend: Es ist entweder als gelesen ohne Einfluss auf den Werkzeugweg vermerkt oder erzeugt eine Warnung pro Programm, die der Maschinenbediener versteht.

Regeln, die nicht vom Kern abhängen — Zerlegung von Zahlen und Ausdrücken, Zyklusparameter, Regeln für Achsen und Spindeln, Lesen der Einstellungsdatei —, kann der Assistent mit Unit-Tests abdecken. Tests ergänzen den Durchlauf echter Programme, ersetzen ihn aber nicht.
