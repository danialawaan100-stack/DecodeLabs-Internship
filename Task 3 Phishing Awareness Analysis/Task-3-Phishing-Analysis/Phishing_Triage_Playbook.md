# Phishing Triage Playbook & Standard Operating Procedures
**DecodeLabs - Project 3: Phishing Awareness Analysis**

## 1. Introduction
This toolkit serves as the detection phase documentation for identifying phishing attempts. It provides non-expert triage checklists, standard operating procedures (SOPs) for header parsing, and a clear decision tree. 

## 2. Phishing Red Flag Checklist
When evaluating communications, look for the following cognitive triggers and visual illusions:

*   **Sender-Domain Mismatch:** The display name conflicts with the actual routing domain in the headers[cite: 1].
*   **Fake Forwarded Chains:** `FW:` threads containing strange timestamps[cite: 1].
*   **Dangerous Attachments:** Uncommon file extensions like `.iso`, `.js`, or `.scr`[cite: 1].
*   **Urgent Bypass Requests:** Demands for secrecy or bypassing normal security procedures[cite: 1].
*   **MFA Fatigue:** Multiple unprompted authenticator push notifications[cite: 1].
*   **Typosquatting & Subdomain Traps:** URLs buried at the end of a string (e.g., `www.company.tech.login-update.com`)[cite: 1].
*   **QR Code Prompts (Quishing):** Unsolicited codes demanding a scan to bypass desktop filters[cite: 1].

## 3. SOP: Parsing Email Headers
To properly identify sophisticated impersonation, standard email displays must be bypassed in favor of raw headers.

1.  **Extract the Header:** Open the email properties to view the expanded header.
2.  **Compare 'From' vs 'Return-Path':** The `From` address is what the user sees. The `Return-Path` is where replies are routed. If they do not match, the domain is likely spoofed[cite: 1].
3.  **Read URLs Right to Left:** Locate the true root domain to identify fake subdomains[cite: 1].

## 4. Triage Decision Tree
Every triage event must end in a definitive action based on the "Pause, Verify, Report" methodology[cite: 1].

*   **Condition 1:** The email passes all domain checks, contains no urgency triggers, and matches expected internal communication.
    *   **Actionable Outcome:** **SAFE** -> Close the ticket.
*   **Condition 2:** The email contains mild urgency, unexpected attachments, or an unusual sender, but lacks clear malicious links.
    *   **Actionable Outcome:** **SUSPICIOUS** -> Warn User. Apply the Five-Minute rule and verify via a secondary out-of-band channel (e.g., phone call)[cite: 1].
*   **Condition 3:** The email contains blatant sender-domain mismatches, aggressive credential prompts, or known dangerous file extensions.
    *   **Actionable Outcome:** **MALICIOUS** -> Block Domain & Escalate. Report using the internal plugin to purge the threat from all inboxes[cite: 1].

## 5. Technical Implementation (Bonus)
A Python script (`phishing_analyzer.py`) has been developed alongside this playbook to automate the parsing of `From`/`Return-Path` mismatches and urgency keywords, providing an immediate Actionable Outcome.