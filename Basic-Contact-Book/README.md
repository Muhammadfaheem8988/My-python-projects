**Simple Python Contact Book**

A clean, dictionary-based CLI application for managing personal contacts. This program allows users to store, retrieve, and manage contact information using a fast and intuitive menu system.

**Features**

Add Contacts:Store names and phone numbers in a persistent runtime dictionary.

View All: List all saved contacts in a formatted view.

Quick Search: Find a specific phone number by entering a name.

Delete Contact: Easily remove entries from your contact list.

Data Integrity: Uses .strip() to ensure no accidental whitespace messes up your searches.
----

**Installation & UsageRequirement:** 

Python 3.x

Run the script:

Bash

python basic_contact_book.py

Navigate the Menu:1: Add a new person.2: See everyone in the book.3: Search for a specific friend.4: Remove a contact.5: Close the app.

Technical DetailsThis project utilizes Python dictionaries for $O(1)$ average time complexity on lookups and deletions, making it highly efficient for managing data by unique keys (names).
----

**License**

This project is open-source and available under the MIT License.
-----