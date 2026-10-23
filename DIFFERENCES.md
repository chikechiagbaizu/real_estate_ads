# Odoo 16/17 (Course) vs Odoo 19.0 (Mine)

A running log of differences I encounter while following Miracle Ayodele's Odoo 16/17 technical course using Odoo 19.0.

This document records compatibility issues, required code changes, and environment differences as I progress through the course.

**How to read each entry:** What the course demonstrates → what I use in Odoo 19.0 → why the difference matters.

> **Status guide**
>
> - **Confirmed:** Reproduced or verified against Odoo 19.0.
> - **To verify:** A potential version difference that I have not yet tested.
> - **Not applicable:** The difference does not affect my implementation.

## Known Changes to Investigate

The following are potential compatibility differences to check as I reach the relevant sections. They are not confirmed findings until I test them against Odoo 19.0.

| Area | Course version | Odoo 19.0 to investigate | Section | Status |
|---|---|---|---|---|
| View modifiers | `attrs` in Odoo 16; direct modifiers in Odoo 17 | Direct expressions such as `invisible="state == 'done'"` | 4, 5 | Confirmed |
| List view tag | `<tree>` | `<list>` | 3, 5 | Confirmed |
| SQL constraints | `_sql_constraints` | `models.Constraint` class attributes | 4 | Confirmed |
| Client-side actions | Legacy JavaScript widgets / early OWL components | Current OWL-based APIs and component patterns | 7 | To verify |

**Note:** Version history provides useful clues, but actual findings should be based on reproducible tests or the Odoo 19.0 source code and documentation.

## Log by Section

### Section 1: Introduction

No code differences encountered.

### Section 2: Environment Setup

This course uses **Docker Compose** to run Odoo 19.0 and PostgreSQL 15 in separate containers.

| Component | Configuration |
|---|---|
| Odoo image | `odoo:19.0` |
| PostgreSQL image | `postgres:15-alpine` |
| Python | Bundled with the Odoo image |
| Access URL | `http://localhost:8070` |
| Configuration file | `odoo.conf`, mounted into the container |
| Custom addons | `./custom_addons` → `/mnt/extra-addons` |
| Persistent storage | Docker named volumes for Odoo and PostgreSQL data |
| Development options | `--dev=all`, `--workers=0` |

**Docker Compose vs native installation**

In a native installation, Odoo, its Python dependencies, and PostgreSQL are installed and managed directly on the host operating system. With Docker Compose, Odoo and PostgreSQL run in separate containers, reducing host-level dependency management and helping maintain a reproducible environment.

Odoo connects to the PostgreSQL service using the Compose hostname `web-db`, rather than `localhost`.

**Environment-specific note:** The commands and paths used in this repository reflect my Docker Compose configuration. Developers running Odoo from source with a Python virtual environment must adapt the configuration file, database connection settings, and addons paths to their own environment.

### Section 3: Creating the First Odoo Application

**Confirmed difference: List view root element**

- **Course (Odoo 16/17):** `<tree>`
- **My implementation (Odoo 19.0):** `<list>`
- **Reason:** Odoo 19.0 uses `<list>` as the root element for list views.
- **Impact:** Update the view XML when porting older course examples to Odoo 19.0.

No other version-related differences were encountered in this section.

### Section 4: In-depth Understanding of Models and Logic

**Topics covered:** Relational fields, notebook/page elements, basic widgets, ORM decorators, transient models, and abstract models.

#### Confirmed differences

**1. View modifiers: `attrs` removed**

- **Course (Odoo 16):** Uses `attrs` to define conditional view behavior, such as invisibility and read-only states.
- **My implementation (Odoo 19.0):** Uses direct modifier expressions, for example, `invisible="state == 'done'"`.
- **Reason:** The legacy `attrs` and `states` view attributes were removed in newer Odoo versions.
- **Impact:** Older XML view definitions using these attributes must be adapted.

**2. List view element: `<tree>` replaced by `<list>`**

- **Course (Odoo 16/17):** Uses `<tree>` as the list-view root element.
- **My implementation (Odoo 19.0):** Uses `<list>`.
- **Reason:** Odoo uses `<list>` as the root element for list views.
- **Impact:** Older list-view XML definitions must be updated when porting them to Odoo 19.0.

No other version-related differences were encountered in this section.

### Section 5: Understanding Odoo Views

**Topics covered:** Search, Kanban, Pivot, Graph, Gantt, and Calendar views.

#### Confirmed differences

**1. List view element: `tree` replaced by `list`**

- **Course (Odoo 16):** May use `<tree>` as the root element for list views.
- **My implementation (Odoo 19.0):** Uses `<list>`.
- **Reason:** Odoo 19.0 uses `<list>` as the root element for list views.
- **Impact:** Older XML view definitions using `<tree>` must be adapted when porting to Odoo 19.0.

No other version-related differences were encountered in this section.

### Section 6: Groups, Access Rights, and Record Rules

**Topics covered:** User groups, access control lists (ACLs), model access rights, record rules, and group-based security.

#### Confirmed differences

**1. Group creation: Privilege category introduced in the workflow**

- **Course (Odoo 16/17):** Groups can be created and configured without the additional Privilege creation step used in my Odoo 19.0 workflow.
- **My implementation (Odoo 19.0):** I needed to create a **Privilege** under a category before creating the group.
- **Reason:** Odoo 19.0 organizes group configuration using the newer Privileges and Groups interface, where privileges help organize access rights and associate groups with application features.
- **Impact:** When configuring security in Odoo 19.0, I need to understand the relationship between categories, privileges, and groups rather than following the older group-creation workflow directly.

---

*This document will be updated as I progress through the course. Only tested or source-verified findings will be marked as confirmed.*
