# Digital Banking Analysis in Vietnam

## Project Overview

This project analyzes the digital banking market in Vietnam, covering market overview, technology trends, competitive landscape, strategic analysis, and recommendations. It includes data analysis scripts, research notes, and a final consulting report.

## Repo Structure

- `00_Cover_Page.md`: Cover page for the report
- `/01_Research/`: Market research notes and data
- `/02_Analysis/`: Analysis files including scripts and markdowns
- `/03_Recommendations/`: Strategic proposals
- `/data/`: Raw data files
- `/deliverables/`: Output reports and charts
- `template.tex`: LaTeX template for PDF formatting
- `README.md`: This file

## How to Run

1. Make sure you have [Pandoc](https://pandoc.org/) and LaTeX (e.g., TeX Live) installed.
2. Use the command below to build the PDF report:

```bash
pandoc \
  00_Cover_Page.md \
  01_Research/market_overview.md \
  01_Research/tech_trends.md \
  01_Research/competitor_list.md \
  02_Analysis/swot_analysis.md \
  02_Analysis/porters_five_forces.md \
  03_Recommendations/strategy_proposals.md \
  04_Conclusion.md \
  --pdf-engine=xelatex \
  --variable geometry:"top=2.5cm,bottom=2.5cm,left=2.5cm,right=2.5cm" \
  --toc \
  -o deliverables/Digital_Banking_in_Vietnam.pdf
