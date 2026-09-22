---
title: "Additional options"
---

<link rel="stylesheet" href="assets/manual.css">

<div id="ht-wrap-container"><div class="ht-content" id="ht-content"><div class="ht-content-header"><h1 id="src-129936331">Additional options</h1></div><div class="wiki-content sp-grid-section" data-index-for-search="true" id="main-content">
<p>Robot controller can use external axes and it is necessary to assign correct positions (indices) for these axes in the assembly. Default CAM-system postprocessors use index-based axes identifiers (<strong class="">ExtAxis1Pos</strong> for the first axis, <strong class="">ExtAxis2Pos</strong> etc). Some custom postprocessors can use axis address instead of indices (<strong class="">E1, E2, E3, J4</strong> etc).</p>
<p>Click <img alt="images/download/attachments/129936331/button.PNG" class="confluence-embedded-image doc-inline" src="images/download/attachments/129936331/button.PNG" style="--doc-image-width:50px"/>
     button to open the Assembly parameters panel. Then go to the <i class=""><strong class="">Axes</strong></i> tab.</p>
<p><a class="doc-image-link" href="images/download/attachments/129936331/image2023-11-29_10-53-11.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129936331/image2023-11-29_10-53-11.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="1239" src="images/download/attachments/129936331/image2023-11-29_10-53-11.png" style="--doc-image-width:430px" width="430"/></a>
</p>
<ul class=""><li class=""><p>Address - axis designation.</p>
</li><li class=""><p>Control:</p>
</li></ul><ol class=""><li class=""><p>Countinuous.</p>
</li><li class=""><p>Indexed - indicates that rotation will be carried out incrementally.</p>
</li><li class=""><p>Manual - implies that the operation is entirely manual.</p>
</li></ol><ul class=""><li class=""><p>Shortest path rotation - refers to the rotation around an axis or point using the most direct path between the initial and final positions in three-dimensional space.</p>
</li><li class=""><p>Scale is a setting with four positions. Each position corresponds to a specific angular increment. Position 1 equals 90 degrees, Position 2 equals 180 degrees, and so on.</p>
</li></ul><p>Define <strong class="">Address </strong>and <strong class="">External axis position (index) </strong>here. MachineMaker will show axis identifier (like ExtAxis3Pos) in tooltip. You can use it in the postprocessor.</p>
<p><a class="doc-image-link" href="images/download/attachments/129936331/Address.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129936331/Address.png" class="confluence-embedded-image image-center doc-image doc-detail" height="281" src="images/download/attachments/129936331/Address.png" style="--doc-image-width:314px" width="314"/></a>
</p>
<p>Axis address and axis index must be unique in the assembly context. If you try to set use a value that has been already taken, MachineMaker will propose to replace the existing one.</p>
<p>It is not possible to change the robot axis address and index. You can change external addresses only.</p>
<p>It is also possible to define additional axes parameters here: <strong class="">Control type (Continues, Indexed, Manual)</strong>, <strong class="">Brakes </strong>and <strong class="">Shortest path rotation mode.</strong></p>
</div></div></div>
