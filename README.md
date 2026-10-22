# Odoo Technical Course: Learning Notes & Code (Odoo 19.0)

> **This is a personal learning repository, not an original product.**
>
> This repository documents my progress through [The Complete Odoo 16/17 Technical Course: From Zero to Hero](https://www.udemy.com/course/the-complete-odoo-technical-course-2023-from-zero-to-hero/) by **Miracle Ayodele**.
>
> The course teaches Odoo 16/17, but I am following along using **Odoo 19.0**. The code in this repository is written by me as I work through the lectures and adapt the examples to Odoo 19.
>
> No course videos or paid learning materials are included. If you find the course useful, please purchase it and support the instructor.

## Why This Repository Exists

I'm building my career as an Odoo developer. Alongside a project-based roadmap focused on practical development, testing, API integrations, and deployment, I use this course to strengthen my understanding of the Odoo framework.

This course complements my independent project work in four ways:

- **Structured foundations:** A section-by-section introduction to Odoo's technical framework.
- **A second teaching perspective:** An instructor's explanations alongside my own experiments and projects.
- **A completion certificate:** An additional milestone upon finishing the course.
- **A visible learning trail:** Section-by-section Git commits documenting my progress and development workflow.

## The Challenge: Learning Odoo 16/17 Concepts on Odoo 19

The course was recorded for Odoo 16/17, but my development environment uses Odoo 19.0. As a result, some examples require adjustments because of changes in the framework, APIs, views, or configuration.

Rather than silently changing the examples, I document relevant differences in [`DIFFERENCES.md`](DIFFERENCES.md), including:

- What the instructor demonstrates.
- What I changed to make it work in Odoo 19.
- Why the change was necessary, where I can establish the reason.

This process helps me understand the framework rather than simply copy working code. It also creates a practical reference for developers following older Odoo tutorials with newer versions.

## How I Work

| Principle | Approach |
|---|---|
| **One commit per section** | Each completed course section gets its own commit and, where appropriate, a Git tag such as `section-04`. |
| **Type, understand, rebuild** | I type the examples, experiment with them, and practise rebuilding the functionality without relying on the lecture. |
| **Odoo 19.0 target** | I implement the course examples against Odoo 19.0 and document relevant version differences. |
| **Document the learning** | I record meaningful compatibility changes in `DIFFERENCES.md`. |
| **Consistent commits** | Commit messages follow a format such as `section-04: add computed fields and onchange (19.0 port)`. |

## Course Progress

**Course:** 14 sections, 63 lectures, approximately 10.5 hours. The course page lists June 2024 as its last update.

| # | Section | Status |
|---:|---|:---:|
| 1 | Introduction | ✅ |
| 2 | Setting up the Odoo Development Environment & Understanding the Foundation | ✅ |
| 3 | Creating your First Odoo Application | ✅ |
| 4 | In-depth Understanding of Models and Logic | ✅ |
| 5 | In-depth Understanding of Views | ✅ |
| 6 | Expanding on Security: Groups, Access Rights and Record Rules | 🟨 |
| 7 | Understanding Automation, Actions and Reports | ⬜ |
| 8 | Internationalization (i18n and `.po` files) | ⬜ |
| 9 | Getting Advanced with Mixins and Useful Classes | ⬜ |
| 10 | Working with Emails and Templates | ⬜ |
| 11 | Logic and View Inheritance | ⬜ |
| 12 | Working with XML-RPC, JSON-RPC and Web Controller | ⬜ |
| 13 | Miscellaneous | ⬜ |
| 14 | Odoo Cloud Hosting for Custom Deployment | ⬜ |

**Legend:** ⬜ Not started · 🟨 In progress · ✅ Completed

**Certificate of completion:** Pending. I will add the certificate link after completing the course.

## Repository Structure

```text
.
├── README.md
├── DIFFERENCES.md
└── <module_name>/
    ├── __manifest__.py
    ├── models/
    ├── views/
    ├── security/
    └── ...
```

`DIFFERENCES.md` records relevant differences between the course examples and my Odoo 19 implementation. The module directory contains the application built throughout the course and grows as I complete each section.

## Running the Code

### Prerequisites

- Odoo 19.0
- Python version supported by Odoo 19.0 (for native installations)
- PostgreSQL version supported by Odoo 19.0
- Docker Engine and Docker Compose (for the containerized setup)

### Option 1: Docker Compose

My development environment uses Docker Compose, with Odoo and PostgreSQL running in separate containers.

From the directory containing `docker-compose.yml`, run:

```bash
docker compose exec odoo-app odoo \
  -c /etc/odoo/odoo.conf \
  -r <odoo-database-user> \
  -d <odoo-database> \
  -u <module_name> \
  --addons-path=/usr/lib/python3/dist-packages/odoo/addons,/mnt/extra-addons \
  --stop-after-init
```

Replace the placeholders with your database credentials, database name, and module's technical name. Ensure the module is already installed before using `-u` to update it.

My local configuration mounts custom addons at `/mnt/extra-addons`. The standard addons path shown above is specific to my Docker image; verify it if you use a different image or configuration.

To install a module for the first time, replace `-u` with `-i`:

```bash
docker compose exec odoo-app odoo \
  -c /etc/odoo/odoo.conf \
  -r <odoo-database-user> \
  -d <odoo-database> \
  -i <module_name> \
  --addons-path=/usr/lib/python3/dist-packages/odoo/addons,/mnt/extra-addons \
  --stop-after-init
```

### Option 2: Native Installation with a Python Virtual Environment

For developers running Odoo from source with a Python virtual environment, activate the environment and run the following from the Odoo source directory:

```bash
./odoo-bin \
  -c odoo.conf \
  -d course_db \
  -i <module_name> \
  --addons-path=<path-to-odoo-addons>,<path-to-this-repo>,<path-to-other-custom-addons> \
  --stop-after-init
```

Replace the example paths with the actual paths on your machine. Include the standard Odoo addons directory and any directories containing the custom modules you need.

Use `-i` to install a module for the first time or `-u` to update an installed module.

**Note:** `--stop-after-init` makes Odoo exit after initialization and the requested operation. It is useful for development and troubleshooting, but it does not leave the web server running afterward.

## Viewing Previous Sections

Each section is tracked through Git. To inspect the repository at a particular section, use its tag:

```bash
git checkout section-04
```

This checks out the tagged commit in a detached HEAD state. To continue development, return to your working branch:

```bash
git switch main
```

Replace `main` if your default branch has a different name.

## Related Work

- [equipment_loan_tracker](https://github.com/chikechiagbaizu/equipment_loan_tracker) — An independent Odoo module featuring computed fields, constraints, a wizard, and record-level security.

## Credits and Disclaimer

- **Instructor:** Miracle Ayodele, creator of the Udemy course.
- **Course:** [The Complete Odoo 16/17 Technical Course: From Zero to Hero](https://www.udemy.com/course/the-complete-odoo-technical-course-2023-from-zero-to-hero/).
- This repository is an independent learning project. It is not affiliated with, endorsed by, or sponsored by the instructor or Udemy.
- The course curriculum and instruction belong to their respective owner. This repository documents my own learning and Odoo 19 adaptations.
- My original code is licensed under LGPL-3. This does not automatically relicense third-party materials or grant rights to redistribute course content.

## Author

**Chike Chiagbaizu**
