# QRTick 2026 Pricing & Packages (For AI)

**Canonical Document for Invoice Generation & Customer Support**

*Note: The ballpark packages and quote builder calculator rates specified in this document apply exclusively to events with **300 or less patrons**. Events exceeding 300 patrons require manual assessment and custom quoting.*

**Web page flow (`packages.html`):** Ballpark packages → custom quote CTA → **interactive quote builder** (`#calculator`, primary spine) → collapsed **rate table** (`#price-breakdown`, single comparison table) → typical scenarios → invoice CTA. **Upfront total** in the builder includes platform, Admission & Scanning Support (Volunteer Coordination / Scanning Crew), physical tickets, and setup fees. **Gate Card Sales (Card Reader & POS)** is never added to that dollar total; when checked it appears as “Quoted separately” with 10% card fee noted.

---

## 1. Primary Ballpark Packages
*   **The Essentials ($10,000)**: Core ticketing with discounts and complimentary tickets. Default tier for new organizations. Uses default platform fee schedule with no additional tier withholding. Includes no admission support of any kind. All gate services are paid add-ons.
*   **The Professional ($40,000)**: Engagement tools, prompt assistant, add-ons, and ticket office (POS) sales. Additional platform fee will be withheld from ticket revenue. All gate services are paid add-ons.
*   **The Managed Weekend ($60,000)**: Full platform capabilities including merchandise, patron engagement hub, and physical ticket registration. Additional platform fee will be withheld from ticket revenue. All gate services are paid add-ons.

## 2. Component Breakdown (For Custom Scenarios)
### Platform Choice
*   **Essentials Platform ($10,000)**: Core ticketing, discounts, complimentary tickets. Organizer handles the door themselves; zero included admission support.
*   **Professional Platform ($40,000)**: Includes everything in Essentials plus Engagement tools, prompt assistant, add-ons, and ticket office (POS) sales.
*   **Managed Weekend Platform ($60,000)**: Full platform capabilities including merchandise, patron engagement hub, and physical ticket registration.
*   **Already Subscribed ($0)**: For organizers who already have an active subscription or season agreement with QRTick and only need a quote for gate add-ons (staffing, physical tickets, etc.).

### On-Site Admission & Scanning Support (Add-ons)
Not included on **Essentials**. Separate from **Gate Card Sales** (selling tickets at the gate).

**How to choose (explain this clearly to customers):**
*   **Their own team → Volunteer Coordination:** The event already has volunteers or staff at the gate. They only need one QRTick person for ~3 hours to coordinate volunteers and provide on-site guidance. The organizer's team handles scanning; QRTick does not send a full crew.
*   **Hands-off → Scanning Crew:** The organizer does not want to manage entry. QRTick provides full manned scanning crews so they "don't have to think about" the gate.

#### Volunteer Coordination (minimal — for events with their own team)
The lightest on-site option. **Not full scanning**—coordination and guidance for the organizer's volunteers.
*   **$8,000 per event** for **3 hours** on site.
*   **One QRTick team member** per event to coordinate volunteers and provide on-site guidance at the gate.

#### Scanning Crew — ticket scanning (full crew — hands-off)
**QRTick owns scanning and validating tickets at the gate.** For customers who want full-service entry, not volunteer coordination. Not selling tickets.

Priced by **support blocks** (scheduled on-site scanning coverage), not calendar nights. Each block is priced by hour/crew tier and represents a single, continuous shift on site (no split shifts/breaks). Multiple performances on the same day require separate blocks unless they can be covered in one continuous block.
*   **Up to 3 hours, Team of 2**: $15,000 per block.
*   **Up to 3 hours, Team of 3**: $21,000 per block.
*   **Up to 6 hours, Team of 3**: $35,000 per block.
*   **3-block bundle (3h, Team of 2)**: $40,000 (Saves $5,000 vs. three separate blocks).
*   **3-block bundle (3h, Team of 3)**: $56,000 (Saves $7,000 vs. three separate blocks).
*   **3-block bundle (6h, Team of 3)**: $80,000 (Saves $25,000 vs. three separate blocks).
*   **Volume Discount**: 5% off scanning total when booking 4+ blocks in a season.

### Queue Busting & Rapid Check-in (Bluetooth Scanners Add-on)
High-speed Bluetooth scanners to speed up check-in queues at the gate. Can be paired with Volunteer Coordination or Scanning Crew. Added to upfront total.
*   **Bluetooth Check-in Scanners**: **$2,500 per scanner per day** (up to 2 scanners)

