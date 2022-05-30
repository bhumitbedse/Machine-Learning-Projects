from chatterbot import ChatBot  
from chatterbot.trainers import ListTrainer
import spacy 
spacy.load('en_core_web_sm')
# from spacy.lang.en import English
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot('<b>BVM BOT</b>')

# nlp = spacy.load("en_core_web_sm")

chatbot = ChatBot(
    'ChatBot for BVM College Enquiry',
    # storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch', 
            'default_response': "Hi there, Welcome to BVM! 👋 If you need any assistance, I'm always here.Go ahead and write the number of any query. 😃✨<b><br><br>  Which of the following user groups do you belong to? <br><br>1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br><br>",
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'   
) 
trainer = ListTrainer(chatbot)

# python app.py
# Training with Personal Ques & Ans 
conversation = [
"Hi",
"Helloo!",
"Hey",

"How are you?",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"Great",
"Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"good",
"Go ahead and write the number of any query. 😃✨ <br> 2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"fine",
"Go ahead and write the number of any query. 😃✨ <br> 2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"Thank You",
"Your Welcome 😄",

"Thanks",
"Your Welcome 😄",

"Bye",
"Thank You for visiting!..",

"What do you do?",
"I am made to give Information about Fr. BVM college.",

"What else can you do?",
"I can help you know more about Fr. BVM",
    
    "1",
    "<b>STUDENT <br>The following are frequently searched terms related to student . Please select one from the options below : <br> <br> 1.1 Curriculars <br>1.2  Extra-Curriculars<br>1.3  Administrative<br>1.4 Examination <br>1.5 Placements </b>",
    
    "1.1",
    "<b>  CURRICULAR <br>  These are the top results: <br> <br> 1.1.1 Academic Calendar <br> 1.1.2 Syllabus </b>",
    "1.1.1",
    "<b > 1.1.1 Academic Calender<br>The link to Academic Calender👉<a href=" 'https://www.bvmengineering.ac.in/comman_page1.aspx?page_id=95' ">Click Here</a> </b>",
    "1.1.2",
    "<b> 1.1.2 Syllabus<br>The link to Syllabus 👉 <a href=" 'https://www.bvmengineering.ac.in/syllabi/UG1920/CP/B.Tech.%20CP%20Structure-18-19.pdf '">Click Here</a> </b>",

    "1.2",
    "<b>EXTRA-CURRICULAR<br>These are the top results: <br> <br> 1.2.1 Events<br> 1.2.2 Day Celebration <br> 1.2.3 Udaan</b> <br>1.2.4 Student's Corner",
    "1.2.1",
    "<b > 1.2.1 Events<br>The link to Events👉 <a href=" 'https://www.bvmengineering.ac.in/comman_page1.aspx?page_id=2134' ">Click Here</a></b>",
    "1.2.2",
    "<b > 1.2.2 Day celebration<br>The link to Day Celebration👉<a href=" 'https://www.flickr.com/photos/195084262@N04/sets/72177720296897017/ '">Click Here</a> </b>",
    "1.2.3",
    "<b > 1.2.3 Udaan <br>The link to Udaan👉 <a href=" 'https://www.bvmengineering.ac.in/comman_page1.aspx?page_id=3188' ">Click Here</a> </b>",
    "1.2.4",
    "<b > 1.2.4 Student's Corner <br>The link to Student's Corner👉 <a href=" 'https://bvmengineering.ac.in/Student%20Corner/Student%20Corner.pdf' ">Click Here</a> </b>",

    "1.3",
    "<b>1.3 ADMINISTRATIVE<br>These are the top results: <br>  1.3.1 Notices </b>",
    "1.3.1",
    "<b> 1.3.1 Notices<br>The link to Notices👉 <a href=" 'https://www.bvmengineering.ac.in/NDashboard.aspx?notice_type=All-Notice' ">Click Here</a> </b>",

    "1.4",
    "<b > EXAMINATION <br>These are the top results:<br> 1.4.1 Notices<br> 1.4.2 Examination Process <br> 1.4.3 Question Paper Archive </b>",
    "1.4.1",
    "<b > 1.4.1 Notices<br>The link to Notices👉 <a href=" 'https://www.bvmengineering.ac.in/NDashboard.aspx?notice_type=Examination-Notice'">Click Here</a> </b>",
    "1.4.2",
    "<b > 1.4.2 Question Paper Archive<br>The link to Archives👉 <a href=" 'https://bvmengineering.ac.in/Exam%20papers/Exam%20Papers.pdf' ">Click Here</a> </b>",

    "1.5",
    "<b > PLACEMENTS These are the top results:<br> 1.5.1 Placements<br> 1.5.2 Placement Statistics<br> 1.5.3 campus placement eligibility </b>",
    "1.5.1",
    "<b> 1.5.1 Placements<br>The link to Placements👉 <a href=" 'https://www.bvmengineering.ac.in/Placement%20Details%20of%20Past%20Years/BVM_Placement%20Brochure_2020-21.pdf' ">Click Here</a> </b>",
    "1.5.2",
    "<b > 1.5.2 Placement Statistics<br>The link to Placement Statistics👉 <a href=" 'https://www.bvmengineering.ac.in/comman_page1.aspx?page_id=4' ">Click Here</a> </b>",
    "1.5.3",
    "<b > 1.5.3 Campus Placement Eligibility<br>The link to Campus Placement Eligibilty👉 <a href=" 'https://www.bvmengineering.ac.in/documents/2_campus%20placement%20eligibility.PDF' ">Click Here</a> </b>",

    "2",
    "<b >FACULTY<br>The following are frequently searched terms related to faculty. Please select one from the options below :</br></br>2.1 Faculty Details<br>2.2  Change Personal Details </b>",
    
    "2.1",
    "<b > Faculty Details These are the top results:<br> 2.1.1 Faculty Details </b>",
    "2.1.1",
    "<b> 2.1.1 Faculty Details<br>The link to Faculty Details👉<a href=" 'https://www.bvmengineering.ac.in/faculty_info.aspx?branch_id=3' ">Click Here</a> </b>",

    "2.2",
    "<b > CHANGE PERSONAL DETAILS These are the top results:<br> <br> 2.2.1 Site Login <br> </b>",
    "2.2.1",
    "<b> 2.2.1 Site Login<br>The link to Site Login👉<a href=" 'https://erp.bvmengineering.ac.in/' ">Click Here</a> </b>",
   
    "3",
    "<b> PARENTS <br>The following are frequently searched terms related to Parents. Please select one from the options below : <br> <br> 3.1 About Us <br>3.2 Notices <br>3.3 Fee Payment <br>3.4 Placements </b> " ,

    "3.1",
    "<b > ABOUT US<br>These are the top results:<br> <br> 3.1.1 About BVM<br> </b>",
    "3.1.1",
    "<b > 3.1.1 About BVM<br>The link to About BVM👉 <a href=" 'https://www.bvmengineering.ac.in/comman_page1.aspx?page_id=2' ">Click Here</a> </b>",
   

    "3.2",
    "<b > NOTICES<br>These are the top results:<br> <br> 3.2.1 All Notices  </b>",
    "3.2.1",
    "<b > 3.2.1 All Notices <br>The link to All Notices👉 <a href=" 'https://www.bvmengineering.ac.in/NDashboard.aspx?notice_type=All-Notice'  ">Click Here</a> </b>",

    "3.3",
    "<b > Fee Payment<br>These are the top results:<br> <br>3.3.1 Payment Details <br> 3.3.2 Online Payment Portal </b>",
    "3.3.1",
    "<b > 3.3.1 Payment Details<br>The link to Payment Details 👉 <a href=" 'https://bvmengineering.ac.in/comman_page1.aspx?page_id=1130' ">Click Here</a> </b>",
    "3.3.2",
    "<b > 3.3.2 Payment Portal <br>The link to Payment Portal👉<a href=" 'https://www.eduqfix.com/PayDirect/#/student/pay/3Ipcn74cqZEFIZnqw1aGYEroaWMzY3LuPhsKem2KqLQLoyZ1wuK76jn1rudOAy9i/4576' ">Click Here</a> </b>",

    "3.4",
    "<b > PLACEMENTS These are the top results:<br> 1.5.1 Placements<br> 1.5.2 Placement Statistics<br> 1.5.3 campus placement eligibility </b>",
    "3.4.1",
    "<b> 3.4.1 Placements<br>The link to Placements👉 <a href=" 'https://www.bvmengineering.ac.in/Placement%20Details%20of%20Past%20Years/BVM_Placement%20Brochure_2020-21.pdf' ">Click Here</a> </b>",
    "1.5.2",
    "<b > 3.4.2 Placement Statistics<br>The link to Placement Statistics👉 <a href=" 'https://www.bvmengineering.ac.in/comman_page1.aspx?page_id=4' ">Click Here</a> </b>",
    "1.5.3",
    "<b > 3.4.3 Campus Placement Eligibility<br>The link to Campus Placement Eligibilty👉 <a href=" 'https://www.bvmengineering.ac.in/documents/2_campus%20placement%20eligibility.PDF' ">Click Here</a> </b>",

    "4",
    "<b VISITORS <br>The following are frequently searched terms related to visitors. Please select one from the options below : <br> <br> 4.1 About Us<br>4.2 Programs We Offer <br>4.3 Student Bodies <br></b>",
    
    "4.1",
    "<b > ABOUT US<br>These are the top results:<br> <br>4.1.1 About BVM</b>",
    "4.1.1",
    "<b > 4.1.1 About BVM<br>The link to About BVM👉 <a href=" 'https://www.bvmengineering.ac.in/comman_page1.aspx?page_id=2' ">Click Here</a> </b>",
    
    "4.2",
    "<b > PROGRAMS WE OFFER <br>These are the top results:<br> <br>4.2.1 Under-Graduate <br> 4.2.2 Post-Graduate<br> 4.2.3 Ph.D </b>",
    "4.2.1",
    "<b > 4.2.1 Under-Graduate<br>The link to Under-Graduate👉 <a href=" 'https://www.bvmengineering.ac.in/comman_page1.aspx?page_id=5' ">Click Here</a> </b>",
    "4.2.2",
    "<b > 4.2.2 Post-Graduate <br>The link to Post-Graduate👉<a href=" 'https://www.bvmengineering.ac.in/comman_page1.aspx?page_id=6' ">Click Here</a> </b>",
    "4.2.3",
    "<b > 4.2.3 Ph.D <br>The link to Ph.D👉 <a href="' https://bvmengineering.ac.in/PhdSection.aspx?page_id=3183' ">Click Here</a> </b>",

    "4.3",
    "<b>EXTRA-CURRICULAR<br>These are the top results: <br> <br> 4.3.1 Events<br> 4.3.2 Day Celebration <br> 4.3.3 Udaan</b> <br>4.3.4 Student's Corner",
    "4.3.1",
    "<b > 4.3.1 Events<br>The link to Events👉 <a href=" 'https://www.bvmengineering.ac.in/comman_page1.aspx?page_id=2134' ">Click Here</a></b>",
    "4.3.2",
    "<b > 4.3.2 Day celebration<br>The link to Day Celebration👉<a href=" 'https://www.flickr.com/photos/195084262@N04/sets/72177720296897017/ '">Click Here</a> </b>",
    "4.3.3",
    "<b > 4.3.3 Udaan <br>The link to Udaan👉 <a href=" 'https://www.bvmengineering.ac.in/comman_page1.aspx?page_id=3188' ">Click Here</a> </b>",
    "4.3.4",
    "<b > 4.3.4 Student's Corner <br>The link to Student's Corner👉 <a href=" 'https://bvmengineering.ac.in/Student%20Corner/Student%20Corner.pdf' ">Click Here</a> </b>",    

]

trainer.train(conversation)
