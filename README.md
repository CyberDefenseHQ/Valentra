# Valentra

![Valentra Logo](docs/images/valentra-logo.png)

**Version 0.4.0 - Sprint 0 Complete**

Valentra is a security engineering portfolio project designed to demonstrate the incremental development of a modular security platform.

## Sprint 0 - Platform Foundation

Sprint 0 established the application, identity, and user interface foundations required for future security-engineering functionality.

### Current Capabilities

- Flask application factory and modular blueprint architecture
- SQLAlchemy database integration
- Flask-Login integration and user loader
- Bcrypt integration
- Database migration support
- User model with username, password hash, and role fields
- Authentication route scaffolding
- Audit logging foundation
- Health-check endpoint
- Shared application UI template
- Security overview dashboard
- Navigation for Detection, Identity, Incidents, and Reports
- Static CSS and JavaScript assets

## Sprint 0 Release History

### v0.1.0 - Initial Foundation
Established the initial Valentra project structure and development foundation.

### v0.2.0 - Application Foundation
Established the Flask application foundation, extensions, dashboard, and health-check functionality.

### v0.3.0 - Identity Foundation
Added the user model, authentication scaffolding, Flask-Login user loading, and audit logging foundation.

### v0.4.0 - Professional UI Shell
Added the shared application interface, security navigation, dashboard summary cards, CSS styling, and JavaScript foundation.

## Current Dashboard

The Security Overview currently displays demonstration values for:

- Security Score
- Active Incidents
- Detection Rules

These values are placeholders and are not yet generated from live security-event data.

## Current Limitations

Valentra does not yet provide complete authentication, authorization, event ingestion, detection, incident response, or reporting workflows. Components introduced during Sprint 0 establish the foundation for those capabilities rather than representing completed production functionality.

## Next - Sprint 1

Sprint 1 will begin transforming Valentra from a platform foundation into a functioning security application.

Initial development will focus on security-event ingestion and detection, allowing Valentra to process simulated security events and begin generating meaningful detection results.
