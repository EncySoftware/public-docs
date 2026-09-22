---
title: "Grouping elements"
---

<link rel="stylesheet" href="assets/manual.css">

<div id="ht-wrap-container"><div class="ht-content" id="ht-content"><div class="ht-content-header"><h1 id="src-131903382">Grouping elements</h1></div><div class="wiki-content sp-grid-section" data-index-for-search="true" id="main-content">
<p>Equipment elements need to be grouped into nodes. Mark 3D model elements with specific colors to group them.</p>
<p><a class="doc-image-link" href="images/download/attachments/131903382/image2021-5-4_12-55-5.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/131903382/image2021-5-4_12-55-5.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="735" src="images/download/attachments/131903382/image2021-5-4_12-55-5.png" style="--doc-image-width:800px" width="2222"/></a>
</p>
<p>Select a node color from the right panel and mark desired elements on the 3D model. Each element marked with the same color will be added to the same group.</p>
<p><a class="doc-image-link" href="images/download/attachments/131903382/image2024-2-9_15-28-11.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/131903382/image2024-2-9_15-28-11.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="339" src="images/download/attachments/131903382/image2024-2-9_15-28-11.png" style="--doc-image-width:338px" width="338"/></a>
</p>
<div class="confbox admonition admonition-tip">
<span class="admonition-icon confluence-information-macro-icon"></span>
<div class="admonition-body">
<p> <span style="color: #333333;">
I    <span style="color: #333333;">
t is not necessary to mark each and every element. You can keep unnecessary elements unmarked to exclude them from the mechanism. Also, MachineMaker saves data to the source CAD file so it is possible to change groups of elements anytime    </span>
.    </span>
</p>
</div>
</div>
<p>Click marked element again to clear the color. It is also possible to unmark elements right-clicking on them with your mouse button.</p>
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
<p><a class="doc-image-link" href="images/download/attachments/131903382/mark.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/131903382/mark.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="423" src="images/download/attachments/131903382/mark.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
<p>It is possible to delete unnecessary elements from the 3D model using <strong class=""><i class="">Del</i> </strong>key. Use <i class=""><strong class="">Ctrl+Z</strong></i><strong class=""> </strong>to undo element deletion.</p>
<p>MachineMaker stores all imported 3D models in the <i class=""><strong class="">CAD Files</strong></i> folder. You can always reimport the 3D model using <i class=""><strong class="">Reimport </strong></i>button. Turn off<i class=""> <strong class="">Copy imported CAD files</strong></i> checkbox to disable saving original CAD models.</p>
<p><a class="doc-image-link" href="images/download/attachments/131903382/image2024-2-9_15-31-9.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/131903382/image2024-2-9_15-31-9.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="267" src="images/download/attachments/131903382/image2024-2-9_15-31-9.png" style="--doc-image-width:412px" width="412"/></a>
</p>
<p><strong class="">Add file</strong> - function for adding additional files.</p>
<p><a class="doc-image-link" href="images/download/attachments/131903382/image2024-2-9_15-32-6.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/131903382/image2024-2-9_15-32-6.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="262" src="images/download/attachments/131903382/image2024-2-9_15-32-6.png" style="--doc-image-width:414px" width="414"/></a>
</p>
<div class="confbox admonition admonition-tip">
<span class="admonition-icon confluence-information-macro-icon"></span>
<div class="admonition-body">
<p> <span style="color: #333333;">
MachineMaker automatically groups all elements to Base node in jointless mechanisms such as Fixed Tables, Fixed Objects and End Effectors.    </span>
</p>
</div>
</div>
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
<p>It is necessary to enter Mechanism name and select mechanism type. MachineMaker uses 3D model filename as default name. It also automatically selects the brand for the robot. But if you need to replace it, you can easily do so using the drop-down list.</p>
<p><a class="doc-image-link" href="images/download/attachments/131903382/image2024-2-9_15-34-43.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/131903382/image2024-2-9_15-34-43.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="318" src="images/download/attachments/131903382/image2024-2-9_15-34-43.png" style="--doc-image-width:414px" width="414"/></a>
</p>
<div class="confbox admonition admonition-tip">
<span class="admonition-icon confluence-information-macro-icon"></span>
<div class="admonition-body">
<p> <span style="color: #333333;">
MachineMaker will use the Mechanism name as the Project name by default.    </span>
</p>
</div>
</div>
</div></div></div>
