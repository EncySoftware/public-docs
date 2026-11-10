# Prüfung und Bestätigung des Ergebnisses

KI-Unterstützung ändert, wie ein Entwurf entsteht. Sie ändert nicht, wie ein Interpreter abgenommen wird. Ein erfolgreicher Build und eine fehlerfreie Simulation beweisen, dass die Programme durchgelaufen sind — und nicht mehr.

## Geben Sie an, wie weit die Prüfung gekommen ist

Verwenden Sie einen von vier Zuständen und bewahren Sie den Nachweis dafür auf. Der Sinn ist, dass eine unvollständige Prüfung sichtbar ist, und nicht, dass alles „fertig“ heißt.

| Zustand | Was er bedeutet |
|---|---|
| **Nicht geprüft** | Es gibt einen Plan, Änderungen oder einen Build, aber die NC-Programme sind nicht durch den Interpreter gelaufen |
| **Technisch geprüft** | Der Interpreter wurde geladen, die Programme sind durchgelaufen, Protokoll und simulierte Befehle sind gespeichert, aber nicht verglichen und nicht ausgewertet |
| **An Referenzprogrammen geprüft** | Alle Programme sind vor und nach der Änderung durchgelaufen, jeder Unterschied ist erklärt, die Warnungen im Protokoll sind gelesen, alle Produktversionen, für die der Interpreter bestimmt ist, sind geprüft |
| **Für die Maschine abgenommen** | Sie oder der Kunde haben die Simulation für eine konkrete Maschine bestätigt |

Den letzten Zustand vergibt nur ein Mensch. Beschreiben Sie ein Ergebnis niemals als fertig aufgrund eines Exit-Codes oder eines plausiblen Werkzeugwegs.

## Durchlauf der Programme

