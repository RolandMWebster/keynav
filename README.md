# KeyNav CLI

A keyboard-driven CLI for navigating files, bookmarks, and launching apps on macOS.

![KeyNav Screenshot](docs/keynav_screenshot.png "Example screenshot of KeyNav CLI.")
*Example Screenshot of KeyNav CLI.*

## Setup

The following setup is outlined for KeyNav usage with an iTerm2 Hotkey Window, which allows full
navigation via keyboard shortcuts.

### Requirements
- macOS
- [iTerm2](https://iterm2.com/)
- Python 3.8+

### 1. Download and Install iTerm2
- Go to [https://iterm2.com/](https://iterm2.com/) and download the latest version.
- Move iTerm2 to your Applications folder and open it at least once.

### 2. Set Up the Hotkey Window
- Open iTerm2 and go to **Settings -> Keys -> Hotkey**.
- Click **"Create a Dedicated Hotkey Window"**.
- Assign your preferred hotkey (e.g., `Cmd+Shift+Spacebar`).
- Go to **Profiles -> Hotkey Window** (or the profile you selected for the hotkey window):
  - Under **General**, set **"Send text at start"** to:
  ```
  keynav
  ```
- Set any other preferred formatting for the Window, e.g.:
  - Set opacity to 100% for solid background.
  - Set window to fullscreen.
  - Increase text size for readability.

### 3. Configure PATH
- Make sure the `keynav` command is available in your terminal. You may need to add the installation directory to your PATH.
- Ensure the `code` command is available in PATH for opening files in VSCode.
  - In VSCode, open the Command Palette (`Cmd+Shift+P`), type `Shell Command: Install 'code' command in PATH`, and select it.

### 4. Install NavKey CLI
- Clone this repository.
- In the project directory, run:
  ```sh
  pip install -e .
  ```
- Update the `configuration.yaml` file to have your desired configurations.

## Usage
- Press your hotkey (e.g., `Cmd+Shift+Spacebar`) to instantly open KeyNav in iTerm2.
- Use the displayed hotkeys to navigate projects, bookmarks, and apps.

### Example `config.yaml`
```yaml
menu:
  p:
    label: projects
    submenu:
      1:
        label: "sample_project"
        action: "open_vscode"
        path: "/Users/sample_user/Documents/sample_project"
  b:
    label: "bookmarks"
    submenu:
      g:
        label: "Google"
        action: "open_url"
        url: "https://google.com"
  m:
    label: "Messaging"
    submenu:
      t:
        label: "Teams"
        ation: "open_app"
        app: "Microsoft Teams"
      o:
        label: "Outlook"
        action: "open_app"
        app: "Microsoft Outlook"
```

Enjoy fast, distraction-free navigation on your Mac!