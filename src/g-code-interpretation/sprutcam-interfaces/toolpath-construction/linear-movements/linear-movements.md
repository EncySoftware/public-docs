# Lineare Bewegungen

**INCT_LinearMotionFormer** - Schnittstelle des CAM-Systems, die die Bildung linearer Bewegungen vereinfacht. Die Schnittstelle gibt die Funktion **[INCT_CLData.CreateLinearMotionFormer](../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md)** zurück.

**Zweck:**

Lineare Bewegungen werden aus einem Satz des NC-Programms wie folgt gebildet. Der Text des NC-Programms wird [übersetzt](../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md), d. h. in Register mit Werten zerlegt. Die Register mit Werten werden in die Liste der zu interpretierenden Objekte aufgenommen. Die Objekte der Liste werden interpretiert. Bei der [Interpretation der Objekte](../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md) wird dem Werkzeugweg (**INCT_CLData**) anhand der geänderten Werte der Register, die mit den Maschinenachsen des kinematischen Schemas verknüpft sind, ein Befehl für eine mehrachsige Bewegung hinzugefügt ([**INCT_CLData.OpenMultiMotion, AddMotion, CloseMultiMotion**](../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md)).

Im Einzelnen ergeben sich daraus folgende Schritte.

Vor der Interpretation des NC-Programms:

1. *Die Liste der Register abfragen, die mit den Maschinenachsen im kinematischen Schema verknüpft sind.*
2. *Die Liste der Register mit den Achsindizes speichern.*

Vor der Interpretation eines Satzes:

1. *Die aktuellen Koordinaten der Werkzeugposition für alle Achsen abfragen, die mit den Maschinenachsen im kinematischen Schema verknüpft sind.*

Bei der Interpretation der Register:

1. *Die neuen Werte der Register des Satzes abfragen, die mit den Maschinenachsen im kinematischen Schema verknüpft sind.*
2. *Die neuen Werte für alle geänderten Register des Satzes setzen, die mit den Maschinenachsen im kinematischen Schema verknüpft sind.*

Nach der Interpretation des Satzes oder während der Interpretation, aber nach der Interpretation aller Register:

1. *Die neuen Achskoordinaten mit den alten auf Änderungen vergleichen.*
2. *Gab es eine Änderung:*
3. *Die Methode **OpenMultiMotion** ausführen.*
4. *Den Wert jeder Achse auf Änderung prüfen und, wenn sich die Werkzeugposition entlang der Achse geändert hat, **AddMotion** ausführen.*
5. *Die Methode **CloseMultiMotion** ausführen.*

*Für Befehle, die Bewegungen in den physischen Koordinaten der Maschine erfordern, muss außerdem die Bewegungsart auf **gtmPhysic** umgeschaltet werden.*

Die oben *kursiv* markierten Schritte sind im Generator linearer Bewegungen (**INCT_LinearMotionFormer**) implementiert. Der Generator vereinfacht das Schreiben eines Interpreters.

Wir empfehlen, für den gesamten Interpretationszyklus des NC-Programms einen einzigen Generator linearer Bewegungen zu erstellen. Er wird bei der Initialisierung des Interpreters erstellt ([**INCT_Interpreter.Initialize**](../../../interpreter-loading-and-initialization/interpreter-loading-and-initialization.md)).

**Beschreibung der Schnittstellenmethoden:**