Schalten Sie vor jedem Durchlauf das Protokoll ein, wie in der [erweiterten Einrichtung](advanced-setup.md#werkzeuge-zum-bauen-und-debuggen) beschrieben: Ohne es gibt es nichts, womit die Warnungen verglichen werden könnten.

Ein einzelnes Programm lässt sich von Hand prüfen: G-Code basierte Operation, gewählter Interpreter, Berechnung, dann Simulation und Protokoll. Alle Programme nach jeder Änderung so durchlaufen zu lassen, dauert lange. Der Assistent kann ein kleines Durchlaufprogramm erstellen, das ohne Ihre Klicks das Projekt öffnet, jedes NC-Programm mit dem Interpreter simuliert und die simulierten Befehle und das Protokoll dieses Durchlaufs speichert. Es darf nur auf der öffentlichen Programmierschnittstelle des CAM-Systems für externe Anwendungen aufbauen, CAMIPC: Sie ist in der [Dokumentation zur CAM API](https://docs.encycam.com/technical/CAMAPI/3/en/src/ExternalApplications/Main.html) (auf Englisch) beschrieben, und die Bibliothek für die Verbindung zum CAM-System gehört zu dessen Installation. Wo die Dokumentation einen Schritt nicht zeigt (zum Beispiel, wie der Text des NC-Programms in eine Operation geladen oder ihr Interpreter gewählt wird), und in ENCY Tuner, der keine solche dokumentierte Schnittstelle hat, bleibt der Durchlauf manuell: Sie berechnen die Operationen, und der Assistent bereitet die Liste der Programme und Schritte vor und sammelt und vergleicht danach die Ergebnisse. Bewahren Sie das Durchlaufprogramm im Repository des Interpreters auf und geben Sie es niemals an den Kunden weiter.

Bevor Sie dem Durchlaufprogramm vertrauen, prüfen Sie es an einem bewusst eingebauten Fehler: Geben Sie ihm ein NC-Programm mit einem Fehler und mit einem unbekannten Wort und vergewissern Sie sich, dass es beides gezählt hat. Ein Zähler, der das falsche Feld des Protokolls liest, zeigt bei allem „0 Fehler“.

Lassen Sie die Programme einzeln laufen: Durchläufe in einem Prozess des CAM-Systems schreiben in eine Protokolldatei, und parallel gestartete Prozesse können den Kern unter Umständen gar nicht starten.

## Vergleich

1. Vergleichen Sie die Zusammenfassungen aller Programme vorher und nachher. Eine geänderte Anzahl von Warnungen oder Befehlen in einem Programm, das von der Änderung nicht betroffen war, erklären Sie zuerst.
2. Beginnen Sie bei jedem geänderten Programm mit dem ersten Unterschied und verfolgen Sie ihn bis zu dem Satz und dem Wort, das ihn verursacht hat. Ein unbeabsichtigter Unterschied ist wichtiger als ein beabsichtigter.
3. Lesen Sie die Warnungen selbst, nicht nur ihre Anzahl: Jede nennt ein Wort, eine Achse oder einen Zyklus.
4. Randfälle, die in den Programmen nicht vorkommen, prüfen Sie mit einem kurzen Programm: das Wort in allen Schreibweisen aus der Liste, an den Grenzen, weggelassen, wiederholt. Bauen Sie es aus dem Kopf eines echten Programms derselben Operation und ersetzen Sie nur die zu prüfenden Sätze — ohne Kopf ergibt ein Programm unter Umständen keine einzige Bewegung.

Ein Unterschied, der durch die Prüfung selbst und nicht durch den Interpreter entsteht — ein anderes Koordinatensystem der Testoperation, eine andere Maschine im Projekt —, ist kein Ergebnis: Benennen Sie ihn und schließen Sie ihn aus.

## Prüfung über den Postprozessor

Wenn es einen Postprozessor des Kunden und ein Projekt des CAM-Systems gibt, schließen Sie den Kreis: Erzeugen Sie NC-Programme aus den Operationen des Projekts, lassen Sie sie durch den Interpreter laufen und vergleichen Sie die Simulation mit dem Werkzeugweg der Operation selbst. Eine Abweichung kann sich als Fehler des Postprozessors herausstellen. Der Interpreter simuliert, was die Steuerung mit dem Programm tun würde, nicht was die Operation beabsichtigt hat: Einen solchen Fehler melden Sie dem Autor des Postprozessors, statt ihn im Interpreter zu verstecken.

## Sicherheitsprüfung

Sehen Sie vor der Übergabe jede Änderung auf Fälle durch, in denen die Simulation sicherer aussieht als die Maschine: ein fehlender Rückzug, ein erratener Startpunkt, ein Zyklus, der nicht simuliert wird, die Operation aber scheinbar abgeschlossen lässt. Prüfen Sie jeden solchen Fall mit einem kurzen Programm. Lassen Sie nach jeder Runde von Korrekturen aufgrund von Anmerkungen erneut alle Programme laufen.

## Vorbereitung der Übergabe

Der Kunde erhält einen Ordner pro Produktversion: die Datei `*.snci`, die Bibliothek des Interpreters und `InterpreterSettings.ini`, die Datei `*.deps.json` nur, wenn der Interpreter ohne sie nicht geladen wird (das wird an einer unveränderten Installation geprüft). Der Assistent kopiert die benötigten Dateien nach Namen, statt den ganzen Build-Ordner zu archivieren: Darin liegen Debug-Dateien und Hilfsdateien des SDK-Pakets. Dazu kommt eine README in der Sprache des Kunden: was unterstützt wird, Einschränkungen, Einstellungen, welcher Ordner für welche Produktversion ist, ob das Produkt eine Lizenzoption zum Laden eines eigenen Interpreters braucht und welche Vereinfachungen bewusst gemacht wurden, damit sie nicht für Fehler gehalten werden.

Prüfen Sie vor dem Versand:

- in den Dateien gibt es keine Spuren Ihres Computers: Benutzernamen, Home-Ordner, interne Server. Die Bibliothek für die Übergabe wird ohne Debug-Informationen oder mit Pfadzuordnung gebaut: Ein gewöhnlicher Build schreibt den Pfad zur Datei `*.pdb` auf Ihrem Computer hinein;
- in den Dateien kommen keine Namen vor, die nicht zu diesem Kunden gehören: Namen anderer Kunden, Ihres Computers und seiner Benutzer, interner Server und Paketquellen — weder in Dateinamen, Pfaden, Einstellungen, Startkonfigurationen und Verweisen auf SDK-Pakete noch in der README. Gesucht wird im Inhalt jeder Datei, in den Kodierungen UTF-8 und UTF-16, nicht nur in den Namen; dasselbe gilt für alles, was zusammen mit dem Paket versendet wird;
- das Projekt lässt sich, falls der Kunde die Quellen verlangt, aus einer sauberen Kopie mit dem veröffentlichten SDK-Paket bauen;
- der Interpreter funktioniert in einer unveränderten Installation des Produkts.

Stellen Sie das Paket aus Quellen zusammen, die im Verlauf festgehalten sind, und notieren Sie, was wann an wen gesendet wurde.

## Was der Assistent nicht tun darf

Er darf dem Ergebnis nicht den Zustand „Für die Maschine abgenommen“ zuweisen, keine Referenzprogramme, Maschine oder Projekt ändern, damit der Vergleich aufgeht, keine Prüfung einer Produktversion behaupten, die er nicht gestartet hat, und kein Paket ohne Ihre Erlaubnis versenden.
