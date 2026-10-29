# Bohrzyklus mit Spanbruch

**INCT_PeckDrillingCycleFormer** - Schnittstelle des CAM-Systems, die die Bildung der Bewegungen in Zyklen mit Spanbruch vereinfacht. Wird die Funktion **[INCT_CLData.CreateDrillingCycleFormer](../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md), [INCT_GeomCLData.CreateDrillingCycleFormer](../../basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md)** mit dem Parameter **dctPeck** aufgerufen, gibt sie ein Objekt zurück, das zwei Schnittstellen implementiert: **INCT_DrillingCycleFormer**, **INCT_PeckDrillingCycleFormer**.

Über die Schnittstelle **INCT_DrillingCycleFormer** werden die Grundparameter des Bohrzyklus mit Spanbruch festgelegt. Ihre Verwendung ist im Artikel [Bohrzyklus](../drilling-cycle/drilling-cycle.md) beschrieben.

Die Schnittstelle **INCT_PeckDrillingCycleFormer** ergänzt den Generator um die Möglichkeit, die Parameter für die Bildung des Werkzeugwegs mit Spanbruch zu steuern.

<img src="../../../../../images/129931519/PeckDrillingCycle.png" alt="PeckDrillingCycle" width="700">

**Zweck:**

Die Bewegungen in den verschiedenen Bohrzyklen mit Spanbruch folgen bei den unterschiedlichen Steuerungen im Allgemeinen demselben Ablauf:

1. Positionieren des Werkzeugs über dem Mittelpunkt der Bohrung bzw. der nächsten Bohrung im Eilgang.
2. Fahren des Werkzeugs auf die Ebene der Eilgangbewegung im Eilgang.
3. Fahren des Werkzeugs auf die Ebene des Bohrungsgrunds im Arbeitsvorschub.
4. Rückkehr auf die Ebene der Eilgangbewegung im Eilgang.
5. Rückkehr auf die Rückzugsebene im Eilgang.
6. Ist die Anzahl der Wiederholungen noch nicht erreicht, Rückkehr zu Schritt 1.

In solchen Zyklen wird die Bohrung (der Schritt „Fahren auf die Ebene des Bohrungsgrunds“) nicht in einem Durchgang, sondern in mehreren Iterationen gebohrt. Beispiele solcher Zyklen: Fanuc: G73, G83; Sinumerik: CYCLE83; Heidenhain: CYCL DEF 200, 203, 205 u. a.

**Verwendung des Generators:**

Wir empfehlen, für jeden neuen Zyklus in einem Satz des NC-Programms einen neuen Generator des Bohrzyklus zu erstellen, außer wenn ein Zyklus in einem neuen Satz wiederholt wird (entspricht CYCL CALL bei Heidenhain). Die Schnittstelle des alten Generators muss daher beim Erstellen eines neuen Generators oder beim Beenden des Interpreters freigegeben werden.

Mit der Schnittstelle **INCT_DrillingCycleFormer** lässt sich der Werkzeugweg aus vorgegebenen Parametern bilden: Ausgangsposition, Ebene der Eilgangbewegung, Bohrungsgrund, Anzahl der Wiederholungen usw. Außerdem können auf jedem Abschnitt die für einen bestimmten Zyklus nötigen Besonderheiten ergänzt (Verweilzeit, orientierter Spindelhalt, Gewindeschneiden usw.), Art oder Wert des Vorschubs geändert oder vom Generator vorbereitete Werkzeugbewegungen übersprungen werden.

Mit der Schnittstelle **INCT_PeckDrillingCycleFormer** lassen sich verschiedene Parameter festlegen, die die Anzahl der Iterationen, die Schnitttiefe je Iteration, die Art des Abhebens des Werkzeugs usw. steuern.

Um die Befehle für den Werkzeugweg entlang des Zyklus zu bilden, sind folgende Schritte nötig:

