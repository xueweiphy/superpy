# SOFTSUSY3.3.7 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.3.7       # version number
Block MODSEL  # Select model
     1    2   # gmsb
Block SMINPUTS             # Standard Model inputs
     1    1.27934000e+02   # alpha_em^(-1)(MZ) SM MSbar
     2    1.16637000e-05   # G_Fermi
     3    1.17200000e-01   # alpha_s(MZ)MSbar
     4    9.11876000e+01   # MZ(pole)
     5    4.25000000e+00   # mb(mb)
     6    1.73300000e+02   # Mtop(pole)
     7    1.77700000e+00   # Mtau(pole)
Block MINPAR               # SUSY breaking input parameters
     3    1.50000000e+01   # tanb
     4    1.00000000e+00   # sign(mu)
     1    5.50000000e+04   # lambda
     2    1.10000000e+05   # M_mess
     5    3.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=1.40393059e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04002914e+01   # MW
        25     1.13490900e+02   # h0
        35     5.21240296e+02   # H0
        36     5.20983332e+02   # A0
        37     5.27369461e+02   # H+
   1000021     1.26173540e+03   # ~g
   1000022     2.28535959e+02   # ~neutralino(1)
   1000023     3.75233587e+02   # ~neutralino(2)
   1000024     3.72951413e+02   # ~chargino(1)
   1000025    -4.13392489e+02   # ~neutralino(3)
   1000035     4.99918100e+02   # ~neutralino(4)
   1000037     4.99055791e+02   # ~chargino(2)
   1000039     1.43385000e-09   # ~gravitino
   1000001     1.20488840e+03   # ~d_L
   1000002     1.20241249e+03   # ~u_L
   1000003     1.20488689e+03   # ~s_L
   1000004     1.20241098e+03   # ~c_L
   1000005     1.14758238e+03   # ~b_1
   1000006     1.07335356e+03   # ~t_1
   1000011     3.57165363e+02   # ~e_L
   1000012     3.47961931e+02   # ~nue_L
   1000013     3.57174169e+02   # ~mu_L
   1000014     3.47960449e+02   # ~numu_L
   1000015     1.70023965e+02   # ~stau_1
   1000016     3.47284327e+02   # ~nu_tau_L
   2000001     1.15609487e+03   # ~d_R
   2000002     1.15885504e+03   # ~u_R
   2000003     1.15609277e+03   # ~s_R
   2000004     1.15885396e+03   # ~c_R
   2000005     1.16444589e+03   # ~b_2
   2000006     1.17679744e+03   # ~t_2
   2000011     1.75959752e+02   # ~e_R
   2000013     1.75953798e+02   # ~mu_R
   2000015     3.58179612e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.44799242e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.79037941e-01   # N_{1,1}
  1  2    -3.93670929e-02   # N_{1,2}
  1  3     1.70915022e-01   # N_{1,3}
  1  4    -1.03551909e-01   # N_{1,4}
  2  1    -1.83724335e-01   # N_{2,1}
  2  2    -5.63240752e-01   # N_{2,2}
  2  3     5.90958119e-01   # N_{2,3}
  2  4    -5.47515960e-01   # N_{2,4}
  3  1    -4.48716273e-02   # N_{3,1}
  3  2     6.02110871e-02   # N_{3,2}
  3  3     7.00738748e-01   # N_{3,3}
  3  4     7.09454980e-01   # N_{3,4}
  4  1    -7.56083115e-02   # N_{4,1}
  4  2     8.23155339e-01   # N_{4,2}
  4  3     3.61277959e-01   # N_{4,3}
  4  4    -4.31482221e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1    -5.07716939e-01   # U_{1,1}
  1  2     8.61523946e-01   # U_{1,2}
  2  1    -8.61523946e-01   # U_{2,1}
  2  2    -5.07716939e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1    -6.05590190e-01   # V_{1,1}
  1  2     7.95776679e-01   # V_{1,2}
  2  1    -7.95776679e-01   # V_{2,1}
  2  2    -6.05590190e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.84791582e-01   # F_{11}
  1  2     9.58589461e-01   # F_{12}
  2  1     9.58589461e-01   # F_{21}
  2  2    -2.84791582e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.68624868e-01   # F_{11}
  1  2     8.83397268e-01   # F_{12}
  2  1     8.83397268e-01   # F_{21}
  2  2    -4.68624868e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.09706299e-01   # F_{11}
  1  2     9.93964048e-01   # F_{12}
  2  1     9.93964048e-01   # F_{21}
  2  2    -1.09706299e-01   # F_{22}
Block gauge Q= 1.09054794e+03  # SM gauge couplings
     1     3.63267433e-01   # g'(Q)MSSM DRbar
     2     6.43393996e-01   # g(Q)MSSM DRbar
     3     1.05266438e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.09054794e+03  
  3  3     8.58369082e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.09054794e+03  
  3  3     2.03134516e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.09054794e+03  
  3  3     1.51774742e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.09054794e+03 # Higgs mixing parameters
     1     4.04626301e+02    # mu(Q)MSSM DRbar
     2     1.44867358e+01    # tan beta(Q)MSSM DRbar
     3     2.43598874e+02    # higgs vev(Q)MSSM DRbar
     4     3.09090404e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.09054794e+03  # MSSM DRbar SUSY breaking parameters
     1     2.38808736e+02      # M_1(Q)
     2     4.47862453e+02      # M_2(Q)
     3     1.20463536e+03      # M_3(Q)
    21     1.05466514e+05      # mH1^2(Q)
    22    -1.42379399e+05      # mH2^2(Q)
    31     3.47483228e+02      # meL(Q)
    32     3.47481747e+02      # mmuL(Q)
    33     3.47025872e+02      # mtauL(Q)
    34     1.64108734e+02      # meR(Q)
    35     1.64102366e+02      # mmuR(Q)
    36     1.62130137e+02      # mtauR(Q)
    41     1.16012220e+03      # mqL1(Q)
    42     1.16012065e+03      # mqL2(Q)
    43     1.12329055e+03      # mqL3(Q)
    44     1.11707457e+03      # muR(Q)
    45     1.11707346e+03      # mcR(Q)
    46     1.04218586e+03      # mtR(Q)
    47     1.11313379e+03      # mdR(Q)
    48     1.11313163e+03      # msR(Q)
    49     1.10893777e+03      # mbR(Q)
Block au Q= 1.09054794e+03  
  1  1    -3.61154563e+02      # Au(Q)MSSM DRbar
  2  2    -3.61154057e+02      # Ac(Q)MSSM DRbar
  3  3    -3.40565809e+02      # At(Q)MSSM DRbar
Block ad Q= 1.09054794e+03  
  1  1    -3.83972262e+02      # Ad(Q)MSSM DRbar
  2  2    -3.83971555e+02      # As(Q)MSSM DRbar
  3  3    -3.76216470e+02      # Ab(Q)MSSM DRbar
Block ae Q= 1.09054794e+03  
  1  1    -3.76468440e+01      # Ae(Q)MSSM DRbar
  2  2    -3.76465697e+01      # Amu(Q)MSSM DRbar
  3  3    -3.75621449e+01      # Atau(Q)MSSM DRbar
