---
title: "Assemblies"
---

<link rel="stylesheet" href="assets/manual.css">

<div id="ht-wrap-container"><div class="ht-content" id="ht-content"><div class="ht-content-header"><h1 id="src-129931045">Assemblies</h1></div><div class="wiki-content sp-grid-section" data-index-for-search="true" id="main-content">
<div class="section section-1" id="src-129931045_id-.Assembliesv18-Connectors">
<h1 class="heading"><span>Connectors</span></h1>
<p>Each mechanism or object has at least one connector. It is possible to connect two mechanisms using their connectors.</p>
<p>A robot always has 2 connectors: first one at the base coordinate system (3) and the second one at the flange (4).</p>
<p>A table has at least 2 connectors: at the base (1) and at the table top (2).</p>
<p>End effector has one connector at the base (5).</p>
<p>It is possible to place the robot on the table by linking the robot connector (3) to the table connector (2). It is also possible to place an end effector on the robot flange by linking the end effector connector to the robot flange connector.</p>
<p><a class="doc-image-link" href="images/download/attachments/129931045/image2021-5-6_15-38-13.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129931045/image2021-5-6_15-38-13.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-standard" height="339" src="images/download/attachments/129931045/image2021-5-6_15-38-13.png" style="--doc-image-width:640px" width="735"/></a>
</p>
<p>A table can hold several mechanisms. If this is the case, it must have several connectors.</p>
<p><a class="doc-image-link" href="images/download/attachments/129931045/image2021-5-6_15-42-51.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129931045/image2021-5-6_15-42-51.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-standard" height="705" src="images/download/attachments/129931045/image2021-5-6_15-42-51.png" style="--doc-image-width:640px" width="1012"/></a>
All empty connectors will be used as workpiece connectors in CAM system.</p>
<p><a class="doc-image-link" href="images/download/attachments/129931045/image2021-5-6_15-57-35.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129931045/image2021-5-6_15-57-35.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-standard" height="1340" src="images/download/attachments/129931045/image2021-5-6_15-57-35.png" style="--doc-image-width:640px" width="1542"/></a>
</p>
</div>
<div class="section section-1" id="src-129931045_id-.Assembliesv18-Managetableconnectors">
<h1 class="heading"><span>Manage table connectors</span></h1>
<p>It is possible to add several connectors. Create a new table or edit an existing one and open the <a class="external-link" href="https://kb.sprutcam.com/display/MMUMAU15/Build+kinematic+schema">kinematics panel</a>. You can check <i class=""><strong class="">User coordinate systems</strong></i><strong class=""> </strong>panel to manage connectors.</p>
<p><a class="doc-image-link" href="images/download/attachments/129931045/image2024-2-9_16-26-44.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129931045/image2024-2-9_16-26-44.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="382" src="images/download/attachments/129931045/image2024-2-9_16-26-44.png" style="--doc-image-width:404px" width="404"/></a>
</p>
<p>Use <img alt="images/download/attachments/129931045/image2024-2-9_16-30-13.png" class="confluence-embedded-image confluence-content-image-border doc-inline" src="images/download/attachments/129931045/image2024-2-9_16-30-13.png" style="--doc-image-width:22px"/>
 button to add a new connector.</p>
<p><a class="doc-image-link" href="images/download/attachments/129931045/image2024-2-9_16-28-49.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129931045/image2024-2-9_16-28-49.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="385" src="images/download/attachments/129931045/image2024-2-9_16-28-49.png" style="--doc-image-width:414px" width="414"/></a>
</p>
<p>Click on a connector to select it. It is also possible to select a connector in 3D View. Double-click on the connector name to modify it. Use <i class=""><strong class="">Enter</strong></i><strong class=""> </strong>key to validate the new name and <i class=""><strong class="">Esc</strong></i><strong class=""> </strong>key to cancel.</p>
<p><a class="doc-image-link" href="images/download/attachments/129931045/manage_table_connectors_3.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129931045/manage_table_connectors_3.png" class="confluence-embedded-image image-center doc-image doc-detail" height="377" src="images/download/attachments/129931045/manage_table_connectors_3.png" style="--doc-image-width:411px" width="411"/></a>
</p>
<p>Use <img alt="images/download/attachments/129931045/image2024-2-9_16-30-44.png" class="confluence-embedded-image doc-inline" src="images/download/attachments/129931045/image2024-2-9_16-30-44.png" style="--doc-image-width:22px"/>
 button to delete the connector.</p>
