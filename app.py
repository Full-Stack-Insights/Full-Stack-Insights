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
'''
Make built-in functions available in Jinja2 templates:
    Jinja2 templates use a Python-like syntax, they do not 
    directly expose all Python built-in functions like isinstance() and zip(). 
    By updating the Jinja2 environment's globals, we can make these functions
    accessible within our templates.
    
'''

app.jinja_env.globals.update(zip=zip, isinstance=isinstance)

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
    # print(f"Requested language dashboard: {language}")
    # print(request.args.get('concept'))
    if language == "html":
        language= "HTML"
        resources = ["HTML Tutorial", "https://www.w3schools.com/html"]
        concepts = [
            "Semantic Elements",    
            "Complex Forms",
            "Tables & Lists",
            "Media & Graphics",
            "Accessibility",
            "Best Practices"
        ]
        print(language)
        return render_template("dashboard/dashboard.html.jinja2", lang=language, concepts=concepts, resources=resources)
    
    elif language == "css":
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
        
    elif language == "javascript":
        language= "JavaScript"
        resources = ["JavaScript Tutorial", "https://www.w3schools.com/js"]
        concepts = [
            "ES6+ Features",
            "DOM Manipulation",
            "Async Programming", 
            "Error Handling",
            "Modules",
            "Best Practices"
        ]
        return render_template("dashboard/dashboard.html.jinja2", lang=language, concepts=concepts, resources=resources)
        
    elif language == "python":
        language= "Python"
        resources = ["Python For Beginners", "https://www.python.org/about/gettingstarted"]
        concepts = [
            "Lists",
            "Templating Engines",
            "Data Processing for Frontend", 
            "File Handling & Media",
            "Frontend Asset Management",
            "PyScript",
            "Python-based UI Frameworks"
        ]
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