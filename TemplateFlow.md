# Jinja Template Flow

### Template System
- **Base Template:** Provides common HTML structure with header, main content blocks, and a comprehensive footer
- **Index Template:** Extends base template with a hero banner and learning resource cards
- **Template Inheritance:** Uses Jinja2's {% extends %} pattern for maintainable code




- app.py                 # 
# Extends [base.html.jinja2](./base.html)
- [`├── index.html.jinja2`](./index.html)






# Static Files
```
├── static/              # Static assets directory
│   ├── css/            # Stylesheets
│   │   ├── main.css    # Main styles
│   │   ├── footer.css  # Footer-specific styles
│   │   ├── home-banner.css  # Banner styles
│   │   └── home-cards.css   # Card component styles
│   └── images/         # Image assets (currently empty)
```