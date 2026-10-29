# Interaktion mit dem Text des NC-Programms

**INCT_ProgramManager** - Schnittstelle für die Arbeit mit dem Text des NC-Programms. Sie ermöglicht den Zugriff auf die Texte des NC-Programms und legt fest, in welcher Reihenfolge sie dem Interpreter übergeben werden.

**Beschreibung der Schnittstellenmethoden:**

<table>
<thead>
<tr><th>Methode</th><th>Beschreibung der Methode</th><th>Verwendung</th></tr>
</thead>
<tbody>
<tr><td><strong>Get_Count</strong></td><td><p>Die Funktion gibt die Anzahl der Texte des NC-Programms (Dateien*) zurück, die der Postprozessor für die aktuelle Operation erzeugt hat.</p><p>Keine Eingabeparameter.</p></td><td rowspan="3"><p>Erzeugt der Postprozessor mehrere Texte des NC-Programms (Dateien*), kann es nötig sein, die Reihenfolge zu ändern, in der sie dem Interpreter übergeben werden.</p><p>Ob mehrere Texte vorhanden sind, liefert die Funktion <strong>Get_Count</strong>.</p><p>In manchen Fällen erzeugt der Postprozessor Dateien* mit eindeutigen Namen und Hilfsdaten (ohne NC-Programm), die nicht interpretiert werden müssen, oder umgekehrt eine Kopfdatei, aus der die übrigen Texte aufgerufen werden. Zum Erkennen solcher Dateien anhand des Namens dient die Funktion <strong>Get_Name</strong>.</p><p>Soll die Reihenfolge der vom Postprozessor erzeugten Texte geändert werden, dient dazu die Funktion <strong>AddToOrderList</strong>, die einen Text in die Interpretationsliste aufnimmt. Die Texte werden dem Interpreter in der Reihenfolge der Liste übergeben, vom zuerst aufgenommenen bis zum zuletzt aufgenommenen.</p></td></tr>
<tr><td><strong>Get_Name</strong></td><td><p>Die Funktion gibt den Namen der Datei* mit dem Text des NC-Programms anhand ihres Index zurück (Zeichenkette).</p><p>Eingabeparameter: <strong>Index</strong> (Ganzzahl) - Nummer des vom Postprozessor für die aktuelle Operation erzeugten Textes (der Datei*), Werte von 0 bis <strong>Get_Count</strong> -1.</p></td></tr>
<tr><td><strong>AddToOrderList</strong></td><td><p>Die Methode nimmt den Text des NC-Programms (die Datei*) mit dem angegebenen Index in die Interpretationsliste auf. Die Texte werden dem Interpreter in der Reihenfolge dieser Liste übergeben, vom zuerst aufgenommenen bis zum zuletzt aufgenommenen. Texte, die nicht in der Liste stehen, werden dem Interpreter nicht übergeben. Wurde kein Text in die Liste aufgenommen, erhält der Interpreter alle Dateien in der Reihenfolge, in der der Postprozessor sie für die aktuelle Operation erzeugt hat.</p><p>Eingabeparameter: <strong>Index</strong> (Ganzzahl) - Nummer des vom Postprozessor für die aktuelle Operation erzeugten Textes (der Datei*), Werte von 0 bis <strong>Get_Count</strong> -1.</p></td></tr>
<tr><td><strong>GetPartByIndex</strong></td><td><p>Die Funktion gibt den Text des NC-Programms (Schnittstelle <strong>INCT_Program</strong>) anhand des Index des Textes (der Datei*) zurück.</p><p>Eingabeparameter: <strong>Index</strong> (Ganzzahl) - Nummer des vom Postprozessor für die aktuelle Operation erzeugten Textes (der Datei*), Werte von 0 bis <strong>Get_Count</strong> -1.</p></td><td>Um die Reihenfolge der Texte (Dateien*) für den Interpreter festzulegen, kann es nötig sein, den Inhalt eines oder mehrerer Texte der aktuellen Operation zu analysieren. Die Funktion liefert für die angegebene Nummer die Schnittstelle <strong>INCT_Program</strong>, mit deren Funktionen die Zeilen des Textes gelesen werden.</td></tr>
<tr><td><strong>GetPartByLabels</strong></td><td><p>Die Funktion gibt den Text des NC-Programms (Schnittstelle <strong>INCT_Program</strong>) zwischen den angegebenen Marken zurück. Die Suche beginnt am Anfang des NC-Programms.</p><p>Eingabeparameter: <strong>StartLabel</strong> (Zeichenkette), <strong>StopLabel</strong> (Zeichenkette) - Marken für Anfang und Ende des Textes.</p></td><td>Reicht der im Kern eingebaute Generator (<a href="../../toolpath-construction/turning-machining-cycle/turning-machining-cycle.md">Bearbeitungszyklus beim Drehen</a>) nicht aus, um den Werkzeugweg eines Drehzyklus zur Konturbearbeitung (vergleichbar mit CYCLE95 der Sinumerik-Steuerung) zu bilden, kann der Text des NC-Programms mit der Kontur abgefragt und selbst analysiert werden. Dafür ist diese Funktion vorgesehen.</td></tr>
</tbody>
</table>

