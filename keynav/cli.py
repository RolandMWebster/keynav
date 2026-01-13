"""Command line interface for KeNav."""

import subprocess
import sys
from pathlib import Path

import readchar
import yaml

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RED = "\033[31m"


def load_config():
    """Load the configuration file."""
    config_path = Path(__file__).parent.parent / "config.yaml"
    if not config_path.exists():
        print(f"Config file not found: {config_path}")
        sys.exit(1)
    with open(config_path) as f:
        return yaml.safe_load(f)


def open_vscode(path: str):
    """Open a folder in VS Code."""
    subprocess.run(["code", path])


def open_url(url: str):
    subprocess.run(["open", "-a", "Safari", url])


def open_app(app_name: str):
    subprocess.run(["open", "-a", app_name])


def clear_screen():
    """Clear the terminal screen."""
    print("\033c", end="")


def display_menu(menu: dict, breadcrumb: str = ""):
    clear_screen()
    if breadcrumb:
        print(f"\n[{breadcrumb}]")
    print()
    for key, item in menu.items():
        print(f"  {BOLD}{YELLOW}{key}{RESET} -> {item['label']}")
    print(
        f"\n {BOLD}{CYAN}b{RESET} -> back    {BOLD}{CYAN}q{RESET} -> main/quit    {BOLD}{CYAN}Q{RESET} -> quit    {BOLD}{CYAN}R{RESET} -> refresh config"
    )
    print()


def get_menu_item(menu: dict, choice: str):
    """Get a menu item by choice."""
    if choice in menu:
        return menu[choice]
    try:
        int_choice = int(choice)
        if int_choice in menu:
            return menu[int_choice]
    except ValueError:
        pass
    return None


def navigate(menu: dict, breadcrumb: str = "", parent_stack=None, main_menu=None):
    if parent_stack is None:
        parent_stack = []
    if main_menu is None:
        main_menu = (menu, breadcrumb, parent_stack)
    while True:
        display_menu(menu, breadcrumb)
        print("> ", end="", flush=True)
        choice = readchar.readkey()
        print(choice)

        if choice == "Q":
            sys.exit(0)
        if choice == "b":
            if parent_stack:
                prev_menu, prev_breadcrumb, prev_stack = parent_stack.pop()
                return prev_menu, prev_breadcrumb, prev_stack
            else:
                print("Already at the main menu.")
                continue
        if choice == "q":
            if not parent_stack:
                # At main menu, exit
                sys.exit(0)
            else:
                # Go back to main menu
                while parent_stack:
                    prev_menu, prev_breadcrumb, prev_stack = parent_stack.pop(0)
                return prev_menu, prev_breadcrumb, prev_stack
        if choice == "R":
            # Refresh config and return to main menu
            print("Refreshing config...")
            config = load_config()
            menu = config["menu"]
            breadcrumb = ""
            parent_stack = []
            main_menu = (menu, breadcrumb, parent_stack)
            return main_menu

        item = get_menu_item(menu, choice.lower())
        if item:
            if "submenu" in item:
                new_breadcrumb = (
                    f"{breadcrumb} > {item['label']}" if breadcrumb else item["label"]
                )
                # push current state to stack
                parent_stack.append((menu, breadcrumb, parent_stack.copy()))
                menu, breadcrumb, parent_stack = navigate(
                    item["submenu"], new_breadcrumb, parent_stack, main_menu
                )
            elif "action" in item:
                action = item["action"]
                if action == "open_vscode":
                    print(f"Opening folder: {item['path']}")
                    open_vscode(item["path"])
                elif action == "open_url":
                    print(f"Opening URL: {item['url']}")
                    open_url(item["url"])
                elif action == "open_app":
                    print(f"Opening application: {item['app']}")
                    open_app(item["app"])
                return main_menu
        else:
            print(f"{RED}Invalid choice: {choice}{RESET}")


def main():
    """Entry point for the KeyNav CLI."""
    config = load_config()
    print(f"{BOLD}KeyNav - Keyboard Shortcut Based Navigator")
    menu = config["menu"]
    breadcrumb = ""
    parent_stack = []
    main_menu = (menu, breadcrumb, parent_stack)
    while True:
        menu, breadcrumb, parent_stack = navigate(
            menu, breadcrumb, parent_stack, main_menu
        )


if __name__ == "__main__":
    main()
