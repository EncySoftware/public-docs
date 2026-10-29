# Laden und Initialisierung des Interpreters

Im CAM-System besteht das **Laden des Interpreters in den Speicher** aus folgenden Schritten:

- Lesen der Interpreter-Einstellungsdatei.
- Laden der Liste der Register aus der Interpreter-Einstellungsdatei.
- Laden des Eltern-Interpreters in den Speicher (das Laden des Eltern-Interpreters wiederholt alle Schritte des Ladens eines Interpreters in derselben Reihenfolge).
- Laden der Programmbibliothek des Interpreters in den Speicher und Abfragen der Schnittstelle **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md)** (durch Aufruf der Funktion **NCT_GetInterface** der geladenen Programmbibliothek).
- Prüfen, ob die Bezeichner der Einstellungsdatei und der Programmbibliothek übereinstimmen (den Bezeichner der Programmbibliothek liefert die Funktion **INCT_Interpreter.GetIdentifier**), sowie Prüfen der Bezeichner des Eltern-Interpreters.
- Laden der Liste der Register aus der Programmbibliothek (Aufruf der Funktion **INCT_Interpreter.GetRegisters**).
- Laden der Listen der Register der Eltern-Interpreter.

Nach dem Laden des Interpreters sind die Programmbibliothek des Interpreters und ihre Eltern-Bibliotheken (falls vorhanden) geladen, und die resultierende Liste der Register (Basisregister) ist gebildet. Dabei haben die Register der Einstellungsdatei Vorrang vor den Registern der Programmbibliothek (d. h. sie überschreiben sie), und die Register abgeleiteter Interpreter haben Vorrang vor den Registern der Eltern-Interpreter, wenn ein Register mit diesem Namen in beiden Listen vorhanden ist.

**Die Initialisierung des Interpreters** besteht aus folgenden Schritten:

- Initialisierung der Eltern-Interpreter (die Initialisierung eines Eltern-Interpreters wiederholt alle Schritte der Initialisierung eines Interpreters in derselben Reihenfolge).
- Übergabe der Schnittstellen des CAM-Systems an die Programmbibliothek nacheinander (die Methode **INCT_Interpreter.SetInterface** der Programmbibliothek des Interpreters wird mehrmals aufgerufen, einmal für jede übergebene Schnittstelle).
- Initialisierung der Programmbibliothek (Aufruf der Methode **INCT_Interpreter.Initialize**).

Bei der Initialisierung werden dem Interpreter Objekte des CAM-Systems übergeben, die folgende Schnittstellen implementieren:

- Zugriff auf die gebildete Liste der Register (Basisregister) **[INCT_SysState](../sprutcam-interfaces/basic-interfaces/register-list/register-list.md)**;
- Steuerung der Einstellungen für die Analyse des NC-Programms **[INCT_Analyzer](../sprutcam-interfaces/managing-nc-program-analysis/managing-nc-program-analysis.md)**;
- Zugriff auf die Liste der zu interpretierenden Objekte **[INCT_BlockExecArray](../sprutcam-interfaces/basic-interfaces/list-of-objects-to-interpret/list-of-objects-to-interpret.md)**;
- Abfrage der Einstellungen der Ausrüstung **[INCT_Equipment](../sprutcam-interfaces/basic-interfaces/equipment-parameters/equipment-parameters.md)**;
- Bildung des Werkzeugwegs in Maschinenachsen **[INCT_CLData](../sprutcam-interfaces/basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md)**;
- Bildung des Werkzeugwegs in geometrischen Achsen **[INCT_GeomCLData](../sprutcam-interfaces/basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md)**;
- Interaktion mit dem Kern des CAM-Systems, der den Interpreter bedient, **[INCT_Kernel](../sprutcam-interfaces/basic-interfaces/sprutcam-kernel-interface/cam-system-kernel-interface.md)**;
- Eltern-Interpreter **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md)**.

Anschließend wird die Initialisierungsmethode der Bibliothek des Interpreters ausgeführt.
