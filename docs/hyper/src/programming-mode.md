---
title: "Programming Mode"
---

<link rel="stylesheet" href="assets/manual.css">

<div id="ht-wrap-container"><div class="ht-content"><div class="ht-content-header"><h1 id="src-150697525"> <span>Programming Mode</span></h1></div><div class="wiki-content sp-grid-section" data-index-for-search="true" id="main-content">
<p><img alt="Programming mode with arrows identifying the program structure tree, calculation buttons, control panel, and simulation slider" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/programming-mode-annotated-2026-09-16.png" width="800"/>
</p>
<div class="section section-1" id="src-150697525_safe-id-aWQtLlByb2dyYW1taW5nTW9kZXYxLUFwcGxpY2F0aW9uQXJlYTo">
<h1 class="heading"><span>Application Area:</span></h1>
<p> <span style="color: #000000;">
Programming Mode represents the pivotal operational environment in which theoretical plans are executed and robotic systems become operational. It functions as a multifaceted control center—a dedicated workspace for automation management and system configuration.    </span>
</p>
<p> <span style="color: #000000;">
In Programming Mode, the <strong class="">Control Panel</strong> shifts to the right side of the screen and the <strong class="">Program Structure Tree</strong> is added.    </span>
</p>
<div class="section section-2" id="src-150697525_id-.ProgrammingModev1-Buttonsforcalculatethetrajectory.">
<h2 class="heading"><span>Buttons for calculate the trajectory.</span></h2>
<p> <span style="color: #000000;">
<span style="color: #000000;">
<strong class="">Quick</strong> </span>
<strong class=""> calculation</strong> <span style="color: #000000;">
<strong class=""> button. </strong>Calculates the trajectory without considering the checkboxes in <strong class="">collision avoidance</strong> commands.    </span>
</span>
</p>
<p> <span style="color: #000000;">
<span style="color: #000000;">
<strong class="">Safe</strong> </span>
<strong class=""> Path</strong> <span style="color: #000000;">
<strong class="">button. </strong>Computes trajectory with collision avoidance — only for commands where the flag is enabled.    </span>
<br/> </span>
</p>
</div>
<div class="section section-2" id="src-150697525_id-.ProgrammingModev1-Sliderforsimulation.">
<h2 class="heading"><span>Slider for simulation.</span></h2>
<p> <span style="color: #000000;">
Simulate trajectory (speed controlled by slider).<br/> </span>
</p>
</div>
<div class="section section-2" id="collision-detection">
<h2 class="heading"><span>Collision detection</span></h2>
<p><strong>Collision detection</strong> helps identify collisions between mechanisms and objects in your project. To enable it, open <strong>Project settings &gt; Main &gt; Simulation</strong> and turn on the <strong>Collision detection</strong> toggle.</p>
<p><a href="images/download/attachments/150697525/collision-detection-settings-2026-09-17.png" rel="noopener" target="_blank"><img alt="Simulation settings with the Collision detection toggle outlined" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/collision-detection-settings-2026-09-17.png" width="800"/></a></p>
<p>After you enable this option, ENCY Hyper builds a collision model for your project. A progress indicator appears at the top of the screen. Wait for the model to finish building before checking for collisions.</p>
<p><img alt="Collision model creation progress indicator" class="confluence-embedded-image manual-image manual-icon" src="images/download/attachments/150697525/collision-model-progress-2026-09-17.png" width="45"/></p>
<p>Once the model is ready, simulate the robot movements to check where collisions may occur between mechanisms and objects. Colliding components are highlighted in red in the graphics window, as shown below.</p>
<p><a href="images/download/attachments/150697525/collision-detection-example-2026-09-17.png" rel="noopener" target="_blank"><img alt="Programming Mode showing colliding components highlighted in red" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/collision-detection-example-2026-09-17.png" width="800"/></a></p>
</div>
<div class="section section-2" id="src-150697525_safe-id-aWQtLlByb2dyYW1taW5nTW9kZXYxLVRoZVByb2dyYW1TdHJ1Y3R1cmVUcmVlY29uc2lzdHNvZjo">
<h2 class="heading"><span>The Program Structure Tree consists of:</span></h2>
<p> <span style="color: #000000;">
<strong class=""><i class=""> <span style="color: #000000;">
Buttons:    </span>
</i></strong> </span>
</p>
<p><strong class=""> <span style="color: #000000;">
<strong class="">Add a command. </strong> </span>
</strong> <span style="color: #000000;">
Allows you to add basic commands.     </span>
<strong class=""> <span style="color: #000000;">
<strong class=""><img alt="Add command button with the plus sign highlighted" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/add-command-highlighted-2026-09-16.png" width="297"/>
</strong> </span>
</strong></p>
<p><strong class=""> <span style="color: #000000;">
<strong class="">Clear. </strong> </span>
</strong> <span style="color: #000000;">
To clear all commands and restart from the initial state.     </span>
<strong class=""> <span style="color: #000000;">
<img alt="Clear program menu item" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/clear-program-2026-09-16.png" width="158"/>
</span>
</strong></p>
<p><strong class=""><strong class=""> <span style="color: #000000;">
Creates a Group.    </span>
</strong></strong> <span style="color: #000000;">
Commands can be organized into groups. Once created, a group can be copied, and the tray assignments for all commands in the group can be modified collectively. Efficient handling of repetitive tasks across multiple trays. <img alt="Create group button" class="confluence-embedded-image manual-image manual-icon" src="images/download/attachments/150697525/create-group-clean-2026-09-16.png" width="30"/>
</span>
</p>
<p><strong class=""> <span style="color: #000000;">
<strong class=""><i class="">Commands:</i></strong> </span>
</strong></p>
<p><strong class=""> <span style="color: #000000;">
Start    </span>
<span style="color: #000000;">
.     </span>
</strong> <span style="color: #000000;">
Set robot initial position. The Control Panel features navigation for robot movement in space.     </span>
<span style="color: #000000;">
<a href="robot-navigation.md">See more</a> </span>
</p>
<p><strong class=""> <span style="color: #000000;">
End    </span>
<span style="color: #000000;">
.     </span>
</strong> <span style="color: #000000;">
Set    </span>
<span style="color: #000000;">
 robot final position. The Control Panel features navigation for robot movement in space. <a href="robot-navigation.md">See more</a> </span>
