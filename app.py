"""
Full Stack Insights Project
=========================================

This Flask application serves as a comprehensive guide of various advanced aspects
of full stack development, including:

1. HTML
2. CSS
3. JavaScript
4. Python

"""

from flask import Flask, request, render_template

app = Flask(__name__)


# =============================================================================
# HOME PAGE - Navigation and Overview
# =============================================================================

@app.route('/')
def home():
    """Main page with cards with links to different sections of the dashboard."""
    return render_template('index.html.jinja2')

@app.route("/dashboard/<language>")
def dashboard(language):
    """Renders the dashboard for a specific programming language."""
    return render_template('dashboard/dashboard.html.jinja2', language=language)





# =============================================================================
# MAIN APPLICATION RUNNER
# =============================================================================

if __name__ == '__main__':
    print("="*60)
    print("🚀 Full Stack Insights Server Starting...")
    print("="*60)
    print("📍 Visit: http://127.0.0.1:5000")
    print("📚 Documentation: See README.md")
    print("⚡ Debug Mode: Enabled")
    print("="*60)
    
    app.run(debug=True, host='127.0.0.1', port=5000)