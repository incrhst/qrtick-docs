document.addEventListener("DOMContentLoaded", () => {
    // Inject menu HTML into body
    const menuHTML = `
        <div id="menu-overlay" class="menu-overlay"></div>
        <nav id="side-menu" class="side-menu">
            <div class="side-menu-header">
                <button id="close-menu-btn" class="close-btn" aria-label="Close menu">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                </button>
            </div>
            <div class="side-menu-links" style="flex-grow: 1;">
                <a href="/" class="side-menu-link">Home / Docs</a>
                <a href="what-to-expect" class="side-menu-link">What to Expect</a>
                <a href="packages" class="side-menu-link">Packages & Pricing</a>
                <a href="guide" class="side-menu-link">Fundraiser Guide</a>
                <a href="manager-guide" class="side-menu-link">Manager Guide</a>
                <a href="event-setup-guide" class="side-menu-link">Event Setup Guide</a>
                <a href="checklist" class="side-menu-link">Launch Checklist</a>
                <a href="fee-calculator" class="side-menu-link">Fee Calculator</a>
                <a href="https://qrtick.com" class="side-menu-link" style="color:#FDC230; font-weight:700; margin-top: auto; border-top: 1px solid #f0f0f0;">&larr; Return to Main Site</a>
            </div>
        </nav>
    `;

    document.body.insertAdjacentHTML('beforeend', menuHTML);

    const menuBtn = document.getElementById("menu-btn");
    const closeBtn = document.getElementById("close-menu-btn");
    const sideMenu = document.getElementById("side-menu");
    const overlay = document.getElementById("menu-overlay");

    function openMenu() {
        if (sideMenu) sideMenu.classList.add("open");
        if (overlay) overlay.classList.add("open");
        document.body.style.overflow = 'hidden'; // Prevent scrolling
    }

    function closeMenu() {
        if (sideMenu) sideMenu.classList.remove("open");
        if (overlay) overlay.classList.remove("open");
        document.body.style.overflow = '';
    }

    if (menuBtn) {
        menuBtn.addEventListener("click", openMenu);
    }

    if (closeBtn) {
        closeBtn.addEventListener("click", closeMenu);
    }

    if (overlay) {
        overlay.addEventListener("click", closeMenu);
    }
});
