quiz = {
    "quesriona 1": {
        "question": "what is the capital of Jharkhand?",
        "answer": "ranchi"
    },
    "questiona 2":{
    "question": "what is the capital of Karala?",
    "answer": "thiruvananthapuram"
    },
    "questiona 3":{
    "question": "what is the capital of Bihar?",
    "answer": "patna"
    },
    "questiona 4":{
    "question": "what is the capital of Uttar Pradesh?",
    "answer": "lucknow"
    },
    "questiona 5":{
    "question": "what is the capital of Himachal Pradesh?",
    "answer": "shimla"
    },
    "questiona 6":{
    "question": "what is the capital of Uttarakhand?",
    "answer": "dehradun"
    },
    "questiona 7":{
    "question": "what is the capital of Rajasthan?",
    "answer": "jaipur"
    },
    "questiona 8":{
    "question": "what is the capital of Tamil Nadu?",
    "answer": "chennai"
    }   
}
 
score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")
    
    if answer.lower() == value['answer'].lower():
        print('corract 👍')
        score = score + 1
        print("your score is:" + str(score))  
        print("")
        print("")
    else:
        print("wrong!👎🫣")
        print("The answer is:" + value['answer']) 
        print("your score is:" + str(score))
        print("")
        print("")
print("you got"+ str(score)+ "out of 8 question corractlly")   
print(("your percentage is " + str(int(score/8 *100)) + "% 🥳👏"))
