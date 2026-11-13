"""Rebuilds the tables (LaTeX fragments parts1.tex, parts2.tex) and figures of Additional files 1 and 2
from the aggregated CSV results in results/. Run from the repository root: python docs/make_additional_files.py"""
import pandas as pd, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T=os.path.join(ROOT,"results","tables"); X=os.path.join(ROOT,"results","experiments"); SIM=os.path.join(ROOT,"results","simulation")
os.makedirs("build",exist_ok=True); os.chdir("build")
plt.rcParams.update({"font.family":"serif","font.size":9,"axes.spines.top":False,"axes.spines.right":False})
OUTN={"usaha_tutup":"Business closed","ihs_laba":"IHS profit (Rp)","tenaga_kerja":"Workers"}
SCH={"random":"Random","group":"Group","spatial":"Spatial-block"}
VAR={"ihs_laba07":"IHS profit 2007","pekerja07":"Workers 2007","ihs_aset07":"IHS assets 2007","umur_usaha07":"Enterprise age 2007",
 "n_usaha07":"Number of enterprises 2007","usaha_di_rumah07":"Enterprise at home 2007","pinjam07":"Borrowed in 2007",
 "ihs_pinjam07":"IHS loan amount 2007","log_pce07":"Log per-capita expenditure 2007","hhsize07":"Household size 2007",
 "kepala_perempuan":"Head female","usia_kepala":"Head age","pendidikan_kepala":"Head schooling (years)","perkotaan07":"Urban 2007",
 "n_lembaga_kredit_desa07":"Credit institutions in community","jarak_lembaga_min07":"Distance to nearest institution (km)"}
def f3(x): return "" if pd.isna(x) else f"{x:.3f}".replace("-","$-$")
def tex_table(df, cols, caption, label, note, align=None, long=False, size="\\small"):
    align = align or "l"+"r"*(len(cols)-1)
    head=" & ".join(cols)+r" \\"
    body="\n".join(" & ".join(str(v) for v in r)+r" \\" for r in df.values)
    if long:
        return (f"{size}\n\\begin{{longtable}}{{{align}}}\n\\caption{{{caption}}}\\label{{{label}}}\\\\\n\\toprule\n{head}\n\\midrule\n\\endfirsthead\n"
                f"\\toprule\n{head}\n\\midrule\n\\endhead\n{body}\n\\bottomrule\n\\multicolumn{{{len(cols)}}}{{p{{0.95\\textwidth}}}}{{\\footnotesize {note}}}\n\\end{{longtable}}\n\\normalsize\n")
    return (f"\\begin{{table}}[!htbp]\n\\centering\n\\caption{{{caption}}}\\label{{{label}}}\n{size}\n\\begin{{tabular}}{{{align}}}\n\\toprule\n{head}\n\\midrule\n{body}\n\\bottomrule\n\\end{{tabular}}\n"
            f"\\par\\vspace{{2pt}}\\begin{{minipage}}{{0.95\\textwidth}}\\footnotesize {note}\\end{{minipage}}\n\\end{{table}}\n")
