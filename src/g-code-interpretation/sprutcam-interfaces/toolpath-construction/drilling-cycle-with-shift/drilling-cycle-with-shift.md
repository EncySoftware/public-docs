# Bohrzyklus mit Verschiebung

**INCT_DrillingCycleWithShiftFormer** - Schnittstelle des CAM-Systems, die die Bildung der Bewegungen in Bohrzyklen mit Verschiebung vereinfacht. Wird die Funktion **[INCT_CLData.CreateDrillingCycleFormer](../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md), [INCT_GeomCLData.CreateDrillingCycleFormer](../../basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md)** mit dem Parameter **dctWithShift** aufgerufen, gibt sie ein Objekt zurück, das zwei Schnittstellen implementiert: **INCT_DrillingCycleFormer**, **INCT_DrillingCycleWithShiftFormer**.

Über die Schnittstelle **INCT_DrillingCycleFormer** werden die Grundparameter des Bohrzyklus mit Verschiebung festgelegt. Ihre Verwendung ist im Artikel [Bohrzyklus](../drilling-cycle/drilling-cycle.md) beschrieben.

Die Schnittstelle **INCT_DrillingCycleWithShiftFormer** ergänzt den Generator um die Möglichkeit, die Parameter für die Bildung des Werkzeugwegs mit Verschiebung zu steuern.

<img src="../../../../../images/129931497/DrillingCycleFormerWithShift.png" alt="DrillingCycleFormerWithShift" width="400">

**Zweck:**

Die Bewegungen in den verschiedenen Bohrzyklen mit Verschiebung folgen bei den unterschiedlichen Steuerungen im Allgemeinen demselben Ablauf:

1. Positionieren des Werkzeugs über dem Mittelpunkt der Bohrung bzw. der nächsten Bohrung im Eilgang.
2. Fahren des Werkzeugs auf die Ebene der Eilgangbewegung im Eilgang.
3. Fahren des Werkzeugs auf die Ebene des Bohrungsgrunds im Arbeitsvorschub.
4. Rückkehr auf die Ebene der Eilgangbewegung im Eilgang.
5. Rückkehr auf die Rückzugsebene im Eilgang.
6. Ist die Anzahl der Wiederholungen noch nicht erreicht, Rückkehr zu Schritt 1.

Auf einem oder mehreren Abschnitten solcher Zyklen ist der Werkzeugweg entlang einer oder mehrerer Achsen verschoben. Beispiele solcher Zyklen: Fanuc: G76, G87; Sinumerik: CYCLE86; Heidenhain: CYCL DEF 202 u. a.

**Verwendung des Generators:**

Wir empfehlen, für jeden neuen Zyklus in einem Satz des NC-Programms einen neuen Generator des Bohrzyklus zu erstellen, außer wenn ein Zyklus in einem neuen Satz wiederholt wird (entspricht CYCL CALL bei Heidenhain). Die Schnittstelle des alten Generators muss daher beim Erstellen eines neuen Generators oder beim Beenden des Interpreters freigegeben werden.

Mit der Schnittstelle **INCT_DrillingCycleFormer** lässt sich der Werkzeugweg aus vorgegebenen Parametern bilden: Ausgangsposition, Ebene der Eilgangbewegung, Bohrungsgrund, Anzahl der Wiederholungen usw. Außerdem können auf jedem Abschnitt die für einen bestimmten Zyklus nötigen Besonderheiten ergänzt (Verweilzeit, orientierter Spindelhalt, Gewindeschneiden usw.), Art oder Wert des Vorschubs geändert oder vom Generator vorbereitete Werkzeugbewegungen übersprungen werden.

Mit der Schnittstelle **INCT_DrillingCycleWithShiftFormer** lässt sich für jeden Schritt des Zyklus außer dem ersten eine Verschiebung der Koordinaten der Zielpunkte festlegen. Auf jedem dieser Schritte fährt das Werkzeug wie folgt vom aktuellen Punkt zum neuen Punkt:

- vom aktuellen Punkt zum verschobenen aktuellen Punkt;
- vom verschobenen aktuellen Punkt zum verschobenen neuen Punkt;
- vom verschobenen neuen Punkt zum neuen Punkt.

Um die Befehle für den Werkzeugweg entlang des Zyklus zu bilden, sind folgende Schritte nötig:

1. Die Schnittstellen des Generators abfragen (**[INCT_CLData.CreateDrillingCycleFormer](../../basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md), [INCT_GeomCLData.CreateDrillingCycleFormer](../../basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md)** mit dem Parameter **dctWithShift**).
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
12. Die Art der Verschiebung der Zielpunkte festlegen (**SetShiftByOneAxis** oder **SetShiftBySomeAxis**).
13. Die Abschnitte des Werkzeugwegs festlegen, auf denen die Verschiebung wirkt (**Set_ShiftPathSet**).
14. Die Befehle für den Werkzeugweg entlang des Zyklus bilden (**MakeWorkpath**).

