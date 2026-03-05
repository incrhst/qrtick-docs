import re

with open('packages.html', 'r') as f:
    content = f.read()

# Replace the top navigation & header block
top_block = """    <!-- SITE HEADER -->
    <header class="header">
        <a href="https://qrtick.com" class="logo-link" target="_blank" rel="noopener noreferrer">
            <img src="./qrtick-logo-alt.svg" alt="Qrtick Logo" class="logo">
        </a>
        <a href="https://qrtick.com" class="home-link" target="_blank" rel="noopener noreferrer">Visit Qrtick.com →</a>
    </header>

    <div class="nav-bar">
        <a href="index" class="back-link">← Back to Documentation</a>
    </div>

    <!-- PRICING HEADER -->
    <header class="pricing-header">
        <p class="eyebrow">QRTick Pricing</p>
        <h1>Choose Your QRTick Experience</h1>
    </header>"""

new_top_block = """    <!-- SITE HEADER -->
    <header class="header">
        <a href="https://qrtick.com" class="logo-link" target="_blank" rel="noopener noreferrer">
            <img src="./qrtick-logo-alt.svg" alt="Qrtick Logo" class="logo">
        </a>
        <a href="https://qrtick.com" class="home-link" target="_blank" rel="noopener noreferrer">Visit Qrtick.com →</a>
    </header>

    <main class="container">
        <a href="index" class="back-link" style="margin-bottom: 2rem;">← Back to Documentation</a>

        <!-- PRICING HEADER -->
        <header class="pricing-header">
            <p class="eyebrow">QRTick Pricing</p>
            <h1>Choose Your QRTick Experience</h1>
        </header>"""

content = content.replace(top_block, new_top_block)

# Replace the closing block
close_block = """    <!-- PAYMENT -->
    <div class="payment-section">
        <div class="payment-inner">
            <div>
                <p class="section-label">Payment Terms</p>
                <p class="section-title">Simple, Flexible Billing</p>
                <div class="payment-terms">
                    <div class="payment-term">
                        <h4>Standard Policy</h4>
                        <p>No upfront cost. We withhold the platform and service fees directly from your ticket sales.
                        </p>
                    </div>
                    <div class="payment-term">
                        <h4>Upfront Discount</h4>
                        <p>Save 5% on your total package and add-ons when you pay in full at the time of booking.</p>
                    </div>
                </div>
            </div>
            <div class="invoice-cta">
                <p>Want to see exactly what you'd pay? <strong>Give us details about your event</strong> and ask us for
                    a sample invoice — including your 5%
                    upfront discount applied across your full package.</p>
                <a href="https://tally.so/r/nW4Nak" class="cta-btn">Request a Sample Invoice</a>
            </div>
        </div>
    </div>

    <footer class="footer">"""

new_close_block = """    <!-- PAYMENT -->
    <div class="payment-section" style="border-radius: 12px; margin-top: 2rem;">
        <div class="payment-inner">
            <div>
                <p class="section-label">Payment Terms</p>
                <p class="section-title">Simple, Flexible Billing</p>
                <div class="payment-terms">
                    <div class="payment-term">
                        <h4>Standard Policy</h4>
                        <p>No upfront cost. We withhold the platform and service fees directly from your ticket sales.
                        </p>
                    </div>
                    <div class="payment-term">
                        <h4>Upfront Discount</h4>
                        <p>Save 5% on your total package and add-ons when you pay in full at the time of booking.</p>
                    </div>
                </div>
            </div>
            <div class="invoice-cta" style="border-radius: 8px;">
                <p>Want to see exactly what you'd pay? <strong>Give us details about your event</strong> and ask us for
                    a sample invoice — including your 5%
                    upfront discount applied across your full package.</p>
                <a href="https://tally.so/r/nW4Nak" class="cta-btn" style="border-radius: 4px;">Request a Sample Invoice</a>
            </div>
        </div>
    </div>

    </main>

    <footer class="footer">"""

content = content.replace(close_block, new_close_block)

# Remove the `.header`, `.logo`, `.home-link`, `body`, `.footer`, etc base styles since they will be imported from qrtick-docs.css
import_css = '<link rel="stylesheet" href="qrtick-docs.css">'
if import_css not in content:
    content = content.replace('<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">', 
                              '<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">\n    <link rel="stylesheet" href="qrtick-docs.css">')

# Modify the custom CSS to remove duplicated definitions that we want from qrtick-docs.css
# This needs to be carefully targeted
css_to_remove = [
r'''
        body {
            font-family: 'Montserrat', sans-serif;
            background: var(--white);
            color: var(--black);
            font-size: 15px;
            line-height: 1.6;
        }

        /* ─── HEADER ─── */
        .header {
            padding: 2rem;
            text-align: center;
            background-color: var(--black);
            box-shadow: 0 2px 4px rgba(61, 57, 57, 0.1);
        }

        .logo {
            max-width: 200px;
            height: auto;
        }

        .logo-link {
            display: inline-block;
            transition: opacity 0.2s;
        }

        .logo-link:hover {
            opacity: 0.8;
        }

        .home-link {
            display: block;
            margin-top: 1rem;
            color: var(--gold);
            text-decoration: none;
            font-weight: 500;
        }

        .home-link:hover {
            text-decoration: underline;
        }''',

r'''        /* ─── NAVIGATION ─── */
        .nav-bar {
            max-width: 1100px;
            margin: 2rem auto 0 auto;
            padding: 0 40px;
        }

        .back-link {
            display: inline-block;
            color: var(--gold);
            text-decoration: none;
            font-weight: 500;
            background-color: var(--black);
            padding: 0.5rem 1rem;
            border-radius: 4px;
            font-size: 0.9rem;
        }

        .back-link:hover {
            background-color: #555;
        }''',

r'''        .footer {
            padding: 2rem;
            background: var(--black);
            text-align: center;
            color: #EEEEEE;
        }

        .footer-link {
            color: var(--gold);
            text-decoration: none;
        }

        .footer-logo {
            max-width: 120px;
            margin-bottom: 0.5rem;
        }'''
]

for block in css_to_remove:
    content = content.replace(block, "")

# Ensure stacking of tiers works in the new 800px width container.
# Currently tiers are 1fr 1fr, let's just make them 1fr 1fr but since container is 800px, 
# 1fr 1fr means 320px per side. That might be a bit cramped for the 1fr 1fr layout.
# Let's stack them vertically everywhere!
content = content.replace(r'''        .tier {
            padding: 48px 36px;
            border: 1px solid rgba(61, 57, 57, 0.15);
            display: grid;
            grid-template-columns: 1fr 1fr;
            grid-template-areas:
                "info features"
                "cta cta";
            gap: 40px;
            align-items: start;
            background: var(--white);
        }''', r'''        .tier {
            padding: 48px 36px;
            border: 1px solid rgba(61, 57, 57, 0.15);
            display: grid;
            grid-template-columns: 1fr;
            grid-template-areas:
                "info"
                "features"
                "cta";
            gap: 24px;
            align-items: start;
            background: var(--white);
            border-radius: 12px;
        }''')

with open('packages.html', 'w') as f:
    f.write(content)

