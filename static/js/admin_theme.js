// SMS Admin Theme — Dynamic Styles (Light Portal Theme)
// Applies clean, light styling to match the Admin Portal
document.addEventListener('DOMContentLoaded', function () {

    // ── Card Headers: white background with dark text (matching portal) ──
    var cardHeaders = document.querySelectorAll('.card-header');
    cardHeaders.forEach(function (header) {
        header.style.setProperty('background-image', 'none', 'important');
        header.style.setProperty('background-color', '#ffffff', 'important');
        header.style.setProperty('background', '#ffffff', 'important');
        header.style.setProperty('color', '#1E1E2D', 'important');
        header.style.setProperty('padding', '18px 22px', 'important');
        header.style.setProperty('border-bottom', '1px solid #E5E7EB', 'important');
        header.style.setProperty('font-weight', '600', 'important');
        header.style.setProperty('font-size', '16px', 'important');
        header.style.setProperty('border-radius', '16px 16px 0 0', 'important');

        // Style children text
        var children = header.querySelectorAll('h5, h3, .card-title, span');
        children.forEach(function (el) {
            el.style.setProperty('color', '#1E1E2D', 'important');
            el.style.setProperty('font-weight', '600', 'important');
            el.style.setProperty('font-family', "'Outfit', sans-serif", 'important');
            el.style.setProperty('font-size', '16px', 'important');
        });
    });

    // ── Sidebar: Light background ──
    var sidebar = document.querySelector('.main-sidebar');
    if (sidebar) {
        sidebar.style.setProperty('background', '#FAFAFA', 'important');
        sidebar.style.setProperty('border-right', '1px solid #E5E7EB', 'important');
        sidebar.style.setProperty('box-shadow', 'none', 'important');
    }

    // ── Brand link ──
    var brand = document.querySelector('.brand-link');
    if (brand) {
        brand.style.setProperty('background', '#FAFAFA', 'important');
        brand.style.setProperty('border-bottom', '1px solid #E5E7EB', 'important');
    }

    var brandText = document.querySelector('.brand-text');
    if (brandText) {
        brandText.style.setProperty('color', '#1E1E2D', 'important');
        brandText.style.setProperty('font-weight', '700', 'important');
    }

    // ── Inject a high-priority style tag to override AdminLTE active states ──
    var overrideStyle = document.createElement('style');
    overrideStyle.textContent = [
        '.sidebar-light-primary .nav-sidebar > .nav-item > .nav-link.active,',
        '.sidebar-light-primary .nav-sidebar > .nav-item > .nav-link.active:hover,',
        '.sidebar-light-primary .nav-sidebar > .nav-item > .nav-link.active:focus,',
        '[class*="sidebar-light"] .nav-sidebar > .nav-item > .nav-link.active,',
        'body .main-sidebar .nav-sidebar > .nav-item > .nav-link.active {',
        '  background-color: #E8E6FF !important;',
        '  background-image: none !important;',
        '  background: #E8E6FF !important;',
        '  color: #6C63FF !important;',
        '  font-weight: 600 !important;',
        '}',
        '.sidebar-light-primary .nav-sidebar > .nav-item > .nav-link.active p,',
        'body .main-sidebar .nav-sidebar > .nav-item > .nav-link.active p {',
        '  color: #6C63FF !important;',
        '}',
        '.sidebar-light-primary .nav-sidebar > .nav-item > .nav-link.active i,',
        '.sidebar-light-primary .nav-sidebar > .nav-item > .nav-link.active .nav-icon,',
        'body .main-sidebar .nav-sidebar > .nav-item > .nav-link.active i,',
        'body .main-sidebar .nav-sidebar > .nav-item > .nav-link.active .nav-icon {',
        '  color: #6C63FF !important;',
        '}',
        '.nav-sidebar > .nav-item > .nav-link {',
        '  background-color: transparent !important;',
        '  background-image: none !important;',
        '}',
    ].join('\n');
    document.head.appendChild(overrideStyle);

    // ── Sidebar nav items: light theme styles ──
    var navLinks = document.querySelectorAll('.nav-sidebar .nav-link');
    navLinks.forEach(function (link) {
        // Reset all nav links first
        link.style.setProperty('background-color', 'transparent', 'important');
        link.style.setProperty('background-image', 'none', 'important');
        link.style.setProperty('background', 'transparent', 'important');
        link.style.setProperty('color', '#6B7280', 'important');
        link.style.setProperty('border-radius', '10px', 'important');

        // Icons
        var icon = link.querySelector('i, .nav-icon');
        if (icon) {
            icon.style.setProperty('color', '#6B7280', 'important');
        }

        // Text
        var text = link.querySelector('p');
        if (text) {
            text.style.setProperty('color', '#6B7280', 'important');
        }

        // Active state – subtle light purple
        if (link.classList.contains('active')) {
            link.style.setProperty('background-color', '#E8E6FF', 'important');
            link.style.setProperty('background-image', 'none', 'important');
            link.style.setProperty('background', '#E8E6FF', 'important');
            link.style.setProperty('color', '#6C63FF', 'important');
            link.style.setProperty('font-weight', '600', 'important');
            if (icon) icon.style.setProperty('color', '#6C63FF', 'important');
            if (text) text.style.setProperty('color', '#6C63FF', 'important');
        }
    });

    // ── Sidebar headers ──
    var navHeaders = document.querySelectorAll('.nav-header');
    navHeaders.forEach(function (h) {
        h.style.setProperty('color', '#6B7280', 'important');
        h.style.setProperty('font-size', '11px', 'important');
        h.style.setProperty('font-weight', '600', 'important');
        h.style.setProperty('letter-spacing', '1.2px', 'important');
        h.style.setProperty('text-transform', 'uppercase', 'important');
    });

    // ── User panel in sidebar ──
    var userPanel = document.querySelector('.user-panel');
    if (userPanel) {
        userPanel.style.setProperty('border-bottom', '1px solid #E5E7EB', 'important');
        var userInfo = userPanel.querySelector('.info a');
        if (userInfo) {
            userInfo.style.setProperty('color', '#1E1E2D', 'important');
        }
    }

    // ── Cards: white, rounded, subtle border ──
    var cards = document.querySelectorAll('.card');
    cards.forEach(function (card) {
        card.style.setProperty('border-radius', '16px', 'important');
        card.style.setProperty('border', '1px solid #E5E7EB', 'important');
        card.style.setProperty('box-shadow', 'none', 'important');
        card.style.setProperty('background', '#ffffff', 'important');
        card.style.setProperty('overflow', 'hidden', 'important');
    });

    // ── Content wrapper background ──
    var contentWrapper = document.querySelector('.content-wrapper');
    if (contentWrapper) {
        contentWrapper.style.setProperty('background', '#F4F3FF', 'important');
    }

    // ── Add/Change buttons polish ──
    var addLinks = document.querySelectorAll('a.addlink');
    addLinks.forEach(function (link) {
        link.style.setProperty('background', '#34D399', 'important');
        link.style.setProperty('color', '#ffffff', 'important');
        link.style.setProperty('border-radius', '20px', 'important');
        link.style.setProperty('padding', '6px 16px', 'important');
        link.style.setProperty('font-size', '12px', 'important');
        link.style.setProperty('font-weight', '600', 'important');
        link.style.setProperty('text-decoration', 'none', 'important');
        link.style.setProperty('display', 'inline-flex', 'important');
        link.style.setProperty('align-items', 'center', 'important');
    });

    var changeLinks = document.querySelectorAll('a.changelink');
    changeLinks.forEach(function (link) {
        link.style.setProperty('background', '#6C63FF', 'important');
        link.style.setProperty('color', '#ffffff', 'important');
        link.style.setProperty('border-radius', '20px', 'important');
        link.style.setProperty('padding', '6px 16px', 'important');
        link.style.setProperty('font-size', '12px', 'important');
        link.style.setProperty('font-weight', '600', 'important');
        link.style.setProperty('text-decoration', 'none', 'important');
        link.style.setProperty('display', 'inline-flex', 'important');
        link.style.setProperty('align-items', 'center', 'important');
    });

    // ── Action Bar: fix alignment (label wraps select causing stacking) ──
    var actionsBar = document.querySelector('.actions');
    if (actionsBar) {
        actionsBar.style.setProperty('display', 'flex', 'important');
        actionsBar.style.setProperty('flex-direction', 'row', 'important');
        actionsBar.style.setProperty('align-items', 'center', 'important');
        actionsBar.style.setProperty('flex-wrap', 'nowrap', 'important');
        actionsBar.style.setProperty('gap', '12px', 'important');
        actionsBar.style.setProperty('padding', '12px 22px', 'important');
        actionsBar.style.setProperty('background', '#E8E6FF', 'important');
        actionsBar.style.setProperty('border-radius', '12px', 'important');
        actionsBar.style.setProperty('margin-bottom', '16px', 'important');

        // Fix label: use display contents so its children join the flex row
        var actionLabel = actionsBar.querySelector('label');
        if (actionLabel) {
            actionLabel.style.setProperty('display', 'contents', 'important');
            actionLabel.style.setProperty('font-size', '14px', 'important');
            actionLabel.style.setProperty('font-weight', '600', 'important');
            actionLabel.style.setProperty('color', '#1E1E2D', 'important');
        }

        // Fix select
        var actionSelect = actionsBar.querySelector('select');
        if (actionSelect) {
            actionSelect.style.setProperty('flex', '1', 'important');
            actionSelect.style.setProperty('height', '38px', 'important');
            actionSelect.style.setProperty('min-width', '0', 'important');
            actionSelect.style.setProperty('max-width', '300px', 'important');
            actionSelect.style.setProperty('border-radius', '10px', 'important');
            actionSelect.style.setProperty('border', '1px solid #E5E7EB', 'important');
            actionSelect.style.setProperty('padding', '6px 12px', 'important');
            actionSelect.style.setProperty('font-size', '14px', 'important');
            actionSelect.style.setProperty('font-family', "'Outfit', sans-serif", 'important');
            actionSelect.style.setProperty('background', '#ffffff', 'important');
        }

        // Fix button
        var actionButton = actionsBar.querySelector('button, .button');
        if (actionButton) {
            actionButton.style.setProperty('flex-shrink', '0', 'important');
            actionButton.style.setProperty('height', '38px', 'important');
            actionButton.style.setProperty('display', 'inline-flex', 'important');
            actionButton.style.setProperty('align-items', 'center', 'important');
        }

        // Fix counter
        var actionCounter = actionsBar.querySelector('.action-counter');
        if (actionCounter) {
            actionCounter.style.setProperty('flex-shrink', '0', 'important');
            actionCounter.style.setProperty('white-space', 'nowrap', 'important');
        }

        // Hide select-across hidden input
        var selectAcross = actionsBar.querySelector('.select-across');
        if (selectAcross) {
            selectAcross.style.setProperty('display', 'none', 'important');
        }
    }

    // ── Search Bar: fix horizontal alignment ──
    var searchForm = document.querySelector('#changelist-search');
    if (searchForm) {
        var searchDiv = searchForm.querySelector('div');
        if (searchDiv) {
            searchDiv.style.setProperty('display', 'flex', 'important');
            searchDiv.style.setProperty('flex-direction', 'row', 'important');
            searchDiv.style.setProperty('align-items', 'center', 'important');
            searchDiv.style.setProperty('gap', '10px', 'important');
            searchDiv.style.setProperty('width', '100%', 'important');
        }

        var searchLabel = searchForm.querySelector('label');
        if (searchLabel) {
            searchLabel.style.setProperty('display', 'inline-flex', 'important');
            searchLabel.style.setProperty('align-items', 'center', 'important');
            searchLabel.style.setProperty('margin', '0', 'important');
            searchLabel.style.setProperty('padding', '0', 'important');
            searchLabel.style.setProperty('height', '38px', 'important');
            searchLabel.style.setProperty('flex-shrink', '0', 'important');
        }

        var searchInput = searchForm.querySelector('input[type="text"]');
        if (searchInput) {
            searchInput.style.setProperty('flex', '1', 'important');
            searchInput.style.setProperty('min-width', '200px', 'important');
            searchInput.style.setProperty('max-width', '400px', 'important');
            searchInput.style.setProperty('height', '38px', 'important');
            searchInput.style.setProperty('border-radius', '10px', 'important');
            searchInput.style.setProperty('border', '1px solid #E5E7EB', 'important');
            searchInput.style.setProperty('padding', '6px 14px', 'important');
        }

        var searchSubmit = searchForm.querySelector('input[type="submit"]');
        if (searchSubmit) {
            searchSubmit.style.setProperty('flex-shrink', '0', 'important');
            searchSubmit.style.setProperty('height', '38px', 'important');
            searchSubmit.style.setProperty('padding', '0 18px', 'important');
            searchSubmit.style.setProperty('border-radius', '10px', 'important');
            searchSubmit.style.setProperty('background', '#6C63FF', 'important');
            searchSubmit.style.setProperty('color', '#fff', 'important');
            searchSubmit.style.setProperty('border', 'none', 'important');
            searchSubmit.style.setProperty('font-weight', '600', 'important');
            searchSubmit.style.setProperty('cursor', 'pointer', 'important');
        }
    }
});
