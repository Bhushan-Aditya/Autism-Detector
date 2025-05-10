import matplotlib.pyplot as plt
import seaborn as sns

def generate_risk_report(eye_contact, repetitive, gestures):
    """
    eye_contact: bool
    repetitive: bool
    gestures: bool
    Returns: (fig, risk_level, risk_factors)
    """
    risk_factors = {
        'Limited Eye Contact': not eye_contact,
        'Repetitive Movements': repetitive,
        'Reduced Gestures': not gestures
    }
    risk_score = sum(risk_factors.values())
    if risk_score == 0:
        risk_level = 'Low'
    elif risk_score == 1:
        risk_level = 'Moderate'
    else:
        risk_level = 'High'
    # Plot
    fig, ax = plt.subplots(figsize=(6,3))
    sns.barplot(x=list(risk_factors.keys()), y=[int(v) for v in risk_factors.values()], palette='Reds', ax=ax)
    ax.set_ylim(0,1)
    ax.set_title(f'ASD Risk Factors (Level: {risk_level})')
    ax.set_ylabel('Flagged (1=Yes, 0=No)')
    plt.tight_layout()
    return fig, risk_level, risk_factors 