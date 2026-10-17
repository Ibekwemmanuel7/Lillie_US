# Lillie US

Integration project for Southern US satellite intelligence. VHAGAR and Vaughan are installed through exact upstream Git commit references. Vulcan is the mineral research component, included as a commit-pinned Git submodule under `modules/ml_mineral`.

## Product responsibilities

| Component | Domain | Integration status |
|---|---|---|
| VHAGAR | Wildfire and burned-area methods | Commit-pinned Python dependency |
| Vaughan | Hurricane research | Commit-pinned Python dependency |
| Vulcan | Mineral-prospectivity research | Commit-pinned Git submodule |
| [Vantage](https://github.com/Ibekwemmanuel7/Vantage) | Southern US agriculture and farmer/adviser workflows | Design stage; no source commit pinned |
| [Vepris](https://github.com/Ibekwemmanuel7/Vepris) | Southern US forestry and timberland-management workflows | Design stage; documentation revision recorded |
| [Viga](https://github.com/Ibekwemmanuel7/Viga) | Oil-spill detection | Awaiting owner-led separation from LillieWatch; no source commit pinned |

Vepris owns the proposed forest-condition, harvest, replanting, storm-disturbance and recovery workflows. It may consume VHAGAR fire products later; this interface is not implemented. Vantage remains focused on agriculture. Planned repositories are recorded separately in `source-pins.json` and are not installed by the project.

Viga is the dedicated oil-spill detection project. Its owner will separate the relevant code from LillieWatch. Once that source is published and reviewed, Lillie US can pin a specific Viga commit and select its integration method. Registration does not copy LillieWatch code or establish detection performance.

## Pinned dependencies

| Package | Repository | Commit |
|---|---|---|
| VHAGAR | [VHAGAR](https://github.com/Ibekwemmanuel7/VHAGAR) | `42ffa5afeb6d358108a3c4d1f962d9b8747ae3af` |
| Vaughan | [vaughan](https://github.com/Ibekwemmanuel7/vaughan) | `095374d4e74fa7c6125165460599b9270f21ece7` |

`pyproject.toml` contains the installable dependency references. `source-pins.json` records the same source revisions for inspection. These pins do not lock transitive packages or establish Southern validation or operational readiness.

## Install

Requires Python 3.11 or later and Git. From the repository root, create and activate a virtual environment, then run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install .
```

Vaughan requires PyTorch and other scientific dependencies, so installation can be substantial. The VHAGAR reference installs its core dependencies; optional geospatial, archive and serving extras should be selected when the corresponding workflow is implemented.

No unified Lillie US application package is shipped yet. VHAGAR and Vaughan remain external dependencies. Vulcan runs from its own directory so its existing `src` and `scripts` imports do not collide with other components.

## Mineral research component

[Vulcan](https://github.com/Ibekwemmanuel7/Vulcan) contains the reusable experimental mineral-prospectivity framework. Lillie US tracks a specific Vulcan commit at `modules/ml_mineral`; `source-pins.json` records the same commit as the Git submodule entry.

Clone this repository with its pinned submodule:

```powershell
git clone --recurse-submodules https://github.com/Ibekwemmanuel7/Lillie_US.git
```

For an existing checkout:

```powershell
git submodule update --init --recursive
```

See [Vulcan setup and scientific scope](modules/ml_mineral/README.md) and [integration notes](modules/ml_mineral/INTEGRATION.md). Vulcan is not installed by `pip install .`; use its dedicated environment. Existing configurations target Nigerian geology and require Southern US adaptation and validation.

To advance Vulcan, review and test the desired upstream commit, check out that exact SHA inside `modules/ml_mineral`, update its entry in `source-pins.json`, and commit both the submodule pointer and manifest in Lillie US. Ordinary submodule initialisation uses the recorded commit, not the latest upstream branch.

## Update a Python dependency pin

For VHAGAR or Vaughan, review and validate the chosen upstream commit, then update its full SHA in both `pyproject.toml` and `source-pins.json`, and update the table above. Commit the coordinated change. Branch names and moving tags are not accepted as source pins. Vulcan uses the submodule update procedure above.

Local planning documents are maintained separately and are not part of the initial dependency-pinning commit.
