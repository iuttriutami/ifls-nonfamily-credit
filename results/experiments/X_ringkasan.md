# Eksperimen penutup (MODE=FULL, S=20, lightgbm=True)

## X1 repeated cross-fitting

```
 scheme      outcome      check  ate_median  se_adj      p  ate_min  ate_max  share_signif  att_median    n  S
  group     ihs_laba       main      1.7495  0.4491 0.0001   1.4944   2.1490          1.00      1.2782 4326 20
  group tenaga_kerja       main      0.2835  0.1162 0.0147   0.1855   0.3964          0.95      0.2114 4326 20
  group  usaha_tutup       main     -0.0942  0.0272 0.0005  -0.1116  -0.0733          1.00     -0.0663 4326 20
 random     ihs_laba       main      1.6587  0.4656 0.0004   0.9598   1.9459          0.95      1.0901 4326 20
 random     ihs_laba   nonmover      2.0498  0.6261 0.0011   1.4633   2.9044          1.00         NaN 3294 20
 random     ihs_laba     trim10      1.5679  0.5096 0.0021   0.8876   1.9260          0.90         NaN 3909 20
 random     ihs_laba unweighted      1.5101  0.4418 0.0006   1.0563   1.6978          1.00         NaN 4326 20
 random tenaga_kerja       main      0.2285  0.1190 0.0548   0.0925   0.3057          0.65      0.1015 4326 20
 random  usaha_tutup       main     -0.0785  0.0282 0.0054  -0.1065  -0.0466          0.90     -0.0521 4326 20
 random  usaha_tutup   nonmover     -0.0748  0.0398 0.0599  -0.1163  -0.0532          0.60         NaN 3294 20
 random  usaha_tutup     trim10     -0.0613  0.0301 0.0418  -0.0869  -0.0292          0.75         NaN 3909 20
 random  usaha_tutup unweighted     -0.0710  0.0263 0.0069  -0.0927  -0.0512          0.95         NaN 4326 20
spatial     ihs_laba       main      2.0094  0.4763 0.0000   1.7191   2.2713          1.00      1.2666 4326 20
spatial tenaga_kerja       main      0.3211  0.1223 0.0086   0.2169   0.3780          0.95      0.2290 4326 20
spatial  usaha_tutup       main     -0.1015  0.0275 0.0002  -0.1255  -0.0893          1.00     -0.0644 4326 20
```

## X2 overlap

```
    outcome                              estimand     est     se    n      p
usaha_tutup       ATE on 0.00<=e<=1.00 (no refit) -0.0785 0.0282 4326 0.0054
usaha_tutup       ATE on 0.02<=e<=0.98 (no refit) -0.0787 0.0282 4323 0.0053
usaha_tutup       ATE on 0.05<=e<=0.95 (no refit) -0.0791 0.0277 4253 0.0044
usaha_tutup       ATE on 0.10<=e<=0.90 (no refit) -0.0708 0.0251 3921 0.0049
usaha_tutup       ATE on 0.15<=e<=0.85 (no refit) -0.0565 0.0259 3375 0.0291
usaha_tutup Overlap-weighted AIPW, weights e(1-e) -0.0647 0.0225 4326 0.0040
usaha_tutup                  share e<0.1 or e>0.9  0.0666    NaN 4326    NaN
   ihs_laba       ATE on 0.00<=e<=1.00 (no refit)  1.6587 0.4656 4326 0.0004
   ihs_laba       ATE on 0.02<=e<=0.98 (no refit)  1.6618 0.4670 4323 0.0004
   ihs_laba       ATE on 0.05<=e<=0.95 (no refit)  1.7188 0.4405 4253 0.0001
   ihs_laba       ATE on 0.10<=e<=0.90 (no refit)  1.5301 0.4191 3921 0.0003
   ihs_laba       ATE on 0.15<=e<=0.85 (no refit)  1.2520 0.4169 3375 0.0027
   ihs_laba Overlap-weighted AIPW, weights e(1-e)  1.4267 0.3660 4326 0.0001
   ihs_laba                  share e<0.1 or e>0.9  0.0666    NaN 4326    NaN
```

## X3 pre-trend placebo

```
     outcome    weights     est     se    n  sd_outcome  std_effect      p
d_ihs_laba_m   weighted -0.0492 0.1659 2213      1.4634     -0.0336 0.7670
d_ihs_laba_m unweighted  0.0122 0.1267 2213      1.4634      0.0083 0.9232
d_ihs_aset_m   weighted -0.0987 0.2202 2213      1.6842     -0.0586 0.6540
d_ihs_aset_m unweighted -0.2040 0.1888 2213      1.6842     -0.1211 0.2800
   d_pekerja   weighted  0.0673 0.4654 2190      5.6487      0.0119 0.8851
   d_pekerja unweighted  0.2102 0.4554 2190      5.6487      0.0372 0.6443
```

