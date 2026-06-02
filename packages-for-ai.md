# QRTick 2026 Pricing & Packages (For AI)

**Canonical Document for Invoice Generation & Customer Support**

**Web page flow (`packages.html`):** Ballpark packages → custom quote CTA → **interactive quote builder** (`#calculator`, primary spine) → collapsed **rate table** (`#price-breakdown`, single comparison table) → typical scenarios → invoice CTA. **Upfront total** in the builder includes platform, Basic/scanning gate support, physical tickets, and setup fees. **Gate Sales** is never added to that dollar total; when checked it appears as “Quoted separately” with 10% card fee noted.

---

## 1. Primary Ballpark Packages
*   **The Essentials ($10,000)**: Entry tier. Essentials Platform + self-managed entry only. **Includes no gate support of any kind** — no Basic Gate Support, no Gate Experience (scanning), no Gate Sales (door POS/card machine). No discount tools. All gate services are paid add-ons if required.
*   **The Professional ($40,000)**: Managed tier. Professional Platform + discount management (online) + white-glove setup + digital programs. Gate Sales at the door is a separate add-on.
*   **The Managed Weekend ($88,000)**: Series tier. Professional Platform + 3 × 3-hour **Gate Experience** scanning blocks. Gate Sales not included.

## 2. Component Breakdown (For Custom Scenarios)
### Platform Choice
*   **Essentials Platform ($10,000)**: Single event access, self-service tools, digital QR tickets. Organizer handles the door themselves; **zero included gate support** (Basic coordination, full scanning, and Gate Sales are separate add-ons).
*   **Professional Platform ($40,000)**: Managed partnership, unlimited seasonal events, white-glove setup, digital programs, early payout access, discount management for **online** sales (not Gate Sales).

### On-Site Gate Support (Add-ons)
Not included on **Essentials**. Separate from **Gate Sales** (selling at the door).

**How to choose (explain this clearly to customers):**
*   **Their own team → Basic Gate Support:** The event already has volunteers or staff at the gate. They only need one QRTick person for ~3 hours to coordinate volunteers and provide on-site guidance. The organizer's team handles scanning; QRTick does not send a full crew.
*   **Hands-off → Gate Experience:** The organizer does not want to manage entry. QRTick provides full manned scanning crews so they "don't have to think about" the gate.

#### Basic Gate Support (minimal — for events with their own team)
The lightest on-site option. **Not full scanning**—coordination and guidance for the organizer's volunteers.
*   **$10,000 per event** for **3 hours** on site.
*   **One QRTick team member** per event to coordinate volunteers and provide on-site guidance at the gate.

#### Gate Experience — ticket scanning (full crew — hands-off)
**QRTick owns scanning and validating tickets at the gate.** For customers who want full-service entry, not volunteer coordination. Not selling tickets.

Priced by **support blocks** (scheduled on-site scanning coverage), not calendar nights. Each block is priced by hour tier (up to 3 or up to 6 hours). Multiple performances on the same day need separate blocks when each requires its own full coverage window.
*   **Up to 3 hours per scanning block**: $18,000 per block.
*   **Up to 6 hours per scanning block**: $35,000 per block.
*   **3-block bundle (3h tier)**: $48,000 (Saves $6,000 vs. three separate blocks).
*   **3-block bundle (6h tier)**: $80,000 (Saves $25,000 vs. three separate blocks).
*   **Volume Discount**: 5% off scanning total when booking 4+ blocks in a season.

### Gate Sales — selling at the door (Add-on)
**Separate from Gate Experience.** For organizers who sell tickets on site, not only scan them.

Includes:
*   Full tracking of all gate sales
*   On-site point-of-sale (POS) for door purchases
*   Card machine for credit/debit payments at the gate
*   Can be operated by the organizer's team or QRTick staff

**Card processing at the gate:** **10% processing fee** on the transaction amount when patrons pay by card using QRTick's card machine. Quoted separately from scanning block fees; not included in the upfront scanning estimate.

Gate Experience blocks and Gate Sales are priced **independently**—customers may need scanning only, sales only, or both.

**Quote builder URL parameters:** `p` (e|p platform), `bg` (Basic Gate event count × $10,000), `n` (scanning block count), `gt` (3|6 hour tier), `gs` (1 = Gate Sales requested), `qr`, `rf`, `name`, `org`.

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
**CTA**: Direct users to [Request Sample Invoice](https://tally.so/r/nW4Nak)
