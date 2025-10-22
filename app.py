"""
Full Stack Insights Project
=========================================

This Flask application serves as a comprehensive demonstration of various aspects
of full stack development, including:

1. Frontend and Backend Integration
2. RESTful API Design
3. Database Interaction
4. User Authentication
5. Deployment Strategies

Run this application and visit the routes to see live demonstrations.

"""

from flask import Flask, request, render_template


app = Flask(__name__)


# =============================================================================
# HOME PAGE - Navigation and Overview
# =============================================================================

@app.route('/')
def home():
    """Main page with navigation to all URL parameter demonstrations"""
    return render_template('index.html.jinja2')
# =============================================================================
# ERROR HANDLERS
# =============================================================================

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html.jinja2'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html.jinja2'), 500

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