1. Die Schnittstellen des Generators abfragen (**[INCT_CLData.CreateDrillingCycleFormer](../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md), [INCT_GeomCLData.CreateDrillingCycleFormer](../../basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md)** mit dem Parameter **dctPeck**).
2. Die Indizes der Achsen X, Y, Z festlegen, entlang derer die Bewegungen ausgeführt werden (**Set_AxisIndexes**).
3. Die aktuelle Ebene festlegen (**Set_Plane**).
4. Den Mittelpunkt der Bohrung festlegen (**Set_HoleCenter**).
5. Den Modus des Bohrungsmittelpunkts festlegen (**Set_HoleCenterMode**).
6. Die Ebene der Eilgangbewegung festlegen (**Set_RapidLevel**).
7. Die Ebene des Bohrungsgrunds festlegen (**Set_BottomLevel**).
8. Die Rückzugsebene festlegen (**Set_TopLevel**).
9. Den Vorschub (**Set_Feedrate**) und die Maßeinheit des Vorschubs (**Set_MPM**) festlegen.
10. Die Anzahl der Wiederholungen des Zyklus festlegen (**Set_Count**).
11. Einen Ereignishandler des Zyklus zuweisen (**Set_Events**), wenn der Werkzeugweg des Zyklus geändert werden soll.
12. Die Parameter der Iterationen für den Spanbruch festlegen (**Set_StartLevel**, **Set_DepthOfCut**, **Set_DegressionType**, **Set_Degression**, **Set_FullReturn** usw., Beschreibung siehe unten).
13. Die Befehle für den Werkzeugweg entlang des Zyklus bilden (**MakeWorkpath**).

Die Methode **INCT_DrillingCycleFormer.Set_Events** erwartet beim Zyklus mit Spanbruch als Eingabeparameter ein Objekt, das zwei Schnittstellen implementiert: **INCT_DrillingCycleEvents** und **INCT_PeckDrillingCycleEvents**. An die Ereignisse der Schnittstelle **INCT_DrillingCycleEvents** (**BeforeMove**, **OnMove**, **AfterMove**) werden als Bewegungsart neben den im Artikel [Bohrzyklus](../drilling-cycle/drilling-cycle.md) beschriebenen Werten auch folgende übergeben:

**mtPeckMoveToNextDepthLevel** - Fahren auf die nächste Schnitttiefe (nächste Iteration);\
**mtPeckReturnToRapidLevel** - Rückkehr auf die Ebene der Eilgangbewegung in der aktuellen Iteration (Entspanen);\
**mtPeckMoveToClearanceLevel** - Fahren auf die aktuelle Schnittebene abzüglich des Vorhaltabstands nach der Rückkehr von der Ebene der Eilgangbewegung;\
**mtPeckMoveToRetractionLevel** - Abheben und Rückkehr auf die aktuelle Schnittebene (Spanbruch).

**Beschreibung der Methoden der Schnittstelle INCT_PeckDrillingCycleFormer:**

