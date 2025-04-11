# QRTick: Event Management Guide

## How We Set Up Your Event

At QRTick, we handle the technical setup for you:

1. **Initial Setup**: Our team creates your event in our system based on your requirements
2. **Customization**: We configure your event details, ticket types, and pricing structure
3. **Payment Configuration**: We set up your payment provider integration and ensure funds route correctly
4. **Preflight Testing**: We conduct thorough payment tests to verify the entire purchase flow works properly
5. **Final Review**: We ensure everything is working properly before going live

## Managing Your Event

Once your event is set up in our system:

1. **Event Details**:
   - Your event includes name, description, date, location, and an optional banner image
   - Events are marked as "Published" to make them visible to customers
   - Custom branding options available for Premium tier customers

2. **Ticket Configuration**:
   - Each event can have multiple ticket types (e.g., Regular, VIP, Early Bird) depending on your tier
   - Lite tier allows only one ticket type per event, while Standard and Premium tiers support multiple ticket types
   - Each ticket type has a defined capacity (total available tickets)
   - Tickets are marked as "Active" when they're available for purchase
   - Visual distinction between ticket types using pastel color coding
   - Support for digital and printable ticket formats

3. **QRTick Thing**:
   - Mobile-friendly web application - no app installation needed
   - Works with any modern mobile phone through your web browser
   - Separate dedicated platform for real-time ticket management and sales tracking
   - Access granted by associating your email address with Thing
   - Simple login process using your registered email
   - View sales data and scan tickets after logging in
   - Live ticket scanning and validation
   - Up-to-the-minute sales statistics
   - Attendee check-in tracking
   - Multiple device support for simultaneous scanning
   - Works offline with automatic sync when connection is restored

## How Sales Work

1. **Event Listing**: Your published events with available tickets appear on your event page
   - Events with zero remaining tickets show as "SOLD OUT"
   - Each listing displays the remaining ticket count
   - Real-time inventory updates to prevent overselling

2. **Customer Purchase Flow**:
   - Customer selects your event
   - Chooses ticket type and quantity
   - Enters their email address
   - Completes payment through our secure payment processor
   - Receives confirmation email with QR-coded tickets
   - Each ticket has a unique color for easy identification

3. **Ticket Tracking**:
   - Each ticket has a unique QR code for entry validation
   - Order IDs track purchases (e.g., "7630001ab" indicates order timestamp and quantity)
   - Multiple tickets can be purchased in a single transaction
   - Color-coded system for easy ticket management

## Ticket Sharing Features

1. **Digital Sharing Options**:
   - Direct WhatsApp sharing with pre-populated message
   - General sharing via Web Share API on mobile devices
   - Clipboard copying fallback for desktop users
   - Each shared ticket maintains its unique color coding

2. **Security Features**:
   - Secure ticket links with validation
   - Warning messages about sharing responsibility
   - Tracked sharing for security purposes
   - Check-in status visibility on shared tickets

## Checking-In Attendees

1. **QR Code Scanning with Thing**:
   - Use QRTick Thing app for professional scanning
   - Scan QR codes on printed tickets or phone displays
   - Instant validation and check-in marking
   - Prevention of duplicate check-ins
   - Real-time sync across multiple scanning devices
   - Works offline with automatic sync when connection is restored

2. **Manual Check-in via Thing**:
   - Backup manual entry system in Thing
   - Search by ticket number or attendee name
   - Support for offline check-in with sync on reconnection
   - Quick access to attendee details and ticket history

3. **Thing Dashboard Features**:
   - Real-time check-in statistics
   - Multiple device management
   - Staff access control
   - Live attendance tracking
   - Instant alerts for duplicate or invalid tickets
   - Export check-in data for analysis

## Reviewing Sales and Attendance

1. **Sales Dashboard in Thing**:
   - View real-time ticket sales information
   - Track revenue and remaining ticket inventory
   - Get insights on purchase patterns
   - Monitor sharing statistics and patterns

2. **Attendance Tracking**:
   - Monitor check-in rates during your event
   - View attendee information for follow-up
   - Track sharing patterns and group attendance
   - Export detailed reports for analysis

## Communication Features

1. **Automated Emails**:
   - Purchase confirmations with colored tickets
   - Event reminders with check-in instructions
   - Updates and changes to event details
   - Custom branding for Premium tier customers

2. **Sharing Features**:
   - WhatsApp integration for easy ticket sharing
   - Social media sharing capabilities
   - Group ticket distribution
   - Bulk ticket sending for organizers

## Important Notes

- All payments are processed securely through our payment partner
- Payment processing requires initial configuration and testing for each event
- Each transaction is verified and logged for security purposes
- You'll receive confirmation of each successful sale
- Tickets automatically update to show "SOLD OUT" when capacity is reached
- Our system handles email delivery of tickets to your customers
- Color coding helps distinguish between multiple tickets
- WhatsApp sharing is optimized for markets where it's the preferred platform

