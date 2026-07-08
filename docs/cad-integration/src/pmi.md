# PMI (Product Manufacturing Information)

PMI (Product Manufacturing Information) — annotations of manufacturing information: dimensions, tolerances, threads, etc.

A PMI object is created by a `BeginObject_*` call, filled in through its interface, and written to the SGF by a call to `EndObject`.

| Method | Description |
|-------|----------|
| `BeginObject_PMIThread(CADID: string): IPMIGeomThread` | Create a thread object and return the `IPMIGeomThread` interface (see [IPMIGeomThread](pmi-thread.md)) for filling it in. `CADID` is the object's unique identifier in the CAD. |
| `EndObject(obj: IUnknown): boolean` | Write the filled-in object (for example, the one obtained from `BeginObject_PMIThread`) to the SGF file. Returns a flag indicating whether the write succeeded. |

Description of PMI objects:

- **[IPMIGeomThread](pmi-thread.md)** — the thread object: parameters, local coordinate system, associative references to geometry, and a save example.
