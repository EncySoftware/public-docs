---
title: "Receiving assemblies from CAM system"
---

<link rel="stylesheet" href="assets/manual.css">

<div id="ht-wrap-container"><div class="ht-content" id="ht-content"><div class="ht-content-header"><h1 id="src-129933049">Receiving assemblies from CAM system</h1></div><div class="wiki-content sp-grid-section" data-index-for-search="true" id="main-content">
<p>The cell can be supplied as a whole 3D model. From which you need to extract the geometry of each mechanism separately and load them into MachineMaker. To simplify this operation, you can use CAM system.</p>
<p>Consider the process of transferring assemblies using the example of building a robot cell according to such a 3D model.</p>
<p><a class="doc-image-link" href="images/download/attachments/129933049/image2024-8-16_12-22-53.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129933049/image2024-8-16_12-22-53.png" class="confluence-embedded-image image-center doc-image doc-overview" height="896" src="images/download/attachments/129933049/image2024-8-16_12-22-53.png" style="--doc-image-width:800px" width="1268"/></a>
</p>
<p>In our case, the cell will consist of 3 mechanisms:</p>
<ul class=""><li class=""><p>Table;</p>
</li><li class=""><p>Robot;</p>
</li><li class=""><p>Spindle.</p>
</li></ul><p>Therefore, first the 3D model must be divided into these parts. Let's create groups under the same name and move the surfaces that belong to these mechanisms there.</p>
<p><a class="doc-image-link" href="images/download/attachments/129933049/perekidkafailov.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129933049/perekidkafailov.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="590" src="images/download/attachments/129933049/perekidkafailov.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
<div class="section section-1" id="src-129933049_id-.ReceivingassembliesfromCAMsystemv18-Simplifygeometry">
<h1 class="heading"><span>Simplify geometry</span></h1>
<p>The geometry of some mechanisms may be overly detailed which affects the file size, loading and rendering speed. To solve this problem you can use the simplification tool. By simplification we mean the removal (with a certain tolerance) of small faces or faces located inside the shell. A similar function works when importing geometry into MachineMaker (the function is described here: <a href="prepare-and-import-3d-objects.md">3D Models Simplifier</a>).</p>
<p>The function can be called using the context menu with the <i class=""><strong class="">"Simplify GeomModel..."</strong></i> command.</p>
<p><a class="doc-image-link" href="images/download/attachments/129933049/image2024-8-16_12-36-21.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129933049/image2024-8-16_12-36-21.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="363" src="images/download/attachments/129933049/image2024-8-16_12-36-21.png" style="--doc-image-width:283px" width="283"/></a>
</p>
<p>In this window, you can set the simplification parameters by choosing from ready-made options or by setting them manually.</p>
<p style="margin-left:30px;"><i class=""><strong class="">Solid size</strong></i> - specifies the maximum size of solids to be excluded.</p>
<p style="margin-left:30px;"><i class=""><strong class="">Face size</strong></i> - defines the maximum size of faces to be excluded.</p>
<p style="margin-left:30px;"><i class=""><strong class="">Face area</strong></i> - defines the minimum internal face area at which the face will be excluded.</p>
<p>The <i class=""><strong class="">Faces display</strong></i> parameters are responsible for the display modes of internal and external faces and help to visually control which faces will be excluded from the model.</p>
<p><a class="doc-image-link" href="images/download/attachments/129933049/Transparent.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129933049/Transparent.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="590" src="images/download/attachments/129933049/Transparent.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
</div>
<div class="section section-1" id="src-129933049_id-.ReceivingassembliesfromCAMsystemv18-SendingtoMachineMaker">
<h1 class="heading"><span>Sending to MachineMaker</span></h1>
<p>At this stage we begin to transfer the mechanisms to MachineMaker and assemble the cell.</p>
<p>To do this, call the context menu on the selected mechanism and click the <strong class=""><i class="">"Send to MachineMaker..."</i></strong> item.</p>
<p><a class="doc-image-link" href="images/download/attachments/129933049/image2024-8-16_12-47-33.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129933049/image2024-8-16_12-47-33.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-standard" height="573" src="images/download/attachments/129933049/image2024-8-16_12-47-33.png" style="--doc-image-width:547px" width="547"/></a>
</p>
<p><a class="doc-image-link" href="images/download/attachments/129933049/image2024-8-16_12-48-33.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129933049/image2024-8-16_12-48-33.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="235" src="images/download/attachments/129933049/image2024-8-16_12-48-33.png" style="--doc-image-width:372px" width="372"/></a>
</p>
<p>This form will appear. It allows you to set and edit the <i class=""><strong class="">base coordinate system</strong></i> relatively to which the mechanism will be located and <i class=""><strong class="">additional coordinate systems</strong></i> used for the positioning of the mechanism connectors.</p>
<p style="margin-left:30px;"><i class=""><strong class="">Add all possible CS <img alt="images/download/thumbnails/129933049/image2024-8-16_12-49-3.png" class="confluence-embedded-image confluence-thumbnail confluence-content-image-border doc-inline" src="images/download/thumbnails/129933049/image2024-8-16_12-49-3.png" style="--doc-image-width:25px" width="25"/>
</strong></i> - adds the base coordinate systems of neighboring mechanisms. Hovering the mouse cursor over them will show the silhouettes of the mechanisms associated with them.</p>
<p style="margin-left:30px;"><i class=""><strong class="">Ok</strong></i> - sends the 3D model with the set CS to MachineMaker.</p>
<p> <span style="color: #000000;">
<span style="color: #000000;">
When loading geometry into MachineMaker in the     </span>
<i class=""><strong class="">Import mechanism geometry</strong></i> <span style="color: #000000;">
 window, select the type of mechanism to be transferred from the drop-down list.    </span>
