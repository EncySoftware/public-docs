---
title: "Application area:"
---

<link rel="stylesheet" href="assets/manual.css">

<div id="ht-wrap-container"><div class="ht-content"><div class="ht-content-header"><h1 id="src-150697437"> <span>Application area:</span></h1></div><div class="wiki-content sp-grid-section" data-index-for-search="true" id="main-content">
<section id="introduction-application-area">
<h2 class="heading">Application Area</h2>
<p><strong>ENCY Hyper</strong> is a hybrid platform for programming industrial robots. It combines offline program development and testing in a digital twin with online robot control.</p>
<p><strong>Offline mode</strong> lets you verify programs before running them on the physical robot, reducing on-site trial and error. <strong>Online mode</strong> provides real-time feedback for debugging and adjustment, monitors execution, and supports stopping the robot when an anomaly is detected.</p>
<p>Optimized for <strong>Pick and Place</strong>, ENCY Hyper helps reduce idle time and manual intervention while improving production efficiency and consistency. Other applications include assembly, palletizing, sorting, quality inspection, milling, grinding, polishing, painting, and welding.</p>
<p>This manual introduces the platform's functions and workflow. Before deployment, review the supported hardware, available functions, and programming concepts.</p>
</section>
<div class="section section-1" id="src-150697437_safe-id-aWQtLkludHJvZHVjdGlvbnRvRU5DWUh5cGVydjEtV29ya2Zsb3c6">
<h2 class="heading">Workflow</h2>
<ol>
<li><p><strong>Prepare the cell.</strong> Create a <strong>.mma</strong> cell file in MachineMaker or obtain one from your dealer, then load it from the <a href="home-page.md">Home page</a>.</p></li>
<li><p><strong>Open the project.</strong> Double-click its card on the Home page.</p></li>
<li><p><strong>Configure the cell.</strong> Define trays and part attachment points in <a href="cell-mode.md">Cell mode</a>.</p></li>
<li><p><strong>Define parts.</strong> Import models or create primitives and specify their pick points in <a href="parts-mode.md">Parts mode</a>.</p></li>
<li><p><strong>Build the program.</strong> Add command blocks and calculate the trajectory in <a href="programming-mode.md">Programming Mode</a>.</p></li>
<li><p><strong>Run and monitor.</strong> Simulate the program in <a href="run-mode.md">Run Mode</a> and monitor actual operation when a robot is connected.</p></li>
</ol>
</div>
<div class="section section-1" id="src-150697437_safe-id-aWQtLkludHJvZHVjdGlvbnRvRU5DWUh5cGVydjEtUGlja2FuZHBsYWNlKHRyYW5zZmVyZnJvbXRhYmxldG90YWJsZSku">
<h1 class="heading"><span> Pick and place (transfer from table to table).</span></h1>
<p> <span style="color: #000000;">
The example shows simple transfer of a part from one table to another.    </span>
</p>
<details class="scroll-expand-container"><summary class="scroll-expand-control">Click here to expand..</summary><div class="scroll-expand-content">
<h2 id="pick-place-create-project">1. Create a project and assemble the cell</h2>
<p>On the <strong>ENCY Hyper</strong> home page, select <strong>New project &gt; Create in MachineMaker</strong> to create your own robotic cell.</p>
<p><a href="images/download/attachments/150697437/pick-tutorial-new-project-2026-09-17.png" rel="noopener" target="_blank"><img alt="New project page with Create in MachineMaker and Load .mma file options" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697437/pick-tutorial-new-project-2026-09-17.png" width="800"/></a></p>
<p>In <strong>MachineMaker</strong>, assemble the cell using the mechanisms required for your task. This example uses a robot, a gripper, and a table. Export the completed cell to <strong>ENCY Hyper</strong>.</p>
<p><a href="images/download/attachments/150697437/pick-tutorial-machinemaker-2026-09-17.png" rel="noopener" target="_blank"><img alt="Robot, gripper, and table assembled in MachineMaker" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697437/pick-tutorial-machinemaker-2026-09-17.png" width="800"/></a></p>
<h2>2. Add objects and trays in Cell mode</h2>
<p>The project opens on the <strong>Cell</strong> tab. Here you can add objects and define trays with points for locating parts on tables or at other positions in the cell. Add a tray with <strong>3 rows and 3 columns</strong> to the table imported from MachineMaker. Then add a second table directly in <strong>ENCY Hyper</strong> and give it another nine-point tray. One tray will hold the parts to be picked; the other will receive them. See <a href="cell-mode.md">Cell Mode</a> for details.</p>
<p><a href="images/download/attachments/150697437/pick-tutorial-trays-2026-09-17.png" rel="noopener" target="_blank"><img alt="Cell mode with two tables and a tray configured with three rows and three columns" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697437/pick-tutorial-trays-2026-09-17.png" width="800"/></a></p>
<h2>3. Define and place the parts</h2>
<p>On the <strong>Parts</strong> tab, use <strong>Add part</strong> to create a box or cylinder, or use <strong>Import</strong> to load your own 3D model. Configure the gripping settings for each part: <strong>Pick point</strong> defines how the tool grips it, while <strong>Base point</strong> defines the reference point used to position it on a tray. This example uses a cylinder.</p>
<p><a href="images/download/attachments/150697437/pick-tutorial-part-2026-09-17.png" rel="noopener" target="_blank"><img alt="Cylinder dimensions and Base point and Pick point settings in Parts mode" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697437/pick-tutorial-part-2026-09-17.png" width="800"/></a></p>
<p>After creating the part, place it at a tray point with the <strong>left mouse button</strong>. To fill the entire tray, press and hold the left mouse button on a point in that tray, then select <strong>Yes</strong> in the confirmation dialog. Fill the source tray and leave the destination tray empty.</p>
<p><a href="images/download/attachments/150697437/pick-tutorial-filled-tray-2026-09-17.png" rel="noopener" target="_blank"><img alt="Source tray filled with nine cylinders and an empty destination tray" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697437/pick-tutorial-filled-tray-2026-09-17.png" width="800"/></a></p>
<h2>4. Build the program</h2>
<p>Switch to <strong>Programming</strong>, the main workspace for defining and checking the robot program. Click the <strong>+</strong> button to open the command list.</p>
<p><a href="images/download/attachments/150697437/pick-tutorial-commands-2026-09-17.png" rel="noopener" target="_blank"><img alt="Available motion, handling, logic and IO commands" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697437/pick-tutorial-commands-2026-09-17.png" width="172"/></a></p>
<ul>
<li><strong>MOVE</strong> — moves the robot to a point using joint or linear motion.</li>
<li><strong>MOVE EXT</strong> — moves external axes.</li>
<li><strong>MOVE SYNC</strong> — moves mechanisms in parallel.</li>
<li><strong>TRAJECTORY</strong> — imports a machining trajectory from a CAM system.</li>
<li><strong>PICK</strong> — picks up a part from a selected location.</li>
<li><strong>PLACE</strong> — releases a part at a selected location.</li>
<li><strong>WELDING</strong> — performs a welding operation.</li>
<li><strong>GLUING</strong> — applies adhesive along the specified path.</li>
<li><strong>POLISHING</strong> — polishes a surface along a path.</li>
<li><strong>FASTENING</strong> — fastens a part.</li>
<li><strong>IF GOTO</strong> — branches to another program step when a condition is met.</li>
<li><strong>ACTION</strong> — triggers an input/output action.</li>
<li><strong>WAIT</strong> — pauses execution for a specified time.</li>
<li><strong>NAILING</strong> — performs a nailing operation; listed under Legacy.</li>
</ul>
<h3>Set the initial and final robot positions</h3>
<p>Begin with <strong>MOVE</strong>, which can also be configured within the <strong>START</strong> and <strong>END</strong> steps to define the robot's initial and final positions. Select the corresponding step and use the robot movement controls on the right to set the required position. The screenshot highlights <strong>START</strong>, <strong>END</strong>, and the robot movement controls.</p>
<p><a href="images/download/attachments/150697437/pick-tutorial-start-end-2026-09-17.png" rel="noopener" target="_blank"><img alt="START and END steps and the robot movement controls outlined in Programming mode" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697437/pick-tutorial-start-end-2026-09-17.png" width="800"/></a></p>
<h2>5. Configure the Pick operation</h2>
<p>Add a <strong>PICK</strong> operation and select the source tray. Use <strong>Single element</strong> to choose whether the operation handles one part or the whole tray. Turn it <strong>off</strong> to work with all parts in the selected tray; turn it on to pick a single part. For this example, leave it off.</p>
<p><a href="images/download/attachments/150697437/pick-tutorial-pick-options-2026-09-17.png" rel="noopener" target="_blank"><img alt="Pick settings with the Single element toggle outlined and switched off" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697437/pick-tutorial-pick-options-2026-09-17.png" width="800"/></a></p>
<p>The Pick operation provides settings for part selection, gripping, robot configuration, and approach and retract movements:</p>
<ul>
<li><strong>Main Pick settings.</strong> Select the tool's <strong>TCP</strong> and the source tray. Set <strong>Order</strong> to choose the picking sequence, <strong>Preferred part</strong> to select a part type when needed, and <strong>Pick point</strong> to choose the gripping point defined for the part.</li>
<li><strong>Pick position adjustment.</strong> Use the Pick position controls to adjust the robot pose manually and refine how the tool approaches the part.</li>
<li><strong>Fix.</strong> Use this option in the robot configuration settings to correct an unsuitable joint configuration when the robot's axes fold into an undesirable pose.</li>
<li><strong>Avoid collisions.</strong> Enable this option for the relevant movement segments so that trajectory calculation plans a path around obstacles. Use <strong>Safe Path</strong> to calculate movements with collision avoidance enabled.</li>
<li><strong>Safe move distance.</strong> Set the clearance distance for the robot's approach to and withdrawal from the pick point. Adjust the safe move direction and speed as needed for the part and surrounding objects.</li>
</ul>
<p>For detailed command settings, see <a href="programming-mode.md">Programming Mode</a>.</p>
<p>For the<strong class=""> Place</strong> command, simply select the target cell using the left mouse button where the parts will be placed.</p>
<p><a href="images/download/attachments/150697437/pick-tutorial-place-2026-09-17.png" rel="noopener" target="_blank"><img alt="Place operation with the empty destination tray highlighted" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697437/pick-tutorial-place-2026-09-17.png" width="800"/></a></p>
<p>The <strong class="">IF</strong> command allows the program to loop the preceding commands and properly terminate them. In this case, we specify that if all parts have been removed from the table, the robot returns to its Home position.</p>
<p><a href="images/download/attachments/150697437/pick-tutorial-condition-2026-09-17.png" rel="noopener" target="_blank"><img alt="IF condition checking whether Table 2 is empty" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697437/pick-tutorial-condition-2026-09-17.png" width="294"/></a></p>
<p>When your program is ready, you need to calculate it before starting the simulation. Use the Recalculate button for this. You will visually see the trajectory along which your robot will move the parts.</p>
<p><a href="images/download/attachments/150697437/pick-tutorial-calculated-2026-09-17.png" rel="noopener" target="_blank"><img alt="Calculated robot trajectories for the Pick and Place program" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697437/pick-tutorial-calculated-2026-09-17.png" width="800"/></a></p>
<h2 id="pick-place-simulation">6. Simulate the program and check the gripper</h2>
<p>Use the <strong>simulation slider on the right side of the screen</strong> to start the simulation and adjust its speed. The percentage markings indicate the simulation speed.</p>
<p><a href="images/download/attachments/150697437/pick-tutorial-simulation-2026-09-17.png" rel="noopener" target="_blank"><img alt="Simulation running with the speed slider on the right outlined" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697437/pick-tutorial-simulation-2026-09-17.png" width="800"/></a></p>
<p>During simulation, you can see that the gripper jaws do not close around the part. To correct this, configure the gripper's opening and closing actions in <strong>Project settings</strong>.</p>
<h3>Assign the opening and closing actions</h3>
<p>Open <strong>Project settings &gt; End effector parameters</strong>, select your tool, and open its gripper settings. In this example, the path is <strong>Composite end effector &gt; Grippers &gt; My TCP</strong>. Assign <strong>TCP - Open</strong> to <strong>Open IO</strong> and <strong>TCP - Close</strong> to <strong>Close IO</strong>.</p>
<p><a href="images/download/attachments/150697437/pick-tutorial-gripper-2026-09-17.png" rel="noopener" target="_blank"><img alt="Gripper settings linking Open IO to TCP - Open and Close IO to TCP - Close" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697437/pick-tutorial-gripper-2026-09-17.png" width="800"/></a></p>
<h3>Configure the IO signals and linked gripper axis</h3>
<p>Go to <strong>Project settings &gt; IO</strong> and select <strong>TCP - Open</strong>. Open its <strong>Input</strong> and <strong>Output</strong> sections and use <strong>Add</strong> to create an item in each. Configure the signal and the associated gripper axis:</p>
<ul>
<li><strong>Input number / Output number</strong> — the input or output signal number used by the action.</li>
<li><strong>Value</strong> — the expected input value or the value sent to the output.</li>
<li><strong>Linked axis</strong> — the tool axis associated with the signal.</li>
<li><strong>Linked axis value</strong> — the axis value corresponding to the required gripper position.</li>
</ul>
<p>The combined illustration shows the <strong>Input</strong> settings above and the <strong>Output</strong> settings below. In this example, both use signal number <strong>0</strong>, signal value <strong>1</strong>, and linked axis value <strong>50</strong> for the open position. <strong>The IO signal and linked axis values shown here are illustrative only.</strong> Actual production equipment may require different values. Configure them to match the signals and gripper positions used by your robot and tool.</p>
<p><a href="images/download/attachments/150697437/pick-tutorial-io-combined-2026-09-17.png" rel="noopener" target="_blank"><img alt="TCP - Open Input and Output parameter panels combined, showing signal number, value, linked axis, and linked axis value" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697437/pick-tutorial-io-combined-2026-09-17.png" width="800"/></a></p>
<p>Repeat the same procedure for <strong>TCP - Close</strong>: add and configure its Input and Output items, specifying the signal parameters and the linked axis value for the closed gripping position. Click <strong>Apply</strong> to save the settings.</p>
<p>Run the simulation again. The gripper now responds to the opening and closing signals, moving its fingers to grip and release the parts during the Pick and Place sequence.</p>
<p><a href="images/download/attachments/150697437/pick-tutorial-gripper-result-2026-09-17.png" rel="noopener" target="_blank"><img alt="Pick and Place simulation with the gripper fingers responding to the configured opening and closing actions" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697437/pick-tutorial-gripper-result-2026-09-17.png" width="800"/></a></p>
<h2 id="pick-place-run">7. Connect to the robot in Run mode</h2>
<p>Switch to the <strong>Run</strong> tab to connect to the physical robot. Before connecting, open <strong>Project settings &gt; Main &gt; Robot driver settings</strong> and set the robot's <strong>IP address</strong> to match your robot controller.</p>
<p>Return to <strong>Run</strong> and click <strong>Offline</strong> at the top of the screen to establish the connection. Once the robot is connected, the button changes to <strong>Online</strong>.</p>
<p><a href="images/download/attachments/150697437/pick-tutorial-run-2026-09-17.png" rel="noopener" target="_blank"><img alt="Run tab with the Offline connection button at the top and program status and speed controls on the right" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697437/pick-tutorial-run-2026-09-17.png" width="800"/></a></p>
</div></details>
</div>
<div class="section section-1" id="src-150697437_safe-id-aWQtLkludHJvZHVjdGlvbnRvRU5DWUh5cGVydjEtUGlja2FuZHBsYWNlKHRyYW5zZmVyb2Z0aGVwYXJ0ZnJvbXRoZXdvcmtiZW5jaHRvdGhlbWFjaGluZWFuZGJhY2suKS4">
<h1 class="heading"><span>Pick and place (transfer of the part from the workbench to the machine and back.).</span></h1>
<p>Example of part loading/unloading onto machine.</p>
<details class="scroll-expand-container"><summary class="scroll-expand-control">Click here to expand..</summary><div class="scroll-expand-content">
<p> <span style="color: #000000;">
First, import the <a href="attachments/150698029/3/Test_Project.zip">project</a> on the Start Page. <a href="home-page.md">See more</a> </span>
</p>
<p> <span style="color: #000000;">
After loading the project, open it and add an object representing a CNC machine.<br/> </span>
</p>
<p> <span style="color: #000000;">
<img alt="images/download/attachments/150697437/image2025-12-19_16-27-29.png" class="confluence-embedded-image confluence-content-image-border manual-image manual-screenshot" src="images/download/attachments/150697437/image2025-12-19_16-27-29.png" width="800"/>
<br/> </span>
</p>
<p>Add a cell for part processing on the machine surface.</p>
<p><img alt="images/download/attachments/150697437/image2025-12-19_16-30-39.png" class="confluence-embedded-image confluence-content-image-border manual-image manual-screenshot" src="images/download/attachments/150697437/image2025-12-19_16-30-39.png" width="800"/>
</p>
<p>Add a table where the parts will be stored. Add and configure the cell parameters for the table.</p>
<p><img alt="images/download/attachments/150697437/image2025-12-19_16-36-30.png" class="confluence-embedded-image confluence-content-image-border manual-image manual-screenshot" src="images/download/attachments/150697437/image2025-12-19_16-36-30.png" width="800"/>
</p>
<p>Add a table where the parts will be stored. Add and configure the cell parameters for the table.</p>
<p><img alt="images/download/attachments/150697437/image2025-12-22_12-22-14.png" class="confluence-embedded-image confluence-content-image-border manual-image manual-screenshot" src="images/download/attachments/150697437/image2025-12-22_12-22-14.png" width="800"/>
</p>
<p>On the Parts tab, create a cylinder and define its <strong class="">Pick Point</strong>. Leave the <strong class="">Base Point</strong> set to default.</p>
<p><img alt="images/download/attachments/150697437/image2025-12-22_10-24-27.png" class="confluence-embedded-image confluence-content-image-border manual-image manual-screenshot" src="images/download/attachments/150697437/image2025-12-22_10-24-27.png" width="800"/>
</p>
<p>Place the cylinders across the entire cell by holding the left mouse button.</p>
<p><img alt="images/download/attachments/150697437/image2025-12-22_12-23-16.png" class="confluence-embedded-image confluence-content-image-border manual-image manual-screenshot" src="images/download/attachments/150697437/image2025-12-22_12-23-16.png" width="800"/>
</p>
<p>The next step is to build the correct program that enables the robot to transfer parts to the machine for processing.</p>
<p>This robot is equipped with a tool that has two grippers. The logic of our program is to pick up a part and load it into the machine for processing, then place the processed part back onto the table.<br/>To ensure that all parts from the table are used, disable the <strong class="">Single element</strong> slider. Also place one part into the machine cell.</p>
<p><img alt="images/download/attachments/150697437/image2025-12-22_12-28-57.png" class="confluence-embedded-image confluence-content-image-border manual-image manual-screenshot" src="images/download/attachments/150697437/image2025-12-22_12-28-57.png" width="800"/>
</p>
<p>As a result, the robot picks up an unprocessed part from the table, then removes the processed part from the machine and replaces it.</p>
<p><img alt="images/download/attachments/150697437/image2025-12-22_12-40-36.png" class="confluence-embedded-image confluence-content-image-border manual-image manual-screenshot" src="images/download/attachments/150697437/image2025-12-22_12-40-36.png" width="248"/>
</p>
<p>Since we are using multiple parts from the table, the program needs to be looped. To do this, add an <strong class="">IF</strong> command and set the parameters required to loop the part transfer and processing workflow.</p>
<p><img alt="images/download/attachments/150697437/image2025-12-22_12-46-32.png" class="confluence-embedded-image confluence-content-image-border manual-image manual-screenshot" src="images/download/attachments/150697437/image2025-12-22_12-46-32.png" width="800"/>
</p>
<p>After recalculating all commands, the trajectory will appear. You can use the speed slider on the right to observe the program execution. The robot should transfer all parts to the machine and return them to the table.</p>
<p><img alt="images/download/attachments/150697437/image2025-12-22_12-48-1.png" class="confluence-embedded-image confluence-content-image-border manual-image manual-screenshot" src="images/download/attachments/150697437/image2025-12-22_12-48-1.png" width="800"/>
</p>
</div></details>
</div>
</div></div></div>
