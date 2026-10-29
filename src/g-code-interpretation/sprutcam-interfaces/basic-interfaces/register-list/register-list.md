# Registerliste

**INCT_SysState** - Schnittstelle des Zustands des Systems Maschine-Steuerung. Derzeit ermöglicht die Schnittstelle die Arbeit mit der gebildeten Registerliste (unter Berücksichtigung der Einstellungsdatei, der Programmbibliothek und der übergeordneten Interpreter, siehe [Laden und Initialisierung des Interpreters](../../../interpreter-loading-and-initialization/interpreter-loading-and-initialization.md)). Um die gebildete Registerliste von den ursprünglichen Registern des Interpreters, der Einstellungsdatei und der übergeordneten Interpreter zu unterscheiden, heißt sie **Basisregisterliste**.

**Beschreibung der Schnittstellenmethoden:**

| Methode | Beschreibung der Methode | Verwendung |
| --- | --- | --- |
| **FindFirstRegister** | Die Funktion gibt das erste anhand der Adresse gefundene Basisregister zurück (Schnittstelle **INCT_BaseReg**).<br>Eingabeparameter: **Addr** (Zeichenkette) - Adresse des Registers. | Die Funktion kann bei der Implementierung von **INCT_Interpreter.TransLine** verwendet werden, um bei der Analyse des NC-Programmtexts ein Basisregister anhand der Adresse zu suchen. |
| **FindNextRegister** | Die Funktion gibt das nächste anhand der Adresse gefundene Basisregister ab dem Index **FromIdx** zurück (Schnittstelle **INCT_BaseReg**).<br>Eingabeparameter: **FromIdx** (Ganzzahl) - Anfangsindex, **Addr** (Zeichenkette) - Adresse des Registers. | Die Funktion kann bei der Implementierung von **INCT_Interpreter.TransLine** verwendet werden, um bei der Analyse des NC-Programmtexts ein Basisregister anhand der Adresse zu suchen. |
| **Get_BR_ByIndex** | Die Funktion gibt das Basisregister anhand des Index zurück (Schnittstelle **INCT_BaseReg**).<br>Eingabeparameter: **Index** (Ganzzahl) - Index des Registers. | Die Funktion kann beim Durchlaufen der Basisregister verwendet werden, um ein Basisregister anhand des Index abzufragen (zum Beispiel, um die Anfangswerte der Achsen der Werkzeugposition zu ermitteln, die mit den Basisregistern verbunden sind). |
| **Get_BR_ByName** | Die Funktion gibt das Basisregister anhand des Namens zurück (Schnittstelle **INCT_BaseReg**).<br>Eingabeparameter: **Name** (Zeichenkette) - Name des Registers. | Die Funktion kann verwendet werden, um ein Basisregister anhand des Namens zu suchen und bei der Implementierung von **INCT_Interpreter.DefineRegister** den Index des Registers zu bestimmen. |
| **Get_BR_Count** | Die Funktion gibt die Anzahl der Basisregister zurück. | Die Funktion kann verwendet werden, um die Anzahl der Basisregister für das anschließende Durchlaufen der Basisregister abzufragen (zum Beispiel, um die Anfangswerte der Achsen der Werkzeugposition zu ermitteln, die mit den Basisregistern verbunden sind). |

**INCT_SysState2** - Schnittstelle des Zustands des Systems Maschine-Steuerung.

**Beschreibung der Schnittstellenmethoden:**

<table>
<thead>
<tr><th>Methode</th><th>Beschreibung der Methode</th><th>Verwendung</th></tr>
</thead>
<tbody>
<tr><td><strong>Get_SpindleState</strong></td><td>Die Funktion gibt den Zustand der Spindel zurück (Schnittstelle <strong>INCT_SpindleState</strong>).</td><td>Der Zustand der Spindel dient zum Speichern und Austauschen von Informationen zwischen dem Interpreter und seinen übergeordneten Interpretern.</td></tr>
<tr><td><strong>Get_Reg_ByIndex</strong></td><td><p>Die Funktion gibt das Register anhand des Index zurück (Schnittstelle <strong>INCT_Register</strong>).</p><p>Eingabeparameter: <strong>Index</strong> (Ganzzahl) - Index des Registers.</p></td><td rowspan="3">Die Funktionen können verwendet werden, um ein Register anhand des Namens zu suchen oder die Register nach einem benötigten Parameter zu durchlaufen. Zum Beispiel, um die Werte des Registers <strong>INCT_Register.Values</strong> abzufragen (die in <strong>INCT_BaseReg</strong> nicht verfügbar sind).</td></tr>
<tr><td><strong>Get_Reg_ByName</strong></td><td><p>Die Funktion gibt das Register anhand des Namens zurück (Schnittstelle <strong>INCT_Register</strong>).</p><p>Eingabeparameter: <strong>Name</strong> (Zeichenkette) - Name des Registers.</p></td></tr>
<tr><td><strong>Get_Reg_Count</strong></td><td>Die Funktion gibt die Anzahl der Basisregister zurück.</td></tr>
</tbody>
</table>

