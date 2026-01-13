# Alumni & Student Matching Platform

---

## Executive Summary

The Alumni & Student Matching Platform is a privacy-first, automated tool designed to connect current students with alumni based on specific project experience and professional interests. By moving away from manual "best-guess" matching or external social media platforms, this system provides a scalable, secure, and highly relevant networking experience for the MScAC community.

---

## 1. The Value Proposition: Why This Approach?

Current methods for student-alumni outreach face significant hurdles that this platform is designed to eliminate:

- **Bypassing Manual Coordination**: Staff must manually identify matches based on personal memory or resume scanning, which is time-consuming and often misses nuanced technical alignments.
- **Overcoming LinkedIn Barriers**: LinkedIn requires paid subscriptions for messaging and is frequently saturated with unsolicited requests. Many alumni do not check LinkedIn regularly.
- **Privacy-First Design**: This system is an internal-first environment where student and alumni data remain protected.
- **Reduced Administrative Friction**: Automating the matching and initial outreach allows staff to focus on high-level engagement rather than manual email coordination.

---

## 2. Operational Workflow & Privacy Safeguards

### Step-by-Step Process

1. **Student Query**: A student submits a request describing their project interests or technical questions.
2. **Automated Matching**: The system identifies relevant alumni based on internship projects and professional history.
3. **Centralized Outreach**: An automated email is sent from a central program address.
4. **Student Privacy**: Alumni see the student’s query and email only.
5. **Alumnus Privacy**: Student cannot see alumni name, contact details, or employer.
6. **Initiating Contact**: Alumni choose whether to reply. Identity is revealed only if they initiate contact.

### Load Balancing & Monitoring

- **Request Caps**: Limit the number of active requests per alumnus.
- **Queue Management**: Rotate or delay requests if an alumnus is overloaded.
- **Staff Oversight**: All sent requests are archived for monitoring without exposing private details.

---

## 3. Launch Phases

### Phase 1 — Pilot Deployment (Validation)
- **Goal**: Validate match relevance and system flow with a small cohort.
- **Actions**: Configure matching logic, test email templates, verify privacy mechanisms.
- **Success Metrics**: Qualitative feedback and successful delivery of outreach emails.

### Phase 2 — Production Launch (Scale)
- **Goal**: Full-scale availability.
- **Actions**: Expand participation, enable automated load-balancing, provide staff archival dashboard.
- **Maintenance**: Regular data refreshes for new graduates and updated student cohorts.

---

## 4. Resource & Infrastructure Requirements

### Technical Infrastructure
- **Secure Backend Hosting**: Dedicated server or cloud environment (AWS/Azure).
- **Verified Domain**: Program-specific domain for email deliverability.
- **Email Service Provider**: Integration with ESP (e.g., SendGrid, AWS SES) for automated outreach.

### Estimated Effort & Ownership
- **Development & Setup**: 4–6 weeks part-time technical oversight.
- **Ongoing Maintenance**:
  - Technical: Monitor logs, semi-annual data refresh (2–4 hours/month).
  - Administrative: Review dashboards, coordinate with communications team.
- **Handover Plan**: Modular design for IT lead or future student lead with minimal specialized training.

---

## 5. Future Extension: Incoming Student Onboarding
- **Peer Matching**: Connect incoming students with current students.
- **Automated Mentorship**: Match based on undergraduate backgrounds or research interests.
- **Seasonal Activation**: Toggle "on" during summer onboarding and "off" during academic year.

---

## 6. Next Steps
- **Scope Approval**: Confirm prioritized launch of the Alumni Track.
- **IT Consultation**: Review hosting and domain requirements.
- **Timeline Alignment**: Define target dates for Phase 1 Pilot.

