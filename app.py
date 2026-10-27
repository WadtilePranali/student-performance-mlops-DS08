from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

PAGE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Student Performance Demo</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 720px; margin: 40px auto; padding: 0 18px; }
    main { border: 1px solid #ddd; border-radius: 12px; padding: 24px; }
    label { display: block; margin-top: 14px; }
    input { width: 100%; box-sizing: border-box; padding: 10px; margin-top: 5px; }
    button { margin-top: 18px; padding: 10px 16px; cursor: pointer; }
    .result { background: #eef7ee; padding: 12px; border-radius: 8px; margin-top: 18px; }
    .note { color: #555; font-size: .9rem; }
  </style>
</head>
<body>
  <main>
    <h1>Student Performance Demo</h1>
    <p>Enter study details to receive a simple rule-based demonstration result.</p>
    <form method="post">
      <label>Study hours per day (0–16)
        <input type="number" name="study_hours" min="0" max="16" step="0.5" required value="{{ study_hours if study_hours is not none else '' }}">
      </label>
      <label>Attendance percentage (0–100)
        <input type="number" name="attendance" min="0" max="100" step="1" required value="{{ attendance if attendance is not none else '' }}">
      </label>
      <button type="submit">Estimate performance</button>
    </form>
    {% if result %}
      <div class="result"><strong>Demo result:</strong> {{ result }}</div>
    {% endif %}
    <p class="note">Educational demonstration only; this is not a trained ML model or a reliable assessment of a real student.</p>
  </main>
</body>
</html>
"""

def estimate_performance(study_hours, attendance):
    # Transparent baseline rule for CI/CD demonstration; replace with a trained model for an ML extension.
    score = (study_hours / 16.0) * 50 + (attendance / 100.0) * 50
    if score >= 70:
        return "High"
    if score >= 45:
        return "Moderate"
    return "Needs Support"

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    study_hours = None
    attendance = None
    if request.method == "POST":
        try:
            study_hours = float(request.form["study_hours"])
            attendance = float(request.form["attendance"])
            if not (0 <= study_hours <= 16 and 0 <= attendance <= 100):
                raise ValueError("Input out of range")
            result = estimate_performance(study_hours, attendance)
        except (ValueError, KeyError):
            result = "Please enter valid values within the stated ranges."
    return render_template_string(PAGE, result=result, study_hours=study_hours, attendance=attendance)

@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
