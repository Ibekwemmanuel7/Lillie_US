# Repository strategy

Lillie US uses independent product repositories with an integration hub. Each product can evolve, be tested and be released independently. Every product README links back to Lillie US; the hub links to all seven products and records their implementation status and reviewed revisions.

## What a sub repository means here

GitHub repositories remain independent. A portfolio relationship is expressed through links, domain ownership and the hub registry. A Git submodule is a particular integration mechanism: it checks out another repository inside the parent and records one exact commit. It is not required to make a project part of the company portfolio. See the [Git submodule documentation](https://git-scm.com/book/en/v2/Git-Tools-Submodules) and [GitHub repository documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories).

## Selected integration policy

| Situation | Mechanism | Current products |
|---|---|---|
| Packaged Python code consumed by the hub | Dependency pinned to a full commit; later a tested release may be used | VHAGAR and Vaughan |
| Research source needed locally but not yet packaged | Git submodule pinned to a full commit | Vulcan at `modules/ml_mineral` |
| Scope and roadmap without a runtime implementation | Independent repository linked from the registry; documentation revision recorded | Vantage, Vepris, Viga and Velo |

Do not add a second copy of a product to Lillie US. Do not add a submodule solely for visual uniformity, and do not install an unimplemented project as a dependency. When Vulcan is packaged and tested, it may move to a package dependency in a separately reviewed migration.

## Repository responsibilities

**Product repository:** reusable domain methods, code, tests, documentation, examples, source-data adapters and scientific validation protocols.

**Lillie US:** portfolio map, source pins, cross-product configuration and interfaces, coordinated release criteria, and future shared tenant, asset, review, audit and reporting services. These shared services are architectural responsibilities, not a claim that they are already implemented.

Scientific source repositories must not depend on the Lillie US application merely to appear in its portfolio. Links are bidirectional; runtime dependencies should remain acyclic.

## Status and version discipline

`portfolio.json` is the product catalogue and domain-ownership register. `source-pins.json` records installed source pins and documentation references. `pyproject.toml` declares the actual Python dependencies; `.gitmodules` and the Git tree declare the actual submodule. `scripts/validate_portfolio.py` checks agreement between the files.

A product's `reference_commit` identifies the reviewed portfolio documentation. Its `source_commit` identifies the runtime or source checkout used by the hub, where one exists. These can differ: a documentation update must not silently advance a scientific dependency and imply revalidation. The previous VHAGAR and Vaughan runtime pins are preserved during this portfolio documentation change. Vulcan's submodule advances to the reviewed scope-documentation commit; its model and application source is unchanged.

For a code-pin update: review the diff, run checks appropriate to the change, commit upstream first, then update the hub's installation reference and registry together. Never use a moving branch as a source pin. A successful source test suite does not itself establish Southern US accuracy, a customer service level, or legal/engineering conclusions.

## Operational boundaries

Keep datasets, credentials, customer records, trained model artefacts and generated outputs out of routine source commits. Store and distribute them using the applicable access and licence arrangements. Do not choose repository publicity or transfer ownership without a separate explicit decision.

This arrangement does not merge repositories, rename existing packages, move the original local research folders, change licence ownership or extract LillieWatch code. Viga's extraction remains owner-led.
