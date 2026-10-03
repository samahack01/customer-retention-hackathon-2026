"""Post-hackathon educational demo using entirely artificial data.

This is not the original submission. The generated features have no banking
meaning and are not derived from customer records or dataset statistics.
"""

import numpy as np
from scipy.stats import ks_2samp
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split


def evaluate(y_true, scores):
    """Calculate discrimination and ranking metrics for binary labels."""
    y_true = np.asarray(y_true)
    scores = np.asarray(scores)
    top_count = max(1, int(np.ceil(0.20 * len(scores))))
    top_indices = np.argsort(-scores, kind="stable")[:top_count]

    return {
        "auc_roc": float(roc_auc_score(y_true, scores)),
        "ks": float(
            ks_2samp(scores[y_true == 1], scores[y_true == 0]).statistic
        ),
        "lift_at_20_pct": float(
            y_true[top_indices].mean() / y_true.mean()
        ),
    }


def main():
    # Arbitrary simulation settings, unrelated to the event's customer data.
    X, y = make_classification(
        n_samples=2000,
        n_features=10,
        n_informative=6,
        n_redundant=2,
        weights=[0.70, 0.30],
        flip_y=0.05,
        class_sep=0.8,
        random_state=42,
    )

    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.25, stratify=y, random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=6,
        min_samples_leaf=10,
        max_features="sqrt",
        class_weight="balanced_subsample",
        random_state=42,
        n_jobs=-1,
    )

    model.fit(X_train, y_train)
    scores = model.predict_proba(X_val)[:, 1]

    print("SYNTHETIC DEMO ONLY - not hackathon or customer results")
    for name, value in evaluate(y_val, scores).items():
        print(f"{name}: {value:.4f}")


if __name__ == "__main__":
    main()
