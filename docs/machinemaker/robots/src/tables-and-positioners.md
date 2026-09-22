---
title: "Tables and Positioners"
---

<link rel="stylesheet" href="assets/manual.css">

<div id="ht-wrap-container"><div class="ht-content" id="ht-content"><div class="ht-content-header"><h1 id="src-129930810">Tables and Positioners</h1></div><div class="wiki-content sp-grid-section" data-index-for-search="true" id="main-content">
<p>MachineMaker allows you to create static tables, 1-axis positioners and 2-axes positioners.</p>
<p><a class="doc-image-link" href="images/download/attachments/129930810/image2022-4-5_15-30-58.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930810/image2022-4-5_15-30-58.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-standard" height="551" src="images/download/attachments/129930810/image2022-4-5_15-30-58.png" style="--doc-image-width:640px" width="925"/></a>
</p>
<div class="section section-1" id="src-129930810_id-.TablesandPositionersv18-Tables">
<h1 class="heading"><span>Tables</span></h1>
<p>Table is a fixed (static) object which can hold a workpiece or any another object (including robots or another table).</p>
<p>It is possible to add any number of connectors to the table using <img alt="images/download/thumbnails/129930810/image2024-2-9_16-4-0.png" class="confluence-embedded-image confluence-thumbnail doc-inline" height="27" src="images/download/thumbnails/129930810/image2024-2-9_16-4-0.png" style="--doc-image-width:26px"/>
<strong class=""> </strong>button in the <i class=""><strong class="">User</strong></i> <i class=""><strong class="">Coordinate Systems</strong></i><strong class=""> </strong>panel. Use <img alt="images/download/thumbnails/129930810/image2024-2-9_16-4-15.png" class="confluence-embedded-image confluence-thumbnail doc-inline" height="28" src="images/download/thumbnails/129930810/image2024-2-9_16-4-15.png" style="--doc-image-width:26px"/>
 button to delete the connector. Use double click to rename the coordinate system.</p>
<p>Hold down <i class=""><strong class="">Left Control</strong></i><strong class=""> </strong>key and use drag&amp;drop to place the connector in the correct position; it is also possible to specify the connector's position by changing dimensions or the date in the Transformation Panel, for details see "Transformation panel". You can also select the type of added connector assembly equipment or workpiece.</p>
<p>MachineMaker will use connectors to connect mechanisms with each other when building <strong class="">Assemblies</strong>. All empty connectors will be converted into Workpiece holders for CAM system.</p>
<p><a class="doc-image-link" href="images/download/attachments/129930810/image2024-2-9_16-2-46.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930810/image2024-2-9_16-2-46.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-standard" height="847" src="images/download/attachments/129930810/image2024-2-9_16-2-46.png" style="--doc-image-width:640px" width="952"/></a>
</p>
<p>There is a big difference between Fixed Tables and Fixed Objects. A Fixed Object is a standalone static object, it is impossible to place a robot on a Fixed Object. So, Fixed Objects do not have any connectors. Use Fixed Objects option for robot controllers, standalone boxes located in the robot cell, fences and so on. Use Fixed Tables for tables holding robots and workpieces, floors and so on.</p>
<p><a class="doc-image-link" href="images/download/attachments/129930810/image2022-4-5_16-12-3.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930810/image2022-4-5_16-12-3.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-standard" height="731" src="images/download/attachments/129930810/image2022-4-5_16-12-3.png" style="--doc-image-width:604px" width="604"/></a>
</p>
</div>
<div class="section section-1" id="src-129930810_id-.TablesandPositionersv18-1-axispositioner">
<h1 class="heading"><span>1-axis positioner</span></h1>
<p>1-axis positioner has one rotary joint and an unlimited number of connectors. It is possible to add new connectors using<strong class=""> <img alt="images/download/attachments/129930810/image2022-4-5_15-45-7.png" class="confluence-embedded-image doc-inline" src="images/download/attachments/129930810/image2022-4-5_15-45-7.png" style="--doc-image-width:16px"/>
</strong>button in the <i class=""><strong class="">User</strong></i> <i class=""><strong class="">Coordinate Systems</strong></i><strong class=""> </strong>panel.</p>
<p><a class="doc-image-link" href="images/download/attachments/129930810/image2022-4-5_16-18-2.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930810/image2022-4-5_16-18-2.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-standard" height="408" src="images/download/attachments/129930810/image2022-4-5_16-18-2.png" style="--doc-image-width:640px" width="874"/></a>
</p>
</div>
<div class="section section-1" id="src-129930810_id-.TablesandPositionersv18-2-axespositioner">
<h1 class="heading"><span>2-axes positioner</span></h1>
<p>2-axes positioner has 2 rotary joints and an unlimited number of connectors. It is possible to add new connectors using<strong class=""> <img alt="images/download/attachments/129930810/image2022-4-5_15-45-7.png" class="confluence-embedded-image doc-inline" src="images/download/attachments/129930810/image2022-4-5_15-45-7.png" style="--doc-image-width:16px"/>
</strong>button in the <i class=""><strong class="">User</strong></i> <i class=""><strong class="">Coordinate Systems</strong></i><strong class=""> </strong>panel.</p>
<p><a class="doc-image-link" href="images/download/attachments/129930810/image2022-4-5_16-22-47.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930810/image2022-4-5_16-22-47.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-standard" height="575" src="images/download/attachments/129930810/image2022-4-5_16-22-47.png" style="--doc-image-width:640px" width="1000"/></a>
</p>
</div>
</div></div></div>
