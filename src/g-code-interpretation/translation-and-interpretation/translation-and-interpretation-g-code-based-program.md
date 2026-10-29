# Übersetzung und Interpretation des NC-Programms

**Interpretation des NC-Programms.**

Solange die Sätze des NC-Programms nicht zu Ende sind und die Bibliothek des Interpreters nicht das Kennzeichen für das Programmende setzt (Methode **INCT_Interpreter.EndOfProgram**), liest das CAM-System die Sätze des NC-Programms und führt für jeden Satz folgende Schritte aus:

- Übersetzung des Satzes (Analyse des Satzes auf bekannte Konstruktionen - Objekte für die Interpretation);
- Hat die Übersetzung des Satzes mindestens ein Objekt in der Liste der zu interpretierenden Objekte des aktuellen Satzes ergeben (d. h. die Liste **[INCT_BlockExecArray](../sprutcam-interfaces/basic-interfaces/list-of-objects-to-interpret/list-of-objects-to-interpret.md)** ist nicht leer), wird jedes Objekt der Liste **[INCT_BlockExecArray](../sprutcam-interfaces/basic-interfaces/list-of-objects-to-interpret/list-of-objects-to-interpret.md)** nacheinander interpretiert;
- Die Liste der zu interpretierenden Objekte des aktuellen Satzes wird geleert.

**Übersetzung eines Satzes des NC-Programms.**

Solange die Zeichen des Satzes nicht zu Ende sind, führt das CAM-System folgende Schritte aus:

- Der noch nicht verarbeitete Teil des Satzes wird an die Bibliothek des Interpreters übergeben (im ersten Schritt also der ganze Satz). Als Antwort erwartet das CAM-System die Anzahl der Zeichen **ab dem Anfang der übergebenen Zeichenkette**, die der Interpreter als einzelnes Wort oder als andere ihm verständliche Konstruktion erkannt hat (Methode **INCT_Interpreter.TransLine**). Die erkannten Zeichen gelten als verarbeitet und werden aus dem Satz entfernt. Dieser Schritt wird wiederholt, solange der Interpreter am Anfang des verbleibenden Satzes Sinnkonstruktionen (Wörter) erkennt, d. h. dem CAM-System eine Anzahl erkannter Zeichen größer als null zurückgibt, oder bis der Satz zu Ende ist.
- Sobald der Interpreter am Anfang des verbleibenden Satzes keine Sinnkonstruktion erkennen kann, versucht das CAM-System, das Register und seinen Wert nach dem im Artikel [Algorithmus zur Bestimmung von Register und Wert im Satz des NC-Programms](algorithm-for-determining-register-and-values-in-g-code-block/algorithm-for-determining-register-and-values-in-g-code-block.md) beschriebenen Verfahren zu bestimmen.
- Wurde ein Register bestimmt, wird es am Ende der Liste der zu interpretierenden Objekte des aktuellen Satzes hinzugefügt (**[INCT_BlockExecArray](../sprutcam-interfaces/basic-interfaces/list-of-objects-to-interpret/list-of-objects-to-interpret.md)**, mit dem Kennzeichen **Register**). Andernfalls wird der gelesene, nicht erkannte Teil des Satzes übersprungen; er gilt aber ebenfalls als verarbeitet und wird vom Anfang des verbleibenden Satzes entfernt;

**Hinweis.**

Zur Erkennung der Sinnkonstruktionen eines Satzes empfehlen wir, wo immer möglich, den Mechanismus des CAM-Systems zur Bestimmung von Registern und Werten zu verwenden ([Algorithmus zur Bestimmung von Register und Wert im Satz des NC-Programms](algorithm-for-determining-register-and-values-in-g-code-block/algorithm-for-determining-register-and-values-in-g-code-block.md)) und im Interpreter (in der Methode **INCT_Interpreter.TransLine**) nur die Konstruktionen zu verarbeiten, die dieser Mechanismus nicht oder nicht effizient erkennen kann. Die Routinearbeit zur Bestimmung typischer Konstruktionen übernimmt dann der Kern des CAM-Systems, und im Interpreter werden nur seltene Sinnkonstruktionen verarbeitet, die nicht in die allgemeinen Regeln des Algorithmus passen.

**Hinweis.**

Nachdem der Interpreter ein Wort oder eine Sinnkonstruktion erkannt hat, kann er die Informationen darüber selbst speichern (in seinen internen Datenstrukturen) oder die Liste der zu interpretierenden Objekte des aktuellen Satzes verwenden (**[INCT_BlockExecArray](../sprutcam-interfaces/basic-interfaces/list-of-objects-to-interpret/list-of-objects-to-interpret.md)**), d. h. der Liste ein eigenes Element mit dem Kennzeichen **Objekt** oder **Register** hinzufügen. Wir empfehlen die zweite Variante: Dann bleibt die Reihenfolge der Objekte im Satz erhalten, unabhängig davon, ob das Objekt vom Kern des CAM-Systems oder vom Interpreter bestimmt wurde.

**Die Interpretation der Objekte der Liste** besteht aus folgenden Schritten:

- Vor der Interpretation der Objektliste wird die Methode **INCT_Interpreter.BeforeInterprete** aufgerufen; sie teilt dem Interpreter mit, dass die Interpretation des aktuellen Satzes beginnt;
- Für jedes Element der Liste, bei dem das Kennzeichen **IsUsed** nicht gesetzt ist, wird, solange das Kennzeichen für das Ende der Übersetzung (**INCT_Interpreter.EndOfProgram**) nicht gesetzt ist, die Methode **INCT_Interpreter.Interprete** ausgeführt. Danach wird beim interpretierten Element das Kennzeichen **IsUsed** gesetzt;
- Nach der Interpretation der gesamten Objektliste wird die Methode **INCT_Interpreter.AfterInterprete** aufgerufen; sie teilt dem Interpreter mit, dass die Interpretation des aktuellen Satzes abgeschlossen ist;

**Hinweis.**

Bei der Ausführung der Methode **INCT_Interpreter.Interprete** muss der Interpreter den Typ des übergebenen Objekts bestimmen und der Liste der CLDATA-Befehle den passenden Befehl hinzufügen.

Ist zum Beispiel das übergebene Objekt **bei der Fanuc-Steuerung** ein Register mit der Adresse **F** (Vorschub), muss die Methode **[INCT_CLData](../sprutcam-interfaces/basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md).OutFeed** ausgeführt und ihr der Wert des Registers als Parameter übergeben werden.
