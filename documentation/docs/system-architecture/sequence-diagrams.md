---
sidebar_position: 6
---

# Sequence Diagrams

## Use case 1 - Admin creates quiz

```mermaid
sequenceDiagram
    participant Admin
    participant App
    participant System

    Admin->>App: Log in
    App->>Admin: Display 'Choose your role'
    Admin->>App: Select 'Administrator'
    App->>Admin: Prompt to upload video
    Admin->>App: Upload video
    App->>System: Process video & generate quiz
    System-->>App: Quiz generated
    Admin->>App: Approve quiz
    App-->>System: Quiz ready for child
```

## Use case 2 - Learner watches the video and answers quiz

```mermaid
sequenceDiagram
    participant Child
    participant App
    participant System
    
    Child->>App: Open app
    App->>Child: Display available videos
    Child->>App: Select a video
    App->>System: Load video with admin-configured mode
    System-->>App: Video and mode ready
    Child->>App: Start
    App->>Child: Begin playing video
```

## Use case 3 - Learner answers a question using voice

```mermaid
sequenceDiagram
    participant User
    participant App
    participant System
    participant Speech

    App->>User: Display question, prompt to speak
    User->>App: Speak answer
    App->>Speech: Record audio
    Speech-->>App: Convert speech to text
    App->>User: Show recognized answer
    User->>App: Confirm answer
    App->>System: Save answer, move to next question
    alt Speech not recognized
        App->>User: Prompt to retry speaking
    end
```

## Use case 4 - Child interact with video questions

```mermaid
sequenceDiagram
    participant Child
    participant App
    participant System
    participant Video

    Child->>App: Start video
    App->>Video: Play video
    Video-->>App: Pause at question timestamp
    alt Answer required
        App->>Child: Display question, must answer to continue
        Child->>App: Speak answer
        App->>System: Evaluate answer
        System-->>App: Correct, resume video
    else Keep going allowed
        App->>Child: Display question
        Child->>App: Speak answer
        App->>System: Evaluate answer
        alt Answer incorrect
            App->>Child: Show "Rewind Video" or "Keep Going"
            alt Rewind Video
                App->>Video: Rewind to timestamp
                Video-->>Child: Play segment
            else Keep Going
                App->>Video: Resume video
            end
        end
    else Auto-play
        App->>Video: Continue playing, no question shown
    end
    
```

## Use case 5 - Parental report

```mermaid
sequenceDiagram
    participant Admin
    participant App
    participant System

    Admin->>App: Log in
    App->>Admin: Display 'Choose your role'
    Admin->>App: Select 'Administrator'
    Admin->>App: Click 'Dashboard'
    App->>System: Fetch child results
    System-->>App: Send scores, time watched, insights
    App-->>Admin: Display report
```

## Use case 6 - Expert review

```mermaid
sequenceDiagram
    participant Admin
    participant App
    participant System
    participant Video

    Admin->>App: Log in
    App->>Admin: Display 'Choose your role'
    Admin->>App: Select 'Expert Reviewer'
    App->>Admin: Show created/approved quizzes
    Admin->>App: Select quiz to review
    App->>Video: Rewind to timestamp for question
    Admin->>App: Modify question as needed
    App->>System: Save updated quiz
    System-->>App: Quiz ready for child selection
```

## Use case 7 - Admin configures child's learning conditions

```mermaid
sequenceDiagram
    participant Admin
    participant App
    participant System

    Admin->>App: Log in
    App->>Admin: Display admin panel
    Admin->>App: Select a child or session
    App->>Admin: Show current settings
    Admin->>App: Choose interaction mode
    App->>System: Save mode configuration
    System-->>App: Settings saved
    App-->>Admin: Confirmation displayed
```