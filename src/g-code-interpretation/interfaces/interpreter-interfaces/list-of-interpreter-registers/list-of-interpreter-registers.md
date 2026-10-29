# Liste der Interpreter-Register

**INCT_RegisterList** - Schnittstelle, die die Funktion **[INCT_Interpreter](../interpreter-interface/interpreter-interface.md).GetRegisters** des Interpreters zurückgibt. Die Schnittstelle ermöglicht die Arbeit mit der Liste der Register des Interpreters.

**Beschreibung der Schnittstellenmethoden:**

<table>
<thead>
<tr><th>Methode</th><th>Beschreibung der Methode</th><th>Verwendung</th></tr>
</thead>
<tbody>
<tr><td><strong>Get_Count<br></strong></td><td><p>Die Funktion muss dem CAM-System die Anzahl der Register des Interpreters zurückgeben.</p><p>Keine Eingabeparameter.</p></td><td rowspan="2">Beim Bilden der gemeinsamen Liste der Register ruft das CAM-System die Funktion <strong>Get_Count</strong> auf, erhält die Anzahl der Register und ruft danach für jedes Register nacheinander die Funktion <strong>Get_Item</strong> auf.</td></tr>
<tr><td><strong>Get_Item<br></strong></td><td><p>Die Funktion muss dem CAM-System anhand der Nummer des Registers die Schnittstelle <strong>INCT_Register</strong> zurückgeben (siehe unten).</p><p>Eingabeparameter: <strong>Index</strong> (Ganzzahl) - Nummer des Registers. Die Nummerierung beginnt bei 0.</p></td></tr>
</tbody>
</table>

**INCT_Register** - Schnittstelle, die die Funktion **INCT_RegisterList.Get_Item** des Interpreters zurückgibt. Die Schnittstelle ermöglicht die Arbeit mit den Parametern des gewählten Registers des Interpreters.

**Beschreibung der Schnittstellenmethoden:**

| Methode | Beschreibung der Methode | Verwendung |
| --- | --- | --- |
| **Get_Addr** | Die Funktion muss dem CAM-System die Adresse des Registers zurückgeben (Zeichenkette).<br>Keine Eingabeparameter. | Das CAM-System sucht das Register anhand der Adresse in der Liste der Register. |
| **Get_Id** | Die Funktion muss dem CAM-System den Bezeichner des Registers im kinematischen Schema der Maschine zurückgeben (Zeichenkette).<br>Keine Eingabeparameter. | Bezeichner des Registers im kinematischen Schema der Maschine, falls zutreffend. Andernfalls ist die Zeichenkette leer. |
| **Get_Name** | Die Funktion muss dem CAM-System den Namen des Registers zurückgeben (Zeichenkette).<br>Keine Eingabeparameter. | Eindeutiger Name des Registers. Dient zur eindeutigen Bestimmung des Registers in der Liste. |
| **Get_Comment** | Die Funktion muss dem CAM-System den Kommentar des Registers zurückgeben (Zeichenkette).<br>Keine Eingabeparameter. | Die Funktion wird aufgerufen, der zurückgegebene Wert wird in der aktuellen Version jedoch nicht verwendet. |
| **Get_Sign** | Die Funktion muss dem CAM-System die Art des Vorzeichens des Registers zurückgeben (Aufzählungstyp **TNCSign**).<br>**sgnNoSign** - ohne Vorzeichen;<br>**sgnMinus** - nur Minus;<br>**sgnPlusAndMinus** - Plus und Minus.<br>Keine Eingabeparameter. | Die Funktion wird aufgerufen, der zurückgegebene Wert wird in der aktuellen Version jedoch nicht verwendet. |
| **Get_Point** | Die Funktion muss dem CAM-System die Art des Dezimalpunkts des Registers zurückgeben (Aufzählungstyp **TNCPoint**).<br>**pntNoPoint** - ohne Punkt;<br>**pntPoint** - der Punkt kann vorhanden sein oder fehlen;<br>**pntAlwaysPoint** - der Punkt ist immer vorhanden.<br>Keine Eingabeparameter. | Die Funktion wird aufgerufen, der zurückgegebene Wert wird in der aktuellen Version jedoch nicht verwendet. |
| **Get_BeforePoint** | Die Funktion muss dem CAM-System die Anzahl der Stellen vor dem Punkt des Registers zurückgeben (Ganzzahl).<br>Keine Eingabeparameter. | Die Funktion wird aufgerufen, der zurückgegebene Wert wird in der aktuellen Version jedoch nicht verwendet. |
| **Get_AfterPoint** | Die Funktion muss dem CAM-System die Anzahl der Stellen nach dem Punkt des Registers zurückgeben (Ganzzahl).<br>Keine Eingabeparameter. | Die Funktion dient zur Prüfung der Korrektheit von Kreisbögen, daher ist es wichtig, die Anzahl der Stellen nach dem Punkt richtig anzugeben. Der Generator des Werkzeugwegs verwendet diese Funktion im Kern. |
| **Get_LeadingZeros** | Die Funktion muss dem CAM-System das Kennzeichen zurückgeben, ob das Register führende Nullen hat (boolesch).<br>Keine Eingabeparameter. | Die Funktion wird aufgerufen, der zurückgegebene Wert wird in der aktuellen Version jedoch nicht verwendet. |
| **Get_TrailingZeroes** | Die Funktion muss dem CAM-System das Kennzeichen zurückgeben, ob das Register nachgestellte Nullen hat (boolesch).<br>Keine Eingabeparameter. | Die Funktion wird aufgerufen, der zurückgegebene Wert wird in der aktuellen Version jedoch nicht verwendet. |
| **Get_ValueAvail** | Die Funktion muss dem CAM-System den Typ des Registers zurückgeben (Aufzählungstyp **TNCValueAvailType**).<br>**vatValue** - das Register besteht aus Adresse und Wert;<br>**vatOnlyAddr** - das Register besteht nur aus der Adresse;<br>**vatBoth** - das Register kann entweder nur aus der Adresse oder aus Adresse und Wert bestehen.<br>Keine Eingabeparameter. | Wird bei der [Bestimmung des Registers und seines Werts](../../../translation-and-interpretation/algorithm-for-determining-register-and-values-in-g-code-block/algorithm-for-determining-register-and-values-in-g-code-block.md) verwendet. |
| **Get_Values** | Die Funktion muss dem CAM-System die Liste der Werte des Registers zurückgeben (Schnittstelle **INCT_RegisterValues**).<br>Keine Eingabeparameter. | **INCT_RegisterValues.Get_Count** - Anzahl der Werte<br>**INCT_RegisterValues.Get_Value** - Wert nach Index (**Index** - Ganzzahl)<br>Die Liste der Werte des Registers wird bei der [Bestimmung des Registers und seines Werts](../../../translation-and-interpretation/algorithm-for-determining-register-and-values-in-g-code-block/algorithm-for-determining-register-and-values-in-g-code-block.md) verwendet. |
| **Get_Modal** | Die Funktion muss dem CAM-System das Kennzeichen zurückgeben, ob das Register modal ist (boolesch).<br>Keine Eingabeparameter. | Wird beim Kopieren der Werte der Register nach der Interpretation des aktuellen Satzes verwendet. Modale Register gelangen nur dann in **INCT_BlockExecArray**, wenn sich ihr Wert im aktuellen Satz geändert hat. Nichtmodale Register immer, wenn sie im aktuellen Satz vorkommen. |
