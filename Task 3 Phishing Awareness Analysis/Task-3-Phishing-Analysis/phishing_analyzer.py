import re
def analyze_email(file_path):
    print(f"\n--- Analyzing Email: {file_path} ---")
    with open(file_path, 'r') as file:
        content = file.read()
    score = 0
    red_flags = []
    from_match = re.search(r"From:.*<(.*)>|From:\s*([^\n<]+)", content)
    return_path_match = re.search(r"Return-Path:\s*<?([^>\n]+)>?", content)
    if from_match and return_path_match:
        from_email = from_match.group(1) if from_match.group(1) else from_match.group(2)
        return_path = return_path_match.group(1)
        
        if from_email.strip() != return_path.strip():
            score += 40
            red_flags.append(f"Sender-Domain Mismatch: 'From' is {from_email.strip()} but 'Return-Path' is {return_path.strip()}")

    urgent_keywords = ['urgent', 'immediately', 'strictly confidential', 'mandatory', 'password expires', 'lockout']
    found_keywords = [word for word in urgent_keywords if word.lower() in content.lower()]
    
    if found_keywords:
        score += (len(found_keywords) * 15)
        red_flags.append(f"Urgency/Fear Triggers found: {', '.join(found_keywords)}")

    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
    for url in urls:
        if len(url.split('.')) > 3 or "login" in url or "update" in url:
            score += 20
            red_flags.append(f"Suspicious URL structure detected: {url}")

    print("Actionable Outcome:")
    if score >= 50:
        print(">> MALICIOUS: Block Domain & Escalate to Security Team.")
    elif score >= 20:
        print(">> SUSPICIOUS: Warn User and Investigate Further.")
    else:
        print(">> SAFE: Close ticket. No immediate threat detected.")

    if red_flags:
        print("\nRed Flags Identified:")
        for flag in red_flags:
            print(f"- {flag}")

if __name__ == "__main__":
    analyze_email("sample_emails/safe_email.txt")
    analyze_email("sample_emails/malicious_email.txt")