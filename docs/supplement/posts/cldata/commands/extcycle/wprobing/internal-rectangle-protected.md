# Internal rectangle probing protected parameters

![image2022-4-5_19-21-28](../../../../sppx/images/download/attachments/148776098/image2022-4-5_19-21-28.png) ![image2022-4-5_19-22-0](../../../../sppx/images/download/attachments/148776098/image2022-4-5_19-22-0.png)

Internal rectangle probing protected consist of the following steps:

1. The tool moves to the distance specified in the `Feed distance` and approaches the starting position of the cycle. The movement is executed at "Approach feed";
2. The tool approaches a point remote from the first touch point along its `Target vector` at the `Side clearance 1` distance but elevated at the `Top clearance` value + `Depth` value. The movement is executed at "Long link feed";
3. The tool is lowered by a distance equal to `Top clearance` value + `Depth` value. Moving at "Long link feed";
4. The tool approaches the first touch point (moving at "Work feed" ) and then returns (moving at "Long link feed" ) to previous position;
5. The tool is lifted up by a distance equal to `Top clearance` value + `Depth` value. The movement is executed at "Long link feed";
6. The tool returns to the starting position;
7. Steps 2-6 are repeated 3 times for each touch points;
8. The tool is lifted up by a distance equal to `Feed distance`.

## Parameters

| CLDArray | Type | Description |
|---|---|---|
| CmdPrm.Int[-1] | Integer | Probing cycle type: Internal rectangle probing protected value = 7 |
| CmdPrm.Int[-2] | Integer | SubCode of cycle specified in " SubCode for postprocessor " property on the `Job Assignment` tab |
| CmdPrm.Flt[-50] | Double | Feed distance, distance to start position of cycle |
| CmdPrm.Flt[-51] | Double | Depth, distance from top side to center of touch points |
| CmdPrm.Flt[-53] | Double | Width 1, distance from Touch point 1 to Touch point 2 |
| CmdPrm.Flt[-54] | Double | Width 2, distance from Touch point 3 to Touch point 4 |
| CmdPrm.Flt[-55] | Double | Top clearance, distance from top side |
| CmdPrm.Flt[-56] | Double | Side clearance 1, approach distance to touch point 1/ touch point 2 |
| CmdPrm.Flt[-57] | Double | Side clearance 2, approach distance to touch point 3/ touch point 4 |
| CmdPrm.Flt[-100] | Double | First touch point value along X-axis |
| CmdPrm.Flt[-101] | Double | First touch point value along Y-axis |
| CmdPrm.Flt[-102] | Double | First touch point value along Z-axis |
| CmdPrm.Flt[-103] | Double | First target vector value along X-axis |
| CmdPrm.Flt[-104] | Double | First target vector value along Y-axis |
| CmdPrm.Flt[-105] | Double | First target vector value along Z-axis |
| CmdPrm.Flt[-106] | Double | Second touch point value along X-axis |
| CmdPrm.Flt[-107] | Double | Second touch point value along Y-axis |
| CmdPrm.Flt[-108] | Double | Second touch point value along Z-axis |
| CmdPrm.Flt[-109] | Double | Second target vector value along X-axis |
| CmdPrm.Flt[-110] | Double | Second target vector value along Y-axis |
| CmdPrm.Flt[-111] | Double | Second target vector value along Z-axis |
| CmdPrm.Flt[-112] | Double | Third touch point value along X-axis |
| CmdPrm.Flt[-113] | Double | Third touch point value along Y-axis |
| CmdPrm.Flt[-114] | Double | Third touch point value along Z-axis |
| CmdPrm.Flt[-115] | Double | Third target vector value along X-axis |
| CmdPrm.Flt[-116] | Double | Third target vector value along Y-axis |
| CmdPrm.Flt[-117] | Double | Third target vector value along Z-axis |
| CmdPrm.Flt[-118] | Double | Fourth touch point value along X-axis |
| CmdPrm.Flt[-119] | Double | Fourth touch point value along Y-axis |
| CmdPrm.Flt[-120] | Double | Fourth touch point value along Z-axis |
| CmdPrm.Flt[-121] | Double | Fourth target vector value along X-axis |
| CmdPrm.Flt[-122] | Double | Fourth target vector value along Y-axis |
| CmdPrm.Flt[-123] | Double | Fourth target vector value along Z-axis |
| CmdPrm.Flt[-200] | Double | First original touch point value along X-axis specified in the **Job Assignment** |
| CmdPrm.Flt[-201] | Double | First original touch point value along Y-axis specified in the **Job Assignment** |
| CmdPrm.Flt[-202] | Double | First original touch point value along Z-axis specified in the **Job Assignment** |
| CmdPrm.Flt[-203] | Double | First original target vector value along X-axis specified in the **Job Assignment** |
| CmdPrm.Flt[-204] | Double | First original target vector value along Y-axis specified in the **Job Assignment** |
| CmdPrm.Flt[-205] | Double | First original target vector value along Z-axis specified in the **Job Assignment** |
| CmdPrm.Flt[-206] | Double | Second original touch point value along X-axis specified in the **Job Assignment** |
| CmdPrm.Flt[-207] | Double | Second original touch point value along Y-axis specified in the **Job Assignment** |
| CmdPrm.Flt[-208] | Double | Second original touch point value along Z-axis specified in the **Job Assignment** |
| CmdPrm.Flt[-209] | Double | Second original target vector value along X-axis specified in the **Job Assignment** |
| CmdPrm.Flt[-210] | Double | Second original target vector value along Y-axis specified in the **Job Assignment** |
| CmdPrm.Flt[-211] | Double | Second original target vector value along Z-axis specified in the **Job Assignment** |
| CmdPrm.Flt[-212] | Double | Third original touch point value along X-axis specified in the **Job Assignment** |
| CmdPrm.Flt[-213] | Double | Third original touch point value along Y-axis specified in the **Job Assignment** |
| CmdPrm.Flt[-214] | Double | Third original touch point value along Z-axis specified in the **Job Assignment** |
| CmdPrm.Flt[-215] | Double | Third original target vector value along X-axis specified in the **Job Assignment** |
| CmdPrm.Flt[-216] | Double | Third original target vector value along Y-axis specified in the **Job Assignment** |
| CmdPrm.Flt[-217] | Double | Third original target vector value along Z-axis specified in the **Job Assignment** |
| CmdPrm.Flt[-218] | Double | Fourth original touch point value along X-axis specified in the **Job Assignment** |
| CmdPrm.Flt[-219] | Double | Fourth original touch point value along Y-axis specified in the **Job Assignment** |
| CmdPrm.Flt[-220] | Double | Fourth original touch point value along Z-axis specified in the **Job Assignment** |
| CmdPrm.Flt[-221] | Double | Fourth original target vector value along X-axis specified in the **Job Assignment** |
| CmdPrm.Flt[-222] | Double | Fourth original target vector value along Y-axis specified in the **Job Assignment** |
| CmdPrm.Flt[-223] | Double | Fourth original target vector value along Z-axis specified in the **Job Assignment** |
| CmdPrm.Flt[-66] | Integer | Compensate dimensions, retrurn values: 0 - Off, 1 - On |

## See also
- [Probing cycle (WProbing)](wprobing.md)
- [Extended cycle (EXTCYCLE)](../extcycle.md)
- [CLData access model](../../../cldata.md)
