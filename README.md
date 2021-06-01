# ccd-webscraping
This is a basic webscrapper to pull  down and look for changes on the Cheollima Civil Defense website.

## Key Learnings
By default urllib uses a default user agent, which some webservers will block for security reasons, to get around this I spoofed the user agent to appear as a common browser.

## Installation
1. Requirement: Python3
2. Download project as zip and extract or clone repository
3. From command line run 'python3 scraper.py'

## Future Plans
Write cron job to run the script regularly.
Intergrate with twitter API to tweet my account when a change is detected.
Possibly hook up with Arduino for physical alert.
