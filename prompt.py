import os
import subprocess

# Codes ANSI
RESET  = "\033[0m"
BOLD   = "\033[1m"
YELLOW = "\033[33m"
GREEN  = "\033[32m"

def get_git_branch():
    try:
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True,
            text=True,
            timeout=1 
        )
        branche = result.stdout.strip()
        return branche if branche else None
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None

def get_prompt():
  
    # Remplace /home/khalil par ~
    cwd = os.getcwd().replace(os.path.expanduser("~"), "~")
    
    branche = get_git_branch()
    
    if branche:
        # ~/projets/ksh (main)>
        return f"{GREEN}{BOLD}{cwd}{RESET} {YELLOW}({branche}){RESET} Kshell> "
    else:
        return f"{GREEN}{BOLD}{cwd}{RESET} Kshell> "