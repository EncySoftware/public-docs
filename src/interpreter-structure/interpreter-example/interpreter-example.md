# Beispiele für Interpreter mit Quellcodes

Die Beispielprojekte wurden in Microsoft Visual Studio für .NET Framework 4 erstellt und verweisen auf Interop-Assemblys der Typbibliotheken **STNCInterpreter**, **STNCAnalyzer** und **STNCFormers**: `sample_dc` auf die Dateien `..\tlb\STNC*.dll`, die übrigen über COM-Verweise auf registrierte Typbibliotheken. Diese Assemblys sind in den Archiven nicht enthalten: Die `*.tlb`-Dateien stammen aus dem NuGet-Paket (siehe [Interpreter-Bibliothek](../interpreter-library/interpreter-library.md)), die Interop-Assemblys werden daraus mit dem Werkzeug `tlbimp` erstellt. Einen neuen Interpreter in C# erstellen Sie einfacher aus einer Vorlage des CAM-Systems, siehe [Entwicklung eines eigenen Interpreters in (.NET) C#](../../dotnet/developing-a-custom-interpreter-in-net-csharp.md).

## 1\. Interpreter für die Simulation und den Import des Werkzeugwegs (auf Basis der [CLData in Maschinenachsen](../../g-code-interpretation/cam-interfaces/basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md))

### 1.1. Interpreter `sample`.

Implementiert lineare und kreisförmige Bewegungen und den Befehl zum Ändern des Vorschubs für die Steuerung Fanuc 30i (Fräsen).

Der Quellcode der Interpreter-Bibliothek, entwickelt für Microsoft Visual Studio (C#), ist [unter diesem Link](../../../images/129931467/sample_src.zip) zu finden.

Den Interpreter auf Basis der kompilierten Bibliothek (**sample.dll**) und die zugehörige Einstellungsdatei (**sample.snci**) erhalten Sie [unter diesem Link](../../../images/129931467/sample.zip).

### 1.2. Interpreter mit Vererbung `sample_inheritance`.

Nachfolger des Interpreters **sample**. Zusätzlich zu den Befehlen des Eltern-Interpreters implementiert er einige grundlegende Befehle: M, S, T, G04 X P (Verweilzeit).

Der Quellcode der Bibliothek des abgeleiteten Interpreters, entwickelt für Microsoft Visual Studio (C#), ist [unter diesem Link](../../../images/129931467/sample_inheritance_src.zip) zu finden.

Den abgeleiteten Interpreter auf Basis der kompilierten Bibliothek (**sample_inheritance.dll**) und die zugehörige Einstellungsdatei (**sample_inheritance.snci**) erhalten Sie [unter diesem Link](../../../images/129931467/sample_inheritance.zip).

### 1.3. Interpreter mit Vererbung `sample_Fanuc30i_Mill`.

Nachfolger des Interpreters **Fanuc30i_Mill** (im Lieferumfang des CAM-Systems enthalten). Zusätzlich zu den Befehlen des Eltern-Interpreters implementiert er den Befehl G04 X P (Verweilzeit).

Der Quellcode der Bibliothek des abgeleiteten Interpreters, entwickelt für Microsoft Visual Studio (C#), ist [unter diesem Link](../../../images/129931467/sample_Fanuc30i_Mill_src.zip) zu finden.

Den abgeleiteten Interpreter auf Basis der kompilierten Bibliothek (**sample_Fanuc30i_Mill.dll**) und die zugehörige Einstellungsdatei (**sample_Fanuc30i_Mill.snci**) erhalten Sie [unter diesem Link](../../../images/129931467/sample_Fanuc30i_Mill.zip).

### 1.4. Interpreter mit dem Generator für Bohrzyklen `sample_dc`.

Implementiert den Befehl CYCLE81 für die Fräs-Steuerung Sinumerik 840D.

Der Quellcode der Interpreter-Bibliothek, entwickelt für Microsoft Visual Studio (C#), ist [unter diesem Link](../../../images/129931467/sample_dc_src.zip) zu finden.

Den Interpreter auf Basis der kompilierten Bibliothek (**sample_dc.dll**) und die zugehörige Einstellungsdatei (**sample_dc.snci**) erhalten Sie [unter diesem Link](../../../images/129931467/sample_dc.zip).

Zur Demonstration der Arbeit des Interpreters dient das [folgende Projekt](../../../images/129931467/sample_dc_project.zip). Laden Sie das Projekt und den Interpreter herunter, öffnen Sie das Projekt, wählen Sie in den Einstellungen der **G-Code basierten Operation** den Interpreter **sample_dc.snci**, berechnen Sie die Operation und simulieren Sie sie.

## 2\. Interpreter für den Import des Werkzeugwegs (auf Basis der [CLData in geometrischen Achsen](../../g-code-interpretation/cam-interfaces/basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md))

### 2.1. Interpreter `sample_geom`.

Implementiert lineare und kreisförmige Bewegungen für die 3-Achs-Fräsbearbeitung und den Befehl zum Ändern des Vorschubs für die Steuerung Fanuc 30i.

Der Quellcode der Interpreter-Bibliothek, entwickelt für Microsoft Visual Studio (C#), ist [unter diesem Link](../../../images/129931467/sample_geom_src.zip) zu finden.

Den Interpreter auf Basis der kompilierten Bibliothek (**sample_geom.dll**) und die zugehörige Einstellungsdatei (**sample_geom.snci**) erhalten Sie [unter diesem Link](../../../images/129931467/sample_geom.zip).

### 2.2. Interpreter `sample_geom_5x`.

Implementiert lineare und kreisförmige Bewegungen für die 5-Achs-Fräsbearbeitung (Befehle: X, Y, Z, TRAORI, TRAFOOF, A3, B3, C3) und den Befehl zum Ändern des Vorschubs für die Steuerung Sinumerik.

Der Quellcode der Interpreter-Bibliothek, entwickelt für Microsoft Visual Studio (C#), ist [unter diesem Link](../../../images/129931467/sample_geom_5x_src.zip) zu finden.

Den Interpreter auf Basis der kompilierten Bibliothek (**sample_geom_5x.dll**) und die zugehörige Einstellungsdatei (**sample_geom_5x.snci**) erhalten Sie [unter diesem Link](../../../images/129931467/sample_geom_5x.zip).

Zur Demonstration von 5-Achs-Bewegungen dient das [folgende Projekt](../../../images/129931467/sample_GeomCLData_project.zip). Laden Sie das Projekt und den Interpreter herunter, öffnen Sie das Projekt, wählen Sie in den Einstellungen der **G-Code basierten Operation** den Interpreter **sample_geom_5x.snci**, berechnen Sie die Operation und simulieren Sie sie.
