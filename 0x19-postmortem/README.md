
![alt text](image.png)


# WordPress Website 500 Internal Server Error

## Issue Summary
Duration of Outage:
Start: June 18, 2024, 6:00 AM CAT
End: June 18, 2024, 10:55 AM CAT

## Impact:
The WordPress website, running on a LAMP stack, was completely inaccessible, returning a 500 Internal Server Error. Users were unable to access any content or perform any actions on the site. This outage affected 100% of users, leading to a complete disruption of service.

## Root Cause:
A typo in the /var/www/html/wp-settings.php file, where a required PHP file was incorrectly referenced with an extra 'p' in the file extension.

## Timeline
6:00 AM CAT: Issue detected through monitoring alert indicating a 500 Internal Server Error.
6:05 AM CAT: On-call engineer confirmed the issue and began initial diagnostics using curl.
6:15 AM CAT: Assumed the issue was related to recent WordPress plugin updates; began deactivating plugins.
6:30 AM CAT: Deactivating plugins did not resolve the issue. Further investigation required.
6:45 AM CAT: Issue escalated to the DevOps team for deeper analysis.
7:00 AM CAT: Used strace to attach to the Apache process and identify the cause of the 500 error.
7:30 AM CAT: strace output revealed a typo in the /var/www/html/wp-settings.php file.
8:00 AM CAT: Misleading path: Investigated potential database connection issues.
8:30 AM CAT: Correctly identified and fixed the typo in the PHP file.
9:00 AM CAT: Restarted Apache server to apply the changes.
10:45 AM CAT: Confirmed that services were restored.
10:55 AM CAT: Services fully restored, confirmed by monitoring tools and manual checks.
## Root Cause and Resolution
Root Cause:
The issue was caused by a typo in the /var/www/html/wp-settings.php file. The line require_once( ABSPATH . WPINC . ‘/class-wp-locale.phpp’ ); incorrectly referenced the file class-wp-locale.phpp instead of class-wp-locale.php.

Resolution:

Identify the Typo: Used strace to trace system calls and identify the typo in the wp-settings.php file.

Correct the Typo: Edited the wp-settings.php file to correct the typo:
```
require_once( ABSPATH . WPINC . ‘/class-wp-locale.php’ );
```
Restart Apache: Restarted the Apache server to apply the changes and restore service.

## Corrective and Preventative Measures
Improvements:

Code Review: Implement a more thorough code review process to catch typos and other errors before deployment.
Error Logging: Enhance error logging to provide clearer error messages that can help quickly identify issues like typos.
Automation: Automate checks for common configuration errors and typos.
Tasks:

Enhance Code Review Process: Implement peer reviews and automated linting tools to catch errors in code.
Improve Error Logging:
Configure Apache and PHP to provide detailed error logs.
Implement centralized logging to make it easier to track and analyze errors.
Automate Checks:
Develop scripts to check for common configuration errors.
Integrate these scripts into the CI/CD pipeline.
Documentation and Training: Update documentation on debugging practices and provide training sessions for the team on using tools like strace.
