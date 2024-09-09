[]{#/proc/noise_hash}    
## noise_hash proc {#noise_hash-proc byondver="515"}    
**See also:**    
:   [rand proc](/ref/proc/rand)    
:   [rand_seed proc](/ref/proc/rand_seed)    
<!-- -->    
**Format:**    
:   noise_hash(num1, num2, num3\...)    
:   noise_hash(list_of_nums)    
:   noise_hash(hash_name, num1, num2, num3\...)    
:   noise_hash(hash_name, list_of_nums)    
<!-- -->    
**Returns:**    
:   A number between 0 and 1 (excluding 1 itself)    
<!-- -->    
**Args:**    
:   num1, num2, num3\...: Numbers to be hashed (at least one)    
:   list_of_nums: A list containing the numbers to hash    
:   hash_name: A text string indicating the hash type (reserved for    
    future use)    
For some games using concepts of procedural generation, it\'s nice to be    
able to reliably create pseudo-random numbers in a repeatable, reliable    
way. This proc takes all the numbers put into it and hashes them    
together to get a value from 0 to 1. That output value will be the same    
for any given set of input numbers. This can be used on its own or as    
part of a more in-depth noise algorithm.    
If the first argument is a string, that may be used in future versions    
to specify the type of hash to use. For now it is not used.    
Non-numbers provided to the proc will be interpreted arbitrarily. Don\'t    
do that.  