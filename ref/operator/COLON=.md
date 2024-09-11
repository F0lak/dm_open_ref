## := operator 
###### BYOND Version 514
**See also:**
*   [= operator](/ref/operator/=.md) -m
*   [operators](/ref/operator.md) -m<!-- -->
**Format:**
*   A := B


This is the \"assign into\" operator. The value of B is
evaluated, then A. If A is a datum that has an `operator:=` proc
overloading this operator, then that proc will be called with A as its
src and B as its only argument. The return value of the proc (which
defaults to its src, the old value of A) is assigned into the var that
holds A. 

If A was not a datum, then B is assigned into the var
as if this were an ordinary A = B assignment. 

A common use of
this operator might be to copy another datum. This is basically just
\"syntactic sugar\" to make certain datums easier to work with, and is
intended mainly for situations where you\'ve overloaded the operator.