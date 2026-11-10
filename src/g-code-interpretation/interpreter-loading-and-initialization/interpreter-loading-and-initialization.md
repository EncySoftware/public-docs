# Laden und Initialisierung des Interpreters

Im CAM-System besteht das **Laden des Interpreters in den Speicher** aus folgenden Schritten:

- Lesen der Interpreter-Einstellungsdatei.
- Laden der Liste der Register aus der Interpreter-Einstellungsdatei.
- Laden des Eltern-Interpreters in den Speicher (das Laden des Eltern-Interpreters wiederholt alle Schritte des Ladens eines Interpreters in derselben Reihenfolge).
- Laden der Programmbibliothek des Interpreters in den Speicher und Abfragen der Schnittstelle **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md)** (durch Aufruf der Funktion **NCT_GetInterface** der geladenen Programmbibliothek).
- Prüfen, ob die Bezeichner der Einstellungsdatei und der Programmbibliothek übereinstimmen (den Bezeichner der Programmbibliothek liefert die Funktion **INCT_Interpreter.GetIdentifier**), sowie Prüfen der Bezeichner des Eltern-Interpreters.
- Übergeben der Werte der eigenen Parameter, wenn das Objekt des Interpreters die Schnittstelle **INCT_CustomInterpreter** implementiert (Aufruf der Methode **INCT_CustomInterpreter.SetCustomValues**; die Werte stammen aus der Datei `*.sncix`; siehe [Liste der verwendeten Typen](../interfaces/list-of-used-interfaces.md)). Dieser Schritt wird nur ausgeführt, wenn der Interpreter für die Arbeit geladen wird, nicht zur Prüfung und nicht zum Lesen seiner Parameter im Fenster **Dolmetscher-Konfigurator**.
- Laden der Liste der Register aus der Programmbibliothek (Aufruf der Funktion **INCT_Interpreter.GetRegisters**).
- Laden der Listen der Register der Eltern-Interpreter.

Nach dem Laden des Interpreters sind die Programmbibliothek des Interpreters und ihre Eltern-Bibliotheken (falls vorhanden) geladen, und die resultierende Liste der Register (Basisregister) ist gebildet. Dabei haben die Register der Einstellungsdatei Vorrang vor den Registern der Programmbibliothek (d. h. sie überschreiben sie), und die Register abgeleiteter Interpreter haben Vorrang vor den Registern der Eltern-Interpreter, wenn ein Register mit diesem Namen in beiden Listen vorhanden ist.

**Die Initialisierung des Interpreters** besteht aus folgenden Schritten:

- Initialisierung der Eltern-Interpreter (die Initialisierung eines Eltern-Interpreters wiederholt alle Schritte der Initialisierung eines Interpreters in derselben Reihenfolge).
- Übergabe der Schnittstellen des CAM-Systems an die Programmbibliothek nacheinander (die Methode **INCT_Interpreter.SetInterface** der Programmbibliothek des Interpreters wird mehrmals aufgerufen, einmal für jede übergebene Schnittstelle).
- Initialisierung der Programmbibliothek (Aufruf der Methode **INCT_Interpreter.Initialize**).

Bei der Initialisierung werden dem Interpreter Objekte des CAM-Systems übergeben, die folgende Schnittstellen implementieren:

- Zugriff auf die gebildete Liste der Register (Basisregister) **[INCT_SysState](../cam-interfaces/basic-interfaces/register-list/register-list.md)**;
- Steuerung der Einstellungen für die Analyse des NC-Programms **[INCT_Analyzer](../cam-interfaces/managing-nc-program-analysis/managing-nc-program-analysis.md)**;
- Zugriff auf die Liste der zu interpretierenden Objekte **[INCT_BlockExecArray](../cam-interfaces/basic-interfaces/list-of-objects-to-interpret/list-of-objects-to-interpret.md)**;
- Abfrage der Einstellungen der Ausrüstung **[INCT_Equipment](../cam-interfaces/basic-interfaces/equipment-parameters/equipment-parameters.md)**;
- Bildung des Werkzeugwegs in Maschinenachsen (wenn in der Einstellungsdatei des Interpreters `UseGeomCLData` = False ist) **[INCT_CLData](../cam-interfaces/basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md)**;
- Bildung des Werkzeugwegs in geometrischen Achsen (wenn `UseGeomCLData` = True ist) **[INCT_GeomCLData](../cam-interfaces/basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md)**;
- Interaktion mit dem Kern des CAM-Systems, der den Interpreter bedient, **[INCT_Kernel](../cam-interfaces/basic-interfaces/cam-kernel-interface/cam-system-kernel-interface.md)**;
- Eltern-Interpreter **[INCT_Interpreter](../interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md)** (falls vorhanden);
- Kontur (die an **INCT_Kernel.InterpreteContour** übergebene Schnittstelle), wenn der Interpreter im Konturmodus läuft;
- Schutz **[INCT_Connect](../interfaces/interpreter-interfaces/protection-interface/protection-interface.md)**, nur für geschützte Interpreter.

Anschließend wird die Initialisierungsmethode der Bibliothek des Interpreters ausgeführt.
