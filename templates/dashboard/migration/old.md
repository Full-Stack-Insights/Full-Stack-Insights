{# {% macro render_css_concept(css_concept_header, css_concept_intro_h2, css_concept_intro_text, css_concept_details) %}
{# WHOLE CONTAINER #}
<main class="concept-main">

    {# CONCEPT HEADING #}
    <div class="main-concept-heading-container">
        <h1>{{ css_concept_header }}</h1>
    </div>

    {# CONCEPT INTRODUCTION #}
    <section class="main-concept-intro-container" >
        <h2>{{ css_concept_intro_h2 }}</h2>
        {% for line in css_concept_intro_text %}
            <p>{{ line }}</p>
            <br>
        {% endfor %}
    </section>

    {# ALL SUB CONCEPTS SECTION  #}
    <div class="sub-concepts-content-container">
        {% for detail in css_concept_details %}
            {# Detect if using dictionary or list structure #}
            {% if detail is mapping %}
                {# Dictionary structure #}
                {% set title = detail.title %}
                {% set description = detail.description %}
                {% set content = detail.content %}
                {% set demo_data = detail.demo %}
                {% set properties = detail.properties %}
            {% else %}
                {# Legacy list structure #}
                {% set title = detail[0] %}
                {% set description = detail[1] %}
                {% set content = detail[2] %}
                {% set demo_data = detail[3] %}
                {% set properties = detail[4] %}
            {% endif %}

            {# SINGLE SUB CONCEPT SECTION  #}
            <section id="" class="concept-section">
                    <div class="concept-header">
                        <h2 class="css-concept-title">{{ title }}</h2>
                        <p class="css-concept-description">{{ description }}</p>
                    </div>
                    <div class="concept-content">
                <p>{{ content }}</p>
            
                
                <div class="code-block">
                    {% if title == 'Flexbox Basics' %}
                        <span class="code-property">.container</span> {
                        <span class="code-property">display</span>: <span class="code-value">flex</span>;}
                    {% elif title == 'Flex Direction' %}
                        <span class="code-property">flex-direction</span>: <span class="code-value">row</span>; /* default */
                        <span class="code-property">flex-direction</span>: <span class="code-value">column</span>;
                        <span class="code-property">flex-direction</span>: <span class="code-value">row-reverse</span>;
                        <span class="code-property">flex-direction</span>: <span class="code-value">column-reverse</span>;
                    {% elif title == 'Justify Content' %}
                        <span class="code-property">justify-content</span>: <span class="code-value">flex-start</span>; /* default */
                        <span class="code-property">justify-content</span>: <span class="code-value">center</span>;
                        <span class="code-property">justify-content</span>: <span class="code-value">space-between</span>;
                    {% elif title == 'Align Items' %}
                        <span class="code-property">align-items</span>: <span class="code-value">stretch</span>; /* default */
                        <span class="code-property">align-items</span>: <span class="code-value">center</span>;
                        <span class="code-property">align-items</span>: <span class="code-value">flex-end</span>;
                    {% elif title == 'Flex Wrap' %}
                        <span class="code-property">flex-wrap</span>: <span class="code-value">nowrap</span>; /* default */
                        <span class="code-property">flex-wrap</span>: <span class="code-value">wrap</span>;
                        <span class="code-property">flex-wrap</span>: <span class="code-value">wrap-reverse</span>;
                    {% elif title == 'Flex Item Properties' %}
                        <span class="code-property">flex-grow</span>: <span class="code-value">0</span>; /* default - don't grow */
                        <span class="code-property">flex-shrink</span>: <span class="code-value">1</span>; /* default - can shrink */
                        <span class="code-property">flex-basis</span>: <span class="code-value">auto</span>; /* default - based on content */<br>

                        <span>/* Shorthand */</span><br>
                        <span class="code-property">flex</span>: <span class="code-value">1</span>; /* grow: 1, shrink: 1, basis: 0% */
                        <span class="code-property">flex</span>: <span class="code-value">0 1 auto</span>; /* explicit values */
                    {% elif title == 'Flex Basis' %}

                    {% endif %}
                </div>

                <!-------------------------------
                Universal Demo Container Handler: handles both single demo containers and multiple demo containers(any)
                         Sufficient because the data structures follow the standard patterns flat and 2 level nested
                        Auto-Detection: Automatically detects single vs. multiple demo structures
                            - [['Demo A'], ['A1', 'A2', 'A3', 'A4', 'A5']]  (single/flat): Detects flat item list and uses all items for the single demo
                            - [['Demo A', 'Demo B', 'Demo C'], [['A1', 'A2'], ['B1', 'B2', 'B3'], ['C1']]] (multiple/nested): Detects nested item lists and maps each demo to its corresponding item list(uses specific index for each demo)
                            - [['Demo A', 'Demo B', 'Demo C'], [['A1', 'A2'], ['B1', 'B2', 'B3'], ['C1']]]: Any number of demos at the same nesting level
                        Flexible Processing: Handles both flat and nested item arrays
                        Consistent Rendering: Produces uniform output regardless of input format
                        Error Handling: Safe for different data structures


                        Limited with complex or deep nesting, DOESN'T Handle:
                            - Deep nesting (3+ levels): 
                                - [['Deep Demo'], [[['Level1', 'Level2'], ['Level3']]]]
                                    - Results in: Item 1: ['Level1', 'Level2'], Item 2: ['Level3']
                                    - Instead of flattening to individual items
                            - Mixed structures (some demos flat, others nested)
                            - Irregular nesting depths
                            - Complex nested objects
                ------------------------------------->
                {# Handle both dictionary and list demo structures #}
                {% if demo_data is mapping %}
                    {# Dictionary structure - simplified demo handling #}
                    {% if demo_data.headers is defined %}
                        {# Multiple demos #}
                        {% for i in range(demo_data.headers | length) %}
                            <div class="demo-container">
                                <div class="demo-label">{{ demo_data.headers[i] }}</div>
                                <div class="flex-container wrap-nowrap">
                                    {% for item in demo_data.items[i] %}
                                    <div class="flex-item">{{ item }}</div>
                                    {% endfor %}
                                </div>
                            </div>
                        {% endfor %}
                    {% else %}
                        {# Single demo #}
                        <div class="demo-container">
                            <div class="demo-label">{{ demo_data.header }}</div>
                            <div class="flex-container wrap-nowrap">
                                {% for item in demo_data.items %}
                                <div class="flex-item">{{ item }}</div>
                                {% endfor %}
                            </div>
                        </div>
                    {% endif %}
                {% else %}
                    {# Legacy list structure #}
                    {% set demo_names = demo_data[0] %}
                    {% set demo_items = demo_data[1] %}
                    
                    {% for i in range(demo_names | length) %}
                        {% set demo_name = demo_names[i] %}
                        {% set current_items = [] %}
                        
                        {# Detect if items are nested or flat #}
                        {% if demo_items[0] is iterable and demo_items[0] is not string %}
                            {# Nested - use specific index #}
                            {% set current_items = demo_items[i] %}
                        {% else %}
                            {# Single demo - use all items #}
                            {% set current_items = demo_items %}
                        {% endif %}
                        
                        <div class="demo-container">
                            <div class="demo-label">{{ demo_name }}</div>
                            <div class="flex-container wrap-nowrap">
                                {% for item in current_items %}
                                <div class="flex-item">{{ item }}</div>
                                {% endfor %}
                            </div>
                        </div>
                    {% endfor %}
                {% endif %}

                



                <div class="more-info key-concepts">
                    <h3>Key Concepts:</h3>
                    <ul>
                    {% if properties[0] is mapping %}
                        {# Dictionary structure for properties #}
                        {% for property in properties %}
                            <li><strong>{{ property.name | safe }}</strong> {{ property.description }}</li>
                        {% endfor %}
                    {% else %}
                        {# Legacy list structure for properties #}
                        {% for concept in properties %}
                            <li><strong>{{ concept[0] | safe }}</strong> {{ concept[1] }}</li>
                        {% endfor %}
                    {% endif %}
                    </ul>
                </div>

            </div>
            </section>

        {% endfor %}
    </div>


</main>

{% endmacro %} #}


________________________________________________________________________


{# Detect if items are nested or flat(Single name or list of names) #}
                        {% if sub_concept.demo.name is iterable and sub_concept.demo.name is not string %}
                            {% set demo_name_list = sub_concept.demo.name %}
                            {% for name in demo_name_list %}
                                <div class="demo-container">
                                    <div class="demo-label">{{ name }}</div>
                                    <div class="flex-container wrap-nowrap">
                                     {% for examples in sub_concept.demo.examples %}
                                        {# Detect if items are nested or flat(Single name or list of names) #}
                                        {% if examples is iterable and examples is not string %}
                                            {% set examples_list = examples %}
                                            {% for example in examples_list %}
                                                <div class="flex-item">{{ example }}</div>
                                            {% endfor %}
                                        {% endif %}
                                    {% endfor %}
                                    </div>
                                </div>
                            {% endfor %}
                        {% else %}
                            <div class="demo-container">
                                <div class="demo-label">{{ sub_concept.demo.name }}</div>
                                    <div class="flex-container wrap-nowrap">
                                     {% for example in sub_concept.demo.examples %}
                                        <div class="flex-item">{{ example }}</div>
                                    {% endfor %}
                                    </div>
                            </div>
                        {% endif  %}










































































































                                  {% if sub_concept.demo.name is iterable and sub_concept.demo.name is not string %}
                            {% for demo_name, example in zip(sub_concept.demo.name, sub_concept.demo.examples) %}
                                <div class="demo-container">
                                        <div class="demo-label">{{ demo_name }}</div>
                                        <div class="flex-container wrap-nowrap">
                                        {% for example in example %}
                                            <div class="flex-item">{{ example }}</div>
                                        {% endfor %}
                                        </div>
                                </div>
                            {% endfor %}
                        {% else %}
                            <div class="demo-container">
                                    <div class="demo-label">{{ sub_concept.demo.name }}</div>
                                    <div class="flex-container wrap-nowrap">
                                    {% for example in sub_concept.demo.examples %}
                                        <div class="flex-item">{{ example }}</div>
                                    {% endfor %}
                                    </div>
                            </div>
                        {% endif %}