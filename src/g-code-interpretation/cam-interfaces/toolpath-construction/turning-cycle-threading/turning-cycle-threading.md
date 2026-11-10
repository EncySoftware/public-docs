# Gewindeschneiden mit Drehzyklus

**INCT_LatheThreadCuttingCycleFormer** - Schnittstelle des CAM-Systems, die die Bildung der Bewegungen eines Drehzyklus zum Gewindeschneiden vereinfacht. Das Objekt, das diese Schnittstelle implementiert, gibt die Funktion **[INCT_CLData.CreateLatheCycleFormer](../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md), [INCT_GeomCLData.CreateLatheCycleFormer](../../basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md)** zurück, wenn sie mit dem Parameter **lctThreadCutting** aufgerufen wird.

<img src="../../../../../images/129931523/ThreadCuttingCycle_Outer.png" alt="ThreadCuttingCycle_Outer" width="1000">

<img src="../../../../../images/129931523/ThreadCuttingCycle_Inner.png" alt="ThreadCuttingCycle_Inner" width="1000">

<img src="../../../../../images/129931523/ThreadCuttingCycle_Params.png" alt="ThreadCuttingCycle_Params" width="900">

**Zweck:**

Die Bewegungen in den verschiedenen Arten von Drehzyklen zum Gewindeschneiden folgen bei den unterschiedlichen Steuerungen im Allgemeinen demselben Ablauf:

1. Anfahren des Startpunkts oder des Punkts des nächsten Durchgangs auf der Rückzugsebene im Eilgang.
2. Fahren zum Anfangspunkt des Gewindes im Arbeitsvorschub.
3. Gewindeschneiden bis zum Endpunkt im Arbeitsvorschub.
4. Rückkehr auf die Rückzugsebene im Eilgang.
5. Ist die Anzahl der Durchgänge (Schrupp- und Schlichtdurchgänge) noch nicht erreicht, Rückkehr zu Schritt 1.

Beispiel eines solchen Zyklus für Sinumerik: CYCLE97.

Mit dem Generator lässt sich der Werkzeugweg aus vorgegebenen Parametern bilden: Anfangs- und Endpunkt des Gewindes, Rückzugsebene, Gangzahl des Gewindes, Zustellart, Zustellwinkel usw. Außerdem können auf jedem Abschnitt die für einen bestimmten Zyklus nötigen Besonderheiten ergänzt, Art oder Wert des Vorschubs geändert oder vom Generator vorbereitete Werkzeugbewegungen übersprungen werden.

**Verwendung des Generators:**

Wir empfehlen, für jeden neuen Zyklus in einem Satz des NC-Programms einen neuen Generator des Drehzyklus zu erstellen, außer wenn ein Zyklus in einem neuen Satz wiederholt wird. Die Schnittstelle des alten Generators muss daher beim Erstellen eines neuen Generators oder beim Beenden des Interpreters freigegeben werden.

Um die Befehle für den Werkzeugweg entlang des Zyklus zu bilden, sind folgende Schritte nötig:

1. Die Schnittstelle des Generators abfragen (**[INCT_CLData.CreateLatheCycleFormer](../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md), [INCT_GeomCLData.CreateLatheCycleFormer](../../basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md)**).
2. Die Indizes der Längs- und Querachse festlegen, entlang derer die Bewegungen ausgeführt werden (**Set_AxisIndexes**).
3. Die Parameter des Zyklus festlegen (**Set_ThreadOrientation, Set_ThreadDepth, Set_ThreadStep, Set_ThreadStartAngle, Set_StartPoint** usw., Beschreibung siehe unten).
4. Einen Ereignishandler des Zyklus zuweisen (**Set_Events**), wenn der Werkzeugweg des Zyklus geändert werden soll.
5. Die Befehle für den Werkzeugweg entlang des Zyklus bilden (**MakeWorkpath**).

**Beschreibung der Schnittstellenmethoden:**

