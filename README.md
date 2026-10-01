# application_hub
APP1: Network Subnet Planner

A Flask-based network subnet planning tool that automatically calculates the optimal subnet configuration based on the required number of usable hosts.

## Features

- Accepts the required number of usable hosts as input
- Automatically calculates the optimal CIDR prefix
- Generates the corresponding subnet mask
- Selects the appropriate private network class (A, B, or C)
- Calculates the network address
- Determines the usable host address range
- Calculates the broadcast address
- Displays the total usable host capacity

## Technologies

- Python
- Flask
- Jinja2
- HTML/CSS

# APP2: SecOps Lab

A Flask-based cybersecurity learning and security operations laboratory that provides practical tools for exploring fundamental cybersecurity concepts, including password security, hashing, encoding, JWT authentication, network security, web security, and log analysis.

## Features

* Provides a dashboard for accessing security-related tools
* Analyzes password strength and demonstrates password hashing methods
* Provides hashing and encoding tools
* Includes JWT-based authentication and token-related tools
* Provides basic network security tools
* Checks HTTP security headers for a given URL
* Includes a basic log analysis tool
* Supports user authentication and logout functionality

## Technologies

* Python
* Flask
* Jinja2
* HTML/CSS
* JavaScript
* JWT
* zxcvbn
* Argon2
* bcrypt
* scrypt
* PBKDF2
* Vercel

# APP3: CAPEC Explorer

A Flask-based cybersecurity application developed to collect, process, store, and explore **MITRE CAPEC** attack pattern data. The application downloads the CAPEC dataset, processes the CSV data, stores it in PostgreSQL using Supabase, and provides a web interface for exploring attack patterns.

## Features

* Downloads and extracts the CAPEC dataset
* Processes CSV data using Pandas
* Stores data in PostgreSQL with Supabase
* Provides a web interface for exploring CAPEC data
* Supports data parsing and processing

## Technologies

* Python
* Flask
* Jinja2
* Pandas
* Requests
* PostgreSQL
* Supabase
* HTML/CSS
* Vercel
