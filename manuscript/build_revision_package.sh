#!/bin/sh
# Build the revision package: single-file LaTeX zip (manuscript.tex + PNG figures) and a change-marked PDF
# against the version submitted on 20 Oct 2026 (git commit 255e0ff). Run from manuscript/ after build_submission.py.
set -e
OUT=submission_revision; TMP=$(mktemp -d); mkdir -p $OUT
python3 build_latex_package.py manuscript_anon.tex $TMP/new
git archive 255e0ff manuscript review/figures | tar -x -C $TMP
python3 build_latex_package.py $TMP/manuscript/manuscript_anon.tex $TMP/old
(cd $TMP/new && rm -f ../pkg.zip && zip -q ../pkg.zip manuscript.tex *.png); cp $TMP/pkg.zip $OUT/Manuscript_LaTeX.zip
mkdir -p $TMP/diff; cp $TMP/old/*.png $TMP/new/*.png $TMP/diff/
latexdiff --encoding=utf8 --math-markup=whole --config="PICTUREENV=(?:picture|DIFnomarkup|tabular|longtable)[\w\d*@]*" $TMP/old/manuscript.tex $TMP/new/manuscript.tex > $TMP/diff/diff.tex 2>/dev/null
(cd $TMP/diff && pdflatex -interaction=nonstopmode diff.tex >/dev/null; pdflatex -interaction=nonstopmode diff.tex >/dev/null) || true
cp $TMP/diff/diff.pdf $OUT/Manuscript_changes_marked.pdf
echo "written to $OUT"
