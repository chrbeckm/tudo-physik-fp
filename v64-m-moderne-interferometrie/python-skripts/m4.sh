#!/bin/sh
# Werte
sed '/^#/ d' < build/p-m4-werte.csv > build/p-m4-werte-new.csv
cat build/p-m4-werte-new.csv | sed -e 's:$:\t\\\\:g' > build/p-m4-werte.tex
ed build/p-m4-werte.tex << END
1i
\sisetup{table-format=2.0}
\begin{tabular}{S[table-format=3.0] S S S S}
  \toprule
  {p\:/\:$\si{\milli\bar}$}
    & {\$\text{Counts}_1$}
    & {\$\text{Counts}_2$}
    & {\$\text{Counts}_3$}
    & {\$\text{Counts}_4$} \\\\
  \midrule
.
\$a
\bottomrule
\end{tabular}
.
wq
END

# Brechungsindices
sed '/^#/ d' < build/p-m4-behbrech.csv > build/p-m4-behbrech-new.csv
cat build/p-m4-behbrech-new.csv | sed -e 's:$:\t\\\\:g' > build/p-m4-behbrech.tex
ed build/p-m4-behbrech.tex << END
1i
\sisetup{table-format=1.8}
\begin{tabular}{S[table-format=3.0]
    S @{$ {}\pm{}$} S
    S @{$ {}\pm{}$} S
    S @{$ {}\pm{}$} S
    S @{$ {}\pm{}$} S}
  \toprule
  {p\:/\:$\si{\milli\bar}$}
    & \multicolumn{2}{c}{\$n_1$}
    & \multicolumn{2}{c}{\$n_2$}
    & \multicolumn{2}{c}{\$n_3$}
    & \multicolumn{2}{c}{\$n_4$} \\\\
  \midrule
.
\$a
\bottomrule
\end{tabular}
.
wq
END

# Fitparameter
sed '/^#/ d' < build/p-m4-fit.csv > build/p-m4-fit-new.csv
cat build/p-m4-fit-new.csv | sed -e 's:$:\t\\\\:g' > build/p-m4-fit.tex
ed build/p-m4-fit.tex << END
1i
\sisetup{table-format=1.6}
\begin{tabular}{S[table-format=1.0]
    S[table-format=1.3] @{$ {}\pm{}$} S[table-format=1.3] S @{$ {}\pm{}$} S}
  \toprule
  {Messreihe}
    & \multicolumn{2}{c}{\$A\:/\:\SI{e-6}{\per\milli\bar}$}
    & \multicolumn{2}{c}{\$B$} \\\\
  \midrule
.
\$a
\bottomrule
\end{tabular}
.
wq
END
