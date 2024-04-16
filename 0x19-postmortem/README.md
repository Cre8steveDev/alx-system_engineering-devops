# Postmortem: Apache Configuration Error

## Issue Summary:

On Monday, 15th April 2024 between 1:45pm and 2:45pm (WAT), our WordPress website experienced an outage due to a typographical error in the Apache configuration file. This resulted in users being unable to access the website. We estimate that 100% of users were impacted during this period.

## Timeline:

- 1:45pm: I received an alert from our monitoring system (DataDogHQ), as metrics were below the expected threshold of our website traffic. This alert was also followed by a series of complaint mails from customers about inability to access our website.
- 2:00pm: Upon further investigation, I identified errors in the Apache access logs.
- 2:15pm: Using strace, I traced the issue to a typo in the Apache configuration file, where "phpp" was used instead of "php". This prevented Apache from processing PHP scripts, which are critical for WordPress functionality. Sneaky little typo that messed things up, phew!
- 2:30pm: The engineer corrected the typo in the configuration file and restarted the Apache service.
- 2:45pm: The website was back online and functioning normally.

## Root Cause and Resolution:

The root cause of the outage was a typographical error in the Apache configuration file. The directive referencing the PHP interpreter path contained "phpp" instead of the correct value "php". This resulted in Apache failing to process PHP scripts, leading to the website being unavailable.

I resolved the issue by correcting the typo in the configuration file to reflect the correct path to the PHP interpreter. The Apache service was then restarted to apply the changes, restoring website functionality.

## Corrective and Preventative Measures:

- Improved code review process: We will implement a more thorough code review process for all configuration file changes, including manual verification of critical directives.
- Automated configuration checks: We will explore implementing automated tools to detect syntax errors and inconsistencies in configuration files before deployment.
- Enhanced monitoring: We will refine our monitoring system to provide alerts for specific Apache error messages, allowing for faster identification of configuration issues.

## Lessons Learned:

This incident highlights the importance of careful configuration management and robust monitoring practices. By implementing the corrective and preventative measures outlined above, we can minimize the risk of similar outages in the future.
