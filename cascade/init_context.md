<!-- @meta {
  "fileType": "immutable",
  "purpose": "Immutable North-Star: Defines the foundational goals, architectural principles, and AI operational boundaries for this specific project.",
  "editPolicy": "readonly",
  "routeScope": "global"
} -->
# Project North-Star: Initial & Immutable Context

This document provides the foundational, unchanging (immutable) context for the AI agent operating on this project. It outlines the core mission, critical architectural principles, and the AI's defined role and boundaries. This context must underpin all AI reasoning, planning, and actions.

---
## I. Core Project Identity & Mission

*   **Project Name:** `[Specify Project Name - e.g., "NextGen E-commerce Platform", "AI-Powered Medical Diagnosis Assistant"]`
*   **Primary Goal/Mission:** `[Define the single most important objective of this project. Be specific. E.g., "To build a highly scalable and personalized e-commerce experience that achieves market leadership through superior usability and AI-driven recommendations." or "To assist medical professionals by providing rapid, accurate, and evidence-based preliminary diagnostic suggestions from medical imagery and patient data."]`
*   **Key Success Metrics (Conceptual):** `[List 2-3 high-level indicators of project success. E.g., "Significant year-over-year growth in user engagement and conversion rates," "Consistently high customer satisfaction (CSAT > 90%)," or "Demonstrable improvement in diagnostic speed and accuracy for targeted conditions," "Adoption by X number of clinics within Y years."]`

---
## II. Fundamental Architectural Principles & Constraints

*   **Primary Technology Stack (Core Immutable Elements):**
    *   Backend: `[e.g., Python with FastAPI, Java with Spring Boot, Node.js with Express]`
    *   Frontend: `[e.g., React, Angular, Vue.js, SvelteKit]`
    *   Database(s): `[e.g., PostgreSQL, MongoDB, MySQL, Cassandra]`
    *   Primary Cloud Provider: `[e.g., AWS, Azure, GCP, None/On-premise]`
    *   Other Critical Libraries/Frameworks: `[e.g., "Kafka for event streaming," "Kubernetes for orchestration (if applicable)"]`
*   **Overarching Architectural Style (If Fixed & Critical):**
    *   `[e.g., "Microservices architecture with event-driven communication patterns," "Modular Monolith," "Serverless-first for all new backend services," "Strict adherence to Clean Architecture principles."]`
*   **Key Design Non-Negotiables (Immutable Rules):**
    *   `[e.g., "All sensitive user data must be encrypted at rest and in transit using industry-standard algorithms."]`
    *   `[e.g., "The system must be designed for horizontal scalability to accommodate X users/requests."]`
    *   `[e.g., "All new APIs must adhere to the existing OpenAPI v3.x contract defined in /cascade/domains/schema/api_contracts.md."]`
    *   `[e.g., "Accessibility: All user-facing components must meet WCAG 2.1 AA standards."]`
*   **Critical Performance/Scalability Targets (Absolute Minimums):**
    *   `[e.g., "Core API endpoints must maintain an average response time below 150ms under peak load conditions as defined in performance_targets.md."]`
    *   `[e.g., "System must handle a sustained load of 10,000 concurrent users."]`

---
## III. AI Agent's Role & Boundaries within this Project

*   **Primary Role of AI:** `[Be specific. E.g., "To assist in the development of new features for the client-side application, including component creation, state management logic, and unit/integration tests.", "To generate and maintain comprehensive API documentation based on OpenAPI specifications and code comments.", "To identify and propose refactoring opportunities in legacy modules to improve code quality and align with modern best practices."]`
*   **Scope Limitations (Hard Boundaries - What AI Must NOT Do):**
    *   "AI must **never** deploy any code to production environments. All deployments require human review and manual execution of deployment pipelines."
    *   "AI must **never** alter this file (`cascade/init_context.md`), `/cascade/00_BOOTSTRAP.md`, or `/cascade/system_manifest.md`."
    *   "AI must **not** make changes to core security modules (e.g., authentication, authorization) without an approved job plan explicitly detailing the changes and signed off by a human lead (simulated via a `requiresReview: true` flag and positive confirmation if applicable)."
    *   "AI must **not** introduce new core dependencies (e.g., new programming languages, major frameworks) without these being documented as a key decision in the relevant domain's `key_decisions.md` file and approved."
    *   `[Add any other project-specific critical boundaries]`
*   **Preferred Development Practices (Guiding Principles for AI):**
    *   `[e.g., "Strive for Test-Driven Development (TDD) where practical, ensuring new logic is accompanied by robust tests."]`
    *   `[e.g., "Code comments should be clear, concise, and explain the 'why' behind complex logic, not just restate the 'what'."]`
    *   `[e.g., "Follow the Don't Repeat Yourself (DRY) principle diligently."]`
    *   `[e.g., "Ensure all contributions are consistent with coding conventions defined in relevant /cascade/domains/<domain>/conventions.md files."]`

---
## IV. Core Values / Guiding Philosophy (Project-Specific)

*   `[e.g., "User-centricity: Prioritize features and designs that deliver maximum value and ease-of-use to the end-user."]`
*   `[e.g., "Robustness & Reliability: Build for stability and ensure comprehensive error handling."]`
*   `[e.g., "Maintainability: Write clean, well-documented, and easily understandable code."]`
*   `[e.g., "Security by Design: Integrate security considerations into every stage of development."]`
*   `[e.g., "Iterative Progress: Favor incremental improvements and continuous learning."]`

---
This document is immutable and serves as the ultimate reference for the AI's core operational context within this project.