## X4 subgroups

```
    outcome                                                                          group     ate     se    n  base_closure      p
usaha_tutup                                    Enterprise existed in 2000 (history sample) -0.0297 0.0407 2213        0.2918 0.4664
usaha_tutup                                                     Not in 2000 history sample -0.1348 0.0411 2113        0.4880 0.0010
usaha_tutup                                               Enterprise age >= 7 years (2007) -0.0334 0.0407 2129        0.3225 0.4125
usaha_tutup                                                Enterprise age < 7 years (2007) -0.1287 0.0365 1891        0.4271 0.0004
usaha_tutup                                                               Borrowed in 2007 -0.0031 0.0478  970        0.3471 0.9487
usaha_tutup                                                         Did not borrow in 2007 -0.0960 0.0287 3356        0.3830 0.0008
usaha_tutup                                                                     Urban 2007 -0.0848 0.0345 2490        0.3554 0.0139
usaha_tutup                                                                     Rural 2007 -0.0667 0.0367 1836        0.3941 0.0693
usaha_tutup DIFF: Enterprise existed in 2000 (history sample) − Not in 2000 history sample  0.1051 0.0663 4326           NaN 0.1130
usaha_tutup       DIFF: Enterprise age >= 7 years (2007) − Enterprise age < 7 years (2007)  0.0953 0.0597 4020           NaN 0.1106
usaha_tutup                                DIFF: Borrowed in 2007 − Did not borrow in 2007  0.0929 0.0572 4326           NaN 0.1042
usaha_tutup                                                  DIFF: Urban 2007 − Rural 2007 -0.0181 0.0521 4326           NaN 0.7292
   ihs_laba                                    Enterprise existed in 2000 (history sample)  1.0324 0.6449 2213        0.2918 0.1094
   ihs_laba                                                     Not in 2000 history sample  2.3392 0.6852 2113        0.4880 0.0006
   ihs_laba                                               Enterprise age >= 7 years (2007)  1.1415 0.6704 2129        0.3225 0.0886
   ihs_laba                                                Enterprise age < 7 years (2007)  2.4350 0.6055 1891        0.4271 0.0001
   ihs_laba                                                               Borrowed in 2007  0.8462 0.8060  970        0.3471 0.2937
   ihs_laba                                                         Did not borrow in 2007  1.8150 0.4592 3356        0.3830 0.0001
   ihs_laba                                                                     Urban 2007  1.5155 0.5736 2490        0.3554 0.0082
   ihs_laba                                                                     Rural 2007  1.6730 0.6342 1836        0.3941 0.0083
   ihs_laba DIFF: Enterprise existed in 2000 (history sample) − Not in 2000 history sample -1.3067 1.0571 4326           NaN 0.2164
   ihs_laba       DIFF: Enterprise age >= 7 years (2007) − Enterprise age < 7 years (2007) -1.2935 1.0004 4020           NaN 0.1960
   ihs_laba                                DIFF: Borrowed in 2007 − Did not borrow in 2007 -0.9687 0.9155 4326           NaN 0.2900
   ihs_laba                                                  DIFF: Urban 2007 − Rural 2007 -0.1575 0.9026 4326           NaN 0.8615
```

## X5 sensitivity

