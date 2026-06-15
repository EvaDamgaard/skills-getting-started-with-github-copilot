def test_unregister_removes_existing_participant(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity}/participants", params={"email": email}
    )
    activities_response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Removed {email} from {activity}"}
    assert email not in activities_response.json()[activity]["participants"]


def test_unregister_fails_for_missing_participant(client):
    # Arrange
    activity = "Chess Club"
    email = "not.in.club@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity}/participants", params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found in this activity"


def test_unregister_fails_for_missing_activity(client):
    # Arrange
    missing_activity = "Astronomy Club"
    email = "student@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{missing_activity}/participants", params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
