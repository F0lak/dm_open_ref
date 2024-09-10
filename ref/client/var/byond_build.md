[]{#/byond_build var (client).md}    
## byond_build var (client) {#byond_build-var-client byondver="512"}    
**See also:**    
:   [DM_VERSION macro]/DM/preprocessor/DM_VERSION    
:   [byond_version var (client)]/client/var/byond_version    
:   [byond_version var (world)]/world/var/byond_version    
This is the build number (minor version) of BYOND being run by this    
client. Typically this is not useful information, but it can come in    
handy when diagnosing issues reported by players using a beta build.    
Clients running versions of BYOND prior to 512 (major version) will not    
have this information. It is also not guaranteed to exist for non-Dream    
Seeker connections. When not available, byond_build is 0.  