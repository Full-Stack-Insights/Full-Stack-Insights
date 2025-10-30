
// Flex Direction
function setDirection(direction, event) {

    // Change the value of the code example(css_concept_code_block.html.jinja2):
    //  flex-direction: value
    const flexDirectionCodeValue = document.getElementById('flexDirectionValue');
    flexDirectionCodeValue.textContent = direction;

    // Update the demo container class(css_demo_controls.html.jinja2)
    const demo = document.getElementById('directionDemo');
    demo.className = `flex-container direction-${direction}`;
    updateActiveButton(event.target, 'direction');
}

// Justify Content
// function setJustify(direction, event) {

//      // Change the value of the code example(css_concept_code_block.html.jinja2):
//     //  flex-direction: value
//     const flexDirectionCodeValue = document.getElementById('justifyFlexDirectionValue');
//     flexDirectionCodeValue.textContent = direction;

//     // Update the demo container class(css_demo_controls.html.jinja2)
//     const demo = document.getElementById('justifyDemo');
//     demo.className = `flex-container direction-${direction}`;
//     updateActiveButton(event.target, 'direction');


// }






function setJustify(justify, event) {

    // Change the value of the code example: justify-content: value
    const justifyContentCodeValue = document.getElementById('justifyContentValue');
    justifyContentCodeValue.textContent = justify;

    // Update the demo container class
    const demo = document.getElementById('justifyDemo');
    demo.className = `flex-container justify-${justify.replace('flex-', '')}`;
    updateActiveButton(event.target, 'justify');
}

function setAlign(align, event) {
    const demo = document.getElementById('alignDemo');
    demo.className = `flex-container align-${align.replace('flex-', '')}`;
    updateActiveButton(event.target, 'align');
}

function setWrap(wrap, event) {
    const demo = document.getElementById('wrapDemo');
    demo.className = `flex-container wrap-${wrap}`;
    updateActiveButton(event.target, 'wrap');
}

function updateActiveButton(activeBtn, group) {
    // Remove active class from siblings
    const siblings = activeBtn.parentNode.querySelectorAll('.control-btn');
    siblings.forEach(btn => btn.classList.remove('active'));

    // Add active class to clicked button
    activeBtn.classList.add('active');
}