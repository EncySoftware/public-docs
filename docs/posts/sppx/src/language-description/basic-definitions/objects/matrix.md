# Matrix

Three-dimensional matrix

## Parameters

- **Vx**: record
  - **cX**, **cY**, **cZ**: real
- **A**: real
- **Vy**: record
  - **cX**, **cY**, **cZ**: real
- **B**: real
- **Vz**: record
  - **cX**, **cY**, **cZ**: real
- **C**: real
- **Vt**: record
  - **cX**, **cY**, **cZ**: real
- **D**: real

## Methods

- **CreateIdentity** – create unitary matrix
- **CreateBy4points** – create matrix with four 3D points
- **MakeRotMatrix** – create rotational matrix with angle, angleType (1 for degrees or 0 for radians) and number of an axis (1 for "X", 2 for "Y", 3 for "Z")
- **MakeShiftMatrix** – create translation matrix with 3D point
- **CreateAsAxisAngle** – creates matrix as axis and angle
- **CreateByPointAndNormal** – creates matrix by point and normal
- **CreateByVectorAndAngle** – creates matrix by vector and angle
- **Add** – add another matrix to the original
- **Subtract** – subtract another matrix from the original
- **Matr_X_Matr** – multiply the original matrix by another
- **GetDeterminant** – get determinant of a matrix
- **GetCoord** – get coord by row and column of matrix
- **Inverse** – invert matrix
- **Transpose** – transpose matrix
- **CreateBy3Points** – create a basis with three 3D points
- **GetLocalPoint** – represent global 3D point in local coordinate system
- **TransformPoint** – represent local 3D point in global coordinate system
- **GetLocalVector** – represent global 3D vector in local coordinate system
- **TransformVector** – represent local 3D vector in global coordinate system
- **GetLocalMatrix** – represent global 3D matrix in local coordinate system
- **TransformMatrix** – represent local 3D matrix in global coordinate system
- **ToString** – creates string with numbers from the matrix
- **Parse** – creates 4x4 matrix from the string
