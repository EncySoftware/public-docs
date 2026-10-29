# Examples of interpreters with source codes

## 1\. Interpreters for simulation and tool path import (based on [machine CLData](../../g-code-interpretation/sprutcam-interfaces/basic-interfaces/forming-of-the-toolpath-in-machine-axes/forming-of-the-toolpath-in-machine-axes.md))

### 1.1. Interpreter `sample`.

Implements linear and circular movements and the feed change command for the Fanuc 30i controller (milling).

The source code of the interpreter library developed for Microsoft Visual Studio (C#) is available at [this link](../../../images/129931467/sample_src.zip).

The interpreter based on the compiled library (**sample.dll**) and its settings file (**sample.snci**) can be obtained at [this link](../../../images/129931467/sample.zip).

### 1.2. Interpreter with inheritance `sample_inheritance`.

Inheritor of the **sample** interpreter. In addition to the parent's commands, it implements several basic commands: M, S, T, G04 X P (dwell).

The source code of the inheritor interpreter library developed for Microsoft Visual Studio (C#) is available at [this link](../../../images/129931467/sample_inheritance_src.zip).

The inheritor interpreter based on the compiled library (**sample_inheritance.dll**) and its settings file (**sample_inheritance.snci**) can be obtained at [this link](../../../images/129931467/sample_inheritance.zip).

### 1.3. Interpreter with inheritance `sample_Fanuc30i_Mill`.

Inheritor of the **Fanuc_30i_Mill** interpreter (included in the CAM system distribution). In addition to the parent's commands, it implements the G04 X P command (dwell).

The source code of the inheritor interpreter library developed for Microsoft Visual Studio (C#) is available at [this link](../../../images/129931467/sample_Fanuc30i_Mill_src.zip).

The inheritor interpreter based on the compiled library (**sample_Fanuc30i_Mill.dll**) and its settings file (**sample\_Fanuc30i_Mill.snci**) can be obtained at [this link](../../../images/129931467/sample_Fanuc30i_Mill.zip).

### 1.4. Interpreter using the drilling cycle generator `sample_dc`.

Implements the CYCLE81 command for the Sinumerik 840D milling controller.

The source code of the interpreter library developed for Microsoft Visual Studio (C#) is available at [this link](../../../images/129931467/sample_dc_src.zip).

The interpreter based on the compiled library (**sample_dc.dll**) and its settings file (**sample_dc.snci**) can be obtained at [this link](../../../images/129931467/sample_dc.zip).

The [following project](../../../images/129931467/sample_dc_project.zip) demonstrates how the interpreter works. Download the project and the interpreter. Open the project, set the **sample_dc.snci** interpreter in the G-code based operation settings, calculate the operation and simulate it.

## 2\. Interpreters for tool path import (based on [geometric CLData](../../g-code-interpretation/sprutcam-interfaces/basic-interfaces/forming-of-the-toolpath-in-geometric-axes/forming-of-the-toolpath-in-geometric-axes.md))

### 2.1. Interpreter `sample_geom`.

Implements linear and circular movements for 3-axis milling and the feed change command for the Fanuc 30i controller.

The source code of the interpreter library developed for Microsoft Visual Studio (C#) is available at [this link](../../../images/129931467/sample_geom_src.zip).

The interpreter based on the compiled library (**sample_geom.dll**) and its settings file (**sample_geom.snci**) can be obtained at [this link](../../../images/129931467/sample_geom.zip).

### 2.2. Interpreter `sample_geom_5x`.

Implements linear and circular movements for 5-axis milling (commands: X, Y, Z, TRAORI, TRAFOOF, A3, B3, C3) and the feed change command for the Sinumerik controller.

The source code of the interpreter library developed for Microsoft Visual Studio (C#) is available at [this link](../../../images/129931467/sample_geom_5x_src.zip).

The interpreter based on the compiled library (**sample_geom_5x.dll**) and its settings file (**sample_geom_5x.snci**) can be obtained at [this link](../../../images/129931467/sample_geom_5x.zip).

The [following project](../../../images/129931467/sample_GeomCLData_project.zip) demonstrates 5-axis movements. Download the project and the interpreter. Open the project, set the **sample_geom_5x.snci** interpreter in the G-code based operation settings, calculate the operation and simulate it.