parts1=[]
# ---------------- Table A1 variable definitions
A1=[("\\textit{Treatment (IFLS5, 2014)}","",""),
("Non-family credit","1 if any household member obtained a loan from a source other than family or friends in the 12 months before the interview","b2\\_bh: bh07"),
("\\textit{Outcomes (IFLS5, 2014)}","",""),
("Business closed","1 if the household no longer operates any non-farm enterprise (no enterprise reported, or none still operating)","b2\\_nt1: nt01; b2\\_nt2: nt18"),
("Profit","Net profit over the past 12 months, summed over operating enterprises; 0 after closure; IHS and level versions","b2\\_nt2: nt09"),
("Workers","Paid plus unpaid workers in operating enterprises; 0 after closure; winsorised at p99.5","b2\\_nt2: nt22, nt23"),
("\\textit{Pre-treatment covariates (IFLS4, 2007)}","",""),
("Profit, workers","As above, measured in 2007 (IHS of profit)","b2\\_nt2: nt09, nt22, nt23"),
("Assets","Sum of enterprise assets (land, buildings, vehicles, equipment, other); IHS","b2\\_nt2: nt10a, nt10b, nt10c1, nt10c4, nt10h"),
("Enterprise age","2007 minus year the enterprise started (oldest enterprise)","b2\\_nt2: nt15myr"),
("Number of enterprises; at home","Count of operating enterprises; 1 if any is run from home","b2\\_nt2: nt05b"),
("Borrowed in 2007; loan amount","1 if obtained a loan in the past 12 months; IHS of amount","b2\\_bh: bh07, bh10"),
("Per-capita expenditure; size","Log nominal per-capita expenditure; household size","pce07nom"),
("Head sex, age, schooling","Household head (ar02b = 1); schooling converted from education level to years","bk\\_ar1: ar07, ar09, ar16"),
("Urban","1 if urban area","bk\\_sc: sc05"),
("Credit institutions; distance","Number of credit institutions in the community; distance to the nearest (0 if in the community)","Community book 1, section G: g3a, g3b"),
("\\textit{Design variables}","",""),
("Weight","IFLS5 longitudinal household weight with attrition correction","htrack: hwt14la"),
("District","District of residence in 2014; centroid coordinates from embedded table","htrack: sc01\\_14\\_14, sc02\\_14\\_14"),
("Mover","1 if the household moved between waves","htrack"),
("\\textit{Placebo sample (IFLS3, 2000)}","",""),
("2000 covariates and closure 2000--2007","Same definitions as above, measured in 2000; closure if no operating enterprise in 2007","IFLS3 b2\\_nt, b2\\_bh; IFLS4 b2\\_nt1"),]
body="\n".join(f"{a} & {b} & {c} \\\\" for a,b,c in A1)
parts1.append("\\begin{table}[!htbp]\\centering\\caption{Variable definitions and IFLS source variables}\\label{tab:A1}\n\\footnotesize\n\\begin{tabular}{p{3.6cm}p{7.2cm}p{4.2cm}}\n\\toprule\nVariable & Definition & IFLS file: variable \\\\\n\\midrule\n"+body+"\n\\bottomrule\n\\end{tabular}\n\\par\\vspace{2pt}\\begin{minipage}{0.95\\textwidth}\\footnotesize Missing covariate values are median-imputed with missingness indicators. IHS, inverse hyperbolic sine. Variable codes follow the IFLS codebooks; the replication code documents every recode.\\end{minipage}\n\\end{table}\n")
# ---------------- Figure A1 Love plot
t1=pd.read_csv(f"{T}/T1_descriptives.csv"); t1=t1[t1.variable.isin(VAR)].iloc[::-1]
fig,ax=plt.subplots(figsize=(6,4.2)); y=np.arange(len(t1))
ax.scatter(t1.SMD_raw,y,label="Unadjusted",s=18); ax.scatter(t1.SMD_IPW,y,marker="x",label="After IPW",s=22)
for v in (-0.1,0.1): ax.axvline(v,ls=":",c="grey",lw=.8)
ax.axvline(0,c="k",lw=.6); ax.set_yticks(y); ax.set_yticklabels([VAR[v] for v in t1.variable]); ax.set_xlabel("Standardised mean difference (credit − no credit)")
ax.legend(frameon=False,loc="lower right"); fig.tight_layout(); fig.savefig("figA1.pdf"); plt.close(fig)
parts1.append("\\begin{figure}[!htbp]\\centering\\includegraphics[width=0.85\\textwidth]{figA1.pdf}\\caption{Covariate balance before and after inverse probability weighting. Weights use cross-fitted propensity scores from the main specification (random folds, covariate set C). Across 20 cross-fitting splits, 6.7 per cent of households have an average propensity score below 0.1 or above 0.9 and fewer than 0.1 per cent lie outside [0.02, 0.98] (Table A7).}\\label{fig:A1}\\end{figure}\n")
# ---------------- Table A2a 20-split medians
x1=pd.read_csv(f"{X}/X1_repeated.csv"); m=x1[x1.check=="main"].copy()
m["o"]=m.outcome.map({"usaha_tutup":0,"tenaga_kerja":1,"ihs_laba":2}); m["s"]=m.scheme.map({"random":0,"group":1,"spatial":2}); m=m.sort_values(["o","s"])
rows=[[OUTN[r.outcome],SCH[r.scheme],f3(r.ate_median),f3(r.se_adj),f3(r.ate_min),f3(r.ate_max),f"{r.share_signif:.2f}",f3(r.att_median)] for r in m.itertuples()]
parts1.append(tex_table(pd.DataFrame(rows),["Outcome","Folds","Median ATE","SE","Min","Max","Share $p<0.05$","Median ATT"],
 "DML estimates over 20 cross-fitting splits, covariate set C","tab:A2a",
 "Median over 20 random cross-fitting splits; SE is district-clustered and adjusted for split variation, $\\mathrm{median}_s\\{\\mathrm{se}_s^2+(\\hat\\tau_s-\\tilde\\tau)^2\\}^{1/2}$. Min and Max are the smallest and largest split estimates; Share is the fraction of splits with $|t|>1.96$. N = 4326."))
