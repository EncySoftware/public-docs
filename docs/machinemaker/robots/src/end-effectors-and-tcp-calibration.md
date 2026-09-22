---
title: "End effectors and TCP calibration"
---

<link rel="stylesheet" href="assets/manual.css">

<div id="ht-wrap-container"><div class="ht-content" id="ht-content"><div class="ht-content-header"><h1 id="src-129930953">End effectors and TCP calibration</h1></div><div class="wiki-content sp-grid-section" data-index-for-search="true" id="main-content">
<p>It is possible to equip the robot with a static or movable end effector. More information on movable end effectors can be found on <a href="composite-end-effectors.md">Composite End effectors</a> page.Add a new End Effector and select its 3D model file.</p>
<a class="doc-image-link" href="images/download/attachments/129930953/image2024-8-13_11-35-10.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930953/image2024-8-13_11-35-10.png" class="confluence-embedded-image image-center doc-image doc-detail" height="439" src="images/download/attachments/129930953/image2024-8-13_11-35-10.png" style="--doc-image-width:440px" width="549"/></a>
<div class="section section-1" id="src-129930953_id-.EndeffectorsandTCPcalibrationv18-3Dmodel">
<h1 class="heading"><span>3D model</span></h1>
<p>MachineMaker shows a transparent robot and an <a href="prepare-and-import-3d-objects.md">imported end effector CAD model</a>. All 3D model elements are marked as Base node by default. Use the right mouse button to <a href="grouping-elements-into-nodes.md">ungroup unnecessary elements</a>.</p>
<p>You have to define the name of the End Effector and select supported tool types.<br/>Next, place the 3D model on the robot flange. There are 2 ways to specify the correct position:</p>
<ul class=""><li class=""><p>Use Transformation Panel in the right bottom corner</p>
</li><li class=""><p>Turn on <i class=""><strong class="">Base CS Transformation mode,</strong></i> hold down the <i class=""><strong class="">Left Ctrl</strong></i><strong class=""> </strong>key and specify the robot's flange connection point using Drag&amp;Drop</p>
</li></ul>
<a class="doc-image-link" href="images/download/attachments/129930953/endeff.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930953/endeff.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="522" src="images/download/attachments/129930953/endeff.webp" style="--doc-image-width:800px" width="800"/></a>
<a class="doc-image-link" href="images/download/attachments/129930953/endeff2.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930953/endeff2.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="522" src="images/download/attachments/129930953/endeff2.webp" style="--doc-image-width:800px" width="800"/></a>
</div>
<div class="section section-1" id="src-129930953_id-.EndeffectorsandTCPcalibrationv18-TCPcalibration">
<h1 class="heading"><span>TCP calibration</span></h1>
<p>Click TCP tab to open the tool center point panel. It is necessary to place the tool in the correct position.</p>
<p><a class="doc-image-link" href="images/download/attachments/129930953/image2022-4-19_12-35-48.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930953/image2022-4-19_12-35-48.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-standard" height="600" src="images/download/attachments/129930953/image2022-4-19_12-35-48.png" style="--doc-image-width:640px" width="800"/></a>
</p>
<p>You can use the Transformation Panel or hold down the <i class=""><strong class="">Left Ctrl </strong></i>key<i class=""><strong class=""> </strong></i>to enter Drag&amp;Drop mode. Use <i class=""><strong class="">Visualize tool</strong></i><strong class=""> </strong>checkbox to show the tool's visibility. Click <i class=""><strong class="">Reset</strong></i><strong class=""> </strong>to clear all fields.</p>
<p><a class="doc-image-link" href="images/download/attachments/129930953/endeff3.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930953/endeff3.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="522" src="images/download/attachments/129930953/endeff3.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
<p>Use <i class=""><strong class="">Transform End Effector 3D model with TCP</strong></i><strong class=""> </strong>to change the 3D model's position.</p>
<p>Subsequently, TCP calibration is performed on the actual robot to obtain real-world values. To avoid visual discrepancies with the real robot, it is advisable to move the TCP in conjunction with the 3D model of the end effector after obtaining actual calibration numbers."</p>
<p><a class="doc-image-link" href="images/download/attachments/129930953/ikufgdjlfvsdk.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930953/ikufgdjlfvsdk.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="636" src="images/download/attachments/129930953/ikufgdjlfvsdk.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
<p>It is also possible to set the tool overhang if you have tool-tip calibration values from the robot and want to enter these values in the XYZ ABC fields.</p>
<p><a class="doc-image-link" href="images/download/attachments/129930953/image2021-6-25_14-46-35.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930953/image2021-6-25_14-46-35.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="232" src="images/download/attachments/129930953/image2021-6-25_14-46-35.png" style="--doc-image-width:326px" width="326"/></a>
</p>
<div class="confbox admonition admonition-tip">
<span class="admonition-icon confluence-information-macro-icon"></span>
<div class="admonition-body">
<p> <span style="color: #333333;">
You can set the tool overhang to zero and calibrate the tool base point. Or you can specify the tool overhang and calibrate the tool-tip. In    </span>
<span style="color: #333333;">
 CAM system and MachineMaker    </span>