</p>
<p><strong class=""> <span style="color: #000000;">
MOVE    </span>
<span style="color: #000000;">
<strong class="">. </strong> </span>
</strong> <span style="color: #000000;">
Place robot at target position.    </span>
</p>
<details class="scroll-expand-container"><summary class="scroll-expand-control">Click here to expand..</summary><div class="scroll-expand-content">
<p> <span style="color: #000000;">
<i class=""><strong class="">Consists of:</strong></i> </span>
</p>
<p> <span style="color: #000000;">
<strong class="">List of Robot Positions</strong><strong class=""><strong class="">.</strong></strong><i class=""><strong class=""><strong class=""> </strong></strong></i>Remembers the robot’s position. You can assign a name to this position to use it again. The assigned name will be displayed in the robot’s programming tree structure.    </span>
</p>
<p> <span style="color: #000000;">
To add a new position, select <strong class="">Custom</strong><strong class=""> Positions</strong> and move the robot, then save the setting.<br/> </span>
</p>
<p> <span style="color: #000000;">
<img alt="MOVE command with the saved cnc position" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/move-command-2026-09-16.png" width="238"/>
</span>
</p>
<p> <span style="color: #000000;">
<strong class="">Avoid collisions. </strong>Allows calculating a safe trajectory for this movement.    </span>
</p>
<p> <span style="color: #000000;">
If you run the project using the <strong class="">quick</strong><strong class=""> calculation</strong><strong class=""> button</strong>, this checkbox will be ignored.    </span>
</p>
<p> <span style="color: #000000;">
<img alt="Quick calculation button" class="confluence-embedded-image manual-image manual-icon" src="images/download/attachments/150697525/quick-calculation-2026-09-16.png" width="70"/>
</span>
</p>
<p> <span style="color: #000000;">
When using the <strong class="">Safe</strong><strong class=""> Path</strong> button, it automatically calculates a collision‑avoidant trajectory if this option is enabled for the specific movement. <strong class="">The trajectory calculation will take longer.</strong><br/> </span>
</p>
<p> <span style="color: #000000;">
<img alt="images/download/thumbnails/150697525/image2025-12-16_12-17-21.png" class="confluence-embedded-image confluence-thumbnail manual-image manual-screenshot" src="images/download/thumbnails/150697525/image2025-12-16_12-17-21.png" width="149"/>
<br/> </span>
</p>
<p> <span style="color: #000000;">
<strong class="">Linear movement. </strong>Allows linear movement of the robot.    </span>
</p>
<p> <span style="color: #000000;">
<img alt="Robot movement along a curved path" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/movement-nonlinear-2026-09-16.png" width="300"/>
<img alt="Robot movement along a straight path" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/movement-linear-2026-09-16.png" width="300"/>
<br/> </span>
</p>
<p> <span style="color: #000000;">
<strong class="">Navigation for robot movement in space<i class="">. </i></strong>Allows moving the robot in space in various ways.<strong class=""><i class=""> </i></strong><a href="robot-navigation.md">See more</a> </span>
</p>
</div></details>
<p> <span style="color: #000000;">
<strong class="">PICK/PLACE. </strong>Enables the robot to pick up/place a part.    </span>
</p>
<details class="scroll-expand-container"><summary class="scroll-expand-control">Click here to expand..</summary><div class="scroll-expand-content">
<p> <span style="color: #000000;">
<i class=""><strong class="">Working principles:</strong></i><br/> </span>
</p>
<p> <span style="color: #000000;">
To <strong class="">pick</strong> a part, you need to perform a press action on it. The gripper moves to the part’s pickup point. This point was previously defined in the     </span>
<strong class="">Part mode</strong> <span style="color: #000000;">
.    </span>
</p>
<p><img alt="Robot and parts before a pick operation" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/pick-before-2026-09-16.png" width="309"/>
<img alt="Robot picking a part from the tray" class="confluence-embedded-image confluence-thumbnail manual-image manual-screenshot" src="images/download/attachments/150697525/pick-operation-2026-09-16.png" width="290"/>
</p>
<p>To <strong class="">place</strong> a part, you need to click on the attachment point in the tray.</p>
<p><img alt="Robot at the destination tray for a place operation" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/place-operation-2026-09-16.png" width="354"/>
</p>
<p> <span style="color: #000000;">
<i class=""><strong class="">Consists of:</strong></i> </span>
</p>
<p><strong class="">The control panel will change depending on the selected mode.</strong></p>
<p><strong class=""><img alt="images/download/thumbnails/150697525/image2025-12-16_15-35-18.png" class="confluence-embedded-image confluence-thumbnail manual-image manual-icon" src="images/download/thumbnails/150697525/image2025-12-16_15-35-18.png" width="32"/>
1. Pick options.</strong> This tab contains the main settings for gripping.</p>
<details class="scroll-expand-container"><summary class="scroll-expand-control">Click here to expand..</summary><div class="scroll-expand-content">
<p><strong class="">List of points for end effectors. </strong>Allows selecting a grip point on the end effector.</p>
<p><img alt="images/download/attachments/150697525/image2025-12-16_12-57-51.png" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/image2025-12-16_12-57-51.png" width="441"/>
</p>
<p><strong class="">Pick/Holder. </strong>Robot’s position during gripping / Robot position during part placement.</p>
<p><strong class="">Single element. </strong>Allows to take either one part or all parts from the <strong class="">tray.</strong></p>
<p>If you select the entire tray, you will see a template of the sequence for transferring parts from this tray in advance.<strong class=""><br/></strong></p>
<p><strong class=""><img alt="images/download/thumbnails/150697525/image2025-12-16_16-38-22.png" class="confluence-embedded-image confluence-thumbnail manual-image manual-screenshot" src="images/download/thumbnails/150697525/image2025-12-16_16-38-22.png" width="199"/>
</strong></p>
<p><strong class="">Strategy. </strong>Allows selecting a template for the sequence of part transfer from the tray.</p>
<p><strong class="">Spiral from outside.</strong></p>
<p><img alt="images/download/thumbnails/150697525/image2025-12-16_16-42-29.png" class="confluence-embedded-image confluence-thumbnail manual-image manual-screenshot" src="images/download/thumbnails/150697525/image2025-12-16_16-42-29.png" width="300"/>
</p>
<p><strong class="">Spiral from inside.</strong></p>
<p><strong class=""><img alt="images/download/thumbnails/150697525/image2025-12-16_16-42-44.png" class="confluence-embedded-image confluence-thumbnail manual-image manual-screenshot" src="images/download/thumbnails/150697525/image2025-12-16_16-42-44.png" width="300"/>
</strong></p>
<p><strong class="">Row.</strong></p>
<p><strong class=""><img alt="images/download/thumbnails/150697525/image2025-12-16_16-43-14.png" class="confluence-embedded-image confluence-thumbnail manual-image manual-screenshot" src="images/download/thumbnails/150697525/image2025-12-16_16-43-14.png" width="300"/>
</strong></p>
<p><strong class="">Column.</strong></p>
<p><strong class=""><img alt="images/download/attachments/150697525/image2025-12-16_16-43-47.png" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/image2025-12-16_16-43-47.png" width="310"/>
</strong></p>
<p><strong class="">Optimal.</strong></p>
<p><strong class=""><img alt="images/download/thumbnails/150697525/image2025-12-16_16-44-42.png" class="confluence-embedded-image confluence-thumbnail manual-image manual-screenshot" src="images/download/thumbnails/150697525/image2025-12-16_16-44-42.png" width="293"/>
</strong></p>
<p><strong class="">Custom. </strong>Set pickup/drop‑off order for parts.</p>
<p><strong class="">Preferred part. </strong>If the tray contains different types of parts (which we have defined in <strong class="">Part mode</strong>), this option allows you to specify exactly which ones to take.</p>
<p><strong class="">Pick point /Place point. </strong>List of hold points. Pick points are defined in <strong class="">Parts mode</strong> when specifying a part. You can edit them at any time either in this mode or in <strong class="">Parts mode</strong>.</p>
<p><img alt="images/download/attachments/150697525/image2025-12-16_14-32-58.png" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/image2025-12-16_14-32-58.png" width="241"/>
<img alt="images/download/attachments/150697525/image2025-12-16_14-34-24.png" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/image2025-12-16_14-34-24.png" width="202"/>
</p>
<p><strong class="">Avoid creases. </strong>Prevents axis twisting (robot joint overrotation).</p>
<p><strong class="">Skip unreachable points. </strong>When this option is activated, the robot will only pick up parts that it can reach. If this option is not activated and the robot cannot reach a part, the program will display an error and wait for the operator.</p>
</div></details>
<p><strong class=""><strong class=""><img alt="images/download/thumbnails/150697525/image2025-12-16_15-35-44.png" class="confluence-embedded-image confluence-thumbnail manual-image manual-icon" src="images/download/thumbnails/150697525/image2025-12-16_15-35-44.png" width="28"/>
</strong>2. Reference Point Editor. </strong>Allows editing the part’s grip point (if gripping with a gap is required).</p>
<p> <span style="color: #000000;">
The Control Panel features navigation for robot movement in space.     </span>
<a href="robot-navigation.md">See more</a></p>
<p><strong class=""><strong class=""><img alt="images/download/thumbnails/150697525/image2025-12-17_12-17-44.png" class="confluence-embedded-image confluence-thumbnail manual-image manual-icon" src="images/download/thumbnails/150697525/image2025-12-17_12-17-44.png" width="38"/>
</strong>3. Additional points for collision avoidance. </strong>Allows defining additional points or collision‑avoidance strategies between the pick, place, and clearance points.</p>
<details class="scroll-expand-container"><summary class="scroll-expand-control">Click here to expand..</summary><div class="scroll-expand-content">
<p><strong class="">Pick.</strong></p>
<p><strong class="">Avoid collisions. </strong> <span style="color: #000000;">
Handles collision avoidance up to the <strong class="">clearance point</strong>.    </span>
</p>
<p><strong class="">Checks. </strong> <span style="color: #000000;">
A check is required to verify the sensor. For example, to confirm that the tray has extended. In this case, the program will wait until the sensor sends a signal.    </span>
</p>
<p><strong class="">Reference point</strong></p>
<p><strong class="">Before. </strong> <span style="color: #000000;">
Allows moving to a specific point prior to part pick/place.    </span>
</p>
<p><strong class="">Avoid collisions. </strong>Handles movement from the <strong class="">clearance point</strong> to the <strong class="">pick/place point</strong>.</p>
<p><strong class="">After. </strong>Allows moving to a specific point after part <strong class="">pick/place</strong>.</p>
<p><strong class="">Avoid collisions. </strong>Handles movement from the <strong class="">pick/place point</strong> to the <strong class="">clearance point.</strong></p>
<p><strong class="">Edit. </strong>Allows setting a new robot position or editing the existing one.</p>
</div></details>
<p><strong class=""><img alt="images/download/thumbnails/150697525/image2025-12-17_12-16-36.png" class="confluence-embedded-image confluence-thumbnail manual-image manual-icon" src="images/download/thumbnails/150697525/image2025-12-17_12-16-36.png" width="36"/>
4. Clearance. </strong>The position the robot moves to prior to gripping the part.</p>
<details class="scroll-expand-container"><summary class="scroll-expand-control">Click here to expand..</summary><div class="scroll-expand-content">
<p><strong class="">Simple. </strong>Allows creating a simple approach to the grip point.</p>
<p><strong class="">Save move distance. </strong>The position the robot moves to prior to gripping the part.</p>
<p><strong class=""><img alt="images/download/thumbnails/150697525/image2025-12-16_15-51-18.png" class="confluence-embedded-image confluence-thumbnail manual-image manual-screenshot" src="images/download/thumbnails/150697525/image2025-12-16_15-51-18.png" width="300"/>
</strong></p>
<p><strong class="">Safe move direction. </strong>Allows specifying the axis along which to approach the grip point. (X+,X- and etc)</p>
<p><strong class="">Safe move speed. </strong>Allows slowing down the feed rate when approaching the grip point.</p>
<p><strong class="">Sub program. </strong> <span style="color: #000000;">
Allows creating a complex approach to the grip point (e.g., when the robot needs to retrieve a part from a machine, move to a chip‑blow‑off station, and then place the part).    </span>
</p>
<p> <span style="color: #000000;">
In this mode, you can create subroutines consisting of multiple steps (similar to a program tree). To do this, create a command using the «Add a command» button and drag the command not into the main tree, but into the subroutine.    </span>
</p>
<p> <span style="color: #000000;">
<strong class="">You can add commands such as MOVE or IO.</strong> </span>
</p>
<p><img alt="Adding a MOVE command to the approach sub program" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/sub-program-2026-09-16.png" width="300"/>
</p>
<p><br/>For MOVE commands, an option to move the robot in space is available. <a href="robot-navigation.md">See more</a></p>
<p><img alt="MOVE command settings in the sub program" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/sub-program-move-2026-09-16.png" width="300"/>
</p>
</div></details>
</div></details>
<p><strong class="">IF. </strong>Allows looping the program.</p>
<details class="scroll-expand-container"><summary class="scroll-expand-control">Click here to expand..</summary><div class="scroll-expand-content">
<p> <span style="color: #000000;">
<i class=""><strong class="">Working principles:</strong></i><br/> </span>
</p>
<p> <span style="color: #000000;">
If the program doesn’t have an <strong class="">IF</strong> statement, pick/place is performed for only one part.    </span>
</p>
<p><img alt="PICK and PLACE program without an IF statement" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/if-without-loop-2026-09-16.png" width="500"/>
</p>
<p> <span style="color: #000000;">
If you use an <strong class="">IF</strong> statement, it will loop the program. Meanwhile, the program tree shows which blocks the <strong class="">IF</strong> command works with (all commands fit into a single block).    </span>
</p>
<p> <span style="color: #000000;">
The program works in blocks.    </span>
 In this example, there are 3 blocks.</p>
