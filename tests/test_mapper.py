from odyssey_corporate_world_map import map_corporate_sites

def test_map_corporate_sites():
    c = map_corporate_sites("383474814")
    assert c.result["total"] > 0
    assert c.confidence > 0.9
