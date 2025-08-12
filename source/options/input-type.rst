.. _input_type-label:

Input Type
==========


**Entire Sketch**
    Exports all sketch curves in one selectable color.

**Sketch Profiles**
    Exports profiles with selectable colors for each profile loop.
    Profiles loops are defined by their containment within each other.
    The outer most profile loop is identified as :blue-bold:`Perimeters`. Profile loops 
    immediately inside Perimeters are considered :blue-bold:`Insets` and profile loops 
    contained within Insets are considered :blue-bold:`Cutouts`. Lines not part of a 
    profile loop will be included as an Inset. The intent of this scheme is to provide 
    control of SVG line coloring in a predictable way. Options are provided to include 
    or exclude these profile types..

