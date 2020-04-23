<h2>Overview</h2>
<p>
This repository is an automatic reminder application for various documents needed for the international students for our university. A system where students in the institution gets reminders as messages or E-mail, where the students data is to be kept updated in an excel file. Application automatically fetches the data and sends reminders everyday to the selected students.
</p>
<h2>Instructions</h2>
<p> 1.The excel sheet must contain following rows with exact names:<br>
    &ensp;&ensp;&ensp;&ensp;a."name of student"      #shows the name of the student<br>
    &ensp;&ensp;&ensp;&ensp;b."frro 1(rc/rp) start"  #gives start date of the rc/rp process<br>
    &ensp;&ensp;&ensp;&ensp;c."frro 2(rc/rp) start"<br>
    &ensp;&ensp;&ensp;&ensp;d."frro 3(rc/rp) start"<br>
    &ensp;&ensp;&ensp;&ensp;e."frro 4(rc/rp) start"<br>
    &ensp;&ensp;&ensp;&ensp;f."contact number"<br>
    &ensp;&ensp;&ensp;&ensp;g."email"<br>
    2. Names of all the students whose process is going on will be saved in data.json file<br>
    3.If any frro row contain no entries ; for the moment make it as 0000-00-00 i.e as a dummy entry
</p>
<h2>Algorithm</h2>
<p>
1. Script triggers every day at a specific time<br>
2. Check if database is updated. <br>
3. Fetch the database from excel file from cloud. <br>
4. Take the 'frro student date' from the the database.<br>
5. Start the scheduling for 1,2,3,8,9,10 day for the all the students and will send messages to all those students on those specific days.<br>
6. Make the scheduling for same students on 11th month as the same students will have to do the same process after 11 months.<br>
</p>
<br>
<img src="/FRRO_flow diagram.JPG">
<br>
<h2>Libraries needed</h2>
    <i> <p>
        &ensp;&ensp;&ensp;&ensp;1. schedule<br>
        &ensp;&ensp;&ensp;&ensp;2. gspread<br>
        &ensp;&ensp;&ensp;&ensp;3. oauth2client<br>
        &ensp;&ensp;&ensp;&ensp;4. twilio<br>
    </i> </p>
  
<h4> Run the program using <b>main_program.py</b> </h4>

<h2>Developers</h2> 
<p>
    <i>
        &ensp;&ensp;&ensp;&ensp;Harsh Patel <br>
        &ensp;&ensp;&ensp;&ensp;Vatsal Mistry 
    </i>
</p>
