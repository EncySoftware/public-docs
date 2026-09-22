---
title: "Table calibration"
---

<link rel="stylesheet" href="assets/manual.css">

<div id="ht-wrap-container"><div class="ht-content" id="ht-content"><div class="ht-content-header"><h1 id="src-129931151">Table calibration</h1></div><div class="wiki-content sp-grid-section" data-index-for-search="true" id="main-content">
<p>Table calibration function is available from the <a href="assemblies.md">assembly view</a>. Finish editing mechanism by clicking <i class=""><strong class="">Apply</strong></i><strong class=""> </strong>or <i class=""><strong class="">Cancel</strong></i><strong class=""> </strong>buttons to see the entire mechanisms assembly.</p>
<p>Robot has a Base and TCP coordinate systems. It is necessary to specify User Coordinate System position relative to the Robot Base Coordinate System.</p>
<p><a class="doc-image-link" href="images/download/attachments/129931151/image2021-5-5_19-54-52.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129931151/image2021-5-5_19-54-52.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-standard" height="618" src="images/download/attachments/129931151/image2021-5-5_19-54-52.png" style="--doc-image-width:640px" width="742"/></a>
</p>
<div class="confbox admonition admonition-tip">
<span class="admonition-icon confluence-information-macro-icon"></span>
<div class="admonition-body">
<p> <span style="color: #333333;">
Hold down     </span>
<i class=""><strong class="">Left Ctrl</strong></i><strong class=""> </strong> <span style="color: #333333;">
key to show all Coordinate Systems.    </span>
</p>
</div>
</div>
<div class="section section-1" id="src-129931151_id-.Tablecalibrationv18-Howtocalibrateatable">
<h1 class="heading"><span>How to calibrate a table</span></h1>
<p>Select a table using the left mouse button in the Transformation panel on the right. Select the desired User CS as <i class=""><strong class="">Target</strong></i><strong class=""> </strong>and select Robot Base CS in the <i class=""><strong class="">Relative</strong></i><strong class=""> </strong>field. Now you can see User Coordinate System position relatively to the Robot Base Coordinate System in the Move and Rotate fields. Enter correct values to finish calibration.</p>
<p><a class="doc-image-link" href="images/download/attachments/129931151/change3245rgbv.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129931151/change3245rgbv.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="590" src="images/download/attachments/129931151/change3245rgbv.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
<div class="confbox admonition admonition-tip">
<span class="admonition-icon confluence-information-macro-icon"></span>
<div class="admonition-body">
<p> <span style="color: #333333;">
Use Robot's User CS calibration function to obtain accurate values    </span>
</p>
</div>
</div>
</div>
<div class="section section-1" id="src-129931151_safe-id-aWQtLlRhYmxlY2FsaWJyYXRpb252MTgtUXVhdGVybmlvbnMsUmFkaWFuc2FuZEV1bGVyYW5nbGVz">
<h1 class="heading"><span>Quaternions, Radians and Euler angles</span></h1>
<p>Some robots (such as ABB) use quaternions instead of euler angles. For this kind of robots MachineMaker can show quaternions fields. You can switch to Euler angles if you prefer to use human-friendly Euler angles.</p>
<p><a class="doc-image-link" href="images/download/attachments/129931151/image2021-9-6_16-31-35.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129931151/image2021-9-6_16-31-35.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="440" src="images/download/attachments/129931151/image2021-9-6_16-31-35.png" style="--doc-image-width:304px" width="304"/></a>
</p>
<div class="confbox admonition admonition-tip">
<span class="admonition-icon confluence-information-macro-icon"></span>
<div class="admonition-body">
<p> <span style="color: #333333;">
MachineMaker will automatically detect that you are doing table calibration and will switch rotation mode to the correct values system. You can switch it back to the Euler angles without loosing your data.    </span>
</p>
</div>
</div>
<div class="confbox admonition admonition-note">
<span class="admonition-icon confluence-information-macro-icon"></span>
<div class="admonition-body">
<p> <span style="color: #333333;">
MachineMaker will suggest using quaternions only for robots which support it (like ABB).    </span>
</p>
</div>
</div>
</div>
</div></div></div>