| Methode | Beschreibung der Methode |
| --- | --- |
| **Set_DepthOfCut** | Die Methode legt die Schnitttiefe je Iteration fest. Die Schnitttiefe ist der Weg, den das Werkzeug beim Bohren in jeder Iteration zurücklegt.<br>Eingabeparameter: **Value** (Gleitkommazahl) - Schnitttiefe.<br>Keine Ausgabeparameter. |
| **Get_DepthOfCut** | Die Funktion gibt die Schnitttiefe zurück (Gleitkommazahl).<br>Keine Eingabeparameter. |
| **Set_StartLevelType** | Die Methode legt die Art des Werts „Startebene“ fest.<br>Eingabeparameter: **Value** (**TNCStartLevelType**) - Art des Werts:<br>**slFromLevel** - ab dem in **Set_StartLevel** angegebenen Wert wird die erste Schnitttiefe gemessen.<br>**slFirstLevel** - der in **Set_StartLevel** angegebene Wert ist die erste Schnitttiefe.<br>Keine Ausgabeparameter. |
| **Get_StartLevelType** | Die Funktion gibt die Art des Werts „Startebene“ zurück (**TNCStartLevelType**).<br>Keine Eingabeparameter. |
| **Set_StartLevel** | Die Methode legt je nach dem in **Set_StartLevelType** angegebenen Wert die Ebene fest, ab der die erste Schnitttiefe gemessen wird, oder die erste Schnitttiefe selbst.<br>Eingabeparameter: **Value** (Gleitkommazahl) - angegebener Wert.<br>Keine Ausgabeparameter. |
| **Get_StartLevel** | Die Funktion gibt je nach dem in **Set_StartLevelType** angegebenen Wert die Ebene zurück, ab der die erste Schnitttiefe gemessen wird, oder die erste Schnitttiefe selbst (Gleitkommazahl).<br>Keine Eingabeparameter. |
| **Set_Degression** | Die Methode legt den Wert der Degression fest, d. h. die Änderung der Schnitttiefe in jeder Iteration.<br>Eingabeparameter: **Value** (Gleitkommazahl) - Wert der Degression.<br>Wie der Wert verwendet wird, hängt von der in **Set_DegressionType** angegebenen Art der Degression ab.<br>Keine Ausgabeparameter. |
| **Get_Degression** | Die Funktion gibt den aktuellen Wert der Degression zurück (Gleitkommazahl).<br>Keine Eingabeparameter. |
| **Set_DegressionType** | Die Methode legt die Art der Degression fest.<br>Eingabeparameter: **Value** (**TNCDegressionType**) - Art der Degression.<br>**dtNone** - keine Degression, die Schnitttiefe ändert sich nicht;<br>**dtValue** - die Schnitttiefe wird in jeder Iteration um einen festen Wert verringert (der Wert wird in **Set_Degression** angegeben);<br>**dtCoef** - die Schnitttiefe wird in jeder Iteration mit einem Faktor multipliziert (der Faktor wird in **Set_Degression** angegeben).<br>Keine Ausgabeparameter. |
| **Get_DegressionType** | Die Funktion gibt die aktuelle Art der Degression zurück (**TNCDegressionType**).<br>Keine Eingabeparameter. |
| **Set_MinDepthOfCut** | Die Methode legt die minimale Schnitttiefe fest. Der Wert wird in der Regel bei Zyklen mit Degression verwendet.<br>Eingabeparameter: **Value** (Gleitkommazahl) - minimale Schnitttiefe.<br>Keine Ausgabeparameter. |
| **Get_MinDepthOfCut** | Die Funktion gibt die aktuelle minimale Schnitttiefe zurück (Gleitkommazahl).<br>Keine Eingabeparameter. |
| **Set_Retraction** | Die Methode legt den aktuellen Abhebebetrag fest. Der Abhebebetrag ist der Weg, um den das Werkzeug zum Spanbrechen abhebt, nachdem es die aktuelle Schnitttiefe der Iteration erreicht hat, sofern in dieser Iteration nicht auf die Ebene der Eilgangbewegung zurückgekehrt wird (d. h. das Kennzeichen in **Set_FullReturn** ist False).<br>Eingabeparameter: **Value** (Gleitkommazahl) - Abhebebetrag.<br>Wie der Wert verwendet wird, hängt von der in **Set_RetractionType** angegebenen Art des Abhebens ab.<br>Keine Ausgabeparameter. |
| **Get_Retraction** | Die Funktion gibt den aktuellen Abhebebetrag zurück (Gleitkommazahl).<br>Keine Eingabeparameter. |
| **Set_RetractionType** | Die Methode legt die Art des Abhebens fest.<br>Eingabeparameter: **Value** (**TNCRetractionType**) - Art des Abhebens.<br>**rtNone** - es wird nicht abgehoben;<br>**rtValue** - Abheben um einen Betrag (wird in **Set_Retraction** angegeben).<br>Keine Ausgabeparameter. |
| **Get_RetractionType** | Die Funktion gibt die aktuelle Art des Abhebens zurück (**TNCRetractionType**).<br>Keine Eingabeparameter. |
| **Set_RetractionCount** | Die Methode legt die Anzahl der Abhebevorgänge zum Spanbrechen fest.<br>Eingabeparameter: **Value** (Ganzzahl) - Anzahl der Abhebevorgänge zum Spanbrechen.<br>Keine Ausgabeparameter. |
| **Get_RetractionCount** | Die Funktion gibt die Anzahl der Abhebevorgänge zum Spanbrechen zurück (Ganzzahl).<br>Keine Eingabeparameter. |
| **Set_ClearanceType** | Die Methode legt die Art des Vorhaltabstands fest. Der Vorhaltabstand ist der Abstand, um den das Werkzeug nach der Rückkehr von der Ebene der Eilgangbewegung vor der Schnittebene der aktuellen Iteration anhält (d. h. das Kennzeichen in **Set_FullReturn** ist True).<br>Eingabeparameter: **Value** (**TNCClearanceType**) - Art des Vorhaltabstands.<br>**ctNone** - ohne Vorhaltabstand;<br>**ctValue** - Vorhaltabstand als Wert (wird in **Set_Clearance** angegeben).<br>Keine Ausgabeparameter. |
| **Get_ClearanceType** | Die Funktion gibt die aktuelle Art des Vorhaltabstands zurück (**TNCClearanceType**).<br>Keine Eingabeparameter. |
| **Set_Clearance** | Die Methode legt den Vorhaltabstand fest.<br>Eingabeparameter: **Value** (Gleitkommazahl) - Vorhaltabstand.<br>Wie der Wert verwendet wird, hängt von der in **Set_ClearanceType** angegebenen Art des Vorhaltabstands ab.<br>Keine Ausgabeparameter. |
| **Get_Clearance** | Die Funktion gibt den aktuellen Vorhaltabstand zurück (Gleitkommazahl).<br>Keine Eingabeparameter. |
| **Set_FullReturn** | Die Methode legt das Kennzeichen „Rückkehr auf die Ebene der Eilgangbewegung“ fest. Ist das Kennzeichen gesetzt, kehrt das Werkzeug nach Erreichen der Schnitttiefe der aktuellen Iteration auf die Ebene der Eilgangbewegung zurück und fährt danach auf die Schnittebene der Iteration abzüglich des Vorhaltabstands.<br>Eingabeparameter: **Value** (boolesch) - Kennzeichen der Rückkehr.<br>True - mit Rückkehr auf die Ebene der Eilgangbewegung;<br>False - ohne Rückkehr.<br>Keine Ausgabeparameter. |
| **Get_FullReturn** | Die Funktion gibt das Kennzeichen „Rückkehr auf die Ebene der Eilgangbewegung“ zurück (boolesch).<br>Keine Eingabeparameter. |
| **Set_FullReturnStep** | Die Methode legt fest, in welchem Schritt der Iterationen auf die Ebene der Eilgangbewegung zurückgekehrt wird.<br>Beispiel: Als Schritt ist 3 angegeben. Dann wird in jeder dritten Iteration auf die Ebene der Eilgangbewegung zurückgekehrt (Iterationen 3, 6, 9 usw.), in den übrigen Iterationen nicht (Iterationen 1, 2, 4, 5, 7, 8 usw.).<br>Eingabeparameter: **Value** (Ganzzahl) - Schritt der Iterationen.<br>Wirkt nur, wenn in **Set_FullReturn** True (mit Rückkehr) angegeben ist.<br>Keine Ausgabeparameter. |
| **Get_FullReturnStep** | Die Funktion gibt zurück, in welchem Schritt der Iterationen auf die Ebene der Eilgangbewegung zurückgekehrt wird (Ganzzahl).<br>Keine Eingabeparameter. |
| **Set_SameLastSteps** | Die Methode legt die Anzahl der letzten gleichen Schnittschritte fest. Ist der Wert ungleich 0 und 1, wird die angegebene Anzahl der letzten Iterationen mit derselben Schnitttiefe ausgeführt.<br>Eingabeparameter: **Value** (Ganzzahl) - Anzahl der letzten gleichen Schnittschritte.<br>Keine Ausgabeparameter. |
| **Get_SameLastSteps** | Die Funktion gibt die aktuelle Anzahl der letzten gleichen Schnittschritte zurück (Ganzzahl).<br>Keine Eingabeparameter. |