<table>
<thead>
<tr><th>Methode</th><th>Beschreibung der Methode</th><th>Verwendung</th></tr>
</thead>
<tbody>
<tr><td><strong>SetGotoMode</strong></td><td><p>Die Methode legt die Art der gebildeten Bewegungen fest.</p><p>Eingabeparameter: <strong>Mode</strong> (<strong>TNCGotoMode</strong>) - Bewegungsart, siehe Beschreibung von <strong><a href="../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md">OpenMultiMotion</a></strong>.</p><p>Wird die Bewegungsart nicht mit dieser Methode festgelegt, gilt <strong>gtmTooltip</strong>.</p><p>Keine Ausgabeparameter.</p></td><td>Die Methode kann bei der Interpretation von G53 im ISO-Code verwendet werden (Bewegungsart auf <strong>gtmPhysic</strong> setzen und danach wieder auf <strong>gtmTooltip</strong>).</td></tr>
<tr><td><strong>Get_ClearGotoMode</strong></td><td><p>Die Funktion gibt den Wert des Parameters <strong>ClearGotoMode</strong> zurück (boolesch).</p><p>Keine Eingabeparameter.</p></td><td rowspan="2"><p>Der Parameter <strong>ClearGotoMode</strong> steuert das automatische Zurücksetzen der Bewegungsart (siehe <strong>SetGotoMode</strong>) auf <strong>gtmTooltip</strong>. Zurückgesetzt wird in <strong>InitBlock</strong>.</p><p>In der Regel wirkt der Befehl G53 nur im aktuellen Satz, daher ist es sinnvoll, <strong>ClearGotoMode</strong> auf True zu setzen. Nach der Interpretation eines Satzes mit G53 (in dem die Bewegungsart auf <strong>gtmPhysic</strong> gesetzt wird) kehrt die Bewegungsart dann beim nächsten Aufruf von <strong>InitBlock</strong> von selbst auf <strong>gtmTooltip</strong> zurück.</p></td></tr>
<tr><td><strong>Set_ClearGotoMode</strong></td><td><p>Die Methode legt den Wert des Parameters <strong>ClearGotoMode</strong> fest.</p><p>Eingabeparameter: <strong>Value</strong> (boolesch) - Wert des Parameters <strong>ClearGotoMode</strong>.</p><p>Keine Ausgabeparameter.</p></td></tr>
<tr><td><strong>InitAxisIndex</strong></td><td><p>Die Methode fügt einen Achsindex zur Liste hinzu.</p><p>Eingabeparameter: <strong>Index</strong> (Ganzzahl) - Index der Achse, die zur Liste hinzugefügt wird.</p><p>Keine Ausgabeparameter.</p></td><td><p>Dient zum Hinzufügen der Achsen, die mit den Maschinenachsen im kinematischen Schema verknüpft sind. Wird in der Regel direkt nach dem Abfragen der Schnittstelle (Funktion <strong><a href="../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md">INCT_CLData.CreateLinearMotionFormer</a></strong>) in der Implementierung der Methode <strong><a href="../../../interpreter-loading-and-initialization/interpreter-loading-and-initialization.md">INCT_Interpreter.Initialize</a></strong> des Interpreters ausgeführt.</p><p>Die Indizes der Register, die mit den Maschinenachsen verknüpft sind, lassen sich über die Schnittstellen <a href="../../basic-interfaces/register-list/register-list.md"><strong>INCT_SysState</strong></a> und <a href="../../basic-interfaces/equipment-parameters/equipment-parameters.md"><strong>INCT_Equipment</strong></a> abfragen.</p></td></tr>
<tr><td><strong>ClearAxesIndexes</strong></td><td>Die Methode leert die Liste der Achsindizes.</td><td>Wird beim Werkzeugwechsel verwendet, wenn die Namen der Achsen, die das Werkzeug steuern, übereinstimmen.</td></tr>
<tr><td><strong>InitBlock</strong></td><td><p>Die Methode speichert in der internen Liste die aktuellen Werkzeugkoordinaten für alle Achsen der mit <strong>InitAxisIndex</strong> gebildeten Liste. Hat <strong>ClearGotoMode</strong> den Wert True, wird die mit <strong>SetGotoMode</strong> festgelegte Bewegungsart auf <strong>gtmTooltip</strong> gesetzt.</p><p>Keine Ein- und Ausgabeparameter.</p></td><td>Muss vor der Interpretation der Objekte aufgerufen werden, die mit Registern verknüpft sind. Empfohlen wird der Aufruf in der Implementierung der Methode <a href="../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md"><strong>INCT_Interpreter.BeforeInterprete</strong></a>.</td></tr>
<tr><td><strong>SetAxisValue</strong></td><td><p>Die Methode speichert in der internen Liste den neuen Wert der Werkzeugkoordinate für die angegebene Achse.</p><p>Eingabeparameter: <strong>Abs</strong> (boolesch) - Art des neuen Koordinatenwerts, True - absoluter Wert, False - relativer Wert (bezogen auf den aktuellen Koordinatenwert, siehe <strong>InitBlock</strong>); <strong>Index</strong> (Ganzzahl) - Index der Achse; <strong>Value</strong> (Gleitkommazahl) - neuer Wert.</p><p>Keine Ausgabeparameter.</p></td><td>Dient zum Speichern des neuen Werts in der internen Liste, um anschließend den Befehl für eine mehrachsige Bewegung zu bilden. Wird bei der Interpretation in <a href="../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md"><strong>INCT_Interpreter.Interprete</strong></a> verwendet.</td></tr>
<tr><td><strong>MakeWorkpath</strong></td><td>Die Methode vergleicht die Liste der aktuellen Koordinaten (in <strong>InitBlock</strong> gespeichert) mit den neuen Koordinaten der Werkzeugbewegung (in <strong>SetAxisValue</strong> gespeichert). Haben sich Koordinaten geändert, wird im Werkzeugweg ein Befehl für eine mehrachsige Bewegung entlang der geänderten Achskoordinaten gebildet (<a href="../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md"><strong>INCT_CLData.OpenMultiMotion, AddMotion, CloseMultiMotion</strong></a>).</td><td>Zum Bilden des Befehls für eine mehrachsige Bewegung. Wird bei der Interpretation in <strong><a href="../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md">INCT_Interpreter.Interprete</a></strong> nach der Interpretation aller Register verwendet (<a href="../../basic-interfaces/list-of-objects-to-interpret/list-of-objects-to-interpret.md">am Ende der Liste der zu interpretierenden Objekte hinzufügen</a>) oder in <strong><a href="../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md">INCT_Interpreter.AfterInterprete</a></strong>.</td></tr>
</tbody>
</table>