| Methode | Beschreibung der Methode |
| --- | --- |
| **Set_AxisIndexes** | Die Methode legt die Indizes der Längs- und Querachse fest, entlang derer die Bewegungen bei der Bildung des Werkzeugwegs des Zyklus ausgeführt werden.<br>Eingabeparameter: **Value** (**TNCLCAxisIndexes**) - **Transverse** (Ganzzahl) - Index der Querachse, **Longitudinal** (Ganzzahl) - Index der Längsachse.<br>Keine Ausgabeparameter. |
| **Get_AxisIndexes** | Die Funktion gibt die Indizes der Längs- und Querachse zurück, entlang derer die Bewegungen bei der Bildung des Werkzeugwegs des Zyklus ausgeführt werden (**TNCLCAxisIndexes**).<br>Keine Eingabeparameter. |
| **Set_Direction** | Die Methode legt die Richtung des Gewindeschneidzyklus fest.<br>Eingabeparameter: **Value** (**TNCThreadCuttingDirection**) - Richtung des Zyklus: **drLongitudinal** - längs, **drTransverse** - quer.<br>Keine Ausgabeparameter. |
| **Get_Direction** | Die Funktion gibt die Richtung des Zyklus zurück (**TNCThreadCuttingDirection**).<br>Keine Eingabeparameter. |
| **Set_ThreadOrientation** | Die Methode legt die Art der Gewindeorientierung fest.<br>Eingabeparameter: **Value** (**TNCThreadOrientation**, siehe **[INCT_CLData.AddSinglePassThread](../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md)**) - Art der Gewindeorientierung.<br>Keine Ausgabeparameter. |
| **Get_ThreadOrientation** | Die Funktion gibt die Art der Gewindeorientierung zurück (**TNCThreadOrientation**).<br>Keine Eingabeparameter. |
| **Set_ThreadDepth** | Die Methode legt die Gewindetiefe fest.<br>Eingabeparameter: **Value** (Gleitkommazahl) - Gewindetiefe.<br>Keine Ausgabeparameter. |
| **Get_ThreadDepth** | Die Funktion gibt die Gewindetiefe zurück (Gleitkommazahl).<br>Keine Eingabeparameter. |
| **Set_ThreadStep** | Die Methode legt die Gewindesteigung fest.<br>Eingabeparameter: **Value** (Gleitkommazahl) - Gewindesteigung.<br>Keine Ausgabeparameter. |
| **Get_ThreadStep** | Die Funktion gibt die Gewindesteigung zurück (Gleitkommazahl).<br>Keine Eingabeparameter. |
| **Set_ThreadStartAngle** | Die Methode legt den Startwinkel des Gewindes fest.<br>Eingabeparameter: **Value** (Gleitkommazahl) - Startwinkel des Gewindes.<br>Keine Ausgabeparameter. |
| **Get_ThreadStartAngle** | Die Funktion gibt den Startwinkel des Gewindes zurück (Gleitkommazahl).<br>Keine Eingabeparameter. |
| **Set_ThreadStartCount** | Die Methode legt die Gangzahl des Gewindes fest.<br>Eingabeparameter: **Value** (Ganzzahl) - Gangzahl des Gewindes.<br>Keine Ausgabeparameter. |
| **Get_ThreadStartCount** | Die Funktion gibt die Gangzahl des Gewindes zurück (Ganzzahl).<br>Keine Eingabeparameter. |
| **Set_StartPoint** | Die Methode legt die Koordinaten des Anfangspunkts des Gewindes fest.<br>Eingabeparameter: **Value** (**TNC2DPoint**) - Koordinaten des Anfangspunkts des Gewindes.<br>Keine Ausgabeparameter. |
| **Get_StartPoint** | Die Funktion gibt die Koordinaten des Anfangspunkts des Gewindes zurück (**TNC2DPoint**).<br>Keine Eingabeparameter. |
| **Set_EndPoint** | Die Methode legt die Koordinaten des Endpunkts des Gewindes fest.<br>Eingabeparameter: **Value** (**TNC2DPoint**) - Koordinaten des Endpunkts des Gewindes.<br>Keine Ausgabeparameter. |
| **Get_EndPoint** | Die Funktion gibt die Koordinaten des Endpunkts des Gewindes zurück (**TNC2DPoint**).<br>Keine Eingabeparameter. |
| **Set_TaperDist** | Die Methode legt die Kegeligkeit zwischen Anfangs- und Endpunkt des Gewindes fest.<br>Eingabeparameter: **Value** (Gleitkommazahl) - Kegeligkeit zwischen Anfangs- und Endpunkt des Gewindes.<br>Keine Ausgabeparameter. |
| **Get_TaperDist** | Die Funktion gibt die Kegeligkeit zwischen Anfangs- und Endpunkt des Gewindes zurück (Gleitkommazahl).<br>Keine Eingabeparameter. |
| **Set_ChamferLength** | Die Methode legt die Länge der Fase für den Auslauf des Werkzeugs am Ende des Gewindes fest.<br>Eingabeparameter: **Value** (Gleitkommazahl) - Länge der Fase für den Auslauf des Werkzeugs am Ende des Gewindes.<br>Keine Ausgabeparameter. |
| **Get_ChamferLength** | Die Funktion gibt die Länge der Fase für den Auslauf des Werkzeugs am Ende des Gewindes zurück (Gleitkommazahl).<br>Keine Eingabeparameter. |
| **Set_ChamferAngle** | Die Methode legt den Winkel der Fase in Grad fest.<br>Eingabeparameter: **Value** (Gleitkommazahl) - Winkel der Fase in Grad.<br>Keine Ausgabeparameter. |
| **Get_ChamferAngle** | Die Funktion gibt den Winkel der Fase in Grad zurück (Gleitkommazahl).<br>Keine Eingabeparameter. |
| **Set_RetractionPath** | Die Methode legt die Lage der Rückzugsebene fest.<br>Eingabeparameter: **Value** (Gleitkommazahl) - Lage der Rückzugsebene.<br>Keine Ausgabeparameter. |
| **Get_RetractionPath** | Die Funktion gibt die festgelegte Lage der Rückzugsebene zurück (Gleitkommazahl).<br>Keine Eingabeparameter. |
| **Set_RunInPath** | Die Methode legt den Einlaufweg fest.<br>Eingabeparameter: **Value** (Gleitkommazahl) - Einlaufweg.<br>Keine Ausgabeparameter. |
| **Get_RunInPath** | Die Funktion gibt den Einlaufweg zurück (Gleitkommazahl).<br>Keine Eingabeparameter. |
| **Set_RunOutPath** | Die Methode legt den Auslaufweg fest.<br>Eingabeparameter: **Value** (Gleitkommazahl) - Auslaufweg.<br>Keine Ausgabeparameter. |
| **Get_RunOutPath** | Die Funktion gibt den Auslaufweg zurück (Gleitkommazahl).<br>Keine Eingabeparameter. |
| **Set_ThreadAngle** | Die Methode legt den Profilwinkel des Gewindes fest.<br>Eingabeparameter: **Value** (Gleitkommazahl) - Profilwinkel des Gewindes.<br>Keine Ausgabeparameter. |
| **Get_ThreadAngle** | Die Funktion gibt den Profilwinkel des Gewindes zurück (Gleitkommazahl).<br>Keine Eingabeparameter. |
| **Set_InclinationAngle** | Die Methode legt den Winkel einer Flanke des Gewindeprofils zur Senkrechten fest.<br>Eingabeparameter: **Value** (Gleitkommazahl) - Winkel.<br>Keine Ausgabeparameter. |
| **Get_InclinationAngle** | Die Funktion gibt den Winkel einer Flanke des Gewindeprofils zur Senkrechten zurück (Gleitkommazahl).<br>Keine Eingabeparameter. |
| **Set_SequenceType** | Die Methode legt die Zustellart bei den Schruppdurchgängen fest.<br>Eingabeparameter: **Value** (**TNCThreadSequenceType**) - Zustellart bei den Schruppdurchgängen.<br>**stRadial** - radial;<br>**stFlank** - entlang einer Flanke;<br>**stModifiedFlank** - unter einem Winkel;<br>**stAlternateFlank** - wechselnd entlang beider Flanken.<br>Keine Ausgabeparameter. |
| **Get_SequenceType** | Die Funktion gibt die Zustellart bei den Schruppdurchgängen zurück (**TNCThreadSequenceType**).<br>Keine Eingabeparameter. |
| **Set_PlungeAngle** | Die Methode legt den Zustellwinkel für die Zustellart **stModifiedFlank** fest.<br>Eingabeparameter: **Value** (Gleitkommazahl) - Zustellwinkel in Grad.<br>Keine Ausgabeparameter. |
| **Get_PlungeAngle** | Die Funktion gibt den Zustellwinkel für die Zustellart **stModifiedFlank** zurück (Gleitkommazahl).<br>Keine Eingabeparameter. |
| **Set_DepthIsEqual** | Die Methode legt fest, wie die Schnitttiefe bestimmt wird.<br>Eingabeparameter: **Value** (boolesch) - Art der Bestimmung der Schnitttiefe. True - konstante Schnitttiefe, False - konstanter Spanquerschnitt.<br>Keine Ausgabeparameter. |
| **Get_DepthIsEqual** | Die Funktion gibt zurück, wie die Schnitttiefe bestimmt wird (boolesch).<br>Keine Eingabeparameter. |
| **Set_IsPassCountDefined** | Die Methode legt das Verfahren zur Bestimmung der Schnitttiefe fest.<br>Eingabeparameter: **Value** (boolesch) - Verfahren zur Bestimmung der Schnitttiefe. True - nach der Anzahl der Durchgänge, False - nach der Anfangstiefe.<br>Keine Ausgabeparameter. |
| **Get_IsPassCountDefined** | Die Funktion gibt das Verfahren zur Bestimmung der Schnitttiefe zurück (boolesch).<br>Keine Eingabeparameter. |
| **Set_MinCutDepth** | Die Methode legt die kleinstmögliche Tiefe eines Schruppdurchgangs fest.<br>Eingabeparameter: **Value** (Gleitkommazahl) - kleinstmögliche Tiefe eines Schruppdurchgangs.<br>Keine Ausgabeparameter. |
| **Get_MinCutDepth** | Die Funktion gibt die kleinstmögliche Tiefe eines Schruppdurchgangs zurück (Gleitkommazahl).<br>Keine Eingabeparameter. |
| **Set_FirstCutDepth** | Die Methode legt die Tiefe des ersten Schruppdurchgangs fest.<br>Eingabeparameter: **Value** (Gleitkommazahl) - Tiefe des ersten Schruppdurchgangs.<br>Keine Ausgabeparameter. |
| **Get_FirstCutDepth** | Die Funktion gibt die Tiefe des ersten Schruppdurchgangs zurück (Gleitkommazahl).<br>Keine Eingabeparameter. |
| **Set_RoughPassCount** | Die Methode legt die Anzahl der Schruppdurchgänge fest.<br>Eingabeparameter: **Value** (Ganzzahl) - Anzahl der Schruppdurchgänge.<br>Keine Ausgabeparameter. |
| **Get_RoughPassCount** | Die Funktion gibt die Anzahl der Schruppdurchgänge zurück (Ganzzahl).<br>Keine Eingabeparameter. |
| **Set_FinishPassCount** | Die Methode legt die Anzahl der Schlichtdurchgänge fest.<br>Eingabeparameter: **Value** (Ganzzahl) - Anzahl der Schlichtdurchgänge.<br>Keine Ausgabeparameter. |
| **Get_FinishPassCount** | Die Funktion gibt die Anzahl der Schlichtdurchgänge zurück (Ganzzahl).<br>Keine Eingabeparameter. |
| **Set_FinishPassDepth** | Die Methode legt die Tiefe der Schlichtdurchgänge fest.<br>Eingabeparameter: **Value** (Gleitkommazahl) - Tiefe der Schlichtdurchgänge.<br>Keine Ausgabeparameter. |
| **Get_FinishPassDepth** | Die Funktion gibt die Tiefe der Schlichtdurchgänge zurück (Gleitkommazahl).<br>Keine Eingabeparameter. |
| **Set_Feedrate** | Die Methode legt den Arbeitsvorschub fest.<br>Eingabeparameter: **Value** (Gleitkommazahl) - Arbeitsvorschub.<br>Keine Ausgabeparameter. |
| **Get_Feedrate** | Die Funktion gibt den Arbeitsvorschub zurück.<br>Keine Eingabeparameter. |
| **Set_MPM** | Die Methode legt die Maßeinheit des Arbeitsvorschubs fest.<br>Eingabeparameter: **Value** (boolesch) - Maßeinheit des Arbeitsvorschubs. True - mm/min, False - mm/U.<br>Keine Ausgabeparameter. |
| **Get_MPM** | Die Funktion gibt die Maßeinheit des Arbeitsvorschubs zurück.<br>Keine Eingabeparameter. |
| **Set_Events** | Die Methode weist Ereignisse zur Steuerung des Zyklus zu. Mit Ereignissen lassen sich auf jedem gebildeten Abschnitt des Werkzeugwegs die für einen bestimmten Zyklus nötigen Besonderheiten ergänzen (Verweilzeit, orientierter Spindelhalt usw.), Art oder Wert des Vorschubs ändern oder vom Generator vorbereitete Werkzeugbewegungen überspringen.<br>Eingabeparameter: **Value** (Schnittstelle) - Objekt, das die Schnittstellen **INCT_LatheCycleEvents, INCT_LatheThreadCuttingCycleEvents** implementiert. Ausführliche Beschreibung unten.<br>Keine Ausgabeparameter. |
| **Get_Events** | Die Funktion gibt das mit dem Generator verbundene Objekt zurück, das die Ereignisse implementiert (**INCT_LatheCycleEvents, INCT_LatheThreadCuttingCycleEvents**).<br>Keine Eingabeparameter. |
| **MakeWorkpath** | Die Methode bildet den Werkzeugweg des Zyklus nach den angegebenen Parametern. |

