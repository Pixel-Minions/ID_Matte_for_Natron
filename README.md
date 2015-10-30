# zID-Mask
ID masking tool for Natron 2.0


Hello everyone!
This is a my new Pyplug for Natron 2.0 that will allow you to use your Object ID, Material ID, etc as mask in Natron 2.0. It is based on the tool developed by Toxik for Fusion.

It is pretty straightforward to use.

Recommendations:

Use an image format that doesn't have quality loss (ex: exr, tga, etc).
The ID image should NOT have AA
It is recommended that the ID image should have twice the resolution of the beauty image.
You have 3 options:

Color Picker: That will allow you to Select the color. Just click the black square and use the picker over the ID pass using Ctrl + left mouse click.

Filter: Select the appropriate filter according the resolution of the image. Lanczos3 is a good filter when downscaling the image.

Scale Ratio: Changes the resolution of the output image. 0.5 means that the output image is 50% the size of the input image. It is useful when the ID image is twice the resolution of the beauty image.

Any problem or bug, just let me know. Be aware that Natron 2.0 is still in beta. And there may be bugs that should be fixed. At this point the tool works perfectly (September 27, 2015)

Installation

1. Copy the content to a folder called Ztools in your Plugins Folder, my recommendation: C:\Users\YOURUSERNAME\AppData\Local\INRIA\Natron\Plugins

2. Add the path of this folder in the Plug-ins Tab - PyPlugs search path in Natron Preferences
3. Restart Natron

The installation guide is inside the folder.

Enjoy.

