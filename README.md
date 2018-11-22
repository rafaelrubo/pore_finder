# pore_finder
Python routine to count porosity in a rock thin section segmented image

#############

This Python routine reads each line from a text file generated from a segmented RGB image and counts everytime that the value is different from 'white' (255 255 255).

The text files are obtained using 'Get RBG v.1.0', written by Zach Johnson, staff of 'The Imaging Technology Group - Beckman Institute', from the University of Illinois at Urbana-Champaign.

The images are from rock thin sections and they have been segmented to highlight only pores.

The routine calculates total porosity by dividing the amount of pixels different from white by the total amount of pixels from the image.