**INCT_LatheThreadCuttingCycleFormer2** - Schnittstelle des CAM-Systems, die die Bildung der Bewegungen eines Drehzyklus zum Gewindeschneiden vereinfacht.

**Beschreibung der Schnittstellenmethoden:**

| Methode | Beschreibung der Methode |
| --- | --- |
| **Set_Approach** | Die Methode legt die Art des Anfahrens fest.<br>Eingabeparameter: **Value** (**TNCThreadApproach**) - Art des Anfahrens.<br>**taOutside** - von außen (Standard);<br>**taIndise** - von innen.<br>Keine Ausgabeparameter. |
| **Get_Approach** | Die Funktion gibt die Art des Anfahrens zurück (**TNCThreadApproach**).<br>Keine Eingabeparameter. |
| **Get_SignLongitudinal** | Die Funktion gibt das Vorzeichen der Bewegung entlang der Längsachse zurück (Ganzzahl). |
| **Get_SignTransverse** | Die Funktion gibt das Vorzeichen der Bewegung entlang der Querachse zurück (Ganzzahl). |

**INCT_LatheCycleEvents** - Schnittstelle, die im Interpreter implementiert wird und mit der sich das Verhalten eines Drehzyklus steuern lässt. Ausführlich beschrieben im Artikel [Drehzyklus Einstechen](../turning-cycle-grooving/turning-cycle-grooving.md).