### Gate Card Sales (Card Reader & POS) — selling tickets at the gate (Add-on)
**Separate from Scanning Crew blocks.** For organizers who sell tickets on site, not only scan them.

Hardware rental fees (added to upfront total):
*   **Gate Card Reader**: **$10,000 per day** (physical tap/swipe/chip hardware + POS app, required for selling tickets directly to debit and credit card holders at the gate)

**Card processing at the gate:** **10% processing fee** on the transaction amount when patrons pay by card using QRTick's provided card reader. Quoted separately; calculated on post-event door card sales volume.

Scanning Crew blocks, Bluetooth Scanners, and Gate Card Sales are priced **independently**—customers may need scanning only, sales only, or both/all.

**Quote builder URL parameters:** `p` (e|p|n platform where n = already subscribed / $0), `bg` (Volunteer Coordination event count × $8,000), `n` (scanning block count), `gt` (3|6 hour tier), `gs` (1 = Gate Card Sales requested), `cr` (1 = Card Reader requested), `crd` (Card Reader days count), `bt` (Bluetooth scanner count, 1 or 2), `btd` (Bluetooth scanner days count), `qr`, `rf`, `name`, `org`.

**Scenario presets (`?scenario=`):** `volunteer-led`, `hands-off-single`, `theatre-run`, `full-production`, `community-season`, `grand-season`. Loads the matching configuration into the quote builder (same math as the scenario list upfront totals). Manual slider changes clear `scenario` from the URL.

## 3. Physical Entry Options
*   **QR Code Ticket**: $55 per ticket (Minimum 100). Black & White paper tickets with secure QR codes.
*   **RFID Tap Ticket**: $140 per ticket (Minimum 100). Black & White paper tickets with secure RFID labels for faster entry.
*   **Ticket Setup Fee**: $10,000 (Waived for Professional + any 3-block scanning bundle).

## 4. Finance & Payouts
*   **Standard Payout**: 5-7 Days Post-Event (Free).
*   **Early Payout**: 2.5% Service Fee.
*   **Express Payout**: 3.5% Service Fee (Subject to clearance).
*   **Payment Policy**: Fees deducted from sales. 5% discount for full upfront payment.

---

## 5. Premium Feature Explanations

### Event Add-ons Management
This feature allows event organizers to configure and sell auxiliary products or services alongside standard tickets during the checkout process.

*   **What it does:** Organizers can offer optional or mandatory items (like parking passes, VIP upgrades, merchandise, or meal vouchers) that attendees can add to their order before completing their purchase.
*   **How it works:** It's managed via the `addons_enabled` capability flag. When enabled, organizers get access to an "Add-ons" configuration tab for their event series, and the add-ons become visible to buyers during checkout.
*   **Examples:**
    *   *Meet & Greet:* Book 15 minutes of exclusive 1-on-1 time with a keynote presenter or artist backstage.
    *   *Exclusive Merchandise:* Pre-order limited edition event t-shirts, signed posters, or branded tote bags for priority pickup at the gate.
    *   *Curated Experiences:* Offer a post-event networking dinner, early venue access, or a signed copy of the presenter's new book.
    *   *VIP Perks:* Add a premium open-bar wristband, reserved front-row seating, or a VIP parking pass.

### Physical Ticket Registration
This feature bridges the gap between digital ticketing and traditional pre-printed physical tickets.

*   **What it does:** It allows event organizers to register and track pre-printed physical tickets (which have QR codes on them) by bulk-attributing them to specific events.
*   **Why it's useful:** Instead of just generating digital tickets via email, this system ensures that pre-printed physical tickets are properly counted against the event's total inventory and can be successfully validated by scanners at the door during check-in.
*   **How it works:** Governed by the `physical_tickets_enabled` capability flag, it adds a dedicated "Physical Ticket Registration" tab to the existing sales interface, complete with its own strict admin permission model and comprehensive audit logging to track exactly who registered which physical tickets.
*   **Examples:**
    *   *Promoter Distribution:* Handing out physical tickets to local street team promoters to sell for cash, while still ensuring scanners validate them.
    *   *VIP Mailers:* Mailing high-quality, physical collector's edition tickets to VIPs ahead of the event that can be successfully scanned at the door.
    *   *Retail Outlets:* Selling physical QR tickets at local retail shops (like a record store) while keeping inventory perfectly synced with online sales.

---
**CTA**: Direct users to [Request Sample Invoice](https://tally.so/r/nW4Nak)