# ---------------- Table A2b single split all
a2=pd.read_csv(f"{T}/T3_dml_ate.csv"); a2["o"]=a2.outcome.map({"usaha_tutup":0,"tenaga_kerja":1,"ihs_laba":2}); a2["s"]=a2.scheme.map({"random":0,"group":1,"spatial":2})
a2=a2.sort_values(["o","spec","s"])
rows=[[OUTN[r.outcome],r.spec,SCH[r.scheme],f3(r.ATE),f3(r.SE_cl),f3(r.SE_iid),f3(r.ATT),f3(r.ATT_SE)] for r in a2.itertuples()]
parts1.append(tex_table(pd.DataFrame(rows),["Outcome","Set","Folds","ATE","SE (cl.)","SE (iid)","ATT","SE ATT"],
 "DML estimates by outcome, covariate set and fold design, first cross-fitting split","tab:A2b",
 "Single split with the seed used for all single-split analyses. Set A, 2007 household covariates; B, A plus district coordinates; C, B plus leave-one-out district means. SE (cl.), district-clustered; SE (iid), heteroskedasticity-robust without clustering.",long=True))
# ---------------- Table A3 BLP/GATES repeated + CLAN
x6=pd.read_csv(f"{X}/X6_blp_repeated.csv")
rows=[]
for r in x6.itertuples():
    rows.append([OUTN[r.outcome],f3(r.beta_median),f3(r.se_median),f"{r.p_median_x2:.2f}",f"{r.share_beta_negative:.2f}"]+[f3(getattr(r,f"gate{g}_median")) for g in range(1,6)])
parts1.append(tex_table(pd.DataFrame(rows),["Outcome","BLP $\\beta_2$","SE","$p$","Share $\\beta_2<0$","G1","G2","G3","G4","G5"],
 "Best linear predictor and sorted group average treatment effects over 20 splits","tab:A3a",
 "Medians over 20 splits; $p$ is twice the median split $p$-value (Chernozhukov et al. 2025). $\\beta_2>0$ indicates that predicted effects track actual effects. G1--G5 are quintiles of the predicted effect from lowest to highest; for closure, lower predicted values mean larger predicted reductions.",size="\\footnotesize"))
for o in ["usaha_tutup","ihs_laba"]:
    c=pd.read_csv(f"{T}/T6c_clan_{o}.csv",index_col=0)
    rows=[[VAR.get(i,i),f3(r.Q5_highest_tau),f3(r.Q1_lowest_tau),f3(r["diff"])] for i,r in c.iterrows() if i in VAR]
    parts1.append(tex_table(pd.DataFrame(rows),["Characteristic","Q5 (highest predicted)","Q1 (lowest predicted)","Difference"],
     f"Classification analysis (CLAN), {OUTN[o].lower()}, first split",f"tab:A3{o[0]}",
     "Weighted means of pre-treatment characteristics in the top and bottom quintiles of the DR-learner prediction. Given the absence of detectable heterogeneity (Table A3a), these contrasts are descriptive.",size="\\footnotesize"))
# ---------------- Table A4 subgroups profit (and closure for completeness)
x4=pd.read_csv(f"{X}/X4_subgroups.csv")
GN={"Enterprise existed in 2000 (history sample)":"Enterprise present in 2000","Not in 2000 history sample":"Enterprise not present in 2000",
"Enterprise age >= 7 years (2007)":"Enterprise age $\\geq$ 7 years","Enterprise age < 7 years (2007)":"Enterprise age $<$ 7 years",
"Borrowed in 2007":"Borrowed in 2007","Did not borrow in 2007":"Did not borrow in 2007","Urban 2007":"Urban 2007","Rural 2007":"Rural 2007"}
def gname(g):
    if g.startswith("DIFF"): return "\\quad Difference"
    return GN[g]
