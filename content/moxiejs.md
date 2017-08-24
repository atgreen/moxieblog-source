Title: moxiejs: another javascript Moxie simulator
Date: 2016-03-04
Author: green
Category: moxie
Tags: javascript
Slug: introducing-moxiejs

Here's something cool...

<script src="{filename}/js/moxieprocess.js"></script>
<script src="{filename}/js/main.js"></script>
<script async src="{filename}/js/moxiecpu.js" onload="OnAsmJsLoaded()"></script>

<select id="program" name="program" onchange="OnProgramChange()">
<option value="elf/binarytrees">binarytrees</option>
<option value="elf/fasta">fasta</option>
<option value="elf/fannkuchredux">fannkuchredux</option>
<option value="elf/nbody">nbody</option>
<option value="elf/lissa">lissa</option>
</select>
<input id="args" type="text">
<button onclick="OnRunClick()">Run</button>
<p>stdout:
<pre id="stdout"></pre>
<p>stderr:
<pre id="stderr"></pre>
<canvas id="canvas"></canvas>