<p> <span style="color: #000000;">
<strong class="">Block 1 - PICK:</strong> In this case, it looks at the tray and checks whether there is a part inside. Then it picks up the part.    </span>
</p>
<p> <span style="color: #000000;">
<strong class="">Block 2 - PLACE:</strong> It looks at the second tray and searches for a place to put the part.    </span>
</p>
<p> <span style="color: #000000;">
<strong class="">Block 3: - IF:</strong> It checks whether the table is empty, and depending on the answer, performs an action for YES or NO.    </span>
</p>
<p><img alt="images/download/attachments/150697525/if-loop-example-2026-09-16.png" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/if-loop-example-2026-09-16.png" width="500"/>
<img alt="images/download/attachments/150697525/image2025-12-17_11-40-4.png" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/image2025-12-17_11-40-4.png" width="266"/>
</p>
<p> <span style="color: #000000;">
<i class=""><strong class="">Consists of:</strong></i> </span>
</p>
<p><strong class="">IF.</strong> The main condition under which the loop executes.     <span style="color: #000000;">
This could be a condition such as <strong class="">Table</strong><strong class=""> empty</strong> or <strong class="">Table</strong><strong class=""> is</strong><strong class=""> processed</strong>.    </span>
</p>
<p><strong class=""> <span style="color: #000000;">
TARGET OBJECT.     </span>
</strong> <span style="color: #000000;">
The condition applies only to a specific part.    </span>
</p>
<p><strong class=""> <span style="color: #000000;">
YES.     </span>
</strong> <span style="color: #000000;">
What    </span>
<span style="color: #000000;">
 should be done if the condition is true?    </span>
