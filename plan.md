# Alumni & Student Matching Platform

---

## Objective

Design, deploy, and maintain a lightweight matching platform that enables:

- Current students to connect with alumni based on aligned project experience and interests.

The goal is to improve engagement while minimizing administrative overhead and manual coordination.

(i'd like to highlight the ingenuity of the setup, like previously because we have to respect data privacy, when a student wants to ask a question to an appropriate alumni, we have to either 1. rely on informal personal connection program staff (claire might be close to someone, she has to pick an alumnus who would be probably be in the know about some question (but hey shes not a computer scientist so she can only approximate from a resume standpoint like oh they were also a math major in undergrad)) or 2. the student has to go to linkedin and try to message the alum but linkedin has a paywall for multiple connection requests with personal notes and also nobody with an actual career checks linkedin regularly / isnt spammed with lots of slop). so our method is far far better because it's completely protected, there's an automated matching within the machine using unsupervised machine learning (nearest embedding, actually no need to get into this) and the email to alumni comes right from a central address and personal info is revealed on THEIR initiative when they reach out to the student email we provide. 

- Incoming students to connect with current students as part of onboarding and community-building. (this comes later as an aside i guess, like say the setup works well for this and we've already talked to lisha about this and if it works we can show this also)



---

## Alumni Track (Core Pilot)

(oh maybe i duplicated stuff from here above accidentally. help me rethink the structure so that it's comprehensive without being redundant?)

This initial track focuses on alumni engagement by:

- Matching current students with alumni based on prior internship projects, interests, and availability.
- Supporting opt-in participation to respect privacy and willingness.
- Facilitating introductions while preserving participant privacy.
- Incorporating optional scheduling links (e.g., Calendly) to streamline booking. (i don't think we need this, i did clarify in the meeting that in my and my cohort's experience alumni have their own preferences for meeting platforms. but perhaps we should explain the process better overall like step by step what is happening in the model. maybe in its own section?)

This track serves as the foundation for the platform’s matching and outreach capabilities.

---

## Ownership & Ongoing Maintenance

To ensure reliable platform operation over time, clear technical ownership and ongoing work are essential, including:

- Periodic data refresh as alumni and student cohorts evolve.
- Monitoring match quality, user engagement, and system performance.
- Implementing small updates to accommodate new use cases or engagement goals.
- Coordinating with communications and web teams as needed.

(do i need to get more into details? i suppose we need to minimally provide details so that the IT guy will know what is going on. but yeah help prevent me from going into unnecessary detail that overwhelms the program team. do you need info on the setup of my prototype? havent fixed the prototype yet though.)

---

## Launch Phases

**Phase 1 — Pilot Deployment**

- Configure matching logic for alumni–student connections.
- Support limited outreach and testing to validate match quality and user flow.

(hmm is the matching logic is already done? it's just a query on a vector database. but i suppose we need to clarify what exactly we're going to tweak here. like we're going to test it out (make sure matches are decent, make sure the email is sent with the right template, no data privacy breaches) and save and monitor the load limit on any one alumni and decide what to do when an alumni is overloaded (like delay the email being sent, or maybe even just go to the next alum). anyway i think this should be clearer)

**Phase 2 — Production Launch**

- Expand participation volume.
- Add monitoring for match relevance and response rates.

(how about put all sent email connection requests into an archive and make sure the right staff are able to see it and monitor it?)

---

## Optional Future Extension

**Incoming Student Onboarding Track**

- Match incoming students with current students.
- Leverage the same matching and scheduling infrastructure.
- Enable as a seasonal or cohort-based feature.
- Refresh data regularly to reflect changing cohorts.
- Adjust matching logic based on observed usage patterns.

(i think this should be deep instead of broad and more detailed. maybe not just a smattering of bullet points like this one)

---

## Next Steps

- Align on desired launch scope and timeline.
- Confirm which tracks to support in the initial rollout.
- Define level of ongoing support and maintenance.
- Determine the appropriate engagement model for continued development and ownership.

(do we need a resources required section? like engagement model yes, but potentially the time to be spent building the pilot and expanding to production launch and monitoring from then on because it's not just an estimate for me it's an estimate for THEM if they decide to own this later on and let me go when i graduate. also we're going to need to buy a proper domain to host a backend to ensure security right, and setup a proper email service thing, like there's a lot of stuff that actually is required to turn this prototype into a working pilot system and ultimately for production launch. can we reason through this?)