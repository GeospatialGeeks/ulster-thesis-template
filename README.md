# Ulster University thesis template (LaTeX, PDF and Word)

An **unofficial** LaTeX template for Ulster University research degree theses (PhD, MPhil, professional doctorates), set up
to the Doctoral College's *Format of Thesis* guidance, with:

- a PDF that follows the required layout;
- a Word version built from the same source, for supervisors who review in Word.

It is not endorsed by Ulster University. Always check the current guidance and your faculty's requirements before
submission (links below).

## What is set up for you

| Requirement (Doctoral College guidance) | How the template implements it |
|---|---|
| A4 portrait | `geometry` with `a4paper` |
| Sans-serif font (Helvetica or Arial), 12 pt | Helvetica (`helvet`) at 12 pt; Arial in the Word version |
| Line spacing 1.5; extra space after each paragraph | `setspace` (`\onehalfspacing`), `parskip` |
| Binding margin at least 40 mm, other margins at least 20 mm | Left 40 mm; right, top and bottom 25 mm |
| Page numbers, preferably top outer corner; roman numerals for introductory pages | `fancyhdr`, top right; roman, then arabic from Chapter 1 |
| Title page: title (and sub-title), author's full name, faculty "of Ulster University", degree, month and year, word-count statement | `thesis-info.tex` and the title page in `main.tex` |
| Abstract of at most 300 words | `chapters/00_abstract.tex` (with a reminder) |
| Contents, with lists of figures and tables; key of abbreviations | `\tableofcontents`, `\listoffigures`, `\listoftables`; abbreviations with `glossaries` |
| Acknowledgements (including assistance received, and your contribution to collaborative work) | `chapters/00_acknowledgements.tex` |
| Order: preliminary pages, main text, appendices, references | As in `main.tex` |
| Figure numbers and captions below figures; tables numbered separately, with titles above | `caption`; examples in `chapters/04_results.tex` |
| UK English | `babel` British |
| Harvard referencing | `natbib` author-year, `(Author Year)` without a comma; a Harvard (LHS) CSL style for the Word version |
| Declaration on the use of generative AI, where required | `chapters/00_declaration_ai.tex` (template text; follow the Doctoral College guidance on generative AI) |

Hyperlinks for cross-references, citations and URLs are on, in dark colours that print well.

## Use it

**Overleaf**
1. Download this repository as a ZIP (green *Code* button, then *Download ZIP*, or from *Releases*).
2. In Overleaf, choose *New Project*, then *Upload Project*, and select the ZIP.
3. Set the compiler to pdfLaTeX (*Menu*, then *Settings*). The included `latexmkrc` builds the list of abbreviations.

**Your computer** (TeX Live or MiKTeX, with Python 3 for the build script)
```bash
git clone https://github.com/GeospatialGeeks/ulster-thesis-template my-thesis
cd my-thesis
python build.py              # main.pdf
python build.py --docx       # also Thesis.docx (needs pandoc and research-helpers, see below)
```
You can also use `latexmk -pdf main.tex`.

**Word version.** Install [pandoc](https://pandoc.org/installing.html) and the converter:
```bash
pip install git+https://github.com/GeospatialGeeks/research-helpers
```
`python build.py --docx` then writes `Thesis.docx`, keeping:
- the numbers of chapters, sections, tables and figures, and the cross-references as links;
- citations in the Harvard style of `ulster-harvard-lhs.csl`;
- the Ulster page set-up.

Figures need a PNG next to each PDF figure (Word cannot embed PDF).

## Write

1. Fill in `thesis-info.tex`: title, name, faculty, degree, and the month and year of submission.
2. Write the chapters in `chapters/`. Add or rename chapters in `main.tex`.
3. Put figures in `figures/`. Use PDF for the PDF build, plus a PNG of the same name for Word.
4. Add references to `references.bib`. For example, export from Zotero with Better BibTeX, or get BibTeX for a DOI with
   `rh bib refs.bib key=DOI` (research-helpers), which also checks the DOI against Crossref.
5. Cite with `\citep{key}` for "(Author Year)" and `\citet{key}` for "Author (Year)". Cross-reference with
   `\cref{label}`, which writes "Chapter 3", "Table 4.1" and so on.

## Reference list

- **PDF:** uses the `agsm` Harvard style from the `natbib` family. Its reference list is close to, but not identical
  with, the Ulster Library Harvard guides: `agsm` joins the last two authors with "&". Check the Library guide for your
  faculty, and adjust if your examiners require it.
- **Word:** uses `ulster-harvard-lhs.csl`: "Author, A. and Author, B. (Year) Title. Journal, volume, pages. DOI".

## Sources

- Ulster University Doctoral College, [Format of Thesis](https://www.ulster.ac.uk/doctoralcollege/current/submitting-your-thesis/thesis-format)
  and [Notes of guidance](https://www.ulster.ac.uk/doctoralcollege/current/submitting-your-thesis/notesofguidance).
- Ulster University Doctoral College, *Guidance for printing of theses for research degrees*.
- Ulster University Doctoral College, [Guidance on the use of generative AI tools](https://www.ulster.ac.uk/doctoralcollege/current/research-studies-guide/guidance-on-the-use-of-generative-ai-tools).
- Ulster University Library, Harvard referencing guides.

## Licence and contributions

MIT licence (see `LICENSE`): use, adapt and share freely. Corrections and improvements are welcome as issues or pull
requests, especially where the guidance changes.

Maintained by Ammar Ahmad (School of Geography and Environmental Sciences, Ulster University).
