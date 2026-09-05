# Cross-Track Collaboration — Week 5

**Track:** Data Analytics
**Prepared by:** Hillary Emmanuel

HealthConnect is a shared project, so Week 5 asks each track to identify at least one dependency
or collaboration point with another track. This is a simulated handoff: I have worked out what
the Data Science track will need from the Data Analytics work and prepared my outputs for it,
rather than exchanging files with a specific person.

## 1. Which track

Data Science.

## 2. The dependency, and what is being handed over

The Data Science track will build a predictive model on the same 5,000-row appointment dataset.
Their work depends on decisions the Data Analytics track makes first, in particular the
definition of the outcome variable. The handover from my Week 5 work covers three things:

- **The outcome-variable recommendation.** Keep `appointment_outcome` as three classes
  (Attended, No-Show, Cancelled) and do not merge Cancelled into No-Show. Section 5 of the
  notebook (KPI 5) gives the evidence: the cancellation-to-no-show ratio moves in a clear
  direction as booking lead time grows (0.202 down to 0.076), which means the two outcomes
  behave differently and should not be collapsed into one target.
- **Three validated candidate features.** `previous_no_shows`, `booking_lead_days`, and
  `distance_to_clinic_km`. Section 4 of the notebook shows they are independent of each other
  (lead time and distance correlate near zero, and each effect holds up when checked inside
  the others' groups), so the Data Science track can treat all three as useful features
  without first testing for redundancy.
- **The processed dataset and the engineered bands.**
  `data/processed/healthconnect_appointments_prepared.csv`, with the documented boundaries for
  `prior_no_show_bracket`, `lead_time_band`, and `distance_band`, so feature engineering can
  start from there instead of the raw CSV.

## 3. Why the dependency matters

Week 4 already flagged this as a risk. If the Data Science track picked a different prediction
target, for example by merging Cancelled into No-Show, before the outcome categories were
checked, the two tracks' work would drift apart and the KPI framing here would no longer line
up with their model. The outcome-variable decision needs to be settled with evidence before
they lock a target for their baseline model.

## 4. What changed in my Week 5 work as a result

Working out what the Data Science track would need shaped how I did the analysis:

- I kept the three-class outcome throughout and built KPI 5 specifically so the "keep them
  separate" recommendation rests on evidence rather than the Week 4 argument alone.
- I ran the confounding check in Section 4 partly so the three features could be handed over
  as genuinely independent, not just individually interesting.
- I saved the processed dataset and documented every band boundary so the handover is a file
  and a short spec, not something the Data Science track has to reconstruct from the notebook.

If a Data Science intern is available before the model is built, the next step is a short
review of the outcome-variable recommendation with them so it is agreed rather than assumed.