```
     outcome           benchmark   k  estimate     se  r2_YD_given_X  r2_DZ_given_X  RV_q1  RV_q1_alpha05  adj_estimate  adj_lo  adj_hi
 usaha_tutup              (none) NaN   -0.0916 0.0157         0.0079            NaN 0.0852         0.0574           NaN     NaN     NaN
 usaha_tutup            pinjam07 1.0   -0.0916 0.0157            NaN         0.0012    NaN            NaN       -0.0905 -0.1213 -0.0597
 usaha_tutup            pinjam07 2.0   -0.0916 0.0157            NaN         0.0024    NaN            NaN       -0.0893 -0.1201 -0.0585
 usaha_tutup            pinjam07 3.0   -0.0916 0.0157            NaN         0.0036    NaN            NaN       -0.0882 -0.1190 -0.0574
 usaha_tutup          ihs_laba07 1.0   -0.0916 0.0157            NaN         0.0001    NaN            NaN       -0.0909 -0.1217 -0.0602
 usaha_tutup          ihs_laba07 2.0   -0.0916 0.0157            NaN         0.0002    NaN            NaN       -0.0903 -0.1210 -0.0596
 usaha_tutup          ihs_laba07 3.0   -0.0916 0.0157            NaN         0.0003    NaN            NaN       -0.0896 -0.1203 -0.0590
 usaha_tutup jarak_lembaga_min07 1.0   -0.0916 0.0157            NaN         0.0003    NaN            NaN       -0.0904 -0.1211 -0.0596
 usaha_tutup jarak_lembaga_min07 2.0   -0.0916 0.0157            NaN         0.0006    NaN            NaN       -0.0891 -0.1198 -0.0585
 usaha_tutup jarak_lembaga_min07 3.0   -0.0916 0.0157            NaN         0.0009    NaN            NaN       -0.0879 -0.1185 -0.0573
    ihs_laba              (none) NaN    1.6412 0.2691         0.0086            NaN 0.0890         0.0613           NaN     NaN     NaN
    ihs_laba            pinjam07 1.0    1.6412 0.2691            NaN         0.0012    NaN            NaN        1.6283  1.1006  2.1560
    ihs_laba            pinjam07 2.0    1.6412 0.2691            NaN         0.0024    NaN            NaN        1.6153  1.0875  2.1432
    ihs_laba            pinjam07 3.0    1.6412 0.2691            NaN         0.0036    NaN            NaN        1.6024  1.0743  2.1305
    ihs_laba          ihs_laba07 1.0    1.6412 0.2691            NaN         0.0001    NaN            NaN        1.6285  1.1022  2.1548
    ihs_laba          ihs_laba07 2.0    1.6412 0.2691            NaN         0.0002    NaN            NaN        1.6159  1.0908  2.1410
    ihs_laba          ihs_laba07 3.0    1.6412 0.2691            NaN         0.0003    NaN            NaN        1.6032  1.0794  2.1271
    ihs_laba jarak_lembaga_min07 1.0    1.6412 0.2691            NaN         0.0003    NaN            NaN        1.6253  1.0984  2.1522
    ihs_laba jarak_lembaga_min07 2.0    1.6412 0.2691            NaN         0.0006    NaN            NaN        1.6094  1.0831  2.1356
    ihs_laba jarak_lembaga_min07 3.0    1.6412 0.2691            NaN         0.0009    NaN            NaN        1.5935  1.0679  2.1191
tenaga_kerja              (none) NaN    0.2411 0.0609         0.0036            NaN 0.0587         0.0301           NaN     NaN     NaN
tenaga_kerja            pinjam07 1.0    0.2411 0.0609            NaN         0.0012    NaN            NaN        0.2312  0.1120  0.3504
tenaga_kerja            pinjam07 2.0    0.2411 0.0609            NaN         0.0024    NaN            NaN        0.2213  0.1023  0.3402
tenaga_kerja            pinjam07 3.0    0.2411 0.0609            NaN         0.0036    NaN            NaN        0.2114  0.0927  0.3301
tenaga_kerja          ihs_laba07 1.0    0.2411 0.0609            NaN         0.0001    NaN            NaN        0.2384  0.1192  0.3576
tenaga_kerja          ihs_laba07 2.0    0.2411 0.0609            NaN         0.0002    NaN            NaN        0.2357  0.1168  0.3547
tenaga_kerja          ihs_laba07 3.0    0.2411 0.0609            NaN         0.0003    NaN            NaN        0.2331  0.1143  0.3518
tenaga_kerja jarak_lembaga_min07 1.0    0.2411 0.0609            NaN         0.0003    NaN            NaN        0.2386  0.1192  0.3579
tenaga_kerja jarak_lembaga_min07 2.0    0.2411 0.0609            NaN         0.0006    NaN            NaN        0.2361  0.1168  0.3554
tenaga_kerja jarak_lembaga_min07 3.0    0.2411 0.0609            NaN         0.0009    NaN            NaN        0.2336  0.1143  0.3528
```

## X6 BLP repeated

```
    outcome  beta_median  se_median  p_median_x2  share_beta_negative  gate1_median  gate2_median  gate3_median  gate4_median  gate5_median
   ihs_laba      -0.0418     0.1029       1.0000                 0.60        1.3704        1.4535        1.7572        1.5451        1.3686
usaha_tutup      -0.1647     0.0995       0.2768                 0.95       -0.0340       -0.0407       -0.0248       -0.1005       -0.1753
```
