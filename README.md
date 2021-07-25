# KSP-deltav-calc
A simple calculator to immediately calculate required delta-v level

Just make a body as your starting point and using the destination method you can get the delta-v levels to any place you want. The method takes the following arguments:

1) name: The name of the body ("Mun", "Minmus", "Jool", etc)
2) stage: The stage of flight at which you want your vessel to go. It can only be (for now): "Kerbin Orbit", "Intercept", "Low Orbit", "Land"
3) mode: The way in which you want the delta-v levels. It can only be "normal" and "cumulative" which will give you the delta-v levels from one stage of flight to the next and from the beginning to that stage of flight respectively.

Kerbin is the only body for now and it has 2 more methods:
1) to_orbit() : the delta-v to LKO
2) to_keostatinoary_orbit : the delta-v to a keostationary orbit
More bodies and features will be added.