</p>
<p><strong class=""> <span style="color: #000000;">
NO.     </span>
</strong> <span style="color: #000000;">
What should be done if the condition is false?    </span>
</p>
</div></details>
<p><strong class="">IO. </strong>This is required for managing inputs/outputs (external axes of machines and robots — machine doors, rails, etc.). <strong class="">IO</strong> is configured in <strong class="">Project Settings</strong>. <a href="main-menu.md">See more</a></p>
<details class="scroll-expand-container"><summary class="scroll-expand-control">Click here to expand..</summary><div class="scroll-expand-content">
<p> <span style="color: #000000;">
<i class=""><strong class="">Working principles:</strong></i> </span>
</p>
<p>Open <strong>Project settings</strong> and select <strong>IO</strong> in the left panel. The settings already contain predefined IO entries. Select an entry, such as <strong>Open door</strong>, and edit its settings to match your equipment.</p>
<p><img alt="Project settings with predefined IO entries and the Open door settings" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/io-settings-2026-09-16.png" width="500"/></p>
<p>You can also create your own IO entry. Click <strong>Add</strong> at the bottom of the IO list on the left, then configure the new entry.</p>
<p><img alt="Add button for creating a custom IO entry" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/io-add-2026-09-16.png" width="254"/></p>
<p>For example, let’s create an <strong>Open door cnc</strong> command in the settings.</p>
<p>You can configure any input and output signals. For example, let’s set output 250 to value 60. You also need to select the linked axis from the list and assign a value to it.</p>
<p><a href="images/download/attachments/150697525/io-output-settings-2026-09-16.png" rel="noopener" target="_blank"><img alt="IO output settings with output number 250, value 60, and linked axis parameters" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/io-output-settings-2026-09-16.png" width="800"/></a></p>
<p>In the IO window, you can select this action.</p>
<p><a href="images/download/attachments/150697525/io-control-2026-09-16.png" rel="noopener" target="_blank"><img alt="IO Control in Programming mode with IF set to True and ACTION set to Open door" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/io-control-2026-09-16.png" width="800"/></a></p>
<p> <span style="color: #000000;">
<i class=""><strong class="">Consists of:</strong></i> </span>
</p>
<p><strong class=""> <span style="color: #000000;">
IF.     </span>
</strong> <span style="color: #000000;">
It also allows checking a sensor before executing any IO action (e.g., open the machine door if the sensor indicates the machine is not in operation).    </span>
</p>
<p> <span style="color: #000000;">
<span style="color: #000000;">
<i class="">By default, you can trigger IO actions without conditions (True).</i> </span>
<br/> </span>
</p>
<p><strong class=""> <span style="color: #000000;">
ACTION.    </span>
</strong> <span style="color: #000000;">
</span>
<span style="color: #000000;">
It allows you to run the macro event that was configured in the project settings.    </span>
</p>
</div></details>
<p><strong class="">PAUSE. </strong>It allows you to set a delay between actions.</p>
<details class="scroll-expand-container"><summary class="scroll-expand-control">Click here to expand..</summary><div class="scroll-expand-content">
<p><i class=""><strong class="">Consists of:</strong></i></p>
<p><strong class="">WAIT UNTIL. </strong>It allows you to set a delay that waits for a specific event. If a sensor is set to be waited for, the Time field changes its value to reflect the polling interval of that sensor.</p>
<p><i class="">By default without conditions (True).</i> <span style="color: #000000;">
</span>
</p>
<p><strong class="">TIME(sec). </strong>It specifies how many seconds to wait.</p>
</div></details>
<p class="auto-cursor-target"><strong class="">NAILING. </strong>The functionality is designed for nail driving.</p>
<details class="scroll-expand-container"><summary class="scroll-expand-control">Click here to expand..</summary><div class="scroll-expand-content">
<p><i class=""><strong class="">Working principles:</strong></i><br/></p>
<p>The robot approaches the point, sends a signal to the end effector, which pushes the nail and turns it off.</p>
<p><img alt="Robot performing a nailing operation" class="confluence-embedded-image confluence-thumbnail manual-image manual-screenshot" src="images/download/attachments/150697525/nailing-2026-09-16.png" width="238"/>
</p>
<p> <span style="color: #000000;">
<i class=""><strong class="">Consists of:</strong></i> </span>
</p>
<p> <span style="color: #000000;">
<strong class="">Processing action. </strong>It allows you to define an <strong class="">IO</strong> event (to send a signal to the end effector for driving nails).    </span>
</p>
<p> <span style="color: #000000;">
The parameters are the same as in the <strong class="">PICK</strong> operation.    </span>
</p>
</div></details>
<p class="auto-cursor-target" id="operation-welding"><strong class="">WELDING. </strong>Joins parts using spot welding or continuous seam welding.</p>
<details class="scroll-expand-container"><summary class="scroll-expand-control">Click here to expand..</summary><div class="scroll-expand-content">
<p><i><strong>Working principles:</strong></i></p>
<p>For spot welding, the robot positions the welding tool at each specified point and performs a weld. For seam welding, the robot moves the tool continuously along the specified seam while welding.</p>
<p><a href="images/download/attachments/150697525/welding-2026-09-16.png" rel="noopener" target="_blank"><img alt="Robotic welding cell with the welding tool positioned at the joint" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/welding-2026-09-16.png" width="400"/></a></p>
</div></details>
<p class="auto-cursor-target" id="operation-gluing"><strong class="">GLUING. </strong>Applies adhesive to bond parts together.</p>
<details class="scroll-expand-container"><summary class="scroll-expand-control">Click here to expand..</summary><div class="scroll-expand-content">
<p><i><strong>Working principles:</strong></i></p>
<p>The operation follows the same point-based or continuous-path approach as welding. The robot positions the dispensing tool at specified points or moves it along a specified path while dispensing adhesive. The adhesive is applied to the bonding surfaces to join the parts.</p>
<p><a href="images/download/attachments/150697525/gluing-2026-09-16.png" rel="noopener" target="_blank"><img alt="Robot dispensing adhesive along the programmed path on a part" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/gluing-2026-09-16.png" width="400"/></a></p>
</div></details>
<p class="auto-cursor-target" id="operation-polishing"><strong class="">POLISHING. </strong>Performs a continuous polishing pass along a specified seam. The robot guides the polishing tool along the seam to finish its surface.</p>
<p class="auto-cursor-target" id="operation-trajectory"><strong>TRAJECTORY. </strong>Imports a trajectory from a CAM system into <strong>ENCY Hyper</strong>. A simple way to do this is to import a saved CAM project, starting with a cell created in <strong>MachineMaker</strong>.</p>
<details class="scroll-expand-container"><summary class="scroll-expand-control">Click here to expand..</summary><div class="scroll-expand-content">
<p><strong>1. Prepare the cell and CAM operation.</strong> Create the cell in <strong>MachineMaker</strong>, save the project in <strong>.mma</strong> format, and click the button to export it to the CAM system. In the CAM system, create the machining operations. This example uses a simple <strong>2D contouring</strong> operation.</p>
<p><a href="images/download/attachments/150697525/trajectory-cam-operation-2026-09-17.png" rel="noopener" target="_blank"><img alt="A simple 2D contouring operation prepared in the CAM system" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/trajectory-cam-operation-2026-09-17.png" width="800"/></a></p>
<p><strong>2. Save the CAM project and configure the application path.</strong> Save the project in the CAM system. In <strong>ENCY Hyper</strong>, open <strong>Project settings &gt; Main &gt; CAM integration</strong>. In <strong>Path to the CAM application</strong>, specify the path to your CAM application shortcut and click <strong>Apply</strong>.</p>
<p><a href="images/download/attachments/150697525/trajectory-cam-integration-2026-09-17.png" rel="noopener" target="_blank"><img alt="CAM integration settings with the Path to the CAM application field" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/trajectory-cam-integration-2026-09-17.png" width="800"/></a></p>
<p><strong>3. Import the trajectory.</strong> In <strong>Programming Mode</strong>, create a <strong>Trajectory</strong> operation and select the saved CAM project in the file browser. <strong>ENCY Hyper</strong> launches the CAM system and retrieves the trajectory from the operation you created. The imported trajectory then appears in <strong>ENCY Hyper</strong>, as shown below.</p>
<p><a href="images/download/attachments/150697525/trajectory-imported-2026-09-17.png" rel="noopener" target="_blank"><img alt="The imported 2D contouring trajectory displayed in ENCY Hyper Programming Mode" class="confluence-embedded-image manual-image manual-screenshot" src="images/download/attachments/150697525/trajectory-imported-2026-09-17.png" width="800"/></a></p>
</div></details>
</div>
</div>
</div></div></div>
