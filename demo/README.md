# Synthetic Classification Demo

An independent educational demonstration created after the hackathon with AI assistance.

This demo illustrates model training and evaluation using entirely artificial data. It is not the original competition submission.

## What It Demonstrates

- Generating a synthetic binary classification dataset.
- Creating a stratified training-validation split.
- Training a Random Forest classifier.
- Calculating AUC-ROC, KS, and Lift at the top 20%.

The classifier configuration follows the documented hackathon model. The synthetic features, labels, sample size, and class proportions are arbitrary simulation choices.

## What It Does Not Demonstrate

- The original customer data or business feature engineering.
- The original model's performance.
- Prospective customer churn prediction.
- Customer retention impact.
- AWS connectivity or MLflow registration.

The generated features have no banking meaning. Synthetic performance must not be presented as a hackathon result.

## Environment

The script was executed successfully in a Linux environment with:

- Python 3.12.14
- NumPy 2.3.5
- SciPy 1.17.0
- scikit-learn 1.8.0

The Windows PowerShell instructions were successfully verified on the portfolio owner's computer using Python 3.12.10, NumPy 2.3.5, SciPy 1.17.0, and scikit-learn 1.8.0.

## Get the Files

Download the repository through **Code → Download ZIP** and extract it, or clone it using Git.

Open a terminal in the repository's root folder: the folder containing `demo`, `docs`, and the main `README.md`.

Use Python 3.12 for the following commands.

## Windows — PowerShell

Create an isolated environment:

```powershell
py -3.12 -m venv .venv
```

Install the dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install -r demo/requirements.txt
```

Run the demonstration:

```powershell
.\.venv\Scripts\python.exe demo/train_synthetic.py
```

## macOS / Linux

Create an isolated environment:

```bash
python3.12 -m venv .venv
```

Install the dependencies:

```bash
.venv/bin/python -m pip install -r demo/requirements.txt
```

Run the demonstration:

```bash
.venv/bin/python demo/train_synthetic.py
```

## Output

The program prints this notice followed by three metric values:

```text
SYNTHETIC DEMO ONLY - not hackathon or customer results
```

- **AUC-ROC:** discrimination between the artificial classes.
- **KS:** separation between their score distributions.
- **Lift at 20%:** concentration of positive labels in the highest-scored fifth of the validation set relative to overall prevalence.

These metrics describe only the generated classification task.

## Data Handling

The script creates artificial data in memory. It does not read customer files, connect to AWS, or save datasets and trained models.

An internet connection is needed to install dependencies. The training script itself does not require network access.

## Troubleshooting

- **Python is not found:** check that Python 3.12 is installed and available through the command used above.
- **The requirements file cannot be found:** run the commands from the repository root.
- **A module cannot be imported:** install dependencies using the same virtual-environment interpreter used to run the script.

## Relationship to the Original Project

The hackathon implementation was developed collaboratively by Thunderbolt.

This later demo was prepared with AI assistance for the portfolio. It should be evaluated separately from the original submission and its results.

[Return to the project overview](../README.md)
