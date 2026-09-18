---
title: "Parts Mode"
---

<link rel="stylesheet" href="assets/manual.css">

<div id="ht-wrap-container"><div class="ht-content"><div class="ht-content-header"><h1 id="src-150697513"> <span>Parts Mode</span></h1></div><div class="wiki-content sp-grid-section" data-index-for-search="true" id="main-content">
<p><img alt="Parts mode with the parts list, robotic cell, and cylinder properties" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697513/parts-mode-2026-09-16.png" width="800"/>
</p>
<div class="section section-1" id="src-150697513_safe-id-aWQtLlBhcnRzTW9kZXYxLUFwcGxpY2F0aW9uQXJlYTo">
<h1 class="heading"><span>Application Area:</span></h1>
<p>The Part mode allows you to add a model or create it from primitives, as well as place them in the <strong class="">tray</strong>.</p>
<div class="section section-2" id="src-150697513_id-.PartsModev1-Import.">
<h2 class="heading"><span>Import.</span></h2>
<details class="scroll-expand-container"><summary class="scroll-expand-control">Click here to expand..</summary><div class="scroll-expand-content">
<p>It allows you to load a 3D model of the product.</p>
<p><strong class="">Type. </strong>Сylinder, Box, or 3D model.</p>
<p><strong class="">ustom file. </strong>It allows you to reselect the model.</p>
<p><strong class="">Stacking offset. </strong>The parameter determines the vertical alignment relationship between stacked components.</p>
<p>Value = 0: parts are positioned directly atop one another without overlap.</p>
<p>Value &gt; 0: defines the insertion depth for mating parts (e.g., in LEGO‑like interlocking mechanisms, this would equal the height of the connecting cylinder).</p>
<p><strong class="">Base point/ Pick point. </strong>The reference point for placement /<strong class=""> </strong>The gripping point on the part.</p>
<ul class=""><li class=""><p>Unlimited pick and base points can be created.</p>
</li><li class=""><p>Each point supports editing, deletion, and renaming.</p>
</li><li class=""><p>Coordinates can be input manually or selected via model interaction.</p>
</li><li class=""><p>A gripper visualization aids pick point definition, showing the robot’s actual gripping posture.</p>
</li></ul><p><strong class="">Name pont. </strong>Assigns a name to an existing point</p>
<p><strong class=""> <span style="color: #000000;">
Add/Delete a point.     </span>
</strong> <span style="color: #000000;">
Allows you to create/delete a point that is added to the <strong class="">list of points.</strong> </span>
</p>
<p> <span style="color: #000000;">
<strong class="">List of points. </strong>View point names    </span>
</p>
<p> <span style="color: #000000;">
<strong class=""><strong class=""><img alt="List of base points with add and delete buttons" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697513/list-of-points-2026-09-16.png" width="272"/>
</strong><br/></strong> </span>
</p>
<p> <span style="color: #000000;">
<strong class="">X,Y,Z,Rx,Ry,Rz,A,B,C</strong> - Fields for spatial orientation of the point.    </span>
</p>
</div></details>
</div>
<div class="section section-2" id="src-150697513_id-.PartsModev1-Addpart.">
<h2 class="heading"><span>Add part.</span></h2>
<details class="scroll-expand-container"><summary class="scroll-expand-control">Click here to expand..</summary><div class="scroll-expand-content">
<p>It allows you to create a model from primitives. In this template, some parameters are identical to those in <strong class="">Import - 3D model.</strong></p>
<p><strong class="">Сylinder.</strong></p>
<p><strong class="">Diameter. </strong>Distance across the circular base, through the center</p>
<p><strong class="">Height. </strong>Distance between the two bases along the axis</p>
<p><strong class="">Box.</strong></p>
<p><strong class="">Width.</strong> <span style="color: #000000;">
Defines the width    </span>
</p>
<p><strong class="">Depth. </strong> <span style="color: #000000;">
Defines the depth    </span>
</p>
<p><strong class="">Height. </strong> <span style="color: #000000;">
Defines the height    </span>
</p>
</div></details>
</div>
<div class="section section-2" id="src-150697513_id-.PartsModev1-Filterbytray.">
<h2 class="heading"><span>Filter by tray.</span></h2>
<p>It allows you to select a specific tray for work.</p>
</div>
<div class="section section-2" id="src-150697513_id-.PartsModev1-Listofparts">
<h2 class="heading"><span>List of parts</span></h2>
<p>It displays a list of parts for moving and allows you to edit them.</p>
<details class="scroll-expand-container"><summary class="scroll-expand-control">Click here to expand..</summary><div class="scroll-expand-content">
<p><img alt="images/download/attachments/150697513/image2025-11-14_16-36-43.png" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697513/image2025-11-14_16-36-43.png" width="182"/>
</p>
<p>Clicking the part opens a window where you can:</p>
<ol class=""><li class=""><p>View model name</p>
</li><li class=""><p>Edit model</p>
</li><li class=""><p>Delete model</p>
</li><li class=""><p>Show base and pick points</p>
</li><li class=""><p>Rotate model (preview)</p>
</li></ol> </div></details>
</div>
<div class="section section-2" id="src-150697513_id-.PartsModev1-Workspecifics">
<h2 class="heading"><span>Work specifics</span></h2>
<p>In this mode, place the parts in their initial positions.</p>
<details class="scroll-expand-container"><summary class="scroll-expand-control">Click here to expand..</summary><div class="scroll-expand-content">
<p>To position the parts in the tray:</p>
<ul class=""><li class=""><p>Select the required part in the parts tree.</p>
</li><li class=""><p>In the graphics window, choose the attachment point.</p>
</li><li class=""><p>The selected part will appear in this position.</p>
</li></ul><p><img alt="Cylinder placed at a tray attachment point in Parts mode" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697513/place-cylinder-2026-09-16.png" width="444"/>
</p>
<p>The position where a part is already installed (attachment point) changes its color to indicate that the slot is occupied.</p>
<p>To <strong class="">remove</strong> a part from its position, simply click on the attachment point where the part is located.</p>
<p>To add <strong class="">multiple parts</strong> at once, <strong class="">press and hold the left mouse button</strong>. A dialog box will then appear, prompting you to add this part to the entire tray.</p>
<div class="manual-image-pair">
<div style="flex:0 0 auto;"><img alt="images/download/attachments/150697513/image2025-11-19_9-20-19.png" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697513/image2025-11-19_9-20-19.png" width="549"/></div>
<div style="flex:0 0 auto;"><img alt="Tray filled with cylinders next to an empty tray" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697513/filled-tray-2026-09-16.png" width="286"/></div>
</div>
<p><br/>The same mechanism applies to removing parts from the tray.</p>
</div></details>
</div>
</div>
</div></div></div>
