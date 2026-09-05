# HealthConnect Clinic — Week 5 (Data Analytics Track)

**Programme:** AnalystLab Africa Experience Lab
**Project:** Improving Patient Appointment Attendance and Healthcare Support Using Data and AI
**Track:** Data Analytics
**Prepared by:** Hillary Emmanuel
**Week 5 focus:** Exploratory Analysis, KPI Development & Business Insights

---

## What's in this repository

| Path | What it is |
|---|---|
| `reports/Part1_Week4_to_Week5_Transition.md` / `.pdf` | Part 1, a short review of the Week 4 foundation |
| `notebooks/HealthConnect_Week5_Analysis.ipynb` | Main deliverable: the Initial HealthConnect Analytics Notebook (data prep, EDA, confounding check, 5 KPIs, dashboard, insights, recommendations, limitations) |
| `reports/CrossTrack_Collaboration.md` / `.pdf` | The simulated Data Analytics to Data Science handover (brief Section 9) |
| `reports/Week5_Project_Summary.md` / `.pdf` | Part 4, the Week 5 Project Summary |
| `outputs/dashboard/HealthConnect_Week5_Dashboard.pbix` | Power BI dashboard (4 KPI cards + 6 panels, dark-blue theme built into the file) |
| `outputs/dashboard/HealthConnect_Week5_Dashboard.pdf` / `.png` | Static exports of the Power BI dashboard, for viewing without Power BI Desktop |
| `outputs/figures/` | The 11 individual EDA and KPI charts saved from the notebook (same dark theme) |
| `data/HealthConnect_Appointment_Data.csv` | Original dataset, never modified |
| `data/HealthConnect_Data_Dictionary.xlsx` | Original data dictionary |
| `data/processed/healthconnect_appointments_prepared.csv` | Cleaned and derived dataset produced by the notebook (26 columns) |
| `scripts/build_report_pdfs.py` | Rebuilds the report PDFs from the markdown files |
| `requirements.txt` | Python dependencies (direct) |
| `requirements-full.txt` | Exact frozen environment (all transitive dependencies) |

---

## Reproducing the analysis

Developed on **Python 3.14**. No version-specific syntax is used.

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
jupyter lab
```

Then open `notebooks/HealthConnect_Week5_Analysis.ipynb` and run all cells top to bottom.
The notebook reads the two original files from `data/` **read-only** and writes the processed
dataset to `data/processed/`. The original files are never modified.

To open the Power BI dashboard, open `outputs/dashboard/HealthConnect_Week5_Dashboard.pbix`
in Power BI Desktop. It reads `data/processed/healthconnect_appointments_prepared.csv`, and the
dark-blue theme is saved inside the file. `HealthConnect_Week5_Dashboard.pdf` / `.png` are static
exports for anyone without Power BI.

To rebuild the report PDFs after editing the markdown: `python scripts/build_report_pdfs.py`.

---

## Headline findings

- **48.5%** of all scheduled appointment slots are lost to a no-show (only 5.3% are properly cancelled).
- The two strongest predictors are **booking lead time** (27.8% → 67.7% no-show rate) and
  **prior no-show history** (43.5% → 68.8%), confirmed to be independent risk factors.
- **Distance** matters only past a threshold (flat to 15 km, then a jump to 54.1%).
- **Reminders** have a real but small effect (~4 points) — not a solution on their own.
- Long-lead-time patients are less likely to properly cancel, supporting the decision to keep
  Cancelled and No-Show as separate outcome categories.

See `reports/Week5_Project_Summary.md` for the full summary and proposed Week 6 focus.