<div class="confbox admonition admonition-note">
<span class="admonition-icon confluence-information-macro-icon"></span>
<div class="admonition-body">
<p> <span style="color: #333333;">
A table must have at least one connector (user CS), so it is impossible to delete the last one.    </span>
</p>
</div>
</div>
<p>It is possible to change connector position using <a href="building-a-kinematic-scheme.md">transformation panel, dimensions or drag&amp;drop</a>.</p>
</div>
<div class="section section-1" id="src-129931045_id-.Assembliesv18-Connectmechanismstoassembly">
<h1 class="heading"><span>Connect mechanisms to assembly</span></h1>
<p>Hold down <i class=""><strong class="">Left Ctrl</strong></i><strong class=""> </strong>key in Assembly view to show all connectors. Empty connectors will be shown as red dots and busy connectors will be shown as green dots.</p>
<p><a class="doc-image-link" href="images/download/attachments/129931045/image2023-10-27_14-37-9.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129931045/image2023-10-27_14-37-9.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-standard" height="781" src="images/download/attachments/129931045/image2023-10-27_14-37-9.png" style="--doc-image-width:640px" width="1077"/></a>
</p>
<p>Click on a busy connector (green dot) to break the connection between mechanisms.</p>
<p>Hold down <i class=""><strong class="">Left <i class=""><strong class="">Crtl</strong></i><strong class=""> </strong></strong></i>key, drag any mechanism and drop onto to another one. MachineMaker will show a sticky arrow between linking connectors.</p>
<p><a class="doc-image-link" href="images/download/attachments/129931045/linkunlink21323.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129931045/linkunlink21323.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="590" src="images/download/attachments/129931045/linkunlink21323.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
<div class="confbox admonition admonition-tip">
<span class="admonition-icon confluence-information-macro-icon"></span>
<div class="admonition-body">
<p style="text-align:center;"> <span style="color: #333333;">
Use     </span>
<i class=""><strong class="">Left Alt</strong></i><strong class=""> </strong> <span style="color: #333333;">
key to use drag and drop function without snapping mechanisms to each other.    </span>
</p>
</div>
</div>
</div>
<div class="section section-1" id="src-129931045_id-.Assembliesv18-Usingassemblytree">
<h1 class="heading"><span>Using assembly tree</span></h1>
<p>Assembly tree shows all mechanisms and connectors.</p>
<p><a class="doc-image-link" href="images/download/attachments/129931045/image2023-10-27_14-46-20.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129931045/image2023-10-27_14-46-20.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-standard" height="616" src="images/download/attachments/129931045/image2023-10-27_14-46-20.png" style="--doc-image-width:640px" width="904"/></a>
</p>
<p>It is possible to use Drag&amp;Drop in the assembly tree. Drag Kuka Robot and drop it to the <i class=""><strong class="">Mechanisms</strong></i><strong class=""> </strong>node to unlink it from the Rail.</p>
<p><a class="doc-image-link" href="images/download/attachments/129931045/unlink4erezderevo.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129931045/unlink4erezderevo.gif" class="confluence-embedded-image image-center doc-image doc-overview" height="590" src="images/download/attachments/129931045/unlink4erezderevo.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
<p>Drag Kuka Robot and drop it to the Rail node to connect mechanisms again.</p>
<p><a class="doc-image-link" href="images/download/attachments/129931045/narail.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129931045/narail.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="568" src="images/download/attachments/129931045/narail.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
<p>Use <img alt="images/download/attachments/129931045/image2024-2-9_16-34-47.png" class="confluence-embedded-image doc-inline" height="24" src="images/download/attachments/129931045/image2024-2-9_16-34-47.png" style="--doc-image-width:36px" width="36"/>
 button to switch mechanism visibility.</p>
<p><a class="doc-image-link" href="images/download/attachments/129931045/visibilityli.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129931045/visibilityli.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="511" src="images/download/attachments/129931045/visibilityli.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
<p>Use <img alt="images/download/attachments/129931045/image2024-2-9_16-35-17.png" class="confluence-embedded-image doc-inline" src="images/download/attachments/129931045/image2024-2-9_16-35-17.png" style="--doc-image-width:28px"/>
 button to delete a mechanism.</p>
<div class="confbox admonition admonition-warning">
<span class="admonition-icon confluence-information-macro-icon"></span>
<div class="admonition-body">
<p> <span style="color: #333333;">
Be careful when deleting mechanisms. All connected mechanisms also will be deleted. Unlink all child mechanisms if you want to delete only one mechanism.    </span>
</p>
</div>
</div>
<p>It is possible to add several end effectors and select the active end effector using <img alt="images/download/thumbnails/129931045/image2024-2-9_16-36-14.png" class="confluence-embedded-image confluence-thumbnail doc-inline" height="28" src="images/download/thumbnails/129931045/image2024-2-9_16-36-14.png" style="--doc-image-width:32px"/>
 button.</p>
</div>
</div></div></div>