**INCT_PeckDrillingCycleEvents** - Schnittstelle, die im Interpreter implementiert wird und mit der sich die im Bohrzyklus mit Spanbruch berechneten Werte abfragen und steuern lassen. Die Schnittstelle besteht aus einer Reihe von Ereignismethoden, die bei der Berechnung bestimmter Werte innerhalb des Generators ausgeführt werden. Mit ihnen lassen sich während der Bildung des Werkzeugwegs die Schnittebenen der Iterationen, das Kennzeichen „Rückkehr auf die Ebene der Eilgangbewegung“ in einer Iteration sowie Vorhaltabstand und Abhebebetrag abfragen und ändern.

Sind dem Generator Ereignisse zugewiesen, wird für jeden berechneten Wert die entsprechende Methode aufgerufen:

1. Die Methode **INCT_PeckDrillingCycleEvents.OnCalcNextDepth** wird ausgeführt, wenn die nächste berechnete Schnittebene in die interne Liste des Generators aufgenommen wird. Die Anzahl der Schnittebenen (Größe der Liste) ist die Anzahl der Iterationen, in denen das Werkzeug den Bohrungsgrund erreicht. Der Methode wird die berechnete Schnittebene übergeben.
2. Die Methode **INCT_PeckDrillingCycleEvents.OnGetNextFullReturn** wird ausgeführt, nachdem das Kennzeichen „Rückkehr auf die Ebene der Eilgangbewegung“ aus den Parametern des Zyklus berechnet wurde. Der Methode werden die Nummer der Iteration und das berechnete Kennzeichen übergeben.
3. Die Methode **INCT_PeckDrillingCycleEvents.OnGetNextClearance** wird ausgeführt, nachdem der Vorhaltabstand berechnet wurde. Der Methode werden die Nummer der Iteration und der berechnete Vorhaltabstand übergeben.
4. Die Methode **INCT_PeckDrillingCycleEvents.OnGetNextRetraction** wird ausgeführt, nachdem der Abhebebetrag berechnet wurde. Der Methode werden die Nummer der Iteration und der berechnete Abhebebetrag übergeben.

