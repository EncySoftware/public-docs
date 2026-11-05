# Wie KI-gestützte Entwicklung funktioniert

Sie sprechen mit einem KI-Client — einem Chat im Code-Editor oder im Terminal. Der Client liest die Skills und die Dateien Ihres Arbeitsordners, ändert die Quellen des Interpreters, baut ihn und startet das CAM-System oder ENCY Tuner, in dem der Interpreter die NC-Programme simuliert. Besondere Server sind nicht nötig, und von den Erweiterungen für Visual Studio Code nur der Chat selbst und die C#-Erweiterung zum Bauen und Debuggen: Der Assistent arbeitet mit denselben Dateien und Programmen wie Sie.

```text
        Sie
         |
   KI-Client  (Chat in Visual Studio Code oder im Terminal)
         |
         +--> liest die Skills                    Ordner skills
         +--> liest NC-Programme, Maschinen-      Arbeitsordner
         |    projekt, Handbuch der Steuerung,
         |    Ihre Notizen
         +--> ändert und baut den Interpreter     Quellen, .NET SDK
         |
         v
   CAM-System oder ENCY Tuner  --->  Simulation der NC-Programme  --->  Protokoll
                                            |
                                            v
                                    Vergleich und Ihre Prüfung
```

## Woraus alles besteht

| Teil | Was das ist | Was er Ihnen bringt |
|---|---|---|
| KI-Client | Chat-Erweiterung für Visual Studio Code oder Programm im Terminal | Ein Gespräch mit einem Assistenten, der im Arbeitsordner Dateien lesen und ändern sowie Befehle ausführen darf |
| Skills | Textdateien `SKILL.md` | Ein in Worten beschriebener Arbeitsablauf, daher läuft der Zyklus jedes Mal gleich: zuerst die Fakten, dann die Änderung, dann die Prüfung. Die Arbeit führt der allgemeine Skill `interpreter-development`, die übrigen zieht er im Verlauf hinzu |
| Arbeitsordner | Ein gewöhnlicher Ordner auf Ihrem Computer | NC-Programme, Maschinenprojekt, Handbuch der Steuerung und Ihre Notizen — alles, was der Assistent über Ihre Aufgabe weiß |
| Quellen des Interpreters | C#-Projekt aus einer Vorlage oder natives Projekt | Das, was der Assistent ändert |
| .NET SDK und Visual Studio Code mit der C#-Erweiterung | Werkzeuge zum Bauen und Debuggen | Bauen des Interpreters und Start im Debugger mit der Taste `F5` |
| CAM-System oder ENCY Tuner | Das installierte Produkt | Lädt den Interpreter und simuliert NC-Programme in einer G-Code basierten Operation |
| Protokoll der Interaktion mit dem Interpreter | Protokolldatei des Produkts | Was der Kern und der Interpreter mit jedem Satz gemacht haben: gelesene Wörter, Warnungen, Fehler |

## Wie das CAM-System einen Satz liest

Den Ablauf steuert der Kern des CAM-Systems, nicht der Interpreter: Der Kern liest den Text des NC-Programms, zerlegt den Satz anhand der Registertabelle des Interpreters in Wörter, stellt sie in eine Warteschlange und ruft den Code des Interpreters auf, damit er jedes Wort ausführt. Welche Funktionen in welcher Reihenfolge aufgerufen werden, beschreibt der Abschnitt [Ablauf der Interpretation des NC-Programms](../g-code-interpretation/g-code-based-program-interpretation.md); der Skill `nc-interpreter-foundations` gibt das für den Assistenten wieder, zusammen mit den Fallen, in die man am häufigsten gerät: erste Bewegung der Operation, Koordinaten im gedrehten Koordinatensystem, Spindeln, Zyklen.

Die Bedeutung jedes Wortes legt der Interpreter fest, und dasselbe Wort bedeutet auf verschiedenen Steuerungen Verschiedenes. Deshalb beginnt der Assistent immer mit den tatsächlichen Programmen und dem Handbuch der Steuerung und nicht mit dem Namen eines Wortes. Der Interpreter simuliert, was die Steuerung tun würde, nicht was die CAM-Operation beabsichtigt hat.

## C# (.NET) als Standard

Einen neuen Interpreter erstellt der Assistent in C# aus einer Vorlage des CAM-Systems. Ein solcher Interpreter wird mit einem einzigen Befehl gebaut, in Visual Studio Code debuggt und ist gut lesbar für Menschen, die die Maschine besser kennen als das Programmieren. Einen nativen Interpreter in Delphi oder C++ nur, wenn Sie ausdrücklich darum bitten oder einen bereits nativen ändern. Ausführlich: [Arbeitsablauf .NET](dotnet-workflow.md) und [Arbeitsablauf für native Interpreter](native-workflow.md).

## Was der Assistent gut kann und was nicht

Er stellt gut eine Liste aller Wörter zusammen, die in Ihren Programmen vorkommen, findet die Stelle im Interpreter, an der ein Wort gelesen wird, erklärt unbekannten Code, bereitet eine kleine Änderung im Stil des umgebenden Codes vor, lässt alle NC-Programme vor und nach der Änderung laufen und vergleicht die Ergebnisse Satz für Satz.

Er kann kein Verhalten der Steuerung kennen, das weder im Handbuch noch in den Programmen steht, die Maschine nicht sehen, die Sicherheit von Bewegungen nicht beurteilen und keine Verantwortung für einen an den Kunden übergebenen Interpreter tragen. Warum ein erfolgreicher Build und eine fehlerfreie Simulation nicht ausreichen und wie man das Ergebnis prüft, beschreibt der Abschnitt [Prüfung und Bestätigung des Ergebnisses](review-and-verify.md).
