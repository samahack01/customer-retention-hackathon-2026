# Methodology and Technical Decisions

## Scope

This document summarizes the approach developed collaboratively by Thunderbolt during the Caja de Ahorros Hackathon 2026.

It describes the original project. It is not an executable reproduction and does not include customer data or private infrastructure details.

## 1. Problem Definition

The challenge was framed as a binary classification task involving customer cancellation of deposit products.

The model produced a continuous score to rank customers for potential review. A score alone does not explain why a customer leaves or establish which retention action would work.

## 2. Data Preparation

The feature transformation process included:

- Converting required fields to numeric values.
- Aggregating repeated customer records using the median.
- Clipping negative historical balances to zero.
- Replacing remaining missing feature values with zero.
- Returning one numeric feature row per customer.

These choices made the transformation reproducible, but they also introduced limitations.

Zero imputation can make missing information indistinguishable from a genuine zero balance. Clipping negative balances requires business justification because a negative value is not necessarily a data error.

## 3. Feature Engineering

The model used ten features representing:

- Customer age and tenure.
- Historical balance levels.
- Changes between observed balances.
- Average and maximum observed balances.
- The number of observed dates with a positive balance.

These features summarized both customer context and balance patterns.

Multiple features were derived from the same historical observations. They should not be interpreted as independent sources of evidence.

Loan information was not joined to deposit records through an unverified identifier match. Data from different identifier domains requires a defensible mapping.

## 4. Model Configuration

The documented model was a scikit-learn Random Forest classifier with:

| Parameter | Value |
|---|---|
| Number of trees | 300 |
| Maximum depth | 6 |
| Minimum samples per leaf | 10 |
| Features considered per split | Square root of the feature count |
| Class weighting | Balanced subsample |
| Random seed | 42 |

Random Forest was selected to capture nonlinear relationships. Depth and leaf-size constraints limited model complexity, while class weighting addressed class imbalance.

These choices do not establish that Random Forest was the best possible algorithm.

## 5. Internal Evaluation

Customers were split into training and validation subsets using a stratified 75/25 split.

Evaluation used:

- **AUC-ROC:** discrimination between the two classes.
- **KS:** maximum separation between the class score distributions.
- **Lift at the top 20%:** concentration of positive cases among the highest-scored customers relative to the overall validation population.

Internal validation results must be distinguished from the judges' independent evaluation.

AUC is not an accuracy percentage, and Lift does not measure the number of customers retained.

## 6. Reproducibility and Registration

Feature construction was packaged in a reusable transformation function.

The model was registered in MLflow together with the feature transformation code. Its prediction interface returned continuous scores rather than binary labels.

The submission's technical validation checked delivery compatibility. It did not establish the temporal validity of the predictors or readiness for production.

## 7. Main Limitation: Timing of Information

Individual cancellation dates were not available to establish that every balance observation preceded the outcome.

Consequently, the analysis could not rule out temporal leakage or demonstrate prospective churn prediction.

A stratified customer-level split does not resolve this issue if both subsets contain information observed after cancellation.

## 8. Proposed Next Steps

Before operational use:

1. Define a prediction date and a future cancellation window.
2. Construct features using only information available before the prediction date.
3. Evaluate the model on a later period.
4. Assess probability calibration if scores will be interpreted as probabilities.
5. Compare against a simple baseline.
6. Test retention actions with a suitable comparison group.
7. Measure retention outcomes, contact costs, and unintended effects.

These are proposed improvements, not completed project outcomes.

## 9. Collaboration and Attribution

Samuel González participated across data preparation, programming, feature engineering, training, evaluation, registration, presentation, and coordination.

All five team members contributed across the workflow. The implementation and findings represent collaborative work.

## 10. Publication Boundaries

This portfolio excludes original customer records, restricted datasets, credentials, private infrastructure configuration, and trained artifacts.

The repository includes an independent educational demonstration created after the hackathon with AI assistance. It uses entirely artificial data and does not reproduce the original submission or its results.