<br/> </span>
</p>
<p><a class="doc-image-link" href="images/download/attachments/129933049/image2024-8-16_12-50-14.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129933049/image2024-8-16_12-50-14.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="293" src="images/download/attachments/129933049/image2024-8-16_12-50-14.png" style="--doc-image-width:440px" width="534"/></a>
</p>
<p> <span style="color: #99cc00;">
<span style="color: #000000;">
<span style="color: #000000;">
After clicking     </span>
<i class=""><strong class="">Add</strong></i><strong class=""> </strong> <span style="color: #000000;">
button, the mechanism will be added to the scene and you will be able to    </span>
<a href="assemblies.md">get started with cell assembly</a>.<br/> </span>
</span>
</p>
<p> <span style="color: #99cc00;">
<span style="color: #000000;">
<span style="color: #000000;">
Let's start from the Robot mechanism.    </span>
<br/> </span>
</span>
</p>
</div>
<div class="section section-1" id="src-129933049_id-.ReceivingassembliesfromCAMsystemv18-Robot">
<h1 class="heading"><span>Robot</span></h1>
<p>Let's set the base coordinate system <i class=""><strong class="">BaseCS</strong> </i>- this will be the location of the mechanism on the floor. Next set an additional coordinate system <i class=""><strong class="">AdditionalCS</strong></i>, the point to which the next mechanism will be attached. In our case, this is Spindle.</p>
<p><a class="doc-image-link" href="images/download/attachments/129933049/sendtommrobot.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129933049/sendtommrobot.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="590" src="images/download/attachments/129933049/sendtommrobot.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
<p>Finally send it to MachineMaker. In the <i class=""><strong class="">Import mechanism geometry</strong></i> window, select the type of mechanism - <strong class=""><i class="">Robot</i></strong>. Verify that MachineMaker is in <i class=""><strong class="">Robot Cell </strong></i>context mode <img alt="images/download/thumbnails/129933049/image2022-4-21_16-44-0.png" class="confluence-embedded-image confluence-thumbnail confluence-content-image-border doc-inline" src="images/download/thumbnails/129933049/image2022-4-21_16-44-0.png" style="--doc-image-width:120px" width="120"/>
</p>
<p><a class="doc-image-link" href="images/download/attachments/129933049/image2022-4-21_16-42-32.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129933049/image2022-4-21_16-42-32.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="265" src="images/download/attachments/129933049/image2022-4-21_16-42-32.png" style="--doc-image-width:440px" width="535"/></a>
</p>
</div>
<div class="section section-1" id="src-129933049_id-.ReceivingassembliesfromCAMsystemv18-Spindle">
<h1 class="heading"><span>Spindle</span></h1>
<p>Working with the spindle is very similar to the above. The base coordinate system specifies the point of attachment to the <i class=""><strong class="">AdditionalCS</strong> </i>of the robot and the additional coordinate system specifies the point of attachment of the tool. After sending to MachineMaker, you need to select the type of mechanism to load - <i class=""><strong class="">End effector</strong></i>. If the coordinate systems are correct, then the spindle will automatically join the sixth axis of the robot. In any case, you can manually correct the connection.</p>
<p><strong class=""><a class="doc-image-link" href="images/download/attachments/129933049/sendtommspindle.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129933049/sendtommspindle.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="590" src="images/download/attachments/129933049/sendtommspindle.webp" style="--doc-image-width:800px" width="800"/></a>
<br/></strong></p>
</div>
<div class="section section-1" id="src-129933049_id-.ReceivingassembliesfromCAMsystemv18-Table">
<h1 class="heading"><span>Table</span></h1>
<p>The base coordinate system of the table is responsible for the location on the floor, and the additional coordinate systems is used for the placement of other mechanisms. You can any have any number of additional CSs. In our case, the additional coordinate system will be automatically set in the robot's <i class=""><strong class="">BaseCS</strong></i>.</p>
<p>Finally select the type of mechanism - <i class=""><strong class="">Table(fixed)</strong></i><strong class=""> </strong>in MachineMaker. Then place the robot on the table.</p>
<p><a class="doc-image-link" href="images/download/attachments/129933049/sendtommtable.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129933049/sendtommtable.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="590" src="images/download/attachments/129933049/sendtommtable.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
</div>
</div></div></div>