order=[1,0,8,3,2,9,5,4,10,6,7,11]
s=x4[x4.outcome=="ihs_laba"].reset_index(drop=True)
rows=[[gname(s.group[i]),f3(s.ate[i]),f3(s.se[i]),"" if s.group[i].startswith("DIFF") else int(s.n[i]),f"{s.p[i]:.3f}"] for i in range(len(s))]
parts1.append(tex_table(pd.DataFrame(rows),["Subgroup","ATE","SE","N","$p$"],"Effect of credit on IHS profit by subgroup","tab:A4",
 "Weighted means of AIPW scores (random folds, set C) within subgroups, averaged over 20 splits; district-clustered SE. Differences are the first group minus the second in each pair."))
# ---------------- Table A5 closure placebo
p=pd.read_csv(f"{T}/T6_placebo.csv")
u=p[p.weights=="unweighted"].reset_index(drop=True); w=p[p.weights=="weighted"].reset_index(drop=True)
rows=[[u.specification[i].replace("+ ","+\\,"),u.estimator[i],f3(u.estimate[i]),f3(u.se[i]),f3(w.estimate[i]),f3(w.se[i])] for i in range(len(u))]
parts1.append(tex_table(pd.DataFrame(rows),["Specification","Estimator","Unweighted","SE","Weighted","SE"],
 "Closure placebo: effect of 2014 credit on enterprise closure between 2000 and 2007","tab:A5",
 "N = 3560 households with a non-farm enterprise in 2000, 187 districts, 16 provinces. Covariates measured in 2000. Medians over five cross-fitting repetitions with LightGBM learners; district-clustered SE. PLR, partially linear regression. Because closure before 2007 lowers the demand for business credit in 2014, this placebo is biased towards negative values even when credit has no effect (Sect. 6.5)."))
# ---------------- Table A6 sensitivity
x5=pd.read_csv(f"{X}/X5_sensitivity.csv"); BM={"pinjam07":"Borrowed in 2007","ihs_laba07":"IHS profit 2007","jarak_lembaga_min07":"Distance to institution"}
rows=[]
for o in ["usaha_tutup","ihs_laba","tenaga_kerja"]:
    s=x5[x5.outcome==o]; n=s[s.benchmark=="(none)"].iloc[0]
    rows.append([OUTN[o],"--","",f3(n.estimate),f3(n.se),f"RV = {n.RV_q1:.3f}; RV$_{{0.05}}$ = {n.RV_q1_alpha05:.3f}"])
    for r in s[s.benchmark!="(none)"].itertuples():
        rows.append(["",BM[r.benchmark],int(r.k),f3(r.adj_estimate),"",f"[{f3(r.adj_lo)}, {f3(r.adj_hi)}]"])
parts1.append(tex_table(pd.DataFrame(rows),["Outcome","Benchmark","$k$","Estimate","SE","RV or adjusted 95\\% CI"],
 "Sensitivity to unobserved confounding (Cinelli and Hazlett 2020)","tab:A6",
 "Linear probability or linear model with 2007 covariates and province fixed effects, estimated by WLS with classical SE as in sensemakr. RV, robustness value: the partial $R^2$ a confounder would need with both treatment and outcome to remove the estimate (RV$_{0.05}$: to make it insignificant at 5\\%). Benchmark rows give the estimate and interval adjusted for a confounder $k$ times as strongly related to treatment and outcome as the named covariate.",long=True,size="\\footnotesize"))
# ---------------- Table A7 overlap + LOPO
x2=pd.read_csv(f"{X}/X2_overlap.csv"); x2=x2[~x2.estimand.str.startswith("share")]
rows=[[OUTN[r.outcome],r.estimand.replace("<=","$\\leq$").replace("(no refit)","").replace("e(1-e)","$e(1-e)$"),f3(r.est),f3(r.se),int(r.n)] for r in x2.itertuples()]
lo={}
for o in ["usaha_tutup","ihs_laba"]:
    l=pd.read_csv(f"{T}/T5b_lopo_{o}.csv"); lo[o]=(l.ATE.min(),l.ATE.max())
    rows.append([OUTN[o],"Leave one province out, range over 21 (first split)",f"{f3(lo[o][0])} to {f3(lo[o][1])}","",""])
