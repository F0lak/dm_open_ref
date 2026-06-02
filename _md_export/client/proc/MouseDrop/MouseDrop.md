MouseDrop proc (client)
This is called when a mouse button is released after dragging an
        object.  The over_object may be null if dropping over a stat panel or over
        other empty space.
The argument format for this verb is:
MouseDrag(src_object as null|atom in usr.client,\
            over_object as null|atom in usr.client,\
            src_location as null|turf|text in usr.client,\
            over_location as null|turf|text in usr.client,\
            src_control as text, over_control as text, params as text)