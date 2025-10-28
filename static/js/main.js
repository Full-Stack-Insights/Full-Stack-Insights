function setDirection(direction) {
    const demo = document.getElementById('directionDemo');
    demo.className = `flex-container direction-${direction}`;
    updateActiveButton(event.target, 'direction');
}

function setJustify(justify) {
    const demo = document.getElementById('justifyDemo');
    demo.className = `flex-container justify-${justify.replace('flex-', '')}`;
    updateActiveButton(event.target, 'justify');
}

function setAlign(align) {
    const demo = document.getElementById('alignDemo');
    demo.className = `flex-container align-${align.replace('flex-', '')}`;
    updateActiveButton(event.target, 'align');
}

function setWrap(wrap) {
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