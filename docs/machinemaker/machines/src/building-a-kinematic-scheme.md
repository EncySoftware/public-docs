---
title: "Building a kinematic scheme"
---

<link rel="stylesheet" href="assets/manual.css">

<div id="ht-wrap-container"><div class="ht-content" id="ht-content"><div class="ht-content-header"><h1 id="src-129940297">Building a kinematic scheme</h1></div><div class="wiki-content sp-grid-section" data-index-for-search="true" id="main-content">
<p>Click <i class=""><strong class="">Kinematic</strong></i><strong class=""> </strong>tab to open kinematic parameters panel.<a class="doc-image-link" href="images/download/attachments/129940297/Click_kinematic.PNG" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129940297/Click_kinematic.PNG" class="confluence-embedded-image image-center doc-image doc-detail" height="31" src="images/download/attachments/129940297/Click_kinematic.PNG" style="--doc-image-width:440px" width="503"/></a>
</p>
<p>First of all it is necessary to build correct mechanism's kinematic tree, using grag and drop. MachineMaker will show Tool node as a sample tool and Workpiece node as a sample part.</p>
<p><a class="doc-image-link" href="images/download/attachments/129940297/graganddrop.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129940297/graganddrop.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="568" src="images/download/attachments/129940297/graganddrop.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
<p>In the <strong class="">Tool</strong> settings there is a function to select <strong class="">Supported applications</strong> and also additional options.</p>
<p><a class="doc-image-link" href="images/download/attachments/129940297/image2024-2-2_12-36-28.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129940297/image2024-2-2_12-36-28.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-standard" height="809" src="images/download/attachments/129940297/image2024-2-2_12-36-28.png" style="--doc-image-width:640px" width="710"/></a>
</p>
<p><strong class="">Workpiece</strong> also has its own additional parameters.</p>
<p><a class="doc-image-link" href="images/download/attachments/129940297/image2024-2-2_12-44-25.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129940297/image2024-2-2_12-44-25.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="706" src="images/download/attachments/129940297/image2024-2-2_12-44-25.png" style="--doc-image-width:433px" width="433"/></a>
</p>
<p>Next it is necessary to specify parameters of each node.</p>
<p>Set node name and type.</p>
<p><a class="doc-image-link" href="images/download/attachments/129940297/image2023-10-30_12-37-2.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129940297/image2023-10-30_12-37-2.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="517" src="images/download/attachments/129940297/image2023-10-30_12-37-2.png" style="--doc-image-width:414px" width="414"/></a>
</p>
<p>Next it is necessary to specify node <i class=""><strong class="">Address</strong> </i>for Linear and Rotary nodes. It will be used in Postprocessors.</p>
<p><a class="doc-image-link" href="images/download/attachments/129940297/image2023-10-30_12-37-50.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129940297/image2023-10-30_12-37-50.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="160" src="images/download/attachments/129940297/image2023-10-30_12-37-50.png" style="--doc-image-width:370px" width="370"/></a>
</p>
<p>Select linear axis direction. You can select X Y Z or custom. Use <i class=""><strong class="">Orientation</strong></i><strong class=""> </strong>field to define <i class=""><strong class="">Custom</strong></i> direction vector.</p>
<p><a class="doc-image-link" href="images/download/attachments/129940297/image2023-10-30_12-39-36.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129940297/image2023-10-30_12-39-36.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="293" src="images/download/attachments/129940297/image2023-10-30_12-39-36.png" style="--doc-image-width:364px" width="364"/></a>
</p>
<p><a class="doc-image-link" href="images/download/attachments/129940297/limits.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129940297/limits.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="652" src="images/download/attachments/129940297/limits.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
<p>Next define <i class=""><strong class="">Has Brake, Increment </strong></i>and<strong class=""> </strong><i class=""><strong class="">Scale</strong> </i>parameters. Change <i class=""><strong class="">Control</strong> <strong class=""></strong></i>parameter if axis is Indexed or Manual. It is possible to <i class=""><strong class="">Invert Direction</strong></i><strong class=""> </strong>of axis.</p>
<p><a class="doc-image-link" href="images/download/attachments/129940297/image2022-4-20_18-40-54.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129940297/image2022-4-20_18-40-54.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="107" src="images/download/attachments/129940297/image2022-4-20_18-40-54.png" style="--doc-image-width:327px" width="327"/></a>
</p>
<p>For rotary axes it is necessary to specify point of rotation. Hold the <i class=""><strong class="">Left Mouse Button,</strong></i><strong class=""> </strong>drag the bearing and drop it to the snap point. Use <i class=""><strong class="">Transformation Panel</strong></i><strong class=""> </strong>to set position and rotation manually.</p>
<p><a class="doc-image-link" href="images/download/attachments/129940297/dmu50rotary2.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129940297/dmu50rotary2.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="636" src="images/download/attachments/129940297/dmu50rotary2.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
<p>Finally it is necessary to set <i class=""><strong class="">Tool Type</strong></i><strong class=""> </strong>and specify positions of Tool and Workpiece. Place Tool and Workpiece to the correct position at the <i class=""><strong class="">Kinematic tree.</strong></i><strong class=""> </strong>Then hold the <i class=""><strong class="">Left Mouse Button,</strong></i><strong class=""> </strong>drag the bearing and drop it to the snap point. Use <i class=""><strong class="">Transformation Panel</strong></i><strong class=""> </strong>to set position and rotation manually.</p>
<p><a class="doc-image-link" href="images/download/attachments/129940297/dmu502.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129940297/dmu502.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="636" src="images/download/attachments/129940297/dmu502.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
</div></div></div>
