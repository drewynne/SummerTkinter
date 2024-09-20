# Summer Arithmetic Trainer
Summer is an arithmetic trainer designed to adapt to the user's abilities.

It measures the user's reaction times to various questions and scales the question difficulty accordingly.

## Start Difficulty

At the start of the game the difficulty can be selected within a range of 1 to 10. 
- This sets the time allowed for each question to within the range of 3.5s to 35s. 
- This also sets a bias towards addition and subtraction for low difficulties and a bias towards multiplication and division for high difficulties. There is no bias for medium difficulties.

## Consciousness Threshold

Within the code a constant named **consciousness_threshold** is defined as 3.5s. This is, approximately, how long it takes to answer the question from memory with little conscious effort. 

Here each problem can be broken into 3 steps: 
1. Reading the question.
2. Calculating the answer.
3. Submitting the answer.

Reading and interpreting the question in this arithmetic game is almost trivial as there are only four operators. Though it should be noted that mistakes often occur from misreading the question when trying to answer too quickly. I assume that correctly reading the question could take up to 0.5s.

Calculating the answer is where most of the time is used within these arithmetic problems. allowing at least 1 to 2s for this is probably where most people can answer a question they already know the answer to (from memory). Much longer can be required for more challenging problems.

Submitting the answer is also somewhat trivial but on a touch screen it can take up to 0.5s to press the right number and then the submit button.


