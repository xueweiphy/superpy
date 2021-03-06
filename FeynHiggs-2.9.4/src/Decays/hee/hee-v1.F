#if 0
* hee-v1.F
* form factors for {S[10, {hno}]} -> {F[2, {gno1}], -F[2, {gno2}]}
* generated by FormCalc 7.5 on 27-Sep-2012 9:15
* this file is part of FeynHiggs
#endif

#include "hee-vars.h"

	subroutine hee_v1
	implicit none

#include "hee-vars.h"

	ComplexType dup1, dup10, dup11, dup12, dup13, dup14, dup15
	ComplexType dup16, dup17, dup18, dup19, dup2, dup20, dup3
	ComplexType dup4, dup5, dup6, dup7, dup8, dup9, tmp1

#include "inline.h"

	dup1 = SAB*XHiggs(hno,1,uzext) - CAB*XHiggs(hno,2,uzext)

	dup2 = -(SAB*XHiggs(hno,1,uzext)) + CAB*XHiggs(hno,2,uzext)

	dup3 = SBA*XHiggs(hno,1,uzext) + CBA*XHiggs(hno,2,uzext)

	dup4 = CBA*XHiggs(hno,1,uzext) - SBA*XHiggs(hno,2,uzext)

        dup5 = cI*XHiggs(hno,3,uzext) + 
     &    CBA*XHiggs(hno,1,uzext) - SBA*XHiggs(hno,2,uzext)

	dup6 = (-2*m12 + 2*m32)*Sub1 - (F1 + F2)*Mf2(2,gno1)

	dup7 = (-m12 + m22 - 3*m32)*Sub1 + (F1 + F2)*Mf2(2,gno1)

	dup8 = (-2*m22 - MZ2)*Sub1 + (F1 + F2)*Mf2(2,gno1)

	dup9 = F1*(m12 - m22 + 3*m32 - 2*Mf2(2,gno1)) - F2*Mf2(2,gno1)

	dup10 = 2*F2*Mf2(2,gno1) + F1*(2*m12 - 2*m32 + Mf2(2,gno1))

        dup11 = C2A*SAB*XHiggs(hno,1,uzext) + 
     &    CAB*(2*S2A*XHiggs(hno,1,uzext) - 
     &       3*C2A*XHiggs(hno,2,uzext))

        dup12 = C2B*(SAB*XHiggs(hno,1,uzext) - 
     &       CAB*XHiggs(hno,2,uzext)) + 
     &    2*CW2*(SBA*XHiggs(hno,1,uzext) + CBA*XHiggs(hno,2,uzext))

        dup13 = S2A*(-2*SAB*XHiggs(hno,1,uzext) + 
     &       2*CAB*XHiggs(hno,2,uzext)) + 
     &    C2A*(CAB*XHiggs(hno,1,uzext) + SAB*XHiggs(hno,2,uzext))

        dup14 = 2*S2A*SAB*XHiggs(hno,2,uzext) + 
     &    C2A*(3*SAB*XHiggs(hno,1,uzext) - CAB*XHiggs(hno,2,uzext))

        dup15 = cI*(CW2*XHiggs(hno,3,uzext)) + 
     &    (CBA*CW2 - S2B*SAB)*XHiggs(hno,1,uzext) + 
     &    (CAB*S2B - CW2*SBA)*XHiggs(hno,2,uzext)

        dup16 = -(cI*((F1 - F2)*SB*XHiggs(hno,3,uzext))) + 
     &    (F1 + F2)*(SA*XHiggs(hno,1,uzext) - 
     &       CA*XHiggs(hno,2,uzext))

        dup17 = cI*((F1 - F2)*SB*XHiggs(hno,3,uzext)) + 
     &    (F1 + F2)*(SA*XHiggs(hno,1,uzext) - 
     &       CA*XHiggs(hno,2,uzext))

        dup18 = (m12 - m22 + 3*m32)*
     &     (2*F2*SW2 + F1*(-1 + 2*SW2)) + Sub25*Mf2(2,gno1)

        dup19 = (2*m22 + MZ2)*(2*F2*SW2 + F1*(-1 + 2*SW2)) + 
     &    Sub26*Mf2(2,gno1)

        dup20 = 2*(m12 - m32)*(2*F2*SW2 + F1*(-1 + 2*SW2)) - 
     &    Sub27*Mf2(2,gno1)

        tmp1 = cI/(128.D0*Pi**2)*
     &    (ELMZ*Delta(gno1,gno2)*
     &       (cI*(CW*(F1 - F2)*MW2*
     &            ((lint41 + 2*lint43)*Sub54 + 
     &              Sub55*Sub56*
     &               (CW2*(lint40 + 2*lint42) + 
     &                 (-lint40 - 2*lint42)*SW2))) + 
     &         2*Pi*(32*Pi*
     &             (AbbSum2*CW*CW2**2*SW2*
     &               (dMh0G0sq1*XHiggs(hno,1,uzext) + 
     &                 dMHHG0sq1*XHiggs(hno,2,uzext))) + 
     &            (CW*(-2*AlfaMZ*C2B*MW2*
     &                   (SAB*
     &                      (CBA*(2*F1 - 2*F2)*lint54 + 
     &                       lint50*Sub57) + 
     &                     CAB*
     &                      ((2*F1 - 2*F2)*lint56*SBA + 
     &                       lint51*Sub58)) + 
     &                  AbbSum2*CW2*
     &                   (AlfaMZ*
     &                      (C2A*(-lint45 + lint46) + 
     &                       C2B*
     &                       (-3*lint44 - 2*lint47 + 2*lint48 + 
     &                       3*lint49))*S2B + 
     &                     16*Pi*
     &                      (CW2*
     &                       (2*dMA0G0sq1 + 
     &                       dZA0G01*(-2*m12 + MA02))*SW2))) + 
     &               32*Pi*
     &                (CW2**2*dZA0G01*MW*MZ*SW2*(F1 - 2*F2*SW2)))*
     &             XHiggs(hno,3,uzext)))*Mf(2,gno1))/
     &     (CW*CW2**2*MW*SW*SW2)

        tmp1 = tmp1 + cI/(32.D0*Pi)*
     &     (ELMZ*Delta(gno1,gno2)*
     &        (AlfaMZ*CW*(-2*lint55*SBA*Sub59 + 
     &             2*CBA*lint57*Sub61 - lint52*Sub63 + lint53*Sub65
     &             ) + Pi*(CW2**2*dZA0G01*F2*MW*MZ*SW2*
     &             (-16 + 32*SW2)))*Mf(2,gno1)*XHiggs(hno,3,uzext))
     &       /(CW*CW2**2*MW*SW*SW2)

        Cloop(1) = Cloop(1) + 
     &    1/(32.D0*Pi)*(Pi*(CB2*CW2*
     &           ((32*CB*MW*MW2*SW*SW2*tmp1)/(m12 - MZ2) - 
     &             8*ELMZ*(F1*Sub82 - cI*(F2*MW2*Sub75*SW2)))) + 
     &        AlfaMZ*ELMZ*Delta(gno1,gno2)*Mf(2,gno1)*
     &         (CB2*MW2*(dup17*lint34*(8 - 16*SW2)*SW2 + 
     &              dup4*SB*
     &               (lint16*(-2*F2*SW2 + F1*(-1 + 2*SW2)) + 
     &                 dup8*lint17(cc0) + dup7*lint17(cc1) - 
     &                 dup6*lint17(cc2)) + 
     &              CB*dup3*
     &               (-(dup8*lint11(cc0)) - dup7*lint11(cc1) + 
     &                 dup6*lint11(cc2) + 
     &                 CW2*
     &                  (-2*dup10*lint10(cc2) + 
     &                    F2*(4*m22*lint9(cc0) + 2*MW2*lint9(cc0)))
     &                 ) + 
     &              CW2*(dup5*SB*
     &                  (F1*
     &                     (-4*m22*lint20(cc0) - 
     &                       2*(lint19 + MW2*lint20(cc0))) - 
     &                    2*dup9*lint20(cc1)) + 
     &                 2*(dup10*dup5*SB*lint20(cc2) + 
     &                    CB*dup3*
     &                     (dup9*lint10(cc1) + 
     &                       F1*lint10(cc0)*
     &                       (2*m22 + MW2 - 3*Mf2(2,gno1)))))) + 
     &           CW2*(CA2*dup16*lint22 + 
     &              CB2*(-(dup16*lint34) + 
     &                 MW2*
     &                  (6*dup5*F1*SB*lint20(cc0) - 
     &                    6*CB*dup3*F2*lint9(cc0))))*Mf2(2,gno1)))/
     &      (CB*CB2*CW2*MW*MW2*SW*SW2)

        Cloop(1) = Cloop(1) + 
     &    1/(32.D0*Pi)*(AlfaMZ*ELMZ*Delta(gno1,gno2)*
     &        (MW2*(CB*(2*dup12*SB2*
     &                 (F1*lint12(cc1) + F2*lint12(cc2)) + 
     &                CA*dup13*SA*
     &                 (-((F1 + F2)*lint13(cc0)) + 
     &                   F1*lint13(cc1) + F2*lint13(cc1) + 
     &                   F1*lint13(cc2) + F2*lint13(cc2) - 
     &                   F1*lint14(cc0) - F2*lint14(cc0) + 
     &                   F1*lint14(cc1) + F2*lint14(cc1) + 
     &                   F1*lint14(cc2) + F2*lint14(cc2)) + 
     &                dup14*(F1 + F2)*SA2*
     &                 (-lint15(cc0) + lint15(cc1) + lint15(cc2)))+
     &               2*CB2*dup15*SB*
     &              (F1*lint33(cc1) + F2*lint33(cc2))) + 
     &          CW2*dup16*(SB2*
     &              (-lint16 - m12*lint35(cc1) + 
     &                (-m22 + m32)*lint35(cc1) - 2*m22*lint35(cc2))
     &               + SA2*
     &              (lint21 + (m12 + m22 - m32)*lint36(cc1)) + 
     &             CA2*(m12 + m22 - m32)*lint37(cc1)))*Mf(2,gno1)*
     &        Mf2(2,gno1))/(CB*CB2*CW2*MW*MW2*SW*SW2)

        Cloop(1) = Cloop(1) + 
     &    1/(32.D0*Pi)*(AlfaMZ*ELMZ*Delta(gno1,gno2)*Mf(2,gno1)*
     &        (CB*CB2*MW2*Sub17*
     &           (CW2*(F1*Sub18 + F2*Sub19) + 
     &             MW2*(16*F1*SW2**2 + F2*(4 + SW2*(-16 + 16*SW2)))
     &             )*lint1(cc1) + 
     &          CW2*(CB2*(CW2*dup16*
     &                 ((-m12 + m32)*lint38(cc1) + 
     &                   m22*(-lint38(cc1) - 2*lint38(cc2))) + 
     &                dup2*(F1 + F2)*MW2*S2B*SB*
     &                 (lint7(cc0) + lint7(cc1) + lint7(cc2))) + 
     &             CB*(F1 + F2)*MW2*
     &              (C2B*(-(CB2*Sub16*lint1(cc1)) + 
     &                   dup1*SB2*
     &                    (lint6(cc0) + lint6(cc1) + lint6(cc2)))+
     &                  CA2*dup11*
     &                 (lint8(cc0) - lint8(cc1) - lint8(cc2))))*
     &           Mf2(2,gno1) + 
     &          2*CW2**2*(dup17*
     &              (SA2*lint36(cc0) + CA2*lint37(cc0)) - 
     &             dup16*(SB2*lint35(cc0) + CB2*lint38(cc0)))*
     &           Mf2(2,gno1)**2))/(CB*CB2*CW2**2*MW*MW2*SW*SW2)

        Cloop(1) = Cloop(1) + 
     &    1/(32.D0*Pi)*(AlfaMZ*ELMZ*Delta(gno1,gno2)*Mf(2,gno1)*
     &        (4*CW2*(Sub50*SW2*(-1 + 2*SW2)*
     &              (m12*(lint2(cc1) - lint2(cc2)) + 
     &                (m22 - m32)*(lint2(cc1) + lint2(cc2))) + 
     &             ((F2*Sub47*(1 - 2*SW2)**2 + 
     &                   2*F1*(Sub48 + Sub49)*SW2**2)*lint2(cc1) + 
     &                (F1*Sub47*(1 - 2*SW2)**2 + 
     &                   2*F2*(Sub48 + Sub49)*SW2**2)*lint2(cc2))*
     &              Mf2(2,gno1)) + 
     &          CB*(lint1(cc0)*
     &              (Sub17*
     &                 (CW2*(F1*Sub22 - F2*Sub23) + 
     &                   AbbSum1*MW2*SW2*(-16 + 32*SW2)) - 
     &                C2B*CW2*(F1 + F2)*Sub16*Mf2(2,gno1)) + 
     &             lint1(cc2)*
     &              (Sub17*
     &                 (CW2*(F2*Sub20 - F1*Sub21) + 
     &                   MW2*
     &                    (16*F2*SW2**2 + 
     &                      F1*(4 + SW2*(-16 + 16*SW2)))) - 
     &                C2B*CW2*(F1 + F2)*Sub16*Mf2(2,gno1)))))/
     &      (CB*CW2**2*MW*SW*SW2)

        Cloop(1) = Cloop(1) + 
     &    1/(32.D0*Pi)*(AlfaMZ*ELMZ*Delta(gno1,gno2)*Mf(2,gno1)*
     &        (2*(CW2*(CA2*lint4(cc2) + SA2*lint5(cc2))*
     &              Mf2(2,gno1)*
     &              (Sub51*(m22 - Mf2(2,gno1)) - Sub50*Mf2(2,gno1))
     &               + CB2*MW2*lint2(cc0)*
     &              (2*Sub50*Sub52*SW2*(-1 + 2*SW2) + 
     &                (F2*Sub49 + F1*Sub48*(1 - 2*SW2)**2 + 
     &                   4*CW2*(-(F2*Sub49) + Sub51)*SW2)*
     &                 Mf2(2,gno1))) + 
     &          CB2*MW2*(-(SB*lint3(cc2)*
     &                (-(F1*Sub21*Sub24) + 
     &                  F1*S2B*Sub16*Mf2(2,gno1) + 
     &                  F2*(Sub20*Sub24 + S2B*Sub16*Mf2(2,gno1))))-
     &               (SB*(Sub14*lint3(cc0) + Sub12*lint3(cc1)) + 
     &                CB*(-2*Sub8*lint9(cc1) + 2*Sub4*lint9(cc2)))*
     &              XHiggs(hno,1,uzext) + 
     &             (SB*(Sub15*lint3(cc0) + Sub13*lint3(cc1)) + 
     &                CB*(2*Sub10*lint9(cc1) - 2*Sub6*lint9(cc2)))*
     &              XHiggs(hno,2,uzext))))/
     &      (CB*CB2*CW2*MW*MW2*SW*SW2)

        Cloop(1) = Cloop(1) + 
     &    1/(32.D0*Pi)*(AlfaMZ*ELMZ*Delta(gno1,gno2)*Mf(2,gno1)*
     &        (cI*(((CBA*lint21*SA + CA*lint22*SBA)*
     &                (2*F2*SW2 + F1*(-1 + 2*SW2)) + 
     &               CBA*SA*
     &                (dup19*lint29(cc0) + dup18*lint29(cc1)) + 
     &               CA*SBA*
     &                (dup19*lint30(cc0) + dup18*lint30(cc1)) - 
     &               dup20*
     &                (CBA*SA*lint29(cc2) + CA*SBA*lint30(cc2)) - 
     &               C2B*(F1 - F2)*TB*
     &                (SA*SAB*
     &                   (lint23(cc0) + lint23(cc1) - 
     &                     lint23(cc2) + lint24(cc0) - 
     &                     lint24(cc1) + lint24(cc2)) - 
     &                  CA*CAB*lint25(cc2))*Mf2(2,gno1))*
     &             XHiggs(hno,3,uzext)) - 
     &          2*CW2*F2*SB*lint18(cc0)*
     &           (2*m22 + MHp2 - 3*Mf2(2,gno1))*
     &           (-(cI*XHiggs(hno,3,uzext)) + 
     &             CBA*XHiggs(hno,1,uzext) - 
     &             SBA*XHiggs(hno,2,uzext))))/(CB*CW2*MW*SW*SW2)

        Cloop(1) = Cloop(1) - 
     &    cI/(32.D0*Pi)*(AlfaMZ*ELMZ*Delta(gno1,gno2)*Mf(2,gno1)*
     &        (CA*SBA*((F2*(-2*m22 - MHH2) + 
     &                (F1 + F2)*(4*m22 + 2*MHH2)*SW2)*lint32(cc0)+
     &               m22*(-2*F2 + 4*(F1 + F2)*SW2)*lint32(cc1)) + 
     &          (SA*(S2B*SAB*
     &                 (F2*
     &                    (lint27(cc0) + lint27(cc1) - lint27(cc2))
     &                     + F1*
     &                    (-lint27(cc0) - lint27(cc1) + 
     &                      lint27(cc2))) - Sub33*lint31(cc2)) + 
     &             CA*(CAB*
     &                 (C2B*TB*
     &                    (F2*
     &                       (-lint25(cc0) - lint25(cc1) - 
     &                       lint26(cc0) + lint26(cc1) - 
     &                       lint26(cc2)) + 
     &                      F1*
     &                       (lint25(cc0) + lint25(cc1) + 
     &                       lint26(cc0) - lint26(cc1) + 
     &                       lint26(cc2))) + 
     &                   S2B*
     &                    (F2*
     &                       (lint28(cc0) + lint28(cc1) - 
     &                       lint28(cc2)) + 
     &                      F1*
     &                       (-lint28(cc0) - lint28(cc1) + 
     &                       lint28(cc2)))) - Sub32*lint32(cc0) + 
     &                Sub29*lint32(cc1)))*Mf2(2,gno1) + 
     &          SA*(CBA*(F2*(m12 - m22 - m32) + 
     &                (F1 + F2)*(-2*m12 + 2*(m22 + m32))*SW2)*
     &              lint31(cc2) + 
     &             lint31(cc1)*
     &              (CBA*m22*(4*F1*SW2 + F2*(-2 + 4*SW2)) + 
     &                Sub28*Mf2(2,gno1)) + 
     &             lint31(cc0)*
     &              (CBA*(2*m22 + Mh02)*
     &                 (2*F1*SW2 + F2*(-1 + 2*SW2)) - 
     &                Sub31*Mf2(2,gno1))))*XHiggs(hno,3,uzext))/
     &      (CB*CW2*MW*SW*SW2)

        Cloop(1) = Cloop(1) + 
     &    1/(32.D0*Pi)*(AlfaMZ*ELMZ*Delta(gno1,gno2)*Mf(2,gno1)*
     &        (lint34*(CB*(F1 + F2)*Sub17 + 
     &             SB*Sub24*(-2*F1*SW2 + F2*(-1 + 2*SW2))) - 
     &          cI*((-(F2*(2*CW2*lint39*SB + 
     &                    lint34*(CBA*SA + CA*SBA))) - 
     &               4*CW2*SB*Sub41*lint18(cc1) + 
     &               2*((F1 + F2)*lint34*(CBA*SA + CA*SBA)*SW2 + 
     &                  CW2*SB*Sub46*lint18(cc2)) + 
     &               CA*lint32(cc2)*
     &                (-((m12 - m22 - m32)*SBA*
     &                     (2*F1*SW2 + F2*(-1 + 2*SW2))) - 
     &                  Sub34*Mf2(2,gno1)))*XHiggs(hno,3,uzext)) + 
     &          2*((CB*CW2*lint39*Sub35 + 
     &                SB*(-(Sub38*lint18(cc1)) + Sub43*lint18(cc2))
     &                )*XHiggs(hno,1,uzext) + 
     &             (CB*CW2*lint39*Sub36 + 
     &                SB*(Sub40*lint18(cc1) + Sub45*lint18(cc2)))*
     &              XHiggs(hno,2,uzext))))/(CB*CW2*MW*SW*SW2)

#ifdef DETAILED_DEBUG
	DCOUP "v1: Cloop(1) =", Cloop(1) ENDL
#endif

	end
