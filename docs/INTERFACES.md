# Proposed cross product interfaces

Status: portfolio design. These contracts are not implemented APIs or a new shared Python package.

## Ownership

| Producer | Proposed output | Consumer and decision |
|---|---|---|
| VHAGAR | Reviewed fire events and burned-area evidence | Vepris forestry recovery; Vantage farm impact; shared evidence reports |
| Vaughan | Observed or modelled event flood/coastal layers, explicitly distinguished | Vantage, Vepris, Viga and asset managers prioritising inspections |
| Velo | Routine water-resource, watershed and water-quality screening context | Vaughan event analysis; Vantage farm water context; Vepris watershed context |
| Vulcan | Prospectivity research outputs and separately reviewed rights/permit records | Mineral consultants and land/asset review workflows |
| Viga | Spill candidates and reviewed spill-investigation evidence | Environmental consultants and land/asset review workflows |
| Vantage | Crop-zone observations and adviser review outcomes | Farmers and crop consultants |
| Vepris | Stand-change observations and forester review outcomes | Timberland managers and forestry consultants |

Vaughan leads event floods and coastal impacts. Velo leads ongoing water-resource and quality context. Vantage and Vepris own their sector's management decisions. Viga owns spill detection; a flood exposure layer does not establish a release. Vulcan separates prospectivity evidence from mineral-rights and permit interpretation.

## Minimum evidence envelope to design

Each exchanged record should identify schema version, producing product and code/configuration version, stable record and revision IDs, geometry and coordinate reference system, observation interval, upstream availability where known, processing time, source identifiers and provenance, quality/coverage, uncertainty method, review outcome and superseded versions.

Keep observations, model inference, reported third-party information and human conclusions distinct. Explicitly represent unavailable, stale and unresolved evidence. A zero flag or empty result must not silently mean that a property is safe, unaffected or compliant.

Private asset geometry, declared burns, customer documents and assessments require explicit tenant and access scope. Public products must not leak private context through shared event conclusions. Match data retention and redistribution to source terms and customer agreements.

Define units and spatial/temporal tolerances per output. Do not impose one sensor resolution, confidence threshold or latency promise on all seven domains. Interfaces must be validated against the consuming decision before release.
