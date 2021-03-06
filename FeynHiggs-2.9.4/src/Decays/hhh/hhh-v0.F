#if 0
* hhh-v0.F
* form factors for {S[10, {hno}]} -> {S[10, {hno1}], S[10, {hno2}]}
* generated by FormCalc 7.5 on 27-Sep-2012 9:11
* this file is part of FeynHiggs
#endif

#include "hhh-vars.h"

	subroutine hhh_v0
	implicit none

#include "hhh-vars.h"

#include "inline.h"

        Ctree(1) = Ctree(1) + 
     &    1/2.D0*(EL0*MW*((C2A*CAB - 2*S2A*SAB)*Sub2 + 
     &          (2*CAB*S2A + C2A*SAB)*Sub3 + 
     &          C2B*(-(SAB*Sub5) + CAB*Sub7) - 
     &          3*C2A*(SAB*XHiggs(hno,1,uzext)*
     &              XHiggs(hno1,1,uzext)*XHiggs(hno2,1,uzext) + 
     &             CAB*XHiggs(hno,2,uzext)*XHiggs(hno1,2,uzext)*
     &              XHiggs(hno2,2,uzext))))/(CW2*SW)

#ifdef DETAILED_DEBUG
	DCOUP "v0: Ctree(1) =", Ctree(1) ENDL
#endif

	end
