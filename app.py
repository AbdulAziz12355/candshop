from flask import Flask, request, abort

app = Flask(__name__)

# ===== HOME =====
@app.route("/")
def home():
    return """
    <h1>One Star Shop</h1>
    <p>Website is running ✅</p>
    <p>Admin URL: /admin?code=OSO</p>
    """

# ===== ADMIN =====
@app.route("/admin")
def admin():
    code = request.args.get("code")
    if code != "OSO":
        abort(403)

    return """
    <h1>Admin Panel</h1>
    <p>Welcome Admin ✅</p>
    """

# ===== RUN LOCAL (for Termux test only) =====
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
