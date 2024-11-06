import html

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }




question= trivia["question"]
correct= trivia["correct_answer"]
incorrect1= trivia["incorrect_answers"][0]
incorrect2= trivia["incorrect_answers"][1]
incorrect3= trivia["incorrect_answers"][2]



c1 = html.unescape(correct)

wq1 = html.unescape(incorrect1)
wq2 = html.unescape(incorrect2)
wq3 = html.unescape(incorrect3)
print(f'Incorrect:\n {wq1}\n {wq2}\n {wq3}')
print(f'Correct:\n {c1}')
print(question)

#question = trivia["question"]



#incorrect1 = print(trivia["incorrect_answers"][0])
#print(html.unescape(incorrect1))

#correct = trivia["correct_answer"]
#incorrect1 = trivia["incorrect_answers"][0]
#incorrect2 = trivia["incorrect_awswers"][0]

#print(incorrect2)




answer = input(question)
