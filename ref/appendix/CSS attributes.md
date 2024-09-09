[]{#/{{appendix}}/css toc="CSS attributes"}    
## CSS attributes    
DM-CSS is a subset of CSS, and only supports some kinds of selectors and    
attributes.    
The following table lists all supported attributes, and whether they are    
supported in text output, maptext, and in other controls (labels/etc.)    
Other controls will often allow only one style for an entire unit of    
text. A checkbox in \"Other\" only indicates that *some* support exists    
in other controls, but it may vary by the type of control.    
  Attribute          Output   Maptext    
  ------------------ -------- ---------    
  color              ✔️       ✔️    
  background         ✔️       ✔️    
  background-color   ✔️       ✔️    
  background-image   ✔️           
  font               ✔️       ✔️    
  font-family        ✔️       ✔️    
  font-style         ✔️       ✔️    
  font-weight        ✔️       ✔️    
  font-size          ✔️       ✔️    
  text-decoration    ✔️       ✔️    
  text-align         ✔️       ✔️    
  vertical-align              ✔️    
  text-indent        ✔️       ✔️    
  margin-left        ✔️       ✔️    
  margin-right       ✔️       ✔️    
  margin-top                      
  margin-bottom                   
  margin             ✔️       ✔️    
  width              ✔️       ✔️    
  height             ✔️       ✔️    
  line-height        ✔️       ✔️    
  white-space        ✔️       ✔️    
  text-shadow                 ✔️    
  -dm-text-outline            ✔️    
These pseudo-classes are allowed in some contexts, but they can only    
change the text color.    
  Psuedo-class   Output   Maptext    
  -------------- -------- ---------    
  :link          ✔️       ✔️    
  :visited       ✔️           
  :active                     
  :hover                  ✔️  