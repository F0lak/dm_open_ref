## GetAPI proc (client) 
###### BYOND Version 514

<!-- -->
**Format:**
+   GetAPI(Api, Name)
<!-- -->
**Args:**
+   Api: the name of the API (e.g. "steam")
+   Key: the name of the value to read


Interfaces with supported external APIs to read information.
Currently this only has meaning for Steam, for specially built games
that have a Steam app ID. 

This proc returns null any time the
call or its results are invalid: for instance, trying to query a Steam
stat from a user who isn\'t logged into Steam.
  -----------------------------------------------------------------------------------------------------
  Key                       Return type       Description                             
  ------------------------- ----------------- --------------------------------------- -----------------
  `"steam"` API\                                                                      
  Requires that the server                                                            
  and client are using a                                                              
  valid Steam app ID, such                                                            
  as when a game is built                                                             
  for standalone                                                                      
  distribution.                                                                       
  id                        text              Returns the user\'s numeric Steam ID,   
                                              if any. Because this number is too big  
                                              to fit in BYOND\'s numbering system, it 
                                              is returned as text.                    
  name                      text              Returns the user\'s persona name on     
                                              Steam.                                  
  stat:*Name*               num               Returns the value of the stat called    
                                              `Name`.                                 
  achievement:*Name*        num               Returns the date (for use with          
                                              [time2text](/ref/proc/time2text.md))   
                                              the achievement called `Name`, or 0 if  
                                              it hasn\'t been earned.                 
  achievement-data:*Name*   list              Returns information about the           
                                              achievement called `Name`. The result   
                                              is an associative list with named       
                                              values `name` (display name), `desc`    
                                              (description), and optionally `hidden`  
                                              and `icon`. (This call is the same no   
                                              matter which client you call it for.)   
  achievements              list              Returns a list of all possible          
                                              achievements. Each item in the list is  
                                              the internal name of the achievement,   
                                              and it is associated with a list in the 
                                              form described for                      
                                              `achievement-data:`*`Name`*. (This call 
                                              is the same no matter which client you  
                                              call it for.)                           
  -----------------------------------------------------------------------------------------------------

> [!TIP] 
> **See also:**
> +   [SetAPI proc (client)](/ref/client/proc/SetAPI.md) 
> +   [CheckPassport proc (client)](/ref/client/proc/CheckPassport.md) 