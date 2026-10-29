# Interpreter-Bibliothek

Die Programmbibliothek des Interpreters ist eine dynamische Bibliothek ([DLL](https://learn.microsoft.com/troubleshoot/windows-client/deployment/dynamic-link-library)). Unabhängig von der Plattform, für die sie implementiert ist (.NET oder nativ), muss die Bibliothek zwei Funktionen exportieren:

**NCT_GetInterface** - gibt dem CAM-System das Objekt zurück, das die Schnittstelle für das Zusammenwirken des Kerns des CAM-Systems mit der Programmbibliothek implementiert ([**INCT_Interpreter**](../../g-code-interpretation/interfaces/interpreter-interfaces/interpreter-interface/interpreter-interface.md));

**NCT_FreeMemory** - gibt den Speicher aller Objekte frei, die während der Arbeit selbst erstellt oder vom CAM-System erhalten wurden.

**Beispiel einer Klasse in C#, die die Funktionen der Interpreter-Bibliothek beschreibt (Assembly für die Plattform .NET):**

```csharp
namespace sample
{
    public class Interpreter: MarshalByRefObject
    {
        public static INCT_Interpreter NCT_GetInterface()
        {
            /* Implementierung */
        }
        public static void NCT_FreeMemory()
        {
            /* Implementierung */
        }
    }
}
```

**Beschreibung der Funktionen einer nativen Interpreter-Bibliothek in Delphi:**

```pascal
function NCT_GetInterface: INCT_Interpreter; stdcall;
procedure NCT_FreeMemory; stdcall;
```

**Beschreibung der Funktionen einer nativen Interpreter-Bibliothek in C\+\+:**

```cpp
INCT_Interpreter __stdcall NCT_GetInterface();
void __stdcall NCT_FreeMemory();
```

Alle Typen, die für das Zusammenwirken des CAM-Systems mit der Programmbibliothek des Interpreters nötig sind, sind in der [Typbibliothek](https://learn.microsoft.com/windows/win32/midl/com-dcom-and-type-libraries) beschrieben, die zum Lieferumfang des CAM-Systems gehört (Verzeichnis **TypeLibraries\\\*.tlb**).

Die folgenden TLB-Dateien beschreiben die Typen, die beim Zusammenwirken mit der Bibliothek des Interpreters verwendet werden:

- **STNCInterpreter.tlb** - die wichtigsten Typen;
- **STNCAnalyzer.tlb** - Typen zur Steuerung der Analyse des NC-Programms;
- **STNCFormers.tlb** - Typen zur Vereinfachung der Bildung des Werkzeugwegs (lineare und kreisförmige Bewegungen, Zyklen).

Wie die Typbibliothek in Ihre Entwicklungsumgebung eingebunden wird, steht im entsprechenden Abschnitt der Dokumentation der Entwicklungsumgebung.

> [!NOTE]
> **Registrierung der Typbibliothek**
>
> Um die Typbibliothek in Microsoft Visual Studio zu registrieren, gehen Sie wie folgt vor:
>
> Suchen Sie die Datei **tlbImp.exe** auf Ihrem Computer. Führen Sie den Befehl „**tlbimp.exe tlb-filename**“ aus. Dabei wird die Datei „**tlb-filename.dll**“ erstellt (zum Beispiel „STNCAnalyzer.dll“). Fügen Sie diese DLL-Datei über den Menüpunkt „**Add Reference**“ zu Ihrem Projekt hinzu.

Auf der Seite [Beispiele für Interpreter mit Quellcodes](../interpreter-example/interpreter-example.md) finden Sie ein Beispiel für den Quellcode einer Interpreter-Bibliothek, die daraus gebaute DLL und ein Beispiel für eine Einstellungsdatei.
