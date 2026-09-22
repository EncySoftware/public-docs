---
title: "Simplifier"
---

<link rel="stylesheet" href="assets/manual.css">

<div id="ht-wrap-container"><div class="ht-content" id="ht-content"><div class="ht-content-header"><h1 id="src-129934066">Simplifier</h1></div><div class="wiki-content sp-grid-section" data-index-for-search="true" id="main-content">
<p>Simplifier in MachineMaker is intended to simplify complex 3D models. This may include eliminating redundant parts, merging surfaces, optimizing model structure, and other complexity reduction techniques.</p>
<p>To open it you need to click on the drop-down menu and select <strong class="">Simplifier</strong> in the utilities menu.</p>
<p><a class="doc-image-link" href="images/download/attachments/129934066/image2024-8-16_16-42-28.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129934066/image2024-8-16_16-42-28.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="228" src="images/download/attachments/129934066/image2024-8-16_16-42-28.png" style="--doc-image-width:440px" width="508"/></a>
</p>
<p>The main menu of this utility looks like this:</p>
<p><a class="doc-image-link" href="images/download/attachments/129934066/image2024-2-27_11-51-58.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129934066/image2024-2-27_11-51-58.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="575" src="images/download/attachments/129934066/image2024-2-27_11-51-58.png" style="--doc-image-width:800px" width="904"/></a>
</p>
<p>The main window comprises the following sections:</p>
<ol class=""><li class=""><p>New project.</p>
</li><li class=""><p>Import.</p>
</li><li class=""><p>Save as.</p>
</li><li class=""><p>Send to MachineMaker.</p>
</li><li class=""><p>Transformation geometry.</p>
</li><li class=""><p>Simplify geometry.</p>
</li><li class=""><p>Find similar nodes.</p>
</li><li class=""><p>Delete.</p>
</li></ol><p>Transformation geometry is needed to move objects and has identical functions as in CAM system.<br/><a class="doc-image-link" href="images/download/attachments/129934066/rotate.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129934066/rotate.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="592" src="images/download/attachments/129934066/rotate.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
<p>Simplify geometry - This is one of the main functions of this utility. Here you can select different modes of model simplification. There are 4 templates:</p>
<ol class=""><li class=""><p><strong class="">Default</strong> - a mode that removes small objects from the model.</p>
</li><li class=""><p><strong class="">Middle</strong> - a mode that removes most of the objects from the surface of the model.</p>
</li><li class=""><p><strong class="">Maximum</strong> - a mode that removes everything except large parts of the model.</p>
</li><li class=""><p><strong class="">Custom</strong> - a mode in which you manually edit the surface of your model using sliders.</p>
</li></ol><p>The Kuka KR 120 R3100-2 robot model will be used for the illustrative test.</p>
<p><a class="doc-image-link" href="images/download/attachments/129934066/image2024-2-27_12-42-2.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129934066/image2024-2-27_12-42-2.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="807" src="images/download/attachments/129934066/image2024-2-27_12-42-2.png" style="--doc-image-width:800px" width="1096"/></a>
<br/>Before removing unnecessary objects from the robot, you can use the faces display function, where you can see in advance which objects will be removed (marked in red).</p>
<p><a class="doc-image-link" href="images/download/attachments/129934066/red.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129934066/red.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="592" src="images/download/attachments/129934066/red.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
<p>Simplifier also has a<strong class=""> Find similar nodes</strong> function. It is used to search for similar parts in your model, then it sorts them in a list by different nodes such as:</p>
<ul class=""><li class=""><p>Exactly the same</p>
</li><li class=""><p>Similar</p>
</li><li class=""><p>Partially same</p>
</li></ul><p><a class="doc-image-link" href="images/download/attachments/129934066/parts.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129934066/parts.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="592" src="images/download/attachments/129934066/parts.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
<p>If necessary, you can delete nodes using the Delete button.</p>
<p><a class="doc-image-link" href="images/download/attachments/129934066/delete231f.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129934066/delete231f.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="592" src="images/download/attachments/129934066/delete231f.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
</div></div></div>