**INCT_SpindleState** - Schnittstelle des Zustands der Spindel. Der Zustand der Spindel ist für den Interpreter und seine übergeordneten Interpreter gemeinsam. Er dient zum Speichern und Austauschen des Spindelzustands zwischen dem Interpreter und seinen übergeordneten Interpretern.

**Beschreibung der Schnittstellenmethoden:**

| Methode | Beschreibung der Methode |
| --- | --- |
| **Get_MaxSpeed** | Die Funktion gibt die maximale Drehzahl der Spindel zurück (Gleitkommazahl). |
| **Set_MaxSpeed** | Die Methode legt die maximale Drehzahl der Spindel fest.<br>Eingabeparameter: **Value** (Gleitkommazahl) - maximale Drehzahl der Spindel. |
| **Get_RPMSpeed** | Die Funktion gibt die Drehzahl der Spindel bei ausgeschaltetem Modus konstanter Schnittgeschwindigkeit zurück (Gleitkommazahl) (**Get_CSS** = False). |
| **Set_RPMSpeed** | Die Methode legt die Drehzahl der Spindel fest.<br>Eingabeparameter: **Value** (Gleitkommazahl) - Drehzahl der Spindel. |
| **Get_CSSSpeed** | Die Funktion gibt die Drehzahl der Spindel für den Modus konstanter Schnittgeschwindigkeit zurück (Gleitkommazahl) (**Get_CSS** = True). |
| **Set_CSSSpeed** | Die Methode legt die Drehzahl der Spindel für den Modus konstanter Schnittgeschwindigkeit fest.<br>Eingabeparameter: **Value** (Gleitkommazahl) - Drehzahl der Spindel. |
| **Get_Range** | Die Funktion gibt die Nummer des Drehzahlbereichs der Spindel zurück (Ganzzahl). |
| **Set_Range** | Die Methode legt die Nummer des Drehzahlbereichs der Spindel fest.<br>Eingabeparameter: **Value** (Ganzzahl) - Nummer des Drehzahlbereichs der Spindel. |
| **Get_Direction** | Die Funktion gibt die Drehrichtung der Spindel zurück (boolesch). |
| **Set_Direction** | Die Methode legt die Drehrichtung der Spindel fest.<br>Eingabeparameter: **Value** (boolesch) - Drehrichtung der Spindel.<br>**True** - im Uhrzeigersinn;<br>**False** - gegen den Uhrzeigersinn. |
| **Get_CSS** | Die Funktion gibt das Kennzeichen der konstanten Schnittgeschwindigkeit der Spindel zurück (boolesch). |
| **Set_CSS** | Die Methode legt das Kennzeichen der konstanten Schnittgeschwindigkeit der Spindel fest.<br>Eingabeparameter: **Value** (boolesch) - Kennzeichen der konstanten Schnittgeschwindigkeit der Spindel.<br>**True** - Modus konstanter Schnittgeschwindigkeit eingeschaltet;<br>**False** - Modus konstanter Schnittgeschwindigkeit ausgeschaltet. |
| **Get_MaxRPM** | Die Funktion gibt die maximale Drehzahl bei konstanter Schnittgeschwindigkeit der Spindel zurück (Gleitkommazahl) (**Get_CSS** = True). |
| **Set_MaxRPM** | Die Methode legt die maximale Drehzahl bei konstanter Schnittgeschwindigkeit der Spindel fest.<br>Eingabeparameter: **Value** (Gleitkommazahl) - maximale Drehzahl bei konstanter Schnittgeschwindigkeit der Spindel. |
| **Get_Angle** | Die Funktion gibt den Winkel des orientierten Spindelhalts zurück (Gleitkommazahl). |
| **Set_Angle** | Die Methode legt den Winkel des orientierten Spindelhalts fest.<br>Eingabeparameter: **Value** (Gleitkommazahl) - Winkel des orientierten Spindelhalts. |
| **Get_Command** | Die Funktion gibt den Status der Spindel zurück (zuletzt ausgeführter Befehl) (**TNCSpindleCommand**). |
| **Set_Command** | Die Methode legt den Status der Spindel fest (zuletzt ausgeführter Befehl).<br>Eingabeparameter: **Value** (**TNCSpindleCommand**) - Status der Spindel.<br>**scOn** - eingeschaltet;<br>**scOff** - ausgeschaltet;<br>**scOrient** - orientierter Spindelhalt. |
| **Get_IsChanged** | Die Funktion gibt das Kennzeichen zurück, ob sich seit der Ausführung des letzten Spindelbefehls ein Parameter von **INCT_SpindleState** außer der Spindelnummer geändert hat (boolesch).<br>**True** - einer der Parameter hat sich geändert;<br>**False** - die Parameter haben sich nicht geändert. |
| **Set_IsChanged** | Die Methode legt das Kennzeichen fest, ob sich seit der Ausführung des letzten Spindelbefehls ein Parameter von **INCT_SpindleState** außer der Spindelnummer geändert hat. Wird bei der Vererbung von Interpretern verwendet. Den Befehl zum Einschalten, Ausschalten oder Anhalten der Spindel führt einer der Interpreter aus, in der Regel der letzte Nachfolger.<br>Eingabeparameter: **Value** (boolesch) - Kennzeichen der Parameteränderung. |
| **Get_Num** | Die Funktion gibt die Nummer der Spindel zurück (Ganzzahl). |
| **Set_Num** | Die Methode legt die Nummer der Spindel fest.<br>Eingabeparameter: **Value** (Ganzzahl) - Nummer der Spindel. |
| **Get_IsChangedNum** | Die Funktion gibt das Kennzeichen der Änderung der Spindelnummer zurück (boolesch). |
| **Set_IsChangedNum** | Die Methode legt das Kennzeichen der Änderung der Spindelnummer fest.<br>Eingabeparameter: **Value** (boolesch) - Kennzeichen der Änderung der Spindelnummer. |