**INCT_GeomLinearMotionFormer** - Schnittstelle des CAM-Systems, die die Bildung linearer Bewegungen vereinfacht. Die Schnittstelle gibt die Funktion **[INCT_GeomCLData.CreateLinearMotionFormer](../../basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md)** zurück.

Der **Zweck** entspricht der Schnittstelle **INCT_LinearMotionFormer**, jedoch für Bewegungen in geometrischen Achsen. Die Bewegungen werden mit dem Befehl **[CutTo3d](../../basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md)** gebildet. Für die erste Bewegung müssen daher die Koordinaten aller drei Achsen festgelegt werden.

**Beschreibung der Schnittstellenmethoden:**

| Methode | Beschreibung der Methode | Verwendung |
| --- | --- | --- |
| **ClearSpecifiedAxes** | Die Methode leert die Liste der für die erste Bewegung festgelegten Achsen.<br>Keine Ein- und Ausgabeparameter. | Muss zu Beginn jeder Operation aufgerufen werden. Empfohlen wird der Aufruf in der Implementierung der Methode **[INCT_Interpreter.NextOperation](../../../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md)**. |
| **InitBlock** | Die Methode speichert in der internen Liste die aktuellen Werte der drei Werkzeugkoordinaten.<br>Keine Ein- und Ausgabeparameter. | Muss vor der Interpretation der Objekte aufgerufen werden, die mit Registern verknüpft sind. Empfohlen wird der Aufruf in der Implementierung der Methode [**INCT_Interpreter.BeforeInterprete**](../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md). |
| **SetAxisValue** | Die Methode speichert in der internen Liste den neuen Wert der Werkzeugkoordinate für die angegebene Achse.<br>Eingabeparameter: **Abs** (boolesch) - Art des neuen Koordinatenwerts, True - absoluter Wert, False - relativer Wert (bezogen auf den aktuellen Koordinatenwert, siehe **InitBlock**); **Index** (Ganzzahl) - Index der Achse (1-3); **Value** (Gleitkommazahl) - neuer Wert.<br>Keine Ausgabeparameter. | Dient zum Speichern des neuen Werts in der internen Liste, um anschließend den Bewegungsbefehl zu bilden. Wird bei der Interpretation in [**INCT_Interpreter.Interprete**](../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md) verwendet. |
| **MakeWorkpath** | Die Methode vergleicht die Liste der aktuellen Koordinaten (in **InitBlock** gespeichert) mit den neuen Koordinaten der Werkzeugbewegung (in **SetAxisValue** gespeichert). Haben sich Koordinaten geändert und sind die Koordinaten aller drei Achsen festgelegt, wird im Werkzeugweg ein Bewegungsbefehl gebildet (**[INCT_GeomCLData.CutTo3d](../../basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md)**). | Zum Bilden des Bewegungsbefehls. Wird bei der Interpretation in **[INCT_Interpreter.Interprete](../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md)** nach der Interpretation aller Register verwendet ([am Ende der Liste der zu interpretierenden Objekte hinzufügen](../../basic-interfaces/list-of-objects-to-interpret/list-of-objects-to-interpret.md)) oder in **[INCT_Interpreter.AfterInterprete](../../../translation-and-interpretation/translation-and-interpretation-g-code-based-program.md)**. |