**INCT_LatheThreadCuttingCycleEvents** - Schnittstelle, die im Interpreter implementiert wird und mit der sich das Gewindeschneiden steuern lässt. Die Schnittstelle beschreibt die Ereignismethode **OnThread**, die beim Gewindeschneiden innerhalb des Generators ausgeführt wird, sowie Ereignismethoden zur Berechnung der Durchgänge.

**Beschreibung der Schnittstellenmethoden:**

<table>
<thead>
<tr><th>Methode</th><th>Beschreibung der Methode</th><th>Verwendung</th></tr>
</thead>
<tbody>
<tr><td><strong><strong>OnThread</strong><br></strong></td><td><p>Die Methode wird vor jedem Gewindeschneiden bei der Bildung des Werkzeugwegs des Zyklus ausgeführt. Mit ihrer Implementierung lassen sich die Gewindeparameter für die gewählte Iteration ändern.</p><p>Eingabeparameter: <strong>Orient</strong> (<strong>TNCThreadOrientation</strong>) - Gewindeorientierung; <strong>LeadType</strong> (<strong>TNCThreadLeadType</strong>) - Art der Angabe der Gewindesteigung; <strong>Step</strong> (Gleitkommazahl) - Gewindesteigung; <strong>StartAngle</strong> (Gleitkommazahl) - Anfangswinkel der Spindel in Grad (für mehrgängige Gewinde). Siehe <strong><a href="../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md">INCT_CLData.AddSinglePassThread</a>.</strong></p><p>Ein- und Ausgabeparameter: <strong>Handled</strong> (boolesch) - Kennzeichen, ob das Gewindeschneiden in der Implementierung ausgeführt wurde (True - ausgeführt, False - nicht ausgeführt).</p><p>Hat <strong>Handled</strong> nach dem Aufruf von <strong>OnThread</strong> den Wert True, wurde das Gewindeschneiden in der Implementierung von <strong>OnThread</strong> ausgeführt, und der Generator fügt dem Werkzeugweg keinen Befehl zum Gewindeschneiden hinzu.</p><p>Hat <strong>Handled</strong> nach dem Aufruf von <strong>OnThread</strong> den Wert False, geht der Generator davon aus, dass das Gewindeschneiden in der Implementierung von <strong>OnThread</strong> nicht ausgeführt wurde, und fügt dem Werkzeugweg einen Befehl zum Gewindeschneiden hinzu.</p></td><td rowspan="5">Zum Ersetzen der Parameter des Gewindeschneidens oder zum Festlegen eines im Generator nicht vorhandenen Algorithmus für die Änderung des Gewindes in den einzelnen Durchgängen.</td></tr>
<tr><td><strong>OnCalcBaseDepth</strong></td><td><p>Die Methode wird bei <strong>IsPassCountDefined = True</strong> nach der Berechnung der Basistiefe (der ersten Tiefe) ausgeführt. Mit ihrer Implementierung lässt sich die Basistiefe ändern.</p><p>Ein- und Ausgabeparameter: <strong>BaseDepth</strong> (Gleitkommazahl) - Basistiefe.</p></td></tr>
<tr><td><strong>OnCalcCount</strong></td><td><p>Die Methode wird bei <strong>IsPassCountDefined = False</strong> nach der Berechnung der Anzahl der Durchgänge ausgeführt. Mit ihrer Implementierung lässt sich die Anzahl der Durchgänge ändern.</p><p>Ein- und Ausgabeparameter: <strong>Count</strong> (Ganzzahl) - Anzahl der Durchgänge.</p></td></tr>
<tr><td><strong>OnCalcNextDepth</strong></td><td><p>Die Methode wird bei der Berechnung der nächsten Tiefe ausgeführt (wenn die Anzahl der Durchgänge größer oder gleich eins ist). Mit ihrer Implementierung lässt sich die Tiefe für die Iteration ändern.</p><p>Eingabeparameter: <strong>Iteration</strong> (Ganzzahl) - Nummer der Iteration (des Durchgangs);</p><p>Ein- und Ausgabeparameter: <strong>Depth</strong> (Gleitkommazahl) - Tiefe in der Iteration.</p></td></tr>
<tr><td><strong>OnCalcPoint</strong></td><td><p>Die Methode wird bei der Berechnung der Werkzeugposition für die nächste Bewegung ausgeführt. Mit ihrer Implementierung lassen sich die Koordinaten für die Iteration ändern.</p><p>Eingabeparameter: <strong>Iteration</strong> (Ganzzahl) - Nummer der Iteration (des Durchgangs);</p><p>Ein- und Ausgabeparameter: <strong>Point</strong> (<strong>TNC2DPoint</strong>) - Koordinaten der Werkzeugposition in der Iteration.</p></td></tr>
</tbody>
</table>
