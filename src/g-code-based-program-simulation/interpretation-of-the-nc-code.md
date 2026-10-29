# Interpretation des NC-Programms

Unter Interpretation verstehen wir die Umwandlung des Textes eines NC-Programms, seiner Wörter und Sätze, in [technologische CLDATA-Befehle](https://docs.encycam.com/Inp/2/en/10088.html), die den Werkzeugweg bilden. Bei der Interpretation geht das CAM-System mit dem für die Maschine gewählten Interpreter wie folgt vor:

- es liest die Sätze des NC-Programms nacheinander;
- anhand der vom Interpreter erhaltenen Informationen über die Register trennt es aus dem Satz die Wörter (oder Sinnkonstruktionen) heraus oder überlässt es dem Interpreter, die Wörter selbst herauszutrennen;
- es übergibt die Wörter dem Interpreter in der Reihenfolge, in der sie im Satz stehen;
- der Interpreter wandelt die Wörter des NC-Programms unter Berücksichtigung der Besonderheiten der Maschine in technologische CLDATA-Befehle um, die den wiederhergestellten Werkzeugweg bilden.

Die Beschreibung des Interpreters steht im Abschnitt [Struktur des Interpreters](../interpreter-structure/interpreter-structure.md).

Das Zusammenwirken des CAM-Systems mit dem Interpreter, durch das der sekundäre (wiederhergestellte) Werkzeugweg entsteht, ist im Abschnitt [Ablauf der Interpretation des NC-Programms](../g-code-interpretation/g-code-based-program-interpretation.md) beschrieben.