<span style="color: #333333;">
 both options are available.    </span>
</p>
</div>
</div>
</div>
<div class="section section-1" id="src-129930953_id-.EndeffectorsandTCPcalibrationv18-Usingcalibrationapp">
<h1 class="heading"><span>Using calibration app</span></h1>
<p>MachineMaker calibration app allows you to make the most accurate TCP calibration using the 2-point calibration method.</p>
<p><a class="doc-image-link" href="images/download/attachments/129930953/image2022-4-19_12-42-8.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930953/image2022-4-19_12-42-8.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-standard" height="600" src="images/download/attachments/129930953/image2022-4-19_12-42-8.png" style="--doc-image-width:618px" width="618"/></a>
</p>
<p><a class="doc-image-link" href="images/download/attachments/129930953/image2022-4-19_12-43-14.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930953/image2022-4-19_12-43-14.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-standard" height="600" src="images/download/attachments/129930953/image2022-4-19_12-43-14.png" style="--doc-image-width:488px" width="488"/></a>
</p>
<p>First of all it is necessary to calibrate both long and short tools using your robot's standard 4-points calibration method.</p>
<p><a class="doc-image-link" href="images/download/attachments/129930953/4.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930953/4.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-standard" height="450" src="images/download/attachments/129930953/4.webp" style="--doc-image-width:600px" width="600"/></a>
</p>
<p>Next, download the latest version of our mobile app using the link in MachineMaker.</p>
<p><a class="doc-image-link" href="images/download/attachments/129930953/image2022-4-19_12-56-25.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930953/image2022-4-19_12-56-25.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="426" src="images/download/attachments/129930953/image2022-4-19_12-56-25.png" style="--doc-image-width:398px" width="398"/></a>
</p>
<p>Launch the mobile app and fill in calibration values from the robot.</p>
<p><a class="doc-image-link" href="images/download/attachments/129930953/5.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930953/5.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="600" src="images/download/attachments/129930953/5.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
<p>Finally, click <i class=""><strong class="">Send</strong></i><strong class=""> </strong>button and scan the QR code from the MachineMaker. Calculated values will be transferred to your MachineMaker TCP calibration input fields automatically. It is also possible to enter the calculated calibration values manually.</p>
<p><a class="doc-image-link" href="images/download/attachments/129930953/9.webp" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930953/9.gif" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-overview" height="600" src="images/download/attachments/129930953/9.webp" style="--doc-image-width:800px" width="800"/></a>
</p>
</div>
<div class="section section-1" id="src-129930953_safe-id-aWQtLkVuZGVmZmVjdG9yc2FuZFRDUGNhbGlicmF0aW9udjE4LVF1YXRlcm5pb25zLFJhZGlhbnNhbmRFdWxlckFuZ2xlcw">
<h1 class="heading"><span>Quaternions, Radians and Euler Angles</span></h1>
<p>Some robots (such as ABB) use quaternions or Radians instead of euler angles. For this kind of robots MachineMaker will show quaternions fields. You can switch to Euler angles if you prefer to use Euler angles.</p>
<p><a class="doc-image-link" href="images/download/attachments/129930953/image2021-6-25_15-12-4.png" rel="noopener" target="_blank" title="Open full-size image"><img alt="images/download/attachments/129930953/image2021-6-25_15-12-4.png" class="confluence-embedded-image confluence-content-image-border image-center doc-image doc-detail" height="325" src="images/download/attachments/129930953/image2021-6-25_15-12-4.png" style="--doc-image-width:340px" width="340"/></a>
</p>
<div class="confbox admonition admonition-tip">
<span class="admonition-icon confluence-information-macro-icon"></span>
<div class="admonition-body">
<p> <span style="color: #333333;">
MachineMaker will save TCP values in the acceptable format for the robot anyway. So, even if you use Euler angles and set tool position in A B C values, MachineMaker will convert it to quaternions automatically.    </span>
</p>
</div>
</div>
</div>
</div></div></div>
