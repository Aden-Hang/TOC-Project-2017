# TOC Project 2017

Template Code for TOC Project 2017

A telegram bot based on a finite state machine

## FSM
![](https://i.imgur.com/JFQvhsi.png)


## State
* start(initial state)
* hi
* hello
* goodmorning
* plan
* study
* no_plan
* sleep
* n_d
* n_o
* s_d
* s_o

## 流程說明
* 首先進入 start (initial state)
    * 使用者輸入 "Hi" --> Bot 回答 "Hi! What are the plans for today?" 並且傳送一張黑人問號的圖
    * 使用者輸入 "Hello" --> Bot 回答 "Hello! What are the plans for today?" 並且傳送一張黑人問號的圖
    * 使用者輸入 "Goodmorning" --> Bot 回答 "Goodmorning! What are the plans for today?" 並且傳送一張黑人問號的圖
* 之後直接進入 plan 來進行等待使用者回答
    * 使用者輸入 "I have no plan" --> Bot 進入 no_plan 並且回答 "How about go outside and have fun with friends?" 
    * 使用者輸入 "I am going to study" --> Bot 進入 study 並且回答 "Are you kidding me!?" "There is no word call "study" in your dictionary><" 傳送一個嘲笑的圖後回答 "Do you want to get some comics for yourself?"
    * 使用者輸入 "I am going to go to sleep" --> Bot 進入 sleep 並且回答 "Alright, goodbye"
* study state
    * 使用者輸入 "No, I do not like to read comic books" --> Bot 進入 s_d 並且回答 "So, what do you want to do" 
    * 使用者輸入 "Good idea" --> Bot 進入 s_o 並且回答 "You can get them on the third floor"
* no_plan state
    * 使用者輸入 "Outside is raining, I prefer to stay inside" --> Bot 進入 n_d 並且回答 "So, what do you want to do"
    * 使用者輸入 "Ok, see you soon" --> Bot 進入 n_o 並且回答 "Have fun! See you soon~"
* sleep state
    * 直接回到 start state
* s_d state
    * 直接回到 plan state 
* s_o state
    * 直接回到 start state 
* n_d state
    * 直接回到 plan state
* n_o state
    * 直接回到 start state
