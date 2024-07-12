# IP Information App 🌐

## Overview

Welcome to the IP Information App! This sleek desktop application, built using Python, Tkinter, and customtkinter, allows you to effortlessly retrieve and display information about IP addresses. With a clean, dark-themed interface and intuitive controls, you can easily access and copy details about any IP address.

## Features ✨

- **Search IP Information:** Quickly input an IP address to fetch and display detailed information.
- **User-Friendly Display:** View the data in an organized split view with keys on one side and corresponding values on the other.
- **Clipboard Integration:** Copy the information to your clipboard with a single click for convenience.

## Prerequisites ⚙️

Ensure Python is installed on your system. This app depends on the following packages:

- `tkinter`
- `customtkinter`
- `pyperclip`
- `requests`

Install the required packages using pip:

pip install customtkinter pyperclip requests

## Installation 🔧

1. **Install Files:**

      Just Download the main.py!

2. **Install Required Packages:**

    ```bash
    pip install customtkinter pyperclip requests
    ```

## Usage 🚀

1. **Run the Application:**

    ```bash
    python main.py
    ```

2. **Search for IP Information:**

    - Enter an IP address in the input box.
    - Click the "Search Up" button to retrieve the information.

3. **View and Copy Information:**

    - The results will be displayed in two list boxes: one for keys and one for values.
    - Click the "Copy info" button to copy the information to your clipboard.

## Code Breakdown 🔍

- **App Class:** The core of the application, extending `customtkinter.CTk` to provide a modern, custom look.
- **get_info Method:** Retrieves and updates the IP information using the IP-API service.
- **copy Method:** Copies the displayed information to the clipboard.

## Contributing 🤝

Contributions are welcome! Feel free to open an issue or submit a pull request if you have suggestions or improvements.