parts1.append(tex_table(pd.DataFrame(rows),["Outcome","Estimand","Estimate","SE","N"],"Overlap diagnostics and leave-one-province-out estimates","tab:A7",
 "Trimmed rows average the AIPW scores of the main specification over households within the stated propensity range, without re-estimating nuisance functions; medians over 20 splits. The overlap-weighted row weights scores by $e(1-e)$. Table 6 of the main text reports the trimmed estimate with nuisance functions re-estimated.",size="\\footnotesize"))
# ---------------- Figure A2 targeting
fig,axs=plt.subplots(1,2,figsize=(7.2,2.9))
pol=pd.read_csv(f"{T}/T7b_policy.csv")
for ax,o in zip(axs,["usaha_tutup","ihs_laba"]):
    c=pd.read_csv(f"{T}/T7_targeting_curve_{o}.csv")
    ax.fill_between(c.share,c.avg_effect-1.96*c.se,c.avg_effect+1.96*c.se,alpha=.2)
    ax.plot(c.share,c.avg_effect,"o-",ms=3,label="Allocate by predicted effect")
    r=pol[pol.outcome==o].iloc[0]
    ax.axhline(r.ATE,ls="--",c="grey",lw=.8,label="ATE (random allocation)")
    ax.scatter([r.current_share],[r.ATT],c="C3",zorder=5,label="Current borrowers (ATT)")
    ax.set_xlabel("Share of enterprises receiving credit"); ax.set_ylabel(f"Average effect: {OUTN[o].lower()}")
axs[0].legend(frameon=False,fontsize=7); fig.tight_layout(); fig.savefig("figA2.pdf"); plt.close(fig)
parts1.append("\\begin{figure}[!htbp]\\centering\\includegraphics[width=\\textwidth]{figA2.pdf}\\caption{Targeting comparison, first split. The line gives the average effect if credit were allocated to the stated share of enterprises with the largest predicted benefit from the DR-learner, with 95\\% intervals; the dot gives the effect among current borrowers at the current coverage (29\\%).}\\label{fig:A2}\\end{figure}\n")
open("parts1.tex","w").write("\n".join(parts1))
# =============== Additional file 2
S=pd.read_csv(f"{SIM}/sim_summary_FULL.csv")
S["meth"]=np.where(S.method=="DML","DML, "+S.scheme.map(SCH)+", "+S.spec,np.where(S.method=="OLS","OLS, C","Naive"))
S=S.sort_values(["block","n","prev","kappa","rho","method","spec","scheme"])
rows=[[f"{int(r.n)}/{int(r.G)}",f"{r.prev:.2f}",f"{r.kappa:g}",int(r.rho),r.meth,f3(r.ate_true),f3(r.bias),f3(r.rmse),f3(r.cov_iid) if not pd.isna(r.cov_iid) else "--",f3(r.cov_cl),f"{r.se_ratio:.2f}"] for r in S.itertuples()]
B1=tex_table(pd.DataFrame(rows),["$n/G$","$p$","$\\kappa$","$\\rho$","Estimator","True ATE","Bias","RMSE","Cov. iid","Cov. cl.","SE/SD"],
 "Monte Carlo results, all 18 scenarios","tab:B1",
 "500 replications per scenario. Baseline: $n=2000$, $G=50$, $p=0.05$, $\\kappa=1$; other blocks vary one factor. Cov., coverage of nominal 95\\% intervals with iid or district-clustered SE; SE/SD, mean clustered SE over the empirical SD. Monte Carlo SE of coverage $\\leq 0.022$. DML rows give fold design and covariate set.",long=True,size="\\scriptsize")
