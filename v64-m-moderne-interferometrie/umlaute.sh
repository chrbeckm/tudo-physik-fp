#!/bin/bash
cd content
for file in *; do
  sed -i 's|\\"A|Ä|g' $file
  sed -i 's|\\"U|Ü|g' $file
  sed -i 's|\\"O|Ö|g' $file
  sed -i 's|\\"a|ä|g' $file
  sed -i 's|\\"o|ö|g' $file
  sed -i 's|\\"u|ü|g' $file
  sed -i 's|\\ss |ß|g' $file
  sed -i 's|\\ss|ß|g' $file
done
cd ..
