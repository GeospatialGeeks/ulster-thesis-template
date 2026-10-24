"""Build the thesis as PDF and, optionally, as Word.

    python build.py            PDF (pdflatex, BibTeX, makeglossaries, pdflatex twice) -> main.pdf
    python build.py --docx     also Thesis.docx (needs pandoc and: pip install git+https://github.com/AhmadAmmar/research-helpers)

The Word version keeps the chapter, section, table and figure numbers and the cross-references of the PDF, uses the
Ulster Harvard style (ulster-harvard-lhs.csl) and the Ulster page set-up (A4, binding margin 40 mm, Arial 12 pt, 1.5
line spacing). Figures need a PNG beside each PDF figure (Word cannot embed PDF).
"""
import pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent


def run(cmd):
    return subprocess.run(cmd, cwd=HERE, capture_output=True, text=True, errors="replace")


def pdf():
    for c in (["pdflatex", "-interaction=nonstopmode", "main.tex"], ["bibtex", "main"], ["makeglossaries", "main"],
              ["pdflatex", "-interaction=nonstopmode", "main.tex"], ["pdflatex", "-interaction=nonstopmode", "main.tex"]):
        run(c)
    log = (HERE / "main.log").read_text(encoding="utf-8", errors="replace")
    errors = sorted(set(re.findall(r"^! (.*)$", log, re.M)))
    undef = sorted(set(re.findall(r"(?:Reference|Citation) `([^']+)' on page \d+ undefined", log)))
    print(f"PDF: {len(errors)} errors, {len(undef)} undefined references or citations"
          + (": " + ", ".join(errors + undef) if errors or undef else ""))


def info(key):
    t = (HERE / "thesis-info.tex").read_text(encoding="utf-8")
    m = re.search(r"\\newcommand\{\\" + key + r"\}\{(.*?)\}\s*$", t, re.M)
    return m.group(1).replace("\\\\", " ") if m else ""


def docx():
    try:
        from research_helpers.latex2docx import convert, PageSetup
    except ImportError:
        sys.exit("install research-helpers for the Word version: pip install git+https://github.com/AhmadAmmar/research-helpers")
    front = (f"\\textbf{{{info('ThesisTitle')}}}\n\n{info('ThesisAuthor')}\n\n{info('ThesisFaculty')} of Ulster University\n\n"
             f"Thesis submitted for the degree of {info('ThesisDegree')}\n\n{info('SubmissionMonthYear')}\n\n"
             "I confirm that the word count of this thesis is less than 100,000 words excluding the title page, contents, "
             "acknowledgements, summary or abstract, abbreviations, footnotes, diagrams, maps, illustrations, tables, appendices, "
             "and references or bibliography.\n\n")
    code = convert(HERE / "main.tex", HERE / "Thesis.docx", csl=HERE / "ulster-harvard-lhs.csl", front_matter=front,
                   page=PageSetup(left_mm=40, right_mm=25, top_mm=25, bottom_mm=25, font="Arial", size_pt=12, line_spacing=1.5))
    print("Word:", "Thesis.docx" if code == 0 else f"failed ({code})")


if __name__ == "__main__":
    pdf()
    if "--docx" in sys.argv:
        docx()
