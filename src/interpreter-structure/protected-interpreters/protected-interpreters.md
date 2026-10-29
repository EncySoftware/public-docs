# Geschützte Interpreter

Damit der Interpreter nur gemäß der erteilten Lizenz verwendet werden kann, sind folgende Schritte nötig:

1. Der Interpreter muss unter Verwendung der [Schutz-Schnittstelle](../../g-code-interpretation/interfaces/interpreter-interfaces/protection-interface/protection-interface.md) entwickelt werden.
2. Der Interpreter muss [in einen Container gelegt werden](https://docs.encycam.com/ENCY/3/en/10022.html).
3. Zusammen mit dem Interpreter müssen [eine oder mehrere Dateien mit geheimen Daten](../../g-code-interpretation/interfaces/interpreter-interfaces/protection-interface/protection-interface.md) in den Container gelegt werden.

Nachdem die Lizenz für den Container ausgestellt und aktiviert wurde, kann der Benutzer den Interpreter verwenden, siehe [G-Code-basierte Simulation](https://docs.encycam.com/ENCY/3/en/10291.html).
