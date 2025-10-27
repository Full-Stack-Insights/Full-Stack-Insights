# 🪭 Jinja Template Flow

## 📰 Template Template Architecture
```
templates/
├── base.html.jinja2          
├── index.html.jinja2          
└── dashboard/                
    ├── dashboard.html.jinja2  # Main dashboard layout
    ├── top-nav.html.jinja2    # Navigation bar with active states
    ├── sidebar.html.jinja2    # Dynamic sidebar with concepts
    ├── lang_home.html.jinja2
    ├── concept.html.jinja2
    ├── langconcepts/
    ├── macros/
```

### Macros Templates
    macros/
    ├── _concept.html.jinja2
    ├── _lang_home.html.jinja2


### Language Concepts Templates
    langconcepts/
    ├── cssconcepts/
        ├── flexbox.html.jinja2
    ├── htmlconcepts/
        ├── semantic.html.jinja2

- **Base Template[base.html.jinja2](./templates/base.html.jinja2):** Provides common HTML structure with header, main content blocks, and a comprehensive footer


- **Base layout [base.html.jinja2](./templates/base.html.jinja2) is extended by:**
    - [`index.html.jinja2`](./templates/index.html.jinja2): Homepage
    - [`dashboard.html.jinja2`](./templates/dashboard/dashboard.html.jinja2): Main dashboard layout


### Dashboard template system 
- **Main dashboard layout [`dashboard.html.jinja2`](./templates/dashboard/dashboard.html.jinja2) includes**:
    - [`top-nav.html.jinja2`](./templates/dashboard/top-nav.html.jinja2): Navigation bar with active states
    - [`sidebar.html.jinja2`](./templates/dashboard/sidebar.html.jinja2): Dynamic sidebar with concepts
    - [`lang_home.html.jinja2`](): Conditionally rendered
        - uses macro [`_lang_home.html.jinja2`]() to conditionally render the appropiate language home content 
    - [`concept.html.jinja2`](): Conditionally rendered
        - Conditionally renders the appropiate concept


#### Dash Language Home Template flow
- `dashboard.html.jinja2` gets ➡️ `lang_home.html.jinja2` renders its content using macro ➡️  `_lang_home.html.jinja2`
#### Concept Template Flow
- `dashboard.html.jinja2` gets ➡️ `concept.html.jinja2` gets ➡️ `flexbox.html.jinja2` or `semantiic.html.jinja2` renders its content using macro ➡️ `_concept.html.jinja2`







### 📑 Static Files
```
├── static/              # Static assets directory
│   ├── css/            # Stylesheets
│   │   ├── main.css    # Main styles
│   │   ├── footer.css  # Footer-specific styles
│   │   ├── home-banner.css  # Banner styles
│   │   └── home-cards.css   # Card component styles
│   └── images/         # Image assets (currently empty)
```