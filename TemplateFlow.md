# 🪭 Jinja Template Flow

## 📰 Template  Template Architecture
```
templates/
├── base.html.jinja2          
├── index.html.jinja2          
└── dashboard/                
    ├── dashboard.html.jinja2  # Main dashboard layout
    ├── top-nav.html.jinja2    # Navigation bar with active states
    └── sidebar.html.jinja2    # Dynamic sidebar with concepts
```

- **Base Template[base.html.jinja2](./templates/base.html.jinja2):** Provides common HTML structure with header, main content blocks, and a comprehensive footer


- **Base layout [base.html.jinja2](./templates/base.html.jinja2) is extended by:**
    - [`index.html.jinja2`](./templates/index.html.jinja2): Homepage
    - [`dashboard.html.jinja2`](./templates/dashboard/dashboard.html.jinja2): Main dashboard layout


### Dashboard template system 
- **Main dashboard layout [`dashboard.html.jinja2`](./templates/dashboard/dashboard.html.jinja2) includes**:
    - [`top-nav.html.jinja2`](./templates/dashboard/top-nav.html.jinja2): Navigation bar with active states
    - [`sidebar.html.jinja2`](./templates/dashboard/sidebar.html.jinja2): Dynamic sidebar with concepts





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