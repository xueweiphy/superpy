# SOFTSUSY3.3.7 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.3.7       # version number
Block MODSEL  # Select model
     1    1   # sugra
Block SMINPUTS             # Standard Model inputs
     1    1.27934000e+02   # alpha_em^(-1)(MZ) SM MSbar
     2    1.16637000e-05   # G_Fermi
     3    1.17200000e-01   # alpha_s(MZ)MSbar
     4    9.11876000e+01   # MZ(pole)
     5    4.25000000e+00   # mb(mb)
     6    1.73300000e+02   # Mtop(pole)
     7    1.77700000e+00   # Mtau(pole)
Block MINPAR               # SUSY breaking input parameters
     3    1.00000000e+01   # tanb
     4    1.00000000e+00   # sign(mu)
     1    1.62500000e+02   # m0
     2    6.50000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.71847015e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=1.47255167e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03938768e+01   # MW
        25     1.16590647e+02   # h0
        35     9.13242524e+02   # H0
        36     9.13026082e+02   # A0
        37     9.16774188e+02   # H+
   1000021     1.46095543e+03   # ~g
   1000022     2.69508402e+02   # ~neutralino(1)
   1000023     5.09956393e+02   # ~neutralino(2)
   1000024     5.10199718e+02   # ~chargino(1)
   1000025    -8.00033133e+02   # ~neutralino(3)
   1000035     8.11933644e+02   # ~neutralino(4)
   1000037     8.11805051e+02   # ~chargino(2)
   1000001     1.34146969e+03   # ~d_L
   1000002     1.33928632e+03   # ~u_L
   1000003     1.34146645e+03   # ~s_L
   1000004     1.33928308e+03   # ~c_L
   1000005     1.22949940e+03   # ~b_1
   1000006     1.03422929e+03   # ~t_1
   1000011     4.66774888e+02   # ~e_L
   1000012     4.59872905e+02   # ~nue_L
   1000013     4.66841577e+02   # ~mu_L
   1000014     4.59868671e+02   # ~numu_L
   1000015     2.89087317e+02   # ~stau_1
   1000016     4.58388384e+02   # ~nu_tau_L
   2000001     1.28307322e+03   # ~d_R
   2000002     1.28804481e+03   # ~u_R
   2000003     1.28306984e+03   # ~s_R
   2000004     1.28804133e+03   # ~c_R
   2000005     1.27809240e+03   # ~b_2
   2000006     1.26686337e+03   # ~t_2
   2000011     2.96258215e+02   # ~e_R
   2000013     2.96244874e+02   # ~mu_R
   2000015     4.67013511e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05698246e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97359853e-01   # N_{1,1}
  1  2    -1.10125165e-02   # N_{1,2}
  1  3     6.59568883e-02   # N_{1,3}
  1  4    -2.83149619e-02   # N_{1,4}
  2  1     2.53163377e-02   # N_{2,1}
  2  2     9.78266667e-01   # N_{2,2}
  2  3    -1.69169667e-01   # N_{2,3}
  2  4     1.17196563e-01   # N_{2,4}
  3  1    -2.60993979e-02   # N_{3,1}
  3  2     3.77605079e-02   # N_{3,2}
  3  3     7.04849143e-01   # N_{3,3}
  3  4     7.07870504e-01   # N_{3,4}
  4  1    -6.28587955e-02   # N_{4,1}
  4  2     2.03585845e-01   # N_{4,2}
  4  3     6.85725162e-01   # N_{4,3}
  4  4    -6.95975989e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.71012716e-01   # U_{1,1}
  1  2    -2.39027835e-01   # U_{1,2}
  2  1     2.39027835e-01   # U_{2,1}
  2  2     9.71012716e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.86055122e-01   # V_{1,1}
  1  2    -1.66419039e-01   # V_{1,2}
  2  1     1.66419039e-01   # V_{2,1}
  2  2     9.86055122e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.65966530e-01   # F_{11}
  1  2     9.30628013e-01   # F_{12}
  2  1     9.30628013e-01   # F_{21}
  2  2    -3.65966530e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.83050477e-01   # F_{11}
  1  2     1.83335100e-01   # F_{12}
  2  1    -1.83335100e-01   # F_{21}
  2  2     9.83050477e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.08677858e-01   # F_{11}
  1  2     9.94077021e-01   # F_{12}
  2  1     9.94077021e-01   # F_{21}
  2  2    -1.08677858e-01   # F_{22}
Block gauge Q= 1.11123515e+03  # SM gauge couplings
     1     3.62920032e-01   # g'(Q)MSSM DRbar
     2     6.41682875e-01   # g(Q)MSSM DRbar
     3     1.04832149e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.11123515e+03  
  3  3     8.52957181e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.11123515e+03  
  3  3     1.33663442e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.11123515e+03  
  3  3     1.00346567e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.11123515e+03 # Higgs mixing parameters
     1     7.94580395e+02    # mu(Q)MSSM DRbar
     2     9.64525275e+00    # tan beta(Q)MSSM DRbar
     3     2.43836449e+02    # higgs vev(Q)MSSM DRbar
     4     8.63710039e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.11123515e+03  # MSSM DRbar SUSY breaking parameters
     1     2.75273102e+02      # M_1(Q)
     2     5.07741355e+02      # M_2(Q)
     3     1.42112122e+03      # M_3(Q)
    21     1.84083794e+05      # mH1^2(Q)
    22    -6.07500119e+05      # mH2^2(Q)
    31     4.58313575e+02      # meL(Q)
    32     4.58309331e+02      # mmuL(Q)
    33     4.57025846e+02      # mtauL(Q)
    34     2.88221777e+02      # meR(Q)
    35     2.88208050e+02      # mmuR(Q)
    36     2.84031465e+02      # mtauR(Q)
    41     1.29598968e+03      # mqL1(Q)
    42     1.29598638e+03      # mqL2(Q)
    43     1.19534770e+03      # mqL3(Q)
    44     1.24587610e+03      # muR(Q)
    45     1.24587257e+03      # mcR(Q)
    46     1.02690601e+03      # mtR(Q)
    47     1.23973593e+03      # mdR(Q)
    48     1.23973249e+03      # msR(Q)
    49     1.23348242e+03      # mbR(Q)
Block au Q= 1.11123515e+03  
  1  1    -1.44272371e+03      # Au(Q)MSSM DRbar
  2  2    -1.44271731e+03      # Ac(Q)MSSM DRbar
  3  3    -1.11761491e+03      # At(Q)MSSM DRbar
Block ad Q= 1.11123515e+03  
  1  1    -1.75982084e+03      # Ad(Q)MSSM DRbar
  2  2    -1.75981492e+03      # As(Q)MSSM DRbar
  3  3    -1.64571634e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.11123515e+03  
  1  1    -3.84553751e+02      # Ae(Q)MSSM DRbar
  2  2    -3.84546951e+02      # Amu(Q)MSSM DRbar
  3  3    -3.82490675e+02      # Atau(Q)MSSM DRbar
