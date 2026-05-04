def test_get_activities_returns_all_activities_with_expected_shape(client):
    # Arrange
    expected_count = 9

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert len(payload) == expected_count

    sample_activity = payload["Chess Club"]
    assert "description" in sample_activity
    assert "schedule" in sample_activity
    assert "max_participants" in sample_activity
    assert "participants" in sample_activity
    assert isinstance(sample_activity["participants"], list)
