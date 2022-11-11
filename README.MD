# Django QUIZ

## Technical requirements
### Web-UI
  1. Registration
      - [x] registration (with email confirmation)
      - [x] authorization
      - [x] password change
      - [x] passwrod reset

  2. User capability
      - [ ] take any test
      - [ ] go through the test questions (one by one)
      - [ ] completing a pending test
      - [ ] deleting an incomplete test
      - [ ] viewing results

  3. After test completion
      - [ ] report about the number of correct and wrong answers
      - [ ] percantage of correct answers

### Admin site
  1. [ ] User administartion
  2. [ ] Test administration
      - [ ] add test
      - [ ] modify a test
      - [ ] deleting a test
      - [ ] test validation
        - [ ] you cannot save a question:
            - [ ] without indicating the correct answer
            - [ ] in which all answers are correct
        - [ ] test cannot be saved if:
            - [ ] order_num is incorrect (should be between 1 and 100 and incremented by 1)
            - [ ] the maximal order_num value is a less than the maximal allowed number of questions
            - [ ] number of questions less than 3 or more than 100

### Additional requirements
1. [x] Project must be on Git
2. [x] The requirements.txt file must be present
3. [x] venv
4. [ ] PostgreSQL
5. [ ] Availability of data dump
6. [x] bootstrap
7. [ ] API + Tests
8. [ ] Docker image
9. [ ] Caching
10. [ ] Scheduler
11. [ ] Deploy to Amazon

## DB - Schema
![db](db_schema.jpg)
