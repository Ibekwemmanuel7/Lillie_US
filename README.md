# Lillie US

Integration project for Southern US satellite intelligence. The scientific code stays in its upstream repositories and is installed through exact Git commit references.

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

No Lillie US application package is shipped yet. The project currently provides integration metadata; source code is not copied or vendored.

## Update a pin

Review and validate the chosen upstream commit, then update its full SHA in both `pyproject.toml` and `source-pins.json`, and update the table above. Commit the coordinated change. Branch names and moving tags are not accepted as source pins.

Local planning documents are maintained separately and are not part of the initial dependency-pinning commit.
