import os
import sys

print("==================================================")
print("🔍 AI CODE REVIEWER & SECURITY SCANNER v1.0")
print("==================================================")

def scan_file(filepath):
    if not os.path.exists(filepath):
        print(f"❌ Error: File '{filepath}' not found.")
        return
    
    print(f"\n📂 Analyzing file: {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()
    
    issues = []
    # Простейший статический анализ на опасные конструкции (например, для демонстрации американским девелоперам)
    if "eval(" in code:
        issues.append("⚠️ SECURITY WARNING: Usage of 'eval()' detected. This can lead to remote code execution.")
    if "print(" in code:
        issues.append("💡 PERFORMANCE TIP: Consider replacing 'print()' with a proper logging module for production.")
    if len(code.splitlines()) > 100:
        issues.append("💡 STRUCTURE TIP: File is getting large (>100 lines). Consider breaking it into modules.")

    print("\n--- SCAN RESULTS ---")
    if issues:
        for issue in issues:
            print(issue)
    else:
        print("✅ No critical issues found. Clean code!")
    print("==================================================")

if __name__ == "__main__":
    target = input("Enter path to python file to review: ").strip()
    scan_file(target)