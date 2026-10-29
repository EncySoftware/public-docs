# Vererbung von Interpretern

Der Vererbungsmechanismus dient dazu, bereits entwickelte Interpreter bei der Übersetzung und Interpretation von NC-Programmen mit ähnlicher, aber abweichender Syntax wiederzuverwenden. Wie stark sich ein NC-Programm vom ursprünglichen unterscheiden muss, damit statt eines abgeleiteten Interpreters ein neuer Interpreter entwickelt wird, entscheidet der Entwickler selbst.

Ein abgeleiteter Interpreter übersetzt und interpretiert die Abweichungen im NC-Programm und übergibt die Steuerung für die Übersetzung und Interpretation ähnlicher Abschnitte des NC-Programms an den Eltern-Interpreter.

Die Implementierung eines abgeleiteten Interpreters unterscheidet sich von der eines [gewöhnlichen Interpreters](../../../index.md) in folgenden Punkten:

1. In der [Interpreter-Einstellungsdatei](../../interpreter-structure/interpreter-settings-file/interpreter-settings-file.md) (SNCI) werden die Felder **ParentID** und **ParentFileName** ausgefüllt.
2. Bei Bedarf werden vorhandene Register überschrieben oder neue hinzugefügt. Das geschieht durch Änderungen in der Liste der Register der SNCI-Datei oder in der Liste der Register, die die Funktion **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).GetRegisters** der [Programmbibliothek](../../interpreter-structure/interpreter-library/interpreter-library.md) des abgeleiteten Interpreters zurückgibt.
3. Die [Programmbibliothek](../../interpreter-structure/interpreter-library/interpreter-library.md) des abgeleiteten Interpreters wird implementiert. Ob der abgeleitete Interpreter dabei Funktionen und Methoden der Programmbibliothek des Eltern-Interpreters aufruft, hängt von den Algorithmen ab, die für die Übersetzung und Interpretation des NC-Programms vorgesehen sind. Die Schnittstelle des Eltern-Interpreters (**[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md)**) wird dem abgeleiteten Interpreter bei der Initialisierung übergeben.

Ein Interpreter kann nur von einem Eltern-Interpreter abgeleitet werden. Die Anzahl der von einem Eltern-Interpreter abgeleiteten Interpreter und die Tiefe der Vererbung sind nicht begrenzt.

**Vererbung der Register.**

Die Register abgeleiteter Interpreter überschreiben die Register der Eltern-Interpreter. Die Vererbung der Register ist so implementiert, dass in die resultierende Liste ([Liste der Basisregister](../sprutcam-interfaces/basic-interfaces/register-list/register-list.md)) nacheinander geladen werden:

1. die Liste der Register aus der Einstellungsdatei des **abgeleiteten Interpreters**;
2. die Liste der Register aus der Programmbibliothek des **abgeleiteten Interpreters** (**[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).GetRegisters**). Ist ein Register mit diesem Namen bereits in der Liste der Basisregister vorhanden, wird es nicht geladen;
3. die Liste der Register aus der Einstellungsdatei des **Eltern-Interpreters**. Ist ein Register mit diesem Namen bereits in der Liste der Basisregister vorhanden, wird es nicht geladen;
4. die Liste der Register aus der Programmbibliothek des **Eltern-Interpreters**. Ist ein Register mit diesem Namen bereits in der Liste der Basisregister vorhanden, wird es nicht geladen;
5. die Liste der Register aus der Einstellungsdatei des **Eltern-Interpreters des Eltern-Interpreters**. Ist ein Register mit diesem Namen bereits in der Liste der Basisregister vorhanden, wird es nicht geladen;
6. die Liste der Register aus der Programmbibliothek des **Eltern-Interpreters des Eltern-Interpreters**. Ist ein Register mit diesem Namen bereits in der Liste der Basisregister vorhanden, wird es nicht geladen;
7. und so weiter bis zum ersten Eltern-Interpreter.

**Vererbung der Programmbibliothek.**

Bei der [Initialisierung der Programmbibliothek des Eltern-Interpreters](../interpreter-loading-and-initialization/interpreter-loading-and-initialization.md) ruft der Kern des CAM-Systems einige Methoden und Funktionen selbst auf; der abgeleitete Interpreter muss sie nicht aufrufen:

1. **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).GetIdentifier.**
2. **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).GetRegisters.**
3. **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).SetInterface.**
4. **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).Initialize.**

Ob der abgeleitete Interpreter die übrigen Funktionen und Methoden der Programmbibliothek des Eltern-Interpreters aufruft, hängt von den Algorithmen ab, die für die Übersetzung und Interpretation des NC-Programms vorgesehen sind. Damit er die Methoden des Eltern-Interpreters aufrufen kann, wird ihm bei der [Initialisierung der Programmbibliothek des abgeleiteten Interpreters](../interpreter-loading-and-initialization/interpreter-loading-and-initialization.md) unter anderem die Schnittstelle des Eltern-Interpreters übergeben (Funktion **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).SetInterface**).

Im Folgenden die Empfehlungen zum Aufruf von Funktionen und Methoden des Eltern-Interpreters aus dem abgeleiteten Interpreter.

1. **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).TransLine** - **TransLine** des Eltern-Interpreters aufrufen, wenn die Analyse der Zeile des NC-Programms die ursprüngliche Zeile nicht verkürzt hat. Alle Parameter, die die Methode des Eltern-Interpreters zurückgegeben hat (**ProcessedChars, NextLine, BreakLine**), in die Ausgabeparameter der Methode des abgeleiteten Interpreters übernehmen.
2. **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).DefineRegister** - **DefineRegister** des Eltern-Interpreters aufrufen, wenn der abgeleitete Interpreter das Register nicht anhand der Adresse bestimmt hat. Den Parameter **Index** und das Ergebnis, die die Funktion des Eltern-Interpreters zurückgegeben hat, in den Ausgabeparameter und das Ergebnis der Funktion des abgeleiteten Interpreters übernehmen.
3. **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).BeforeInterprete** - **BeforeInterprete** des Eltern-Interpreters immer aufrufen.
4. **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).Interprete** - **Interprete** des Eltern-Interpreters aufrufen, wenn der abgeleitete Interpreter das zu interpretierende Objekt nicht selbst interpretiert.
5. **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).AfterInterprete** - **AfterInterprete** des Eltern-Interpreters immer aufrufen.
6. **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md).EndOfProgram** - **EndOfProgram** des Eltern-Interpreters immer aufrufen, wenn der abgeleitete Interpreter das Ende des NC-Programms nicht festgestellt hat. Das Ergebnis der Funktion des Eltern-Interpreters als Ergebnis der Funktion des abgeleiteten Interpreters zurückgeben.

Auf der Seite [Beispiele für Interpreter mit Quellcodes](../../interpreter-structure/interpreter-example/interpreter-example.md) finden Sie ein Beispiel für die Quellcodes der Bibliothek eines abgeleiteten Interpreters, die daraus erstellte 'dll' und ein Beispiel für die Einstellungsdatei.
