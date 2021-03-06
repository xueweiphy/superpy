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
     3    4.00000000e+01   # tanb
     4    1.00000000e+00   # sign(mu)
     1    1.10000000e+03   # m0
     2    4.00000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    2.16983252e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=3.18669170e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03920253e+01   # MW
        25     1.16236235e+02   # h0
        35     8.61525754e+02   # H0
        36     8.61642788e+02   # A0
        37     8.65532100e+02   # H+
   1000021     9.89071425e+02   # ~g
   1000022     1.66665523e+02   # ~neutralino(1)
   1000023     3.18506535e+02   # ~neutralino(2)
   1000024     3.18589846e+02   # ~chargino(1)
   1000025    -5.72304090e+02   # ~neutralino(3)
   1000035     5.82854925e+02   # ~neutralino(4)
   1000037     5.83780135e+02   # ~chargino(2)
   1000001     1.36942208e+03   # ~d_L
   1000002     1.36725424e+03   # ~u_L
   1000003     1.36937383e+03   # ~s_L
   1000004     1.36720591e+03   # ~c_L
   1000005     1.06940046e+03   # ~b_1
   1000006     8.83941848e+02   # ~t_1
   1000011     1.12881399e+03   # ~e_L
   1000012     1.12568733e+03   # ~nue_L
   1000013     1.12856620e+03   # ~mu_L
   1000014     1.12540601e+03   # ~numu_L
   1000015     9.09373296e+02   # ~stau_1
   1000016     1.03381413e+03   # ~nu_tau_L
   2000001     1.35073742e+03   # ~d_R
   2000002     1.35164048e+03   # ~u_R
   2000003     1.35064524e+03   # ~s_R
   2000004     1.35163421e+03   # ~c_R
   2000005     1.19071764e+03   # ~b_2
   2000006     1.10339838e+03   # ~t_2
   2000011     1.10966060e+03   # ~e_R
   2000013     1.10908755e+03   # ~mu_R
   2000015     1.04051846e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.59715687e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.95557668e-01   # N_{1,1}
  1  2    -1.50008156e-02   # N_{1,2}
  1  3     8.85386605e-02   # N_{1,3}
  1  4    -2.82986017e-02   # N_{1,4}
  2  1     3.52671601e-02   # N_{2,1}
  2  2     9.73576537e-01   # N_{2,2}
  2  3    -1.95743602e-01   # N_{2,3}
  2  4     1.12202478e-01   # N_{2,4}
  3  1    -4.13842032e-02   # N_{3,1}
  3  2     6.10236205e-02   # N_{3,2}
  3  3     7.02059481e-01   # N_{3,3}
  3  4     7.08290866e-01   # N_{3,4}
  4  1    -7.68667995e-02   # N_{4,1}
  4  2     2.19544573e-01   # N_{4,2}
  4  3     6.78938755e-01   # N_{4,3}
  4  4    -6.96371913e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.60684890e-01   # U_{1,1}
  1  2    -2.77641031e-01   # U_{1,2}
  2  1     2.77641031e-01   # U_{2,1}
  2  2     9.60684890e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.86959042e-01   # V_{1,1}
  1  2    -1.60971580e-01   # V_{1,2}
  2  1     1.60971580e-01   # V_{2,1}
  2  2     9.86959042e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.17868549e-01   # F_{11}
  1  2     9.48134793e-01   # F_{12}
  2  1     9.48134793e-01   # F_{21}
  2  2    -3.17868549e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.81146204e-01   # F_{11}
  1  2     1.93266984e-01   # F_{12}
  2  1    -1.93266984e-01   # F_{21}
  2  2     9.81146204e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.65533767e-01   # F_{11}
  1  2     9.86204123e-01   # F_{12}
  2  1     9.86204123e-01   # F_{21}
  2  2    -1.65533767e-01   # F_{22}
Block gauge Q= 9.64465110e+02  # SM gauge couplings
     1     3.62031034e-01   # g'(Q)MSSM DRbar
     2     6.42228064e-01   # g(Q)MSSM DRbar
     3     1.05942699e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.64465110e+02  
  3  3     8.57737747e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.64465110e+02  
  3  3     5.17484588e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.64465110e+02  
  3  3     4.12650541e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.64465110e+02 # Higgs mixing parameters
     1     5.64441324e+02    # mu(Q)MSSM DRbar
     2     3.92312925e+01    # tan beta(Q)MSSM DRbar
     3     2.43738500e+02    # higgs vev(Q)MSSM DRbar
     4     8.94408093e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.64465110e+02  # MSSM DRbar SUSY breaking parameters
     1     1.68500680e+02      # M_1(Q)
     2     3.13075347e+02      # M_2(Q)
     3     8.93584774e+02      # M_3(Q)
    21     4.44460203e+05      # mH1^2(Q)
    22    -3.06145058e+05      # mH2^2(Q)
    31     1.12606067e+03      # meL(Q)
    32     1.12578018e+03      # mmuL(Q)
    33     1.03648260e+03      # mtauL(Q)
    34     1.10757474e+03      # meR(Q)
    35     1.10700146e+03      # mmuR(Q)
    36     9.14608812e+02      # mtauR(Q)
    41     1.34463284e+03      # mqL1(Q)
    42     1.34458378e+03      # mqL2(Q)
    43     1.05342774e+03      # mqL3(Q)
    44     1.32993419e+03      # muR(Q)
    45     1.32992781e+03      # mcR(Q)
    46     8.71832951e+02      # mtR(Q)
    47     1.32831407e+03      # mdR(Q)
    48     1.32822017e+03      # msR(Q)
    49     1.16644858e+03      # mbR(Q)
Block au Q= 9.64465110e+02  
  1  1    -1.25023380e+03      # Au(Q)MSSM DRbar
  2  2    -1.25020210e+03      # Ac(Q)MSSM DRbar
  3  3    -8.39781018e+02      # At(Q)MSSM DRbar
Block ad Q= 9.64465110e+02  
  1  1    -1.45063860e+03      # Ad(Q)MSSM DRbar
  2  2    -1.45055788e+03      # As(Q)MSSM DRbar
  3  3    -1.19476504e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.64465110e+02  
  1  1    -5.72870519e+02      # Ae(Q)MSSM DRbar
  2  2    -5.72572068e+02      # Amu(Q)MSSM DRbar
  3  3    -4.79781637e+02      # Atau(Q)MSSM DRbar
