---
title: "Cell Mode"
---

<link rel="stylesheet" href="assets/manual.css">

<div id="ht-wrap-container"><div class="ht-content"><div class="ht-content-header"><h1 id="src-150697487"> <span>Cell Mode</span></h1></div><div class="wiki-content sp-grid-section" data-index-for-search="true" id="main-content">
<p><img alt="Cell mode with the object tree on the left and the robotic cell in the graphics window" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697487/cell-mode-2026-09-16.png" width="800"/>
</p>
<div class="section section-1" id="src-150697487_safe-id-aWQtLkNlbGxNb2RldjEtQXBwbGljYXRpb25BcmVhOg">
<h1 class="heading"><span>Application Area:</span></h1>
</div>
<div class="section section-1" id="src-150697487_safe-id-aWQtLkNlbGxNb2RldjEtVGhpc21vZHVsZWVuYWJsZXNlZGl0aW5nb2Z0aGVkaWdpdGFsdHdpbm9mdGhlcm9ib3RpY2NlbGwsaW5jbHVkaW5ndGhlYWRkaXRpb25hbmRzcGF0aWFsYXJyYW5nZW1lbnRvZm1lY2hhbmlzbXNpbmEzRGVudmlyb25tZW50Lg">
<p>This module enables editing of the digital twin of the robotic cell, including the addition and spatial arrangement of mechanisms in a 3D environment.</p>
<div class="section section-2" id="src-150697487_id-.CellModev1-Addobject.">
<h2 class="heading"><span>Add object. </span></h2>
<p>At the top‑left position of the interface, you will locate the <strong class="">Add Object</strong> button. This functionality serves as the primary creation tool, enabling the user to incorporate various mechanisms into the workspace. These may include, but are not limited to: tables, boxes, machines, or any other entities with which the robot is designed to interact.</p>
<details class="scroll-expand-container"><summary class="scroll-expand-control">Click here to expand..</summary><div class="scroll-expand-content">
<p><strong class="">Work with mechanisms:</strong></p>
<details class="scroll-expand-container"><summary class="scroll-expand-control">Click here to expand..</summary><div class="scroll-expand-content">
<p><strong class="">Name. </strong>Mechanism name.</p>
<p><strong class="">Width. </strong>Allows you to change the width of the mechanism.</p>
<p><strong class="">Depth. </strong>Allows you to change the depth of the mechanism.</p>
<p><strong class="">Height. </strong>Allows you to change the height of the mechanism.</p>
<p><strong class="">The component creation window will change depending on what you are trying to create.</strong></p>
<p><strong class="">Type of mechanism. </strong>Types of mechanisms for product placement.</p>
<p><strong class="">Box. </strong>The mechanism is presented in the form of a box/tray.</p>
<p><img alt="Box mechanism" class="confluence-embedded-image confluence-thumbnail manual-image manual-screenshot" src="images/download/attachments/150697487/box-2026-09-16.png" width="196"/>
</p>
<p><strong class="">Table. </strong>The mechanism is presented in the form of a table for placing products.</p>
<p><strong class=""><img alt="Table mechanism" class="confluence-embedded-image confluence-thumbnail manual-image manual-screenshot" src="images/download/attachments/150697487/table-2026-09-16.png" width="267"/>
</strong></p>
<p><strong class="">Mill. </strong>The mechanism is presented in the form of a simplified model of a machine for placing products.</p>
<p><img alt="Mill mechanism" class="confluence-embedded-image confluence-thumbnail manual-image manual-screenshot" src="images/download/attachments/150697487/mill-2026-09-16.png" width="276"/>
</p>
<p><strong class="">Back wall. </strong>Rear structural panel.</p>
<p><strong class="">Wall thikness. </strong>Thickness of enclosure walls.</p>
<p><strong class="">Door parameters. </strong>Specifications of access door.</p>
<p><strong class="">Chuck height. </strong>Vertical dimension of the chuck.</p>
<p><strong class="">Chuck diameter. </strong>Outer diameter of the chuck.<strong class=""></strong></p>
<p><strong class="">Chuck positions. </strong>Available mounting/operating positions of the chuck.</p>
<p><strong class="">Empty. </strong>The mechanism does not have a 3D component</p>
<p>When the <strong class="">Apply</strong> button is clicked, the mechanism is added to the component tree, and a second menu opens to edit its position in space. In the component tree, placement positions (<strong class="">tray</strong>) also appear.</p>
<p><img alt="images/download/thumbnails/150697487/image2025-11-19_9-15-42.png" class="confluence-embedded-image confluence-thumbnail manual-image manual-screenshot" src="images/download/thumbnails/150697487/image2025-11-19_9-15-42.png" width="254"/>
</p>
<p><strong class=""><strong class=""><img alt="images/download/thumbnails/150697487/image2025-11-12_15-23-42.png" class="confluence-embedded-image confluence-thumbnail manual-image manual-screenshot" src="images/download/thumbnails/150697487/image2025-11-12_15-23-42.png" width="264"/>
</strong></strong></p>
<p>The menu includes the following items:</p>
<p><strong class="">Name</strong>. Mechanism name.</p>
<p><strong class="">Position. </strong>Modify the component’s position with respect to either the <strong class="">world coordinate system</strong> or the <strong class="">robot’s BaseCS</strong>.</p>
<p><strong class="">X,Y,Z,Rx,Ry,Rz,A,B,C</strong> - Fields for spatial orientation of the mechanism.</p>
<p>In the lower‑right part of the screen, the component navigation mechanism appears. Allows interactive spatial manipulation of the mechanism.</p>
<p>In this window, you can also <strong class="">delete</strong> the mechanism or <strong class="">close</strong> the window to continue working on the project.</p>
</div></details>
<p><strong class="">Work with Tray.</strong></p>
<details class="scroll-expand-container"><summary class="scroll-expand-control">Click here to expand..</summary><div class="scroll-expand-content">
<p>Item location. Each mechanism has at least one drawer.<strong class=""><br/></strong></p>
<p><img alt="images/download/thumbnails/150697487/image2025-11-19_9-16-11.png" class="confluence-embedded-image confluence-thumbnail manual-image manual-screenshot" src="images/download/thumbnails/150697487/image2025-11-19_9-16-11.png" width="174"/>
</p>
<p><strong class="">Name.</strong> Tray name.</p>
<p><strong class="">Zoom extents. </strong>It scales the view so that all objects (<strong class="">Tray</strong>) fit entirely within the viewing window.</p>
<p><strong class="">Pick or Place point.</strong> Allows setting attachment points for the product.</p>
<p><strong class="">None. </strong>In No‑Point mode, no point needs to be set. Useful for creating collision‑control mechanisms (e.g., fences, barriers).</p>
<p><img alt="Barrier mechanism in No-Point mode" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697487/no-point-mode-2026-09-16.png" width="323"/>
</p>
<p><strong class="">Single Point. </strong>It allows you to specify one mounting point.</p>
<p><strong class="">Position. </strong>Modify the component’s position with respect to either the world coordinate system or the robot’s BaseCS. <strong class="">This position is typically calibrated on a physical robot</strong>, and the point(s) are then transferred via coordinates into the system while the <strong class="">Position</strong> - <strong class="">Robot’s BaseCS</strong> is enabled.</p>
<p><strong class="">Transform parent. </strong>This function works only in <strong class="">Position</strong> — <strong class="">Robot’s BaseCS</strong> mode. When enabled, changing the <strong class="">Tray</strong> position also adjusts the mechanism’s position. When disabled, only the <strong class="">Tray</strong> position changes.</p>
<p><strong class="">X,Y,Z,Rx,Ry,Rz,A,B,C</strong> - Fields for spatial orientation of the tray.</p>
<p><strong class="">Stack levels.</strong> It allows you to create an array of points along the height axis.</p>
<p><img alt="images/download/thumbnails/150697487/image2025-11-14_12-48-40.png" class="confluence-embedded-image confluence-thumbnail manual-image manual-screenshot" src="images/download/thumbnails/150697487/image2025-11-14_12-48-40.png" width="300"/>
<img alt="images/download/attachments/150697487/image2025-11-14_12-49-15.png" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697487/image2025-11-14_12-49-15.png" width="329"/>
</p>
<p>In the lower‑right part of the screen, the component navigation mechanism appears. Allows interactive spatial manipulation of the mechanism.</p>
<p><strong class="">Two dimensional array. </strong>It allows you to create a two‑dimensional array. In this template, some parameters are identical to those in <strong class="">Single Point</strong>.</p>
<p><strong class=""><img alt="images/download/attachments/150697487/image2025-11-14_12-51-4.png" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697487/image2025-11-14_12-51-4.png" width="309"/>
</strong></p>
<p><strong class="">Rows. </strong>Number of horizontal rows in the array</p>
<p><strong class="">Columns. </strong>Number of vertical columns in the array</p>
<p><strong class="">Step X. </strong>Horizontal spacing (distance between column centers).</p>
<p><strong class="">Step Y. </strong>Vertical spacing (distance between row centers).</p>
<p><strong class="">Round array. </strong>It allows you to create a circular array. In this template, some parameters are identical to those in <strong class="">Single Point</strong>.</p>
<p><img alt="images/download/attachments/150697487/image2025-11-14_12-51-29.png" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697487/image2025-11-14_12-51-29.png" width="338"/>
</p>
<p><strong class="">Points. </strong>Number of points around the circle.</p>
<p><strong class="">Radius. </strong>Distance from center to each point.</p>
<p><strong class="">DXF. </strong>It allows you to import DXF‑format drawings. The point can be placed within a <strong class="">closed contour</strong>, which will serve as a workpiece holder.</p>
<p>In this template, some parameters are identical to those in <strong class="">Single Point</strong>.</p>
<p><img alt="images/download/attachments/150697487/image2025-11-14_14-52-24.png" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697487/image2025-11-14_14-52-24.png" width="346"/>
<img alt="images/download/attachments/150697487/image2025-11-14_14-47-47.png" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697487/image2025-11-14_14-47-47.png" width="333"/>
</p>
<p><strong class="">Custom file</strong>. It allows you to reselect the model.</p>
</div></details>
</div></details>
</div>
<div class="section section-2" id="src-150697487_id-.CellModev1-TreeofMechanisms.">
<h2 class="heading"><span>Tree of Mechanisms. </span></h2>
<p>Structured list of all elements in your cell.</p>
<ol class=""><li class=""><p>Each mechanism is assigned a unique name, which may be renamed unless the mechanism is locked.</p>
</li><li class=""><p>All mechanisms include tray by default; these may be disregarded if not required for the current task.</p>
</li><li class=""><p>Mechanisms and tray originate from one of two sources:</p>
</li></ol><ul class=""><li class=""><p>predefined entries in the <tt class="Markdown-Word">.mma</tt> cell file (supplied by the vendor);</p>
</li><li class=""><p>user‑generated entries created manually.</p>
</li></ul>
</div>
</div>
</div></div></div>
