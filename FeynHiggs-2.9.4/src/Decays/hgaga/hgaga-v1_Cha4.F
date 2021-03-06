#if 0
* hgaga-v1_Cha4.F
* form factors for {S[10, {hno}]} -> {V[1], V[1]}
* generated by FormCalc 7.5 on 27-Sep-2012 9:09
* this file is part of FeynHiggs
#endif

#include "hgaga-vars.h"

	subroutine hgaga_v1_Cha4
	implicit none

#include "hgaga-vars.h"

#include "inline.h"

        Cloop(1) = Cloop(1) + 
     &    1/(2.D0*Pi*sqrt2)*(Alfa0*EL0*MCha(Cha4)*
     &        (2*Sub40(Cha4)*
     &           (-(Pair1*(lint15(Cha4) - 4*lint16(cc00,Cha4) + 
     &                  2*m22*lint16(cc1,Cha4))) + 
     &             Sub8*lint16(cc2,Cha4) + 4*Abb2*Sub41(Cha4)) - 
     &          lint16(cc0,Cha4)*Sub44(Cha4)))/SW

#ifdef DETAILED_DEBUG
	DCOUP "v1_Cha4: Cloop(1) =", Cloop(1) ENDL
#endif

	end