**Beschreibung der Methoden der Schnittstelle INCT_DrillingCycleWithShiftFormer:**

| Methode | Beschreibung der Methode |
| --- | --- |
| **SetShiftByOneAxis** | Die Methode schaltet die Berechnung der Verschiebung auf „**Berechnung entlang einer Achse**“ um und legt den Betrag der Verschiebung fest. Die Verschiebung erfolgt dann auf allen Schritten entlang einer Achse, abhängig von der mit **Set_Plane** festgelegten Ebene: bei ptXY entlang der X-Achse, bei ptYZ entlang der Y-Achse, bei ptZX entlang der Z-Achse.<br>Eingabeparameter: **Value** (Gleitkommazahl) - Betrag der Verschiebung.<br>Keine Ausgabeparameter. |
| **SetShiftBySomeAxis** | Die Methode schaltet die Berechnung der Verschiebung auf „**Berechnung entlang ausgewählter Achsen**“ um und legt den Betrag der Verschiebung für jede Achse fest. Der Punkt auf der Ebene des Bohrungsgrunds wird dann entlang der ausgewählten Achsen um die angegebenen Beträge verschoben. Die Punkte der übrigen Ebenen werden ebenfalls entlang der ausgewählten Achsen um die angegebenen Beträge verschoben, entlang der Bohrachse jedoch nicht.<br>Eingabeparameter: **Axis** (**TNCShiftAxis.X, Y, Z** - boolesch) - Achsen, entlang derer verschoben wird; **Values** (**TNCShiftValues.X, Y, Z** - Gleitkommazahl) - Beträge der Verschiebung entlang der Achsen.<br>Keine Ausgabeparameter. |
| **Set_ShiftPathSet** | Die Methode legt die Schritte des Werkzeugwegs fest, auf denen der Generator die Verschiebung ausführt.<br>Eingabeparameter: **Value** (**TNCShiftPathSet**) - Menge der Schritte des Werkzeugwegs, auf denen der Generator die Verschiebung ausführt. Es können mehrere Schritte gewählt werden.<br>**spMoveToRapidLevel** - beim Fahren auf die Ebene der Eilgangbewegung;<br>**spMoveToBottomLevel** - beim Fahren auf die Ebene des Bohrungsgrunds;<br>**spReturnToRapidLevel** - bei der Rückkehr auf die Ebene der Eilgangbewegung;<br>**spReturnToTopLevel** - bei der Rückkehr auf die Rückzugsebene.<br>In der Typbibliothek heißt der Typ **SetOfTNCShiftPath** und ist ein Byte; **TNCShiftPathSet** ist sein Name in Delphi (Menge von **TNCShiftPath**). Jeder gewählte Schritt setzt im Byte ein Bit mit der Nummer seines Werts in **TNCShiftPath**: **spMoveToRapidLevel** = 1, **spMoveToBottomLevel** = 2, **spReturnToRapidLevel** = 4, **spReturnToTopLevel** = 8.<br>Keine Ausgabeparameter. |
| **Get_ShiftPathSet** | Die Funktion gibt die festgelegten Schritte des Werkzeugwegs zurück, auf denen der Generator die Verschiebung ausführt (**TNCShiftPathSet**).<br>Keine Eingabeparameter. |
| **Get_ShiftNextHole** | Die Funktion gibt die für die aktuelle Iteration berechneten Koordinaten des verschobenen Punkts der aktuellen Bohrung zurück (**TNC3DPoint**). Der Wert kann nur innerhalb der Ereignisse (**Set_Events**) verwendet werden.<br>Keine Eingabeparameter. |
| **Get_ShiftRapidPoint** | Die Funktion gibt die für die aktuelle Iteration berechneten Koordinaten des verschobenen Punkts auf der Ebene der Eilgangbewegung zurück (**TNC3DPoint**). Der Wert kann nur innerhalb der Ereignisse (**Set_Events**) verwendet werden.<br>Keine Eingabeparameter. |
| **Get_ShiftTopPoint** | Die Funktion gibt die für die aktuelle Iteration berechneten Koordinaten des verschobenen Punkts auf der Rückzugsebene zurück (**TNC3DPoint**). Der Wert kann nur innerhalb der Ereignisse (**Set_Events**) verwendet werden.<br>Keine Eingabeparameter. |
| **Get_ShiftBottomPoint** | Die Funktion gibt die für die aktuelle Iteration berechneten Koordinaten des verschobenen Punkts auf der Ebene des Bohrungsgrunds zurück (**TNC3DPoint**). Der Wert kann nur innerhalb der Ereignisse (**Set_Events**) verwendet werden.<br>Keine Eingabeparameter. |