COL={"random":"C0","group":"C1","spatial":"C2"}
def mcfig(block,xvar,xlab,fname,xt=None):
    d=S[(S.block==block)|((S.block=="baseline"))]
    d=d[(d.method=="DML")&(d.spec=="C")]
    fig,axs=plt.subplots(2,3,figsize=(7.2,4.2),sharex=True)
    for j,rho in enumerate([0,1,2]):
        for sc in ["random","group","spatial"]:
            g=d[(d.rho==rho)&(d.scheme==sc)].drop_duplicates(xvar).sort_values(xvar)
            xs=g[xvar].astype(str) if xt else g[xvar]
            axs[0,j].plot(xs,g.bias,"o-",ms=3,c=COL[sc],label=SCH[sc]); axs[1,j].errorbar(xs,g.cov_cl,yerr=1.96*g.mcse_cov_cl,fmt="o-",ms=3,c=COL[sc],capsize=2)
        axs[0,j].axhline(0,c="k",lw=.5); axs[1,j].axhline(.95,c="k",ls="--",lw=.6); axs[0,j].set_title(f"$\\rho$ = {rho}")
        axs[1,j].set_xlabel(xlab)
    axs[0,0].set_ylabel("Bias"); axs[1,0].set_ylabel("Coverage, clustered SE"); axs[0,0].legend(frameon=False,fontsize=7)
    fig.tight_layout(); fig.savefig(fname); plt.close(fig)
S["nG"]=S.n.astype(str)+"/"+S.G.astype(str)
# B1: by rho and spec at baseline
b=S[(S.block=="baseline")&(S.method=="DML")]
fig,axs=plt.subplots(2,3,figsize=(7.2,4.2),sharex=True)
for j,sp in enumerate("ABC"):
    for sc in ["random","group","spatial"]:
        g=b[(b.spec==sp)&(b.scheme==sc)].sort_values("rho")
        axs[0,j].plot(g.rho,g.bias,"o-",ms=3,c=COL[sc],label=SCH[sc]); axs[1,j].errorbar(g.rho,g.cov_cl,yerr=1.96*g.mcse_cov_cl,fmt="o-",ms=3,c=COL[sc],capsize=2)
    nv=S[(S.block=="baseline")&(S.method=="Naive")].sort_values("rho"); axs[0,j].plot(nv.rho,nv.bias,"k--",lw=.8,label="Naive")
    axs[0,j].axhline(0,c="k",lw=.5); axs[1,j].axhline(.95,c="k",ls="--",lw=.6); axs[0,j].set_title(f"Covariate set {sp}"); axs[1,j].set_xlabel("$\\rho$ (spatial confounding)")
axs[0,0].set_ylabel("Bias"); axs[1,0].set_ylabel("Coverage, clustered SE"); axs[0,0].legend(frameon=False,fontsize=7)
fig.tight_layout(); fig.savefig("figB1.pdf"); plt.close(fig)
mcfig("prevalence","prev","Prevalence $p$","figB2.pdf")
mcfig("size","nG","$n/G$","figB3.pdf",xt=True)
mcfig("overlap","kappa","Overlap parameter $\\kappa$","figB4.pdf")
parts2=[B1]
caps={"figB1":"Bias and coverage by strength of spatial confounding $\\rho$ and covariate set, baseline scenario. Error bars are 95\\% Monte Carlo intervals.",
"figB2":"Bias and coverage by outcome prevalence, covariate set C.","figB3":"Bias and coverage by sample size and number of regions, covariate set C.",
"figB4":"Bias and coverage by overlap ($\\kappa=2.5$ gives weaker overlap), covariate set C."}
for k,v in caps.items():
    parts2.append(f"\\begin{{figure}}[!htbp]\\centering\\includegraphics[width=\\textwidth]{{{k}.pdf}}\\caption{{{v}}}\\label{{fig:{k[3:]}}}\\end{{figure}}\n")
open("parts2.tex","w").write("\n".join(parts2))
print("ok")

# ---- fixed table numbering (A2a, A2b, ...) and in-place floats, as in the submitted PDFs
import re
for fn, nums in [("parts1.tex", ["A1", "A2a", "A2b", "A3a", "A3b", "A3c", "A4", "A5", "A6", "A7"]), ("parts2.tex", ["B1"])]:
    s = open(fn).read().replace("[!htbp]", "[H]").replace("ihs profit (rp)", "IHS profit").replace("business closed, first", "business closure, first")
    pos = [m.start() for m in re.finditer(r"\\begin\{table\}|\\begin\{longtable\}", s)]
    for p, n in sorted(zip(pos, nums), reverse=True):
        s = s[:p] + "\\renewcommand{\\thetable}{%s}" % n + s[p:]
    open(fn, "w").write(s)
print("Now compile docs/additional_file_1.tex and docs/additional_file_2.tex from inside build/ with pdflatex.")
