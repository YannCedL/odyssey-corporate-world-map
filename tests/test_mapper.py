# test de la cartographie mondiale Odyssey
from odyssey_corporate_world_map.mapper import map_corporate_sites

def test_map_corporate_sites():
    contract = map_corporate_sites("383474814")
    assert contract is not None
    assert len(contract.result["sites"]) >= 1
    assert len(contract.evidence) >= 1