**INCT_BaseReg** - Schnittstelle für die Arbeit mit einem Basisregister.

**Beschreibung der Schnittstellenmethoden:**

<table>
<thead>
<tr><th>Methode</th><th>Beschreibung der Methode</th><th>Verwendung</th></tr>
</thead>
<tbody>
<tr><td><strong>SetValue</strong></td><td><p>Die Methode weist dem Basisregister einen neuen Wert zu. Das Basisregister hat drei Felder zum Speichern des Werts: Zeichenkette, Gleitkommazahl, Ganzzahl. Ist der neue Wert nicht leer, wird er in das Zeichenkettenfeld geschrieben, umgewandelt und in die Felder für Ganzzahl und Gleitkommazahl geschrieben.</p><p>Eingabeparameter: <strong>Value</strong> (Zeichenkette) - neuer Wert des Registers.</p></td><td>Die Methode kann bei der Interpretation von Lexemen und Konstrukten verwendet werden, die den Wert des Registers beeinflussen (zum Beispiel Funktionen).</td></tr>
<tr><td><strong>Get_Addr</strong></td><td><p>Die Funktion gibt die Adresse des Basisregisters zurück (Zeichenkette).</p><p>Keine Eingabeparameter.</p></td><td rowspan="7">Die Funktionen können verwendet werden, um bei der Initialisierung, Übersetzung oder Interpretation des NC-Programmtexts die entsprechenden Parameter des Basisregisters abzufragen.</td></tr>
<tr><td><strong>Get_Name</strong></td><td><p>Die Funktion gibt den Namen des Basisregisters zurück (Zeichenkette).</p><p>Keine Eingabeparameter.</p></td></tr>
<tr><td><strong>Get_Id</strong></td><td><p>Die Funktion gibt die Kennung des Basisregisters im kinematischen Schema der Maschine zurück (Zeichenkette).</p><p>Keine Eingabeparameter.</p></td></tr>
<tr><td><strong>Get_Idx</strong></td><td><p>Die Funktion gibt den Index des Basisregisters in der Registerliste zurück (Ganzzahl).</p><p>Keine Eingabeparameter.</p></td></tr>
<tr><td><strong>Get_Str</strong></td><td><p>Die Funktion gibt den Zeichenkettenwert des Basisregisters zurück (Zeichenkette).</p><p>Keine Eingabeparameter.</p></td></tr>
<tr><td><strong>Get_Int</strong></td><td><p>Die Funktion gibt den Zahlenwert des Basisregisters zurück (Ganzzahl).</p><p>Keine Eingabeparameter.</p></td></tr>
<tr><td><strong>Get_Flt</strong></td><td><p>Die Funktion gibt den Zahlenwert des Basisregisters zurück (Gleitkommazahl).</p><p>Keine Eingabeparameter.</p></td></tr>
</tbody>
</table>
