---
title: "Prepare and import 3D objects"
---

<link rel="stylesheet" href="assets/manual.css">

<div id="ht-wrap-container"><div class="ht-content" id="ht-content"><div class="ht-content-header"><h1 id="src-129930751">Prepare and import 3D objects</h1></div><div class="wiki-content sp-grid-section" data-index-for-search="true" id="main-content">
<div class="section section-1" id="src-129930751_id-.Prepareandimport3Dobjectsv18-Supported3Dmodelformats">
<h1 class="heading"><span>Supported 3D model formats</span></h1>
<ul class=""><li class=""><p><strong class="">3dm:</strong> Rhinoceros 3D</p>
</li><li class=""><p><strong class="">sldprt, sldasm:</strong> SоlidWorks</p>
</li><li class=""><p><strong class="">par, psm, pwr, asm:</strong> Solid Edge</p>
</li><li class=""><p><strong class="">stp, step</strong></p>
</li><li class=""><p><strong class="">x_t, x_b</strong> : Parasolid</p>
</li><li class=""><p><strong class="">igs, iges</strong></p>
</li><li class=""><p><strong class="">jt</strong></p>
</li><li class=""><p><strong class="">OSD</strong></p>
</li><li class=""><p><strong class="">STL</strong><strong class=""><br/></strong><strong class=""><br/></strong></p>
</li></ul> <div class="confbox admonition admonition-note">
<span class="admonition-icon confluence-information-macro-icon"></span>
<div class="admonition-body">
<p> <span style="color: #333333;">
<span style="color: #333333;">
It is     </span>
<span style="color: #333333;">
also     </span>
<span style="color: #333333;">
possible to select several files at once. This may be useful if you had split your mechanism and saved each node in a separate file    </span>
.    </span>
</p>
</div>
</div>
<p> <span style="color: #2c2c2c;">
Preparing models    </span>
</p>
<p>Many robot manufacturers (such as KUKA, Abb, Fanuc etc.) provide 3D models of their robots which can be used in MachineMaker without any adaptation.</p>
<p>MachineMaker allows you to make some basic operations with imported 3D models like moving and rotating. Use transformation panel in the lower right corner to transform your 3D models.<a class="doc-image-link" href="images/download/attachments/129930751/moves.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930751/moves.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="423" src="images/download/attachments/129930751/moves.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
<div class="confbox admonition admonition-note">
<span class="admonition-icon confluence-information-macro-icon"></span>
<div class="admonition-body">
<p> <span style="color: #333333;">
<span style="color: #333333;">
It is possible to move and rotate only the entire 3D model. Please use an external CAD system to make more complex operations with the 3D model    </span>
.    </span>
</p>
</div>
</div>
</div>
<div class="section section-1" id="src-129930751_id-.Prepareandimport3Dobjectsv18-BaseCStransformation">
<h1 class="heading"><span>Base CS transformation</span></h1>
<p> <span style="color: #003366;">
<span style="color: #003366;">
It is possible to specify the mechanism's Base Coordinate System using the mouse. Turn on     </span>
<strong class=""><i class="">Base CS editing mode</i></strong> <span style="color: #003366;">
 then hold down the     </span>
<i class=""><strong class="">Left Ctrl</strong></i><strong class=""> </strong> <span style="color: #003366;">
key and drag you Base CS into the correct position.    </span>
</span>
</p>
<p> <span style="color: #003366;">
<a class="doc-image-link" href="images/download/attachments/129930751/basecs.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930751/basecs.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="423" src="images/download/attachments/129930751/basecs.webp" style="--doc-image-width:800px" width="800"/></a>
<br/> </span>
<span style="color: #2c2c2c;">
3D models simplifier    </span>
</p>
<p>MachineMaker automatically simplifies imported files. All unnecessary inner faces and small objects will be deleted.</p>
<p><a class="doc-image-link" href="images/download/attachments/129930751/Screen1.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930751/Screen1.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-standard" height="886" src="images/download/attachments/129930751/Screen1.png" style="--doc-image-width:640px" width="1338"/></a>
</p>
<p><a class="doc-image-link" href="images/download/attachments/129930751/image2021-5-8_13-27-1.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930751/image2021-5-8_13-27-1.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-standard" height="886" src="images/download/attachments/129930751/image2021-5-8_13-27-1.png" style="--doc-image-width:640px" width="1338"/></a>
</p>
<p><a class="doc-image-link" href="images/download/attachments/129930751/Screen3.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930751/Screen3.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-standard" height="886" src="images/download/attachments/129930751/Screen3.png" style="--doc-image-width:640px" width="1338"/></a>
</p>
<p>You can disable the simplifier in the application settings. Or use the integrated <a class="external-link" href="https://docs.encycam.com/MachineMaker/1/robots/en/90.html">simplifier</a> manually.</p>
<p><a class="doc-image-link" href="images/download/attachments/129930751/image2024-8-13_9-54-8.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930751/image2024-8-13_9-54-8.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="598" src="images/download/attachments/129930751/image2024-8-13_9-54-8.png" style="--doc-image-width:440px" width="507"/></a>
</p>
</div>
</div></div></div>
