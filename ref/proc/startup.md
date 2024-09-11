## startup proc
**See also:**
*   [params var (world)](/ref/world/var/params.md) -m
*   [shutdown proc](/ref/proc/shutdown.md) -m
<!-- -->
**Format:**
*   startup(File,Port=0,Options,\...)
<!-- -->
**Args:**
*   File* The dmb file to run in a new server or null to load the
    current world.
*   Port* The network port to start the new server on. A value of 0
    indicates that any available port should be used.
*   Options* Any number of the options listed below. Each option should
    be in an argument by itself. If the option takes a parameter, this
    can be in the same argument or in the following one.
### The valid options are:
-once
*   automatically shuts down the server when all players have logged
    off.
-close
*   Closes the child copy of DreamDaemon after the world it is running
    shuts down.
-log \<logfile\>
*   sends all server output to the specified file. The path to the file
    is relative to the world directory (the path containing the world
    `.dmb` file).
-logself
*   is identical to \"-log \[YourWorldFile\].log\".
-safe
*   runs the server in a special protective mode. The server may only
    access files in the same directory (or below) as the dmb file and
    access to the shell() command is disabled. This is the default mode
    if no security setting is specified and the world is run from a
    directory by the same name as the dmb file.
-home \<path\>
*   runs with the specified \"safe home\" directory. Normally, in safe
    mode the directory containing the world dmb file is the safe home.
-ultrasafe
*   like -safe, this prohibits all file access. This is the default if
    no security mode is specified and the world is not run from a
    directory with the same name.
-trusted
*   allows full access to files on the computer and to the shell()
    command. Note that this does not bypass the normal security of the
    operating system. For example, in the UNIX operating system, all of
    the usual access restrictions apply. This mode merely removes
    BYOND\'s built-in safety checks.
-params \<paramtext\>
*   this is for passing user-defined parameters to the world. Multiple
    parameters may be packed into a single argument or -params may be
    used several times. In either case, the parameters are all loaded
    into world.params when the world starts up. The parameter format is
    \"name1=value1&name2=value2&\...\".
-quiet
*   disables the server\'s normal output indicating the BYOND version
    number and network port.
-nologdates
*   disables automatic date/time output in the log.
-CGI
*   runs the world as a CGI program (to be executed by a web server). A
    /client object is automatically created for the user and any output
    sent to the associated mob gets returned to the user\'s web browser.
    This option is normally specified in the compile-time setting:
    [world.executor](/ref/world/var/executor.md) -m which is automatically
    initialized for you if you include `html/CGI.dm` from the html
    library.
-suid \<path\>
*   runs the world as the owner of the specified directory or path. This
    only works if DreamDaemon is running as root on operating systems
    where there even is such a thing.
-suidself
*   runs the world as the owner of the world dmb file. This only works
    if DreamDaemon is running as root on operating systems where there
    even is such a thing.
-cd \<path\>
*   runs with the specified working directory. Normally, the directory
    containing the world dmb file is used.
-port P
*   sets the network port to P. The port may also be specified as a
    positional argument (following the .dmb name).
-ports \<list\>
*   restricts the range of ports that DreamDaemon and any child worlds
    may use. The syntax of *list* is a comma separated list of ports or
    ranges of ports. Example* `-ports 1234,1236,1240-1250`.
-ip \<address\>
*   sets the IP address of the server. This will only work for an IP
    address the system recognizes as one it can use for hosting. Accepts
    numerical addresses only.
-webclient
*   Enables the webclient, overriding default behavior.
-nowebclient
*   Disables the webclient, overriding default behavior.
-verbose
*   Runtime errors will continue outputting details after a certain
    number of errors has been reached. Without this option, the number
    of errors that provide detailed info (such as call stack) is
    limited. Use this option with caution as it could fill up a log file
    quickly if a problem occurs.
<!-- -->
**Returns:**
*   The address of the new server in the form ip:port.