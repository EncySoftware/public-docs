# EulerConverter

Euler Converter – object of 3D rotation converter.

## Parameters

- **RotatingSequence**: integer, options:
  - 1 – XYZ
  - 2 – XZY
  - 3 – YXZ
  - 4 – YZX
  - 5 – ZXY
  - 6 – ZYX
  - 7 – XYX
  - 8 – XZX
  - 9 – YXY
  - 10 – YZY
  - 11 – ZXZ
  - 12 – ZYZ
  - 13 – AB
  - 14 – AC
  - 15 – BA
  - 16 – BC
- **MovableOrFixed**: integer:
  - 1 – Rotating around movable axes
  - 0 – Rotating around fixed axes
- **AngleInDegrees**: integer
  - 1 – Degrees
  - 0 – Radians

## Methods

- **Init** – create Euler Converter Object
- **AnglesToMatrix** – create translation matrix with 3 angles and 3D point
- **MatrixToAngles** – get 3 angles and point from translation matrix
- **AnglesToAngles** – translate 3 angles of input Convention to 3 angles of output convention
- **AnglesToQuaternion** – translate 3 angles of input convention to quaternion
