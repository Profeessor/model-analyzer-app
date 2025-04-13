def run_model(data):
    # Simulate model computation
    alpha = sum(data) / len(data)
    return {"alpha": round(alpha, 2)} 