---
title: "Composite End effectors"
---

<link rel="stylesheet" href="assets/manual.css">

<div id="ht-wrap-container"><div class="ht-content" id="ht-content"><div class="ht-content-header"><h1 id="src-131903701">Composite End effectors</h1></div><div class="wiki-content sp-grid-section" data-index-for-search="true" id="main-content">
<p>Composite end effectors usually contain movable parts such as fingers.</p>
<p>First of all, it is necessary to connect the end effector with the robot flange. The easiest way is to use <i class=""><strong class="">Base CS transform editing mode.</strong></i></p>
<p><a class="doc-image-link" href="images/download/attachments/131903701/Base_CS_transform_editing_mode_gif_800x600.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/131903701/Base_CS_transform_editing_mode_gif_800x600.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="600" src="images/download/attachments/131903701/Base_CS_transform_editing_mode_gif_800x600.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
<p><i class=""><strong class="">Relative</strong></i><strong class=""> </strong>selector allows you to change coordinate system for the Transformation Panel. Use <i class=""><strong class="">Default</strong></i> for Geometry CS, <i class=""><strong class="">Base CS</strong></i><strong class=""> </strong>for the Robot Flange CS and <i class=""><strong class="">TCP</strong></i><strong class=""> </strong>for the tool center point.</p>
<p><a class="doc-image-link" href="images/download/attachments/131903701/Relative.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/131903701/Relative.png" class="confluence-embedded-image image-center doc-image doc-standard" height="338" src="images/download/attachments/131903701/Relative.png" style="--doc-image-width:640px" width="800"/></a>
</p>
<p>Once this is done, you have to "Grouping elements into nodes".</p>
<p>At that stage we need to select only one movable joint. MachineMaker will automatically add all necessary joints later.</p>
<p><a class="doc-image-link" href="images/download/attachments/131903701/one_movable_joint.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/131903701/one_movable_joint.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-standard" height="527" src="images/download/attachments/131903701/one_movable_joint.png" style="--doc-image-width:639px" width="639"/></a>
</p>
<p>Next, go to the <i class=""><strong class="">Kinematic</strong></i><strong class=""> </strong>tab and define the connectors location. First of all it is necessary to select the connector type, it may be <i class=""><strong class="">Linear</strong></i><strong class=""> </strong>or <i class=""><strong class="">Rotary</strong></i>. Use Drag&amp;Drop and Transformation Panel to set the connector's position and orientation. Set minimal and maximal positions in the <i class=""><strong class="">Limits</strong></i><strong class=""> </strong>panel.<strong class=""></strong></p>
<p style="text-align:center;"><a class="doc-image-link" href="images/download/attachments/131903701/Rotary_Linear_gif_800x600.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/131903701/Rotary_Linear_gif_800x600.gif" class="confluence-embedded-image confluence-content-image-border doc-image doc-overview" height="600" src="images/download/attachments/131903701/Rotary_Linear_gif_800x600.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
<p style="text-align:left;">In order to create copies of movable joint use <i class=""><strong class="">Multiply count</strong></i><strong class=""> </strong>edit.</p>
<p style="text-align:center;"><a class="doc-image-link" href="images/download/attachments/131903701/Gripper_gif_800x600.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/131903701/Gripper_gif_800x600.gif" class="confluence-embedded-image confluence-content-image-border doc-image doc-overview" height="600" src="images/download/attachments/131903701/Gripper_gif_800x600.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
<p>Finally set the TCP and Style similarly to a plain "End Effector"</p>
<p>In some cases, a composite end effector can be linear. Ensure that the "Gripping" type is selected.</p>
<p><a class="doc-image-link" href="images/download/attachments/131903701/image2023-12-18_11-8-28.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/131903701/image2023-12-18_11-8-28.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-standard" height="728" src="images/download/attachments/131903701/image2023-12-18_11-8-28.png" style="--doc-image-width:640px" width="699"/></a>
</p>
<p>In kinematics, choose the "Linear" type and set the necessary limits for the jaws. Also use the "Multiply count edit" function to create copies of the jaws.<br/><br/><br/><a class="doc-image-link" href="images/download/attachments/131903701/image2023-12-18_11-6-56.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/131903701/image2023-12-18_11-6-56.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-standard" height="588" src="images/download/attachments/131903701/image2023-12-18_11-6-56.png" style="--doc-image-width:640px" width="947"/></a>
</p>
<p>Similarly to "Rotary" the limits of jaws movements are edited.</p>
<p><a class="doc-image-link" href="images/download/attachments/131903701/beaz_nazvaniya.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/131903701/beaz_nazvaniya.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="636" src="images/download/attachments/131903701/beaz_nazvaniya.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
</div></div></div>
