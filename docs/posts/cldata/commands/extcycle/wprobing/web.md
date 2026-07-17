# Web probing parameters

![image2022-4-5_19-52-45](../../../../sppx/images/download/attachments/148776108/image2022-4-5_19-52-45.png)

Web probing consist of the following steps:

1. The tool moves the distance specified in the `Feed distance` and approaches the starting position of the cycle. Moving at "Approach feed";
2. The tool approaches a point remote from the first touch point along its `Target vector` at the `Side clearance` distance but elevated at the `Top clearance` value + `Depth` value. Moving at "Long link feed";
3. The tool is lowered by a distance equal to `Top clearance` value + `Depth` value. Moving at "Long link feed";
4. The tool approaches the first touch point (moving at "Work feed" ) and then returns (moving at "Long link feed" ) to previous position;
5. The tool is lifted up by a distance equal to `Top clearance` value + `Depth` value. Moving at "Long link feed";
6. The tool returns to the starting position;
7. Steps 2-6 are repeated for the second touch point;
8. The tool is lifted up by a distance equal to `Feed distance`.

## Parameters

| CLDArray | Type | Description |
|---|---|---|
| CmdPrm.Int[-1] | Integer | Probing cycle type: Web probing value = 9 |
| CmdPrm.Int[-2] | Integer | SubCode of cycle specified in " SubCode for postprocessor " property on the `Job Assignment` tab |
| CmdPrm.Flt[-50] | Double | Feed distance, distance to start position of cycle |
| CmdPrm.Flt[-51] | Double | Depth, distance from top side to center of touch points |
| CmdPrm.Flt[-53] | Double | Width, distance from Touch point 1 to Touch point 2 |
| CmdPrm.Flt[-55] | Double | Top clearance, distance from top side |
| CmdPrm.Flt[-56] | Double | Side clearance, approach distance to touch point 1/ touch point 2 |
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
| CmdPrm.Flt[-200] | Double | First original touch point value along X-axis specified in the Job Assignment |
| CmdPrm.Flt[-201] | Double | First original touch point value along Y-axis specified in the Job Assignment |
| CmdPrm.Flt[-202] | Double | First original touch point value along Z-axis specified in the Job Assignment |
| CmdPrm.Flt[-203] | Double | First original target vector value along X-axis specified in the Job Assignment |
| CmdPrm.Flt[-204] | Double | First original target vector value along Y-axis specified in the Job Assignment |
| CmdPrm.Flt[-205] | Double | First original target vector value along Z-axis specified in the Job Assignment |
| CmdPrm.Flt[-206] | Double | Second original touch point value along X-axis specified in the Job Assignment |
| CmdPrm.Flt[-207] | Double | Second original touch point value along Y-axis specified in the Job Assignment |
| CmdPrm.Flt[-208] | Double | Second original touch point value along Z-axis specified in the Job Assignment |
| CmdPrm.Flt[-209] | Double | Second original target vector value along X-axis specified in the Job Assignment |
| CmdPrm.Flt[-210] | Double | Second original target vector value along Y-axis specified in the Job Assignment |
| CmdPrm.Flt[-211] | Double | Second original target vector value along Z-axis specified in the Job Assignment |
| CmdPrm.Flt[-66] | Integer | Compensate dimensions, retrurn values: 0 - Off, 1 - On |

## See also
- [Probing cycle (WProbing)](wprobing.md)
- [Extended cycle (EXTCYCLE)](../extcycle.md)
- [CLData access model](../../../cldata.md)
