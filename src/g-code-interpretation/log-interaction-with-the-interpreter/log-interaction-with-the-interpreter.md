# Protokoll der Interaktion mit dem Interpreter

Die Interpretation des NC-Programmtexts, einschließlich der Interaktion mit dem Interpreter, wird im Protokoll aufgezeichnet, wenn eine eigene Option des Protokolls eingeschaltet ist. Das Protokoll wird im Fenster **System Einstellungen** gesteuert: Abschnitt &lt;[Log-Dateien](https://docs.encycam.com/ENCY/3/en/23.html)&gt;, Gruppe &lt;**Logs**&gt;, Optionen &lt;**Anwender Logfile**&gt; und &lt;**Protokollinteraktion mit dem Interpreter verwenden**&gt;. Die zweite Option ist nur verfügbar, wenn die erste eingeschaltet ist. In ENCY Tuner wird das Protokoll ebenso eingeschaltet; dort heißen das Fenster **Systemeinrichtung** und der Abschnitt **Zusätzlich**.

Sind beide Optionen eingeschaltet, wird bei Berechnungen im Modus „[Simulation anhand des NC-Programms](https://docs.encycam.com/ENCY/3/en/10291.html)“ sowie bei „[G-Code basierten Operationen](https://docs.encycam.com/ENCY/3/en/10379.html)“ die Interpretation des NC-Programms im Protokoll aufgezeichnet: Meldungen des Kerns über gelesene Wörter und die Zeilen, die der Interpreter schreibt.

Das Protokoll wird in einer Datei pro laufendem Programmprozess geführt: Alle Berechnungen während der Laufzeit des Programms werden in diese Datei geschrieben. Speicherort der Datei:

- ENCY - `%APPDATA%\ENCY Software\ENCY\Version 3\Log\ency-<Prozess-ID>.log`;
- ENCY Tuner - `%APPDATA%\ENCY Software\ENCY Tuner\Version 3\Log\ltuner-<Prozess-ID>.log`.

Überschreitet die Protokolldatei 20 MB, wird ihr bisheriger Inhalt in den Unterordner `RotatedLogs` verschoben, und das Schreiben wird in einer Datei mit demselben Namen fortgesetzt.

Das Protokoll ist für das [Erstellen eines eigenen Interpreters](../../../index.md) gedacht.
