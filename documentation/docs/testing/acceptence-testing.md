---
sidebar_position: 3
---
# Acceptance test

All acceptance tests are in `tests/test_acceptance.py` and use FastAPI's `TestClient` to simulate full user scenarios.

> Note: Automated tests simulate the grading step only. Speech-to-text input is tested manually (see Manual Tests section below).
## Acceptance Test for Use Case 1 - Admin creates quiz

An admin logs in with the wrong password and receives a failure message.

**Details**
- Runs `test_admin_can_login`
- Passes if all tests pass.

## Acceptance Test for Use Case 2 - Learner watches video and answers quiz

A learner opens the app, selects a quiz, and answers a question correctly using voice.

Upon opening the app, the config loads successfully.
The learner speaks their answer and receives confirmation it is correct.

**Details**
- Runs `test_student_loads_app_and_answers_correctly`
- Passes if all tests pass.

## Acceptance Test for Use Case 3 - Learner answers a question using voice

A learner mispronounces their answer slightly but the system still accepts it using fuzzy matching.

The system records the learner's voice, transcribes it, and grades the answer.
Even with a mispronunciation, the system correctly marks the answer as correct.

**Details**
- Runs `test_student_misspells_pikachu_and_still_gets_correct`
- Runs `test_student_answers_spinning_cat_question`
- Passes if all tests pass.

## Manual Tests

These scenarios require a real browser and microphone and were tested manually.

### Student speaks answer into microphone
1. Open the app in a browser
2. Navigate to a video with a quiz question
3. Click the microphone button and say the answer out loud
4. Observe that the speech is transcribed into the answer field
5. Observe that the result shows "correct" or "wrong"

**Observed Result:** Passed , speech was correctly transcribed and graded.