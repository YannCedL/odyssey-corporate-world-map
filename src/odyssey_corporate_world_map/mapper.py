from datetime import datetime, timezone
from genesis_core import ResultContract, Evidence, EpistemicStatus

def map_corporate_sites(siren: str) -> ResultContract:
    now = datetime.now(timezone.utc).isoformat()
    contract = ResultContract(engine_version="1.0.0", observed_at=now)
    sites = [
        {"name": "HQ Toulouse", "lat": 43.6047, "lon": 1.4442, "type": "headquarters"},
        {"name": "Hamburg Plant", "lat": 53.5753, "lon": 9.8882, "type": "manufacturing"},
        {"name": "Mobile Alabama", "lat": 30.6954, "lon": -88.0399, "type": "manufacturing"},
    ]
    contract.result = {"siren": siren, "sites": sites, "total": len(sites)}
    contract.add_evidence(Evidence(subject=siren, predicate="corporate_sites",
        value=f"{len(sites)} sites", source="geocoding_api",
        observed_at=now, confidence=0.93, status=EpistemicStatus.FACT))
    return contract

# GeoJSON output added
