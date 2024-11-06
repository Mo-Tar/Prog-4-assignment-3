# COMP 3504 - Tool Inventory Management System

## Overview

This project is a simple inventory management system for a retail shop that sells tools. The program allows the store owner to:

- Add and delete tools from the inventory.
- Search for tools by tool nameor tool ID.
- Automatically generate order lines when the quantity of a tool falls below a specified threshold.

The project is divided into two 1-week sprints, following agile best practices. The development is done collaboratively using GitHub for version control.

## Programming Language

The application is implemented in Python.


## Features
1. **Add and Delete Tools**: The owner can add new tools to the inventory or delete them.
2. **Search for Tools**: Tools can be searched by name or ID.
3. **Inventory Management**: The system checks if the quantity of an item falls below 10. If so, it automatically generates an order.
4. **Order Generation**: Orders are written to orders.txt and include tool details, supplier information, and total costs.
5. **Data Storage**: Tool information is read from items.txt, and supplier information is read from suppliers.txt.

## Files
- **main.py**: Contains the code for the program.
- **items.txt**: Contains information on tools, including ID, name, quantity, price, and supplier ID.
- **suppliers.txt**: Stores supplier details such as ID, company name, address, and salesperson contact.
- **orders.txt**: Stores order details when inventory falls below the threshold.

## Usage
1. **Launch the Program**
   - Run **'main.py'** file to start the program.
   - You'll be greeted with the **Inventory Menu**.
1. **Main Menu Options**
   - Select the desired option:
       1. **Modify Inventory**: Add, delete, or check the quantity of each item in stock and generate an order line to restock items below 10.
       2. **Search Inventory**: Search for tools by name or ID.
       3. **Exit**: Closes the program.

     

## Contribution
- All team members contributed equally to the development tasks. GitHub issues and task boards were used to track progress and assign tasks. Each team member committed code regularly and followed proper commenting practices in Git commits.
