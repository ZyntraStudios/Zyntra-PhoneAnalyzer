# Zyntra-PhoneAnalyzer
Get public information about a phone number

This project allows you to analyze phone numbers and extract useful information without the need for external APIs.

# With this script you can:

Determine if a number is possible or valid.

View the number in different formats: E.164, international, national, and RFC3966.

Obtain information about the country, region, and carrier.

Find out the time zone associated with the number.

Display the international and national prefixes.

# Installation

Clone this repository to your machine and navigate to the folder:
git clone https://github.com/ZyntraStudios/Zyntra-PhoneAnalyzer
cd Zyntra-PhoneAnalyzer

Install the necessary library:
pip install phonenumbers

# Usage

Run the script:
python analyzer.py

The script will ask you for:

Phone number (example: +34123456789 or 600112233).

Default country code (example: ES, US, MX). If you don't enter it, it will use ES by default.

Banner colors (optional; you can leave it blank for the default values).

# ⚠️ NOTE FOR DEVELOPERS: Never upload real phone numbers to your repository; only use examples of safe numbers.

# Examples of secure numbers

+34123456789
+15551234567
+521234567890

# Contributions

If you want to improve the project:

Fork the repository.

Create your branch: `git checkout -b new-improvement.`

Make your changes and commit: `git commit -m "Added new functionality".`

Push to your branch: `git push origin new-improvement.`

Open a pull request.

# License

This project is licensed under the MIT License.

You can use and modify it freely, but please maintain attribution.
