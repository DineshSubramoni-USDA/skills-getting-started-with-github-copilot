from src.app import activities, get_activities, signup_for_activity


def test_conservation_club_is_available():
    conservation_club = get_activities()["Conservation Club"]

    assert "habitat restoration" in conservation_club["description"]
    assert "wildlife monitoring" in conservation_club["description"]
    assert conservation_club["max_participants"] == 15


def test_student_can_sign_up_for_conservation_club(monkeypatch):
    conservation_club = activities["Conservation Club"]
    monkeypatch.setitem(conservation_club, "participants", [])

    response = signup_for_activity(
        "Conservation Club", "student@mergington.edu"
    )

    assert conservation_club["participants"] == ["student@mergington.edu"]
    assert response == {
        "message": "Signed up student@mergington.edu for Conservation Club"
    }
