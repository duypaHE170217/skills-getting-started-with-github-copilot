from src.app import activities


def test_get_activities_returns_seeded_data(client):
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data
    assert "participants" in data["Chess Club"]
    assert isinstance(data["Chess Club"]["participants"], list)


def test_get_activities_matches_in_memory_store(client):
    response = client.get("/activities")

    assert response.status_code == 200
    assert response.json().keys() == activities.keys()
