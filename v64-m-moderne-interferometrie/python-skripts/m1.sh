#!/bin/sh
sed '/^#/ d' < build/p-m1.csv > build/p-m1-new.csv
cat build/p-m1-new.csv | sed -e 's:$:\t\\\\:g' > build/p-m1.tex
ed build/p-m1.tex << END
1i
\sisetup{table-format=1.3}
\begin{tabular}{S[table-format=3.0] S S S}
  \toprule
  {Polarisationswinkel\;/\;$\si{\degree}$} & {\$I_{\text{max}}\;/\;\si{\ampere}$} & {\$I_{\text{min}}\;/\;\si{\ampere}$} & {Kontrast} \\\\
  \midrule
.
\$a
\bottomrule
\end{tabular}
.
wq
END
