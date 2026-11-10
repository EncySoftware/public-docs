# Ablauf der Interpretation des NC-Programms

Die Interpretation des NC-Programms, das für die Operationen gebildet wurde, besteht aus folgenden Schritten:

1. Vor der Interpretation des NC-Programms der ersten Operation [lädt der Kern des CAM-Systems den Interpreter in den Speicher und initialisiert ihn](interpreter-loading-and-initialization/interpreter-loading-and-initialization.md).
2. Für jede Operation wird [das NC-Programm übersetzt und interpretiert](translation-and-interpretation/translation-and-interpretation-g-code-based-program.md).
3. Nach der Interpretation der letzten Operation [entlädt das CAM-System den Interpreter aus dem Speicher](interpreter-unloading/interpreter-unloading.md).

Die Besonderheiten bei der Verwendung bereits entwickelter Interpreter für NC-Programme anderer, ähnlicher Steuerungen beschreibt der Artikel [Vererbung von Interpretern](interpreter-inheritance/interpreter-inheritance.md).

Die Liste der Schnittstellen, die der Interpreter verwendet und implementiert, steht im Abschnitt [Liste der verwendeten Typen](interfaces/list-of-used-interfaces.md).

Wie die Protokollierung der Interpretation des NC-Programms gesteuert wird, ist im Abschnitt [Protokoll der Interaktion mit dem Interpreter](log-interaction-with-the-interpreter/log-interaction-with-the-interpreter.md) beschrieben.
