"""
Full Stack Insights Project
=========================================

This Flask application serves as a comprehensive guide for CSS advanced topics
and concepts. It provides interactive dashboards, tutorials, and resources
to help users deepen their understanding of CSS and its applications in modern web development.

"""

from flask import Flask, request, render_template

app = Flask(__name__)
'''
Make built-in functions available in Jinja2 templates:
    Jinja2 templates use a Python-like syntax, they do not 
    directly expose all Python built-in functions like isinstance() and zip(). 
    By updating the Jinja2 environment's globals, we can make these functions
    accessible within our templates.
    
'''

app.jinja_env.globals.update(zip=zip, isinstance=isinstance)

@app.route("/dashboard/<language>")
def dashboard(language):
    """Renders the dashboard for a specific programming language."""
    # print(f"Requested language dashboard: {language}")
    # print(request.args.get('concept'))
    
    if language == "css":
        language= "CSS"
        resources = ["CSS Tutorial", "https://www.w3schools.com/css"]
        concepts = [
            "Grid Layout",
            "Flexbox",
            "Animations", 
            "Responsive Design",
            "CSS Variables",
            "Advanced Selectors",
            "Performance"
        ]
        print(language)
        return render_template("dashboard/dashboard.html.jinja2", lang=language, concepts=concepts, resources=resources)
        
        
    else:
        return "Language not found", 404





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