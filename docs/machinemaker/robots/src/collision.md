---
title: "Collision"
---

<link rel="stylesheet" href="assets/manual.css">

<div id="ht-wrap-container"><div class="ht-content" id="ht-content"><div class="ht-content-header"><h1 id="src-129936493">Collision</h1></div><div class="wiki-content sp-grid-section" data-index-for-search="true" id="main-content">
<p>If you are using inaccurate 3D models, CAM system can detect false-positive collisions between nodes. You can add these nodes to the ignore-list to prevent CAM system from detecting false-positive collisions.</p>
<p>Click <img alt="images/download/attachments/129936493/button.PNG" class="confluence-embedded-image doc-inline" src="images/download/attachments/129936493/button.PNG" style="--doc-image-width:50px"/>
button to open the parameters panel. Then go to the <i class=""><strong class="">Collisions</strong></i> tab.</p>
<p><a class="doc-image-link" href="images/download/attachments/129936493/image2025-11-20_9-46-17.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129936493/image2025-11-20_9-46-17.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="485" src="images/download/attachments/129936493/image2025-11-20_9-46-17.png" style="--doc-image-width:407px" width="407"/></a>
</p>
<p>Select first and second nodes and click <strong class="">Add collisions</strong> button. Use <i class=""><strong class="">with children</strong></i><strong class=""> </strong>toggle to add node's children to the ignore-list. Use <img alt="images/download/thumbnails/129936493/image2021-6-25_16-4-13.png" class="confluence-embedded-image confluence-thumbnail doc-inline" height="13" src="images/download/thumbnails/129936493/image2021-6-25_16-4-13.png" style="--doc-image-width:13px"/>
 button to delete a previously added collision from the ignore list.</p>
<p><a class="doc-image-link" href="images/download/attachments/129936493/image2025-11-20_9-47-1.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129936493/image2025-11-20_9-47-1.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="493" src="images/download/attachments/129936493/image2025-11-20_9-47-1.png" style="--doc-image-width:411px" width="411"/></a>
</p>
<p>In the custom collision tab, you can manually compute collisions using user-defined parameters.<br/>This section allows you to specify the mesh resolution for each mechanism node used by the collision-detection algorithm.</p>
<p><a class="doc-image-link" href="images/download/attachments/129936493/image2025-11-20_9-47-27.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129936493/image2025-11-20_9-47-27.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="380" src="images/download/attachments/129936493/image2025-11-20_9-47-27.png" style="--doc-image-width:408px" width="408"/></a>
</p>
<p>If you click <strong class="">“Prepare collision meshes data”</strong>, the application will calculate the number of mechanism positions required for collision detection.</p>
<p style="text-align:center;"><a class="doc-image-link" href="images/download/attachments/129936493/mp4gif.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129936493/mp4gif.gif" class="confluence-embedded-image confluence-content-image-border doc-image doc-overview" height="720" src="images/download/attachments/129936493/mp4gif.webp" style="--doc-image-width:800px" width="1280"/></a>
</p>
<p style="text-align:left;">After calculating the number of mechanism positions, you will be able to sort them by nodes and visually inspect collisions on the mechanisms.</p>
<p style="text-align:center;"><a class="doc-image-link" href="images/download/attachments/129936493/image2025-11-20_10-22-2.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129936493/image2025-11-20_10-22-2.png" class="confluence-embedded-image confluence-content-image-border doc-image doc-standard" height="737" src="images/download/attachments/129936493/image2025-11-20_10-22-2.png" style="--doc-image-width:640px" width="990"/></a>
</p>
<div class="confbox admonition admonition-tip">
<span class="admonition-icon confluence-information-macro-icon"></span>
<div class="admonition-body">
<p>CAM system always ignores collisions between sibling nodes. So it is not necessary to add them to the ignore list.</p>
</div>
</div>
</div></div></div>
