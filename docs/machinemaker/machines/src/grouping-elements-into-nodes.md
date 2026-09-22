---
title: "Grouping elements into nodes"
---

<link rel="stylesheet" href="assets/manual.css">

<div id="ht-wrap-container"><div class="ht-content" id="ht-content"><div class="ht-content-header"><h1 id="src-129940248">Grouping elements into nodes</h1></div><div class="wiki-content sp-grid-section" data-index-for-search="true" id="main-content">
<div class="section section-1" id="src-129940248_Groupingelementsintonodes-Groupingelements">
<h1 class="heading"><span>Grouping elements</span></h1>
<p>Equipment elements need to be grouped into nodes. Mark 3D model elements with specific colors to group them.</p>
<p>You can choose a template that suits your machine.</p>
<p><a class="doc-image-link" href="images/download/attachments/129940248/template.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129940248/template.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="568" src="images/download/attachments/129940248/template.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
<p class="auto-cursor-target">Select a node color from the right panel and mark desired elements on the 3D model. Each element marked with the same color will be added to the same group.</p>
<div class="confbox admonition admonition-tip">
<span class="admonition-icon confluence-information-macro-icon"></span>
<div class="admonition-body">
<p>Use <i class=""><strong class="">Tab, </strong></i><strong class=""> <span style="color: #2c2c2c;">
↑,     </span>
<span style="color: #2c2c2c;">
↓     </span>
</strong> <span style="color: #2c2c2c;">
keys to switch current color.    </span>
</p>
</div>
</div>
<p><a class="doc-image-link" href="images/download/attachments/129940248/markeruyou.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129940248/markeruyou.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="568" src="images/download/attachments/129940248/markeruyou.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
<div class="confbox admonition admonition-tip">
<span class="admonition-icon confluence-information-macro-icon"></span>
<div class="admonition-body">
<p> <span style="color: #333333;">
It is not necessary to mark each element. You can keep unnecessary elements unmarked to exclude them from mechanism. MachineMaker also saves source CAD file, so it is possible to change elements groups anytime.    </span>
</p>
</div>
</div>
<p>Use right mouse button to unmark 3D model element. Note that you can unmark only currently selected node elements. You can also use the keyboard shortcut <strong class="">"Ctrl + z"</strong> to roll back changes.</p>
<p><a class="doc-image-link" href="images/download/attachments/129940248/unmark.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129940248/unmark.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="568" src="images/download/attachments/129940248/unmark.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
<p>It is possible to delete unnecessary elements from the 3D model using <strong class=""><i class="">Del</i> </strong>key. Use <i class=""><strong class="">Ctrl+Z</strong></i><strong class=""> </strong>to undo element deletion.</p>
<p>MachineMaker stores all imported 3D models in the <i class=""><strong class="">CAD Files</strong></i> folder. You can always reimport the 3D model using <i class=""><strong class="">Reimport </strong></i>button. Turn off<i class=""> <strong class="">Copy imported CAD files</strong></i> checkbox to disable saving original CAD models.</p>
<p><a class="doc-image-link" href="images/download/attachments/129940248/image2024-2-9_15-31-9.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129940248/image2024-2-9_15-31-9.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="267" src="images/download/attachments/129940248/image2024-2-9_15-31-9.png" style="--doc-image-width:412px" width="412"/></a>
</p>
<p><strong class="">Add file</strong> - function for adding additional files.</p>
<p><a class="doc-image-link" href="images/download/attachments/129940248/image2024-2-9_15-32-6.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129940248/image2024-2-9_15-32-6.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="262" src="images/download/attachments/129940248/image2024-2-9_15-32-6.png" style="--doc-image-width:414px" width="414"/></a>
</p>
<div class="confbox admonition admonition-note">
<span class="admonition-icon confluence-information-macro-icon"></span>
<div class="admonition-body">
<p> <span style="color: #333333;">
If MachineMaker can't group elements     </span>
<span style="color: #333333;">
correctly     </span>
<span style="color: #333333;">
- see how to     </span>
<a class="external-link" href="https://kb.sprutcam.com/display/MMUMAU15/Prepare+and+import+3D+objects">fix your CAD models</a> <span style="color: #333333;">
.    </span>
</p>
</div>
</div>
<p> <span style="color: #2c2c2c;">
Mechanism name and type    </span>
</p>
<p>It is necessary to enter Mechanism name. MachineMaker uses 3D model filename as default name.</p>
<p><a class="doc-image-link" href="images/download/attachments/129940248/image2023-10-30_11-39-58.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129940248/image2023-10-30_11-39-58.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="540" src="images/download/attachments/129940248/image2023-10-30_11-39-58.png" style="--doc-image-width:413px" width="413"/></a>
</p>
</div>
<div class="section section-1" id="src-129940248_Groupingelementsintonodes-WorldCSposition">
<h1 class="heading"><span>World CS position</span></h1>
<p> <span style="color: #003366;">
It is necessary to specify Machine CS position. Turn on <strong class=""><i class="">Machine CS editing mode</i></strong>, then hold <i class=""><strong class="">Left Ctrl</strong></i><strong class=""> </strong>key and drag you Machine CS into the correct position.<br/> </span>
</p>
<p><a class="doc-image-link" href="images/download/attachments/129940248/cs.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129940248/cs.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="568" src="images/download/attachments/129940248/cs.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
</div>
<div class="section section-1" id="src-129940248_Groupingelementsintonodes-ToolandWorkpieceposition">
<h1 class="heading"><span>Tool and Workpiece position </span></h1>
<p> <span style="color: #003366;">
Open the <strong class="">Kinematic</strong> tab. Hold down the <strong class="">Left Ctrl</strong> key and drag the <strong class="">Tool</strong> and <strong class="">Workpiece</strong> to the desired position.    </span>
</p>
<p> <span style="color: #003366;">
<a class="doc-image-link" href="images/download/attachments/129940248/worktool.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129940248/worktool.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="568" src="images/download/attachments/129940248/worktool.webp" style="--doc-image-width:800px" width="800"/></a>
<br/> </span>
</p>
<div class="confbox admonition admonition-tip">
<span class="admonition-icon confluence-information-macro-icon"></span>
<div class="admonition-body">
<p> <span style="color: #333333;">
MachineMaker will use the Mechanism name as the Project name by default.    </span>
</p>
</div>
</div>
</div>
</div></div></div>
