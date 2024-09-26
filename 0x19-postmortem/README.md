# When a Picture Wasn't Worth a Thousand Words (More like a Thousand Errors! :smile:
## Issue Summary:

On July 20th, 2023, between 10:00 AM - 11:30 AM PST, our e-commerce platform experienced a partial outage affecting image delivery. Customers reported seeing broken image icons on product pages, impacting approximately 70% of users. The root cause was identified as insufficient disk space on the image server due to an unmonitored log file growing excessively.

## Timeline:

**10:05 AM PST**: Customer support tickets reporting broken images began increasing.

**10:10 AM PST**: The issue was escalated to the engineering team after initial investigation by customer support.

**10:15 AM PST**: Engineers began investigating potential CDN issues, assuming the root cause lay there.

**10:30 AM PST**: CDN logs showed no errors, leading the team to investigate the image server directly.

**10:45 AM PST**: Monitoring dashboards revealed critically low disk space on the image server.

**10:50 AM PST**: The excessively large log file was identified and immediately removed, freeing up disk space.

**11:00 AM PST**: Image delivery gradually resumed as the server recovered.

**11:30 AM PST**: Full image functionality was restored.

## Root Cause and Resolution:

The root cause of the outage was an unmonitored log file within the image server, which grew excessively large and consumed all available disk space. This prevented the server from writing new image data, leading to the broken image icons. The immediate resolution involved identifying and removing the problematic log file, freeing up space for normal operations to resume.

## Corrective and Preventative Measures:

This incident highlighted key areas for improvement within our infrastructure:

Monitoring: Implement comprehensive monitoring of disk space utilization across all critical servers.

Log Management: Implement a robust log rotation strategy to prevent excessive log file growth.

Incident Response: Improve internal communication channels and escalation procedures for faster incident resolution.

## Specific Tasks:

[High Priority]: Configure disk space usage alerts on all production servers.

[High Priority]: Implement log rotation for all critical application logs.

[Medium Priority]: Review and update the incident response playbook for improved clarity and efficiency.

[Low Priority]: Investigate and implement automated log analysis tools for proactive issue identification.