**\*** - Bei der Postprozessierung für die Interpretation werden die Dateien mit den Texten des NC-Programms nicht auf dem Datenträger angelegt, die Texte existieren nur im Speicher. Dateinamen und Nummerierung sind aus technischen Gründen erhalten geblieben und dienen dazu, die Reihenfolge der Texte festzulegen.

**INCT_ProgramManager2** - Schnittstelle für die Arbeit mit dem Text des NC-Programms.

**Beschreibung der Schnittstellenmethoden:**

<table>
<thead>
<tr><th>Methode</th><th>Beschreibung der Methode</th><th>Verwendung</th></tr>
</thead>
<tbody>
<tr><td><strong>GetPartByLabelsFromCurPos</strong></td><td><p>Die Funktion gibt den Text des NC-Programms (Schnittstelle <strong>INCT_Program</strong>) zwischen den angegebenen Marken zurück. Die Suche beginnt an der aktuellen Position.</p><p>Eingabeparameter: <strong>StartLabel</strong> (Zeichenkette), <strong>StopLabel</strong> (Zeichenkette) - Marken für Anfang und Ende des Textes; <strong>Direction</strong> (<strong>TNCGetPartDirection</strong>) - Suchrichtung: <strong>gpdForward</strong> - vorwärts ab der aktuellen Position, <strong>gpdBackward</strong> - rückwärts ab der aktuellen Position.</p></td><td rowspan="2">Siehe die Verwendung von <strong>GetPartByLabels</strong>.</td></tr>
<tr><td><strong>GetPartByRegisters</strong></td><td><p>Die Funktion gibt den Text des NC-Programms (Schnittstelle <strong>INCT_Program</strong>) zwischen den angegebenen Registern zurück.</p><p>Eingabeparameter: <strong>StartReg</strong> (INCT_Register), <strong>StartValues</strong> (INCT_RegisterValues), <strong>StopReg</strong> (INCT_Register), <strong>StopValues</strong> (INCT_RegisterValues) - Register und Werte für Anfang und Ende des Textes.</p></td></tr>
</tbody>
</table>

**INCT_GetPartByUser** - Schnittstelle für die Arbeit mit dem Text des NC-Programms.

**Beschreibung der Schnittstellenmethoden:**

<table>
<thead>
<tr><th>Methode</th><th>Beschreibung der Methode</th><th>Verwendung</th></tr>
</thead>
<tbody>
<tr><td><strong>GetPartByUser</strong></td><td><p>Die Funktion gibt die Schnittstelle <strong>INCT_Program</strong> zurück, mit der das NC-Programm bearbeitet werden kann.<br>Eingabeparameter:</p><p>Typ <strong>TNCGetPartOrigin:</strong></p><p><strong>gpoFromCurPos</strong> - Suche ab der aktuellen Position des NC-Programms</p><p><strong>gpoEntireScope</strong> - Suche ab dem Anfang des NC-Programms</p></td><td rowspan="3"><p>Mit der Funktion lassen sich Anfang und Ende eines Unterprogramms anhand beliebiger Marken bestimmen.<br>1) Mit <strong>GetPartByUser</strong> wird die Schnittstelle <strong>INCT_Program</strong> abgefragt.</p><p>2) Die Marken für Anfang und Ende der Unterprogramme können zum Beispiel in <strong>INCT_InterpreterState</strong> übergeben werden; dafür lassen sich auch Register verwenden.</p><p>3) Nach dem Aufruf der Prozedur <strong>DoSubprogram</strong> der Schnittstelle <strong>INCT_Kernel2</strong> wird das Unterprogramm gesucht. Wurde <strong>INCT_InterpreterState</strong> verwendet, können die zuvor gespeicherten Marken abgefragt werden; alternativ wird in der Methode <strong>TransLine</strong> die Anfangsmarke des Unterprogramms erkannt und <strong>IsStart</strong> aufgerufen. Die Prozedur <strong>IsEnd</strong> wird entsprechend verwendet.</p></td></tr>
<tr><td><strong>IsStart</strong></td><td>Die Prozedur markiert den Anfang des Unterprogramms.</td></tr>
<tr><td><strong>IsEnd</strong></td><td>Die Prozedur markiert das Ende des Unterprogramms.</td></tr>
</tbody>
</table>

**INCT_Program** - Schnittstelle zum Lesen des Textes des NC-Programms. Sie stellt den Text bereit, den einige Funktionen von **INCT_ProgramManager** zurückgeben.

**Beschreibung der Schnittstellenmethoden:**

<table>
<thead>
<tr><th>Methode</th><th>Beschreibung der Methode</th><th>Verwendung</th></tr>
</thead>
<tbody>
<tr><td><strong>EndOfFile</strong></td><td>Die Funktion gibt zurück, ob alle Zeilen gelesen sind. True - der Text des NC-Programms ist zu Ende, False - der Text ist noch nicht vollständig gelesen.</td><td rowspan="2">Nach dem Abfragen der Schnittstelle liefert jeder Aufruf von <strong>GetNextLine</strong> die nächste Zeile des NC-Programms, von der ersten bis zur letzten. Nach der letzten Zeile gibt <strong>EndOfFile</strong> den Wert <strong>True</strong> zurück.</td></tr>
<tr><td><strong>GetNextLine</strong></td><td>Die Funktion gibt die nächste Zeile des NC-Programms zurück.</td></tr>
</tbody>
</table>
