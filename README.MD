# Django QUIZ

## Technical requirements
### Web-UI
  1. Registration
      - [x] registration (with email confirmation)
      - [x] authorization
      - [x] password change
      - [x] passwrod reset

  2. User capability
      - [x] take any test
      - [x] go through the test questions (one by one)
      - [x] completing a pending test
      - [x] deleting an incomplete test
      - [x] viewing results

  3. After test completion
      - [x] report about the number of correct and wrong answers
      - [x] percantage of correct answers

### Admin site
  1. [x] User administartion
  2. [x] Test administration
      - [x] add test
      - [x] modify a test
      - [x] deleting a test
      - [ ] test validation
        - [x] you cannot save a question:
            - [x] without indicating the correct answer
            - [x] in which all answers are correct
        - [x] test cannot be saved if:
            - [x] order_num is incorrect (should be between 1 and 100 and incremented by 1)
            - [x] the maximal order_num value is a less than the maximal allowed number of questions
            - [x] number of questions less than 3 or more than 100

### Additional requirements
1. [x] Project must be on Git
2. [x] The requirements.txt file must be present
3. [x] venv
4. [ ] PostgreSQL
5. [x] Availability of data dump
6. [x] bootstrap
7. [x] Unit Test
8. [ ] API + Tests
9. [ ] Docker image
10. [ ] Caching
11. [ ] Scheduler
12. [ ] Deploy to Amazon

## DB - Schema
![db](db_schema.jpg)
