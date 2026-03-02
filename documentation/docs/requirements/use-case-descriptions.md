---
sidebar_position: 5
---

# Use-case descriptions

## Use Case 1 - Admin creates quiz
*As a parent or administrator, I want to generate a quiz for the child to use.*
1. After logging in, the admin selects the 'Administrator' option on the 'Choose your role' page.
2. The app prompts the admin and the admin uploads a video.
3. The system processes the video and generates a quiz.
4. The administrator approves the quiz to be completed by the child.

## Use Case 2 - Learner watches video and answers quiz
*As a child, I want to watch a video and interact with questions based on how the admin configured my session.*
1. The child opens the app and sees available videos.
2. The child selects a video.
3. The system loads the video with the interaction mode configured by the admin.
4. The child selects "Start."
5. The system begins playing the video.

## Use Case 3 - Learner answers a question using voice
*As a user, I want to answer quiz questions using my voice and have my answer scored moments later.*
1. The system displays a question and prompts the user to speak their answer.
2. The system automatically starts to record and the user speaks their answer.
3. The system records the audio and converts it into text.
4. The system displays the recognized answer.
5. The user confirms the answer, and the system saves it and moves to the next question.

**Alternate flow**: If the system cannot recognize the speech clearly, the user is prompted to retry speaking.


## Use Case 4 - Child interacts with video questions
*As a child, I want to interact with video questions based on the mode my admin configured.*

1. The system plays the video and pauses at a question timestamp.
2. The system displays a question based on the admin-configured mode:
   - **Answer required:** The child must answer before the video continues.
   - **Skip allowed:** The child can answer or press “Skip” to continue watching.
   - **Auto-play:** No question is shown; the video plays straight through.
3. If answering, the child speaks their answer using voice input.
4. The system evaluates the answer and shows whether it is correct or incorrect.
5. The video resumes from where it paused.

**Alternate flow:** If the answer is incorrect and the mode allows it, the system offers “Rewind Video” to replay the relevant segment before continuing.

## Use Case 5 - Parental report
*As a parent or guardian, I want to check on my child's progress to be able to make adjustments as necessary.*
1. After logging in, the admin selects the 'Administrator' option on the 'Choose your role' page.
2. The admin clicks on the 'Dashboard' button.
3. The admin views a page containing Piggyback's results, including response scores, time watched, and other insights.
4. The admin views a page containing Piggyback's results, including response scores, time watched, and other insights.

## Use Case 6 - Expert review
*As a parent or guardian, I want to be able to review and modify the quizzes for my child.*
1. After logging in, the admin selects the 'Expert Reviewer' option on the 'Choose your role' page.
2. The screen displays the quizzes that the admin has created and approved.
3. The admin selects one of the quizzes to be reviewed.
4. The admin selects a timestamp with a question and rewinds slightly to look through the video.
5. The admin makes changes to the question as needed.
6. Once done with the whole quiz, the admin saves the quiz for the child to be able to select again.

## Use Case 7 - Admin configures child's learning conditions
*As an admin, I want to set how a child interacts with the video so I can customize their learning experience.*
1. Admin logs into the admin panel.
2. Admin selects a child or session.
3. Admin chooses the interaction mode: "Answer to continue," "Skip allowed," or "Auto-play."
4. System saves the settings and applies them when the child opens the app.
