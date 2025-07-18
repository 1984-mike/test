#!/usr/bin/env python3
"""
Hello World script generated by Claude
Created for 1984-mike/test repository
"""

import datetime

def greet_user():
    """Generate a personalized greeting"""
    current_time = datetime.datetime.now()
    return f"Hello! This file was generated by Claude at {current_time.strftime('%Y-%m-%d %H:%M:%S')}"

def main():
    print("=" * 50)
    print("🤖 Claude Generated Python Script")
    print("=" * 50)
    print(greet_user())
    print("\nThis demonstrates how Claude can:")
    print("✓ Generate code")
    print("✓ Push directly to GitHub")
    print("✓ Create structured projects")
    print("=" * 50)

if __name__ == "__main__":
    main()
