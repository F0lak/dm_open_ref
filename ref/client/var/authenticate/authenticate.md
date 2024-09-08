[]{#/client/var/authenticate}
## authenticate var (client)
This value may be set to 0 at compile-time to disable BYOND hub-based
authentication of users. The default value is 1, which enables
authentication. Hub authentication provides an additional level of
assurance that the user is really the owner of the BYOND key in
question.
When a world requests certification, Dream Seeker generates a random
password and passes it through the hub (for certification) to the world.
The certificate is saved for faster access in the future and for
protection against possible hub outages.
Some applications do not depend on the validity of the user\'s identity.
In that case, it would be more efficient to turn off the extra level of
authentication. In other situations, the hub may not be available, such
as from behind a firewall or on a LAN without internet access. In those
cases, all hub access (including authentication) can be disabled by
entering the command \".configuration hub-address none\" in Dream
Seeker.
Connections to worlds on the same machine are not hub-authenticated to
allow for convenient offline testing.