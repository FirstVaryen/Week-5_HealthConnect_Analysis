# Week 5 Project Summary

**Programme:** AnalystLab Africa Experience Lab
**Project:** HealthConnect Clinic Experience Lab (Improving Patient Appointment Attendance and Healthcare Support Using Data and AI)
**Track:** Data Analytics
**Prepared by:** Hillary Emmanuel
**Week:** Week 5, Solution Development and Implementation

## 1. Week 4's expectations for Week 5

Week 4 left three jobs for Week 5:

1. Calculate and chart the five KPIs (Week 4 only defined them).
2. Check whether the three strongest variables still hold up when looked at together.
3. Agree the outcome-variable definition with the Data Science track before they model.

## 2. The Week 5 deliverables

- Prepared the data on a copy: checked types, missing values, duplicates, category consistency, and cross-field logic. The original CSV was never touched.
- Ran the EDA across all eight dimensions the brief asks for: appointment characteristics, patient characteristics, previous history, reminders, waiting time, distance, cancellations, and no-show outcomes.
- Ran a confounding check. The three strongest variables turned out to be independent risk factors, not one signal showing up three times.
- Calculated, charted, and interpreted all five KPIs.
- Built a Power BI dashboard: four KPI cards and six panels covering the headline number and the five KPIs, on a dark theme, with a sort-order-corrected export of the processed data behind it. PDF and PNG exports included.
- Wrote up five business insights with what each one means for the clinic, five recommendations, and a limitations section.
- Identified and prepared the Data Analytics to Data Science handover (see `CrossTrack_Collaboration.md`).

## 3. Key findings

- The overall no-show rate is 48.5%. Nearly half of every booked slot goes unused, against just 5.3% that are properly cancelled.
- The two strongest predictors are booking lead time (27.8% no-show rate at 0-7 days, rising to 67.7% at 46-60 days) and prior no-show history (43.5% at zero prior misses, rising to 68.8% at three or more). They also stack: a patient with two or more prior no-shows and a 31+ day lead time misses 73.0% of the time. That group is only 4.7% of all bookings.
- Distance only bites past a point. The rate is flat up to 15 km, then jumps to 54.1% beyond 15 km.
- Reminders help a little, about 4 percentage points, but they are not the fix on their own.
- The cancellation-to-no-show ratio drops as lead time grows (0.202 down to 0.076). Patients who book far ahead are less likely to warn the clinic, which is why Cancelled and No-Show should stay separate.

## 4. Challenges

- Getting a reproducible Python setup running on version 3.14, which is new enough that I had to check each package would install before settling on the toolchain.
- Choosing how finely to band the continuous variables. I sized every band by row count so no KPI leans on a group that is too small to trust, and where one group was unavoidably small (the "3+" prior no-show bracket, 93 rows) I flagged it in the notebook rather than hiding it.
- Power BI sorted the band columns alphabetically by default, which would have shown two of the three KPI charts in the wrong order. I added numeric sort-order columns to the export to fix it.

## 5. Decisions and why

- Rows with a missing distance are excluded from distance KPIs, not filled in. Filling them would add made-up values into a variable that actually predicts no-shows. This carries over from the Week 4 plan and still holds.
- `appointment_outcome` stays as three classes. Week 4 argued this on principle; Week 5 has the KPI 5 evidence to back it.
- The individual analysis charts are done in Python inside the notebook, next to the interpretation for each one. The summary dashboard is done in Power BI, since that is the more presentation-ready tool and it was the Week 4 intent.

## 6. Changes to the Week 4 approach

The KPI definitions, the business questions, and the missing-data handling are all unchanged. Week 5 ran the Week 4 plan as written. The one addition is the Power BI dashboard. Week 4 had pushed visualisation tooling to a later phase, and I brought it forward so there is a more presentation-ready version.

## 7. Cross-track collaboration

The Week 5 brief asks each track to identify a dependency with another track and says this is meant to simulate a multidisciplinary environment. The dependency here is Data Analytics to Data Science: they will model on the same dataset, so their outcome-variable choice depends on the categories being checked first. I prepared that handover: the three-class outcome recommendation with KPI 5 as evidence, the three validated independent features, and the processed dataset with documented band boundaries. Working out what they would need also shaped my own analysis (I built KPI 5 and ran the confounding check partly for this). Full write-up in `CrossTrack_Collaboration.md`.

<div style="page-break-before: always;"></div>

## 8. Remaining work

- The predictive model is to be built by the Data Science track.
- The distance and prior-no-show thresholds should be rechecked once there is more data, since the "3+" bracket and the 15+ km band are based on smaller samples.

## 9. Proposed focus for Week 6

- Track the five KPIs against fresh data as it arrives and see whether these patterns hold over time.
- Once the Data Science track has a baseline model, check whether the three validated features actually carry weight in it, not just in a rate comparison.
- Look harder at the double-risk group (two or more prior no-shows plus a 31+ day lead time). It is small at 4.7% of bookings but has the highest no-show rate by a wide margin at 73.0%, so it may be worth designing a specific intervention for later.
