#!/bin/sh
sed '/^#/ d' < build/output.csv > build/output-new.csv

cat build/output-new.csv | sed \
    -e 's:,:\t\&\t:g' \
    -e 's:$:\t\\\\:g' > build/output.tex

ed build/output.tex << END
1i
\begin{tabular}{S[table-format=1.0] S[table-format=5.0] S[table-format=1.3]}
\toprule
{Data 1} & {Data 2} & {Data 3} \\\\
\midrule
.
\$a
\bottomrule
\end{tabular}
.
wq
END