## Platform Security

1. **Ticket Security**:
   - Unique QR codes for each ticket
   - Color coding for visual verification
   - Check-in status tracking
   - Sharing audit trail

2. **System Security**:
   - Encrypted data transmission
   - Secure payment processing
   - Protected customer information
   - Regular security audits

## Need Help?

Contact our support team at support@qrtick.com for assistance with:
- Setting up new events
- Modifying existing events
- Technical support during your event
- Custom requirements
- WhatsApp sharing setup
- Color coding customization
- Integration questions

## Launch Checklist

Before launching your event for ticket sales, follow this comprehensive checklist:

1. **Payment System Setup**:
   - [ ] Switch payment environment from sandbox to production
   - [ ] Verify bank account details are correct
   - [ ] Confirm payment routing is properly configured
   - [ ] Test a real payment with minimal amount (e.g., $1)
   - [ ] Verify the test payment appears in your bank account
   - [ ] Check refund functionality is working

2. **Event Configuration**:
   - [ ] Verify event name and description are correct
   - [ ] Confirm event date and time are accurate
   - [ ] Check location details are complete
   - [ ] Validate ticket types and pricing
   - [ ] Verify ticket quantities and limits
   - [ ] Test promo codes if being used
   - [ ] Review custom branding elements

3. **Ticket Dashboard App (Thing)**:
   - [ ] Ensure all staff emails are associated with Thing
   - [ ] Verify Thing works in staff members' mobile browsers
   - [ ] Test login credentials for all staff members
   - [ ] Verify offline mode functionality
   - [ ] Test QR code scanning on various devices
   - [ ] Practice manual check-in process
   - [ ] Confirm multi-device synchronization
   - [ ] Test exporting attendance reports

4. **Communication Setup**:
   - [ ] Verify email templates are correct
   - [ ] Test purchase confirmation emails
   - [ ] Check ticket attachment formatting
   - [ ] Validate WhatsApp sharing functionality
   - [ ] Confirm all links in emails work
   - [ ] Test email delivery to various providers

5. **Purchase Flow Testing**:
   - [ ] Complete end-to-end purchase test
   - [ ] Verify ticket delivery
   - [ ] Test ticket sharing functionality
   - [ ] Check mobile responsiveness
   - [ ] Validate form error messages
   - [ ] Test maximum ticket purchase limits
   - [ ] Verify sold-out behavior

6. **Security Checks**:
   - [ ] Test duplicate ticket prevention
   - [ ] Verify ticket validation process
   - [ ] Check sharing security features
   - [ ] Validate staff access controls
   - [ ] Test invalid ticket handling

7. **Staff Preparation**:
   - [ ] Train staff on dashboard app usage
   - [ ] Review manual check-in procedures
   - [ ] Practice handling common issues
   - [ ] Distribute emergency contact information
   - [ ] Share offline procedures documentation

8. **Final Verification**:
   - [ ] Verify analytics tracking is active
   - [ ] Test real-time sales monitoring
   - [ ] Confirm automatic inventory updates
   - [ ] Check all automated notifications
   - [ ] Verify customer support contact info
   - [ ] Test emergency stop-sale procedure

9. **Backup Plans**:
   - [ ] Document offline check-in process
   - [ ] Prepare backup scanning devices
   - [ ] Save offline copies of attendee lists
   - [ ] Note emergency support contacts
   - [ ] Review refund/cancellation procedures

10. **Post-Launch Monitoring**:
    - [ ] Monitor initial ticket sales
    - [ ] Check payment processing
    - [ ] Verify email deliveries
    - [ ] Watch real-time analytics
    - [ ] Monitor system performance

**Important Notes**:
- Complete this checklist at least 48 hours before launching ticket sales
- Document any issues encountered during testing
- Keep emergency contact information readily available
- Save a copy of the final configuration for reference
- Monitor system closely during the first hour of sales

Contact support@qrtick.com if you need assistance with any of these steps or encounter issues during the launch process.

## Getting Started with Thing

1. **Initial Setup**:
   - Choose which email address you want associated with Thing
   - We'll set up your access using this email
   - Access Thing through your mobile phone's web browser
   - Log in using your registered email
   - Immediately access your sales data and ticket scanning features

2. **Device Requirements**:
   - Works with any modern smartphone
   - Access through your regular web browser
   - No app installation required
   - Camera access needed for ticket scanning
   - Internet connection for real-time updates (offline mode available)

3. **Staff Access**:
   - Additional staff members can be given access to Thing
   - Each staff member needs their own email association
   - Staff can be granted specific permissions for scanning and/or viewing sales data
   - Multiple staff members can scan tickets simultaneously 