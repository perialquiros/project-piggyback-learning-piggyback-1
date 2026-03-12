from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

#pokemon video
def test_student_misspells_pikachu_and_still_gets_correct():
    # Student knows the answer but misspells it slightly
    response = client.post("/api/check_answer", json={
        "expected": "pikachu",
        "user": "pikahu",
        "question": "what is the name of this yellow pokemon"
    })

   # App should still accept close enough answers
    assert response.status_code == 200
    assert response.json()["status"] == "correct"
    
#Spinning cat video
def test_student_answers_spinning_cat_question():
    # Student watches the O I I A I spinning cat video
    # and is asked what the cat is doing
    response = client.post("/api/check_answer", json={
        "expected": "spinning",
        "user": "spinning",
        "question": "what is the cat doing"
    })
    # Student gets it right
    assert response.status_code == 200
    assert response.json()["status"] == "correct"


def test_admin_can_login():
    # Use Case 1: Admin logs in to access the admin panel
    response = client.post("/api/verify-password", data={
        "user_type": "admin",
        "password": "wrongpassword"
    })
    # Even wrong password returns 200, just with success: false
    assert response.status_code == 200


def test_student_loads_app_and_answers_correctly():
    # App loads
    config_response = client.get("/api/config")
    assert config_response.status_code == 200

    # Learner answers correctly
    answer_response = client.post("/api/check_answer", json={
        "expected": "cat",
        "user": "cat",
        "question": "what animal is in the video"
    })
    assert answer_response.status_code == 200
    assert answer_response.json()["status"] == "correct"


#childrens

from uuid import uuid4

def test_admin_can_create_child_profile():
    # Admin creates an expert first
    expert_id = f"exp_{uuid4().hex[:8]}"
    client.post("/api/admin/experts", json={
        "expert_id": expert_id,
        "display_name": "Test Expert",
        "password": "pass123"
    })

    # Admin creates a child linked to that expert
    resp = client.post("/api/admin/children", json={
        "expert_id": expert_id,
        "first_name": "Emma",
        "last_name": "Smith",
        "icon_key": "pig"
    })
    assert resp.status_code == 200
    child = resp.json()["child"]
    assert child["first_name"] == "Emma"
    assert child["expert_id"] == expert_id
    # child_id should be a 6-digit string
    assert len(child["child_id"]) == 6
    assert child["child_id"].isdigit()


def test_learner_enters_expert_id_and_sees_children():
    # Admin sets up expert + child
    expert_id = f"exp_{uuid4().hex[:8]}"
    client.post("/api/admin/experts", json={
        "expert_id": expert_id,
        "display_name": "Test Expert",
        "password": "pass123"
    })
    client.post("/api/admin/children", json={
        "expert_id": expert_id,
        "first_name": "Liam",
        "last_name": "Jones",
        "icon_key": "rabbit"
    })

    # Learner enters expert ID and gets child list
    resp = client.get(f"/api/learners/experts/{expert_id}/children")
    assert resp.status_code == 200
    children = resp.json()["children"]
    assert any(c["first_name"] == "Liam" for c in children)


def test_learner_cannot_see_inactive_child():
    # Admin creates expert + child, then deactivates the child
    expert_id = f"exp_{uuid4().hex[:8]}"
    client.post("/api/admin/experts", json={
        "expert_id": expert_id,
        "display_name": "Test Expert",
        "password": "pass123"
    })
    create_resp = client.post("/api/admin/children", json={
        "expert_id": expert_id,
        "first_name": "Noah",
        "last_name": "Brown",
        "icon_key": "fox"
    })
    child_id = create_resp.json()["child"]["child_id"]
    client.post(f"/api/admin/children/{child_id}/deactivate")

    # Learner should NOT see the deactivated child
    resp = client.get(f"/api/learners/experts/{expert_id}/children")
    assert resp.status_code == 200
    children = resp.json()["children"]
    assert not any(c["child_id"] == child_id for c in children)


def test_admin_cannot_create_duplicate_child_under_same_expert():
    # Admin creates expert + child
    expert_id = f"exp_{uuid4().hex[:8]}"
    client.post("/api/admin/experts", json={
        "expert_id": expert_id,
        "display_name": "Test Expert",
        "password": "pass123"
    })
    client.post("/api/admin/children", json={
        "expert_id": expert_id,
        "first_name": "Ava",
        "last_name": "Wilson",
        "icon_key": "bear"
    })

    # Creating the exact same child again should fail
    dupe_resp = client.post("/api/admin/children", json={
        "expert_id": expert_id,
        "first_name": "Ava",
        "last_name": "Wilson",
        "icon_key": "owl"
    })
    assert dupe_resp.status_code != 200


def test_child_video_list_scoped_to_expert_assignments():
    # A child with an unlinked expert should return empty video list
    expert_id = f"exp_{uuid4().hex[:8]}"
    client.post("/api/admin/experts", json={
        "expert_id": expert_id,
        "display_name": "Test Expert",
        "password": "pass123"
    })
    create_resp = client.post("/api/admin/children", json={
        "expert_id": expert_id,
        "first_name": "Mia",
        "last_name": "Davis",
        "icon_key": "alligator"
    })
    child_id = create_resp.json()["child"]["child_id"]

    # Expert has no assigned videos, so child should see none
    resp = client.get(f"/api/learners/children/{child_id}/videos")
    assert resp.status_code == 200
    assert resp.json()["videos"] == []
