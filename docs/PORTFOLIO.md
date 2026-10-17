# Lillie US portfolio map

Updated 17 October 2026. [Portfolio hub](https://github.com/Ibekwemmanuel7/Lillie_US).

| Product | Sector and responsibility | Current status | Hub integration |
|---|---|---|---|
| [VHAGAR](https://github.com/Ibekwemmanuel7/VHAGAR) | Wildfire intelligence | Research code; Southern validation separate | Pinned Python dependency |
| [Vaughan](https://github.com/Ibekwemmanuel7/vaughan) | Hurricanes, flood and coastal impacts | Hurricane research; flood/coastal expansion planned | Pinned Python dependency |
| [Vulcan](https://github.com/Ibekwemmanuel7/Vulcan) | Mineral prospectivity, mineral rights and permits | Prospectivity research; rights/permits expansion planned | Pinned Git submodule |
| [Vantage](https://github.com/Ibekwemmanuel7/Vantage) | Southern US agriculture | Initial market and scope designed | Documentation reference only |
| [Vepris](https://github.com/Ibekwemmanuel7/Vepris) | Southern US forestry | Scope designed | Documentation reference only |
| [Viga](https://github.com/Ibekwemmanuel7/Viga) | Oil-spill detection | Awaiting owner-led code separation | Documentation reference only |
| [Velo](https://github.com/Ibekwemmanuel7/Velo) | Water intelligence | Scope designed | Documentation reference only |


## Ownership boundaries

- **VHAGAR:** wildfire and burned-area methods, with validation and release limits retained.
- **Vaughan:** existing hurricane research plus planned event flood and coastal-impact intelligence. Flood observation, coastal change, asset exposure and recovery need their own implementation and references.
- **Vulcan:** existing mineral-prospectivity research plus planned mineral-rights and permit records, linked document geometry and activity review. Prospectivity scores do not establish title or permission.
- **Vantage:** farmer/adviser workflows, initially cotton scouting support in the Texas High Plains. No CropSight migration or inherited validation.
- **Vepris:** forestry, timberland condition, harvesting/replanting and sector recovery decisions; it can consume reviewed hazard outputs.
- **Viga:** oil-spill investigation workflows after the owner separates the relevant code from LillieWatch. No extraction performed by this portfolio work.
- **Velo:** routine water resources, reservoir/surface-water histories, watershed context and locally validated quality/bloom screening. Water safety and chemical conclusions require suitable reference measurements.

## Status discipline

An existing repository is not proof of a ready Southern US product. Current code and proposed scope are labelled separately in every product's `docs/portfolio/SCOPE.md`. The catalogue's `reference_commit` pins that reviewed documentation. `source_commit`, where present, identifies the code reference actually consumed by the hub.

Vulcan is the only actual Git submodule today. VHAGAR and Vaughan are pinned Python dependencies. The other four products are documented repository references. This is a deliberate integration policy, not an incomplete attempt to turn every repository into a submodule.

## Shared platform and customer workflows

Lillie US is the intended home for shared asset/parcel identity, tenant access, evidence provenance, review queues, reporting, customer integrations and coordinated release criteria. These are design responsibilities; a shared production platform is not created by the portfolio map.

Landowner evidence, insurance, lending and infrastructure customers can consume outputs from several products. They do not each require a new repository unless a distinct reusable codebase and delivery need emerge. Methane/emissions and specialist subsidence products remain potential gaps outside the seven current domain briefs.

## Next implementation decisions

1. Preserve each research product's evaluation limits and commit provenance.
2. Define one bounded customer decision and reference dataset for each new or expanded scope before implementation.
3. Complete owner-led Viga separation before selecting a runtime integration.
4. Implement only the shared interfaces needed by actual pilots; keep product dependencies acyclic.
5. Advance code pins only after checks appropriate to their changes. Scope documents alone cannot pass a scientific or operational gate.

See [repository strategy](REPOSITORY_STRATEGY.md) and [proposed interfaces](INTERFACES.md).
