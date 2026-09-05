# Part 1 — Review of Week 4 Foundation

**Programme:** AnalystLab Africa Experience Lab
**Project:** HealthConnect Clinic Experience Lab (Improving Patient Appointment Attendance and Healthcare Support Using Data and AI)
**Track:** Data Analytics
**Prepared by:** Hillary Emmanuel
**Week:** Week 5, Solution Development and Implementation

This is a short recap of where Week 4 left off, so the Week 5 analysis can be read against it. It is not a rerun of the Week 4 submission.

---

## 1. The problem this track defined

My job on the Data Analytics side was to work out which factors are genuinely linked to appointment no-shows at HealthConnect Clinic, using the data rather than the assumptions written into the business scenario. That answer feeds two things: the clinic's own decisions, and the predictive model the Data Science track builds later.

The project question is still: how can HealthConnect Clinic use data and AI to reduce missed appointments and improve the patient support experience?

## 2. Week 4 proposed approach

The plan was a segment-rate analysis. Take the variables that separated Attended from No-Show most clearly, and for each one work out the no-show rate by segment. Two composite KPIs sit on top of that. Five business questions were set, each tied to one KPI so every question has a number attached to it:

| # | Business question | KPI |
|---|---|---|
| Q1 | Does a patient's prior no-show history predict whether they miss the next appointment? | No-Show Rate by Prior No-Show Bracket |
| Q2 | Does booking lead time affect the no-show rate, and is there a point where the risk jumps? | No-Show Rate by Booking Lead-Time Band |
| Q3 | Does distance to the clinic affect attendance, and are some distance bands worse than others? | No-Show Rate by Distance Band |
| Q4 | Does sending a reminder actually reduce no-shows, and is the current approach working? | Wasted Slot Rate (no-show count / total scheduled appointments), split by reminder status |
| Q5 | Should cancellations be measured separately from no-shows? | Cancellation-to-No-Show Ratio |

Other decisions carried into Week 5: the work is done in Python with pandas. Missing values in `distance_to_clinic_km` and `waiting_time_minutes` are excluded and documented, not filled in. `appointment_outcome` stays as three separate classes (Attended, No-Show, Cancelled), and Cancelled is never folded into No-Show. Polished stakeholder visuals were left for a BI tool.

## 3. HealthConnect resources relevant to this track

- `HealthConnect_Appointment_Data.csv`: 5,000 appointment records, 18 variables covering patient demographics, appointment and booking detail, previous appointment history, previous no-shows, reminder information, distance to the clinic, waiting time, and the appointment outcome.
- `HealthConnect_Data_Dictionary.xlsx`: the variable definitions and structure.

The Clinic Knowledge Base sits mostly outside the Data Analytics track and was not used in Week 4.

## 4. Key assumptions and limitations from Week 4

- The dataset is clean. No duplicate records, and no logical contradictions such as prior no-shows exceeding prior appointments, or a booking dated after its appointment.
- Only three variables separate the outcomes: `previous_no_shows`, `booking_lead_days`, and `distance_to_clinic_km`. Reminders show only a weak effect, which goes against what the business scenario assumes. Day, time, appointment type, age, and gender showed nothing useful and were set aside.
- These are associations, not causes. Nothing has been checked for confounding yet, so a long lead time might just be standing in for a long distance.
- The data is synthetic. Some dates run into 2026, which confirms it is simulated for training rather than pulled from live clinic records. Any pattern here holds for this dataset, not necessarily the real world.
- A few segments are tiny. A 100% no-show rate at `previous_no_shows = 5`, for example, comes from very few rows and should not be treated as a stable number.
- `distance_to_clinic_km` is missing for about 1.8% of rows and `waiting_time_minutes` for about 1.2%, so distance KPIs are computed on roughly 98% of appointments.
- One cross-track dependency: the three-class outcome decision has to be agreed with the Data Science track before they lock their modelling target.

## 5. What Week 4 said to do in Week 5

1. Actually calculate and chart the five KPIs. Week 4 only defined and justified them.
2. Check whether the three strongest variables still hold up when looked at together, as a quick confounding check rather than a full model.
3. Talk to the Data Science track about the outcome-variable definition before they start modelling.
