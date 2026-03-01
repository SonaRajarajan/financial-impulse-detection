def generate_risk_score(model, X):
    probs = model.predict_proba(X)[:,1]
    return (probs * 100).round(2)   