#!/bin/bash
set -e

# English CV
pandoc cv.md \
  --template _pandoc/cv-template.tex \
  --pdf-engine=pdflatex \
  -o assets/pdf/profile/CV.pdf
echo "Built: assets/pdf/profile/CV.pdf"

# Japanese CV
pandoc cv_jp.md \
  --template _pandoc/cv-jp-template.tex \
  --pdf-engine=lualatex \
  -o assets/pdf/profile/CV_jp.pdf
echo "Built: assets/pdf/profile/CV_jp.pdf"