**Beschreibung der Schnittstellenmethoden:**

<table>
<thead>
<tr><th>Methode</th><th>Beschreibung der Methode</th><th>Verwendung</th></tr>
</thead>
<tbody>
<tr><td><strong>OnCalcNextDepth</strong></td><td><p>Die Methode wird jedes Mal ausgeführt, wenn die nächste berechnete Schnittebene in die interne Liste des Generators aufgenommen wird.</p><p>Die Größe der gebildeten Liste (Anzahl der Elemente) ist die Anzahl der Iterationen, in denen das Werkzeug den Bohrungsgrund erreicht.</p><p>Ein- und Ausgabeparameter: <strong>Depth</strong> (Gleitkommazahl) - Schnittebene der Iteration (absoluter Wert).</p></td><td><ol><li>Zum Ermitteln der Gesamtzahl der Iterationen, um Vorhaltabstand, Abhebebetrag oder Rückkehr auf die Ebene der Eilgangbewegung nach eigenen, im Zyklus nicht vorgesehenen Algorithmen neu zu berechnen.</li><li>Zum Ändern der Schnittebenen nach eigenen, im Zyklus nicht vorgesehenen Algorithmen.</li></ol></td></tr>
<tr><td><strong>OnGetNextFullReturn</strong></td><td><p>Die Methode wird ausgeführt, nachdem das Kennzeichen „Rückkehr auf die Ebene der Eilgangbewegung“ für die aktuelle Iteration aus den Parametern des Zyklus berechnet wurde.</p><p>Eingabeparameter: <strong>Iteration</strong> (Ganzzahl) - Nummer der Iteration.</p><p>Ein- und Ausgabeparameter: <strong>FullReturn</strong> (boolesch) - Kennzeichen „Rückkehr auf die Ebene der Eilgangbewegung“ in der angegebenen Iteration.</p></td><td>Zum Ändern des Kennzeichens „Rückkehr auf die Ebene der Eilgangbewegung“ für die aktuelle Iteration nach eigenen, im Zyklus nicht vorgesehenen Algorithmen.</td></tr>
<tr><td><strong>OnGetNextClearance</strong></td><td><p>Die Methode wird ausgeführt, nachdem der Vorhaltabstand für die aktuelle Iteration aus den Parametern des Zyklus berechnet wurde. Sie wird nur aufgerufen, wenn das Kennzeichen „Rückkehr auf die Ebene der Eilgangbewegung“ für die Iteration gesetzt ist (<strong>FullReturn</strong> = True).</p><p>Eingabeparameter: <strong>Iteration</strong> (Ganzzahl) - Nummer der Iteration.</p><p>Ein- und Ausgabeparameter: <strong>Clearance</strong> (Gleitkommazahl) - Vorhaltabstand in der angegebenen Iteration.</p></td><td>Zum Ändern des Vorhaltabstands für die aktuelle Iteration nach eigenen, im Zyklus nicht vorgesehenen Algorithmen.</td></tr>
<tr><td><strong>OnGetNextRetraction</strong></td><td><p>Die Methode wird ausgeführt, nachdem der Abhebebetrag für die aktuelle Iteration aus den Parametern des Zyklus berechnet wurde. Sie wird nur aufgerufen, wenn das Kennzeichen „Rückkehr auf die Ebene der Eilgangbewegung“ für die Iteration nicht gesetzt ist (<strong>FullReturn</strong> = False).</p><p>Eingabeparameter: <strong>Iteration</strong> (Ganzzahl) - Nummer der Iteration.</p><p>Ein- und Ausgabeparameter: <strong>Retraction</strong> (Gleitkommazahl) - Abhebebetrag in der angegebenen Iteration.</p></td><td>Zum Ändern des Abhebebetrags für die aktuelle Iteration nach eigenen, im Zyklus nicht vorgesehenen Algorithmen.</td></tr>
</tbody>
</table>
