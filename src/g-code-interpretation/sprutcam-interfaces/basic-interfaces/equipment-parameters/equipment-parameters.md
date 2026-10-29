# Parameter der Ausrüstung

**INCT_Equipment** - Schnittstelle des CAM-Systems für den Zugriff auf einige Parameter der Ausrüstung.

**Beschreibung der Schnittstellenmethoden:**

<table>
<thead>
<tr><th>Methode</th><th>Beschreibung der Methode</th><th>Verwendung</th></tr>
</thead>
<tbody>
<tr><td><strong>GetAxisIndex</strong></td><td><p>Die Funktion gibt den Index einer Maschinenachse anhand ihrer Adresse zurück (Ganzzahl).</p><p>Eingabeparameter: <strong>Addr</strong> (Zeichenkette) - Adresse der Achse ('X', 'Y', 'Z' usw., wie im kinematischen Schema der Maschine angegeben).</p></td><td>Zur Steuerung der Werkzeugbewegung (mit <strong><a href="../forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md">INCT_CLData.AddMotion</a></strong> oder <a href="../../toolpath-construction/linear-movements/linear-movements.md"><strong>CreateLinearMotionFormer</strong></a>) müssen die Achsindizes angegeben werden, die die Funktion <strong>GetAxisIndex</strong> liefert.</td></tr>
<tr><td><strong>GetAxisIndexByNum</strong></td><td><p>Die Funktion gibt den Index einer Haupt- oder Zusatzachse des Roboters anhand ihrer Nummer zurück (Ganzzahl).</p><p>Eingabeparameter: <strong>AxisNum</strong> (Ganzzahl) - Nummer der Roboterachse (1-6); <strong>Ext</strong> (boolesch): False - Achse des Roboters, True - Zusatzachse.</p></td><td>Wird eine Roboterachse über ihre Nummer (nicht über ihre Adresse) angegeben, kann ihr Index mit der Funktion <strong>GetAxisIndexByNum</strong> ermittelt werden. So lassen sich in der Regel die Achsen von Motoman-Robotern ermitteln.</td></tr>
<tr><td><strong>GetXYZindex</strong></td><td><p>Die Funktion gibt den Index der Achse zurück, die der Bewegung entlang der Koordinate X, Y oder Z zugeordnet ist (siehe <a href="../forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md"><strong>INCT_CLData.AddCircle</strong></a>).</p><p>Eingabeparameter: <strong>Ort</strong> (Ganzzahl)</p><p>1 - <strong>X</strong>; 2 - <strong>Y</strong>; 3 - <strong>Z</strong>.</p></td><td>Zum Abfragen der Indizes der Achsen, die X, Y, Z des aktuellen Werkzeugs zugeordnet sind.</td></tr>
<tr><td><strong>CurrentLatheToolWidth</strong></td><td>Die Funktion gibt die Breite des aktuellen Drehwerkzeugs zurück (Gleitkommazahl).</td><td>Wird verwendet, um die Schrittweite der Einstichbreite in <a href="../../toolpath-construction/turning-cycle-grooving/turning-cycle-grooving.md"><strong>INCT_LatheGroovingCycleFormer</strong></a> festzulegen.</td></tr>
<tr><td><strong>GetSpindlesCount</strong></td><td>Die Funktion gibt die Anzahl der Spindeln der aktuellen Maschine zurück (Ganzzahl).</td><td rowspan="2">Zur Ausführung von Befehlen, die eine Spindel der Maschine über ihre Nummer steuern, zum Beispiel SPos[<strong>SpindelIndex</strong>] = Value der Sinumerik-Steuerung.</td></tr>
<tr><td><strong>GetAxisIndexBySpindleIndex</strong></td><td><p>Die Funktion gibt die Nummer der Spindelachse anhand des Spindelindex zurück (Ganzzahl).</p><p>Eingabeparameter: <strong>SpindleIndex</strong> (Ganzzahl) - Spindelindex, mögliche Werte von <strong>0</strong> bis <strong>GetSpindlesCount -1</strong>.</p></td></tr>
<tr><td><strong>GetOperationGroup</strong></td><td><p>Die Funktion gibt den Typ der Operation im CAM-System zurück (<strong>TNCOperationGroup</strong>).</p><p>Typ <strong>TNCOperationGroup:</strong></p><p><strong>ogUnknown</strong> - unbekannt<br><strong>ogMill</strong> - Fräsen<br><strong>ogLathe</strong> - Drehen<br><strong>ogAuxiliary</strong> - Hilfsoperation<br><strong>ogWireEDM</strong> - Drahterodieren<br><strong>ogWelding</strong> - Schweißen aller Art<br><strong>ogAdditive</strong> - additive Verfahren wie Auftragschweißen<br><strong>ogWaterJet</strong> - Wasserstrahlschneiden<br><strong>ogSawing</strong> - Sägen</p></td><td><p><strong>Bei der Entwicklung von Interpretern nur in Ausnahmefällen verwenden.</strong></p><p>Die Funktion wurde eingeführt, um die Lage des Drehwerkzeugs in einer Drehoperation des CAM-Systems auszugleichen, wenn kein Korrekturwert angegeben werden kann.</p></td></tr>
</tbody>
</table>

**INCT_Equipment2** - Schnittstelle des CAM-Systems für den Zugriff auf weitere Parameter der Ausrüstung.

**Beschreibung der Schnittstellenmethoden:**

| Methode | Beschreibung der Methode | Verwendung |
| --- | --- | --- |
| **GetCurrentToolRadius** | Die Funktion gibt den Radius des aktuellen Werkzeugs zurück (Gleitkommazahl). | Kann zur Berechnung der Überläufe für CYCLE90 der Sinumerik-Steuerung verwendet werden. |

**INCT_Equipment_Channels** - Schnittstelle des CAM-Systems für den Zugriff auf die Kanäle der Maschine. Die Schnittstelle wird beim Objekt **INCT_Equipment** abgefragt; das Ergebnis der Abfrage muss geprüft werden: In früheren Versionen des CAM-Systems unterstützt das Objekt sie möglicherweise nicht.

**Beschreibung der Schnittstellenmethoden:**

| Methode | Beschreibung der Methode | Verwendung |
| --- | --- | --- |
| **Get_Count** | Die Funktion gibt die Anzahl der Kanäle der Maschine zurück (Ganzzahl). | |
| **Get_CurrentIndex** | Die Funktion gibt den Index des Kanals zurück, zu dem die aktuelle Operation gehört (Ganzzahl). Die Nummerierung beginnt bei 0. | Zur Interpretation von Mehrkanalprogrammen: Der Interpreter kann feststellen, das Programm welches Kanals er gerade interpretiert. |
| **Get_Channel** | Die Funktion gibt die Schnittstelle des Kanals (**INCT_Channel**) anhand des Index zurück.<br>Eingabeparameter: **Index** (Ganzzahl) - Kanalindex, mögliche Werte von **0** bis **Get_Count - 1**. | |

**INCT_Channel** - Schnittstelle des CAM-Systems für den Zugriff auf die Parameter eines Maschinenkanals.

**Beschreibung der Schnittstellenmethoden:**

| Methode | Beschreibung der Methode | Verwendung |
| --- | --- | --- |
| **Get_Name** | Die Funktion gibt den im kinematischen Schema der Maschine angegebenen Namen des Kanals zurück (Zeichenkette). | |
