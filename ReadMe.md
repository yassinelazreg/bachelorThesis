# Introduction

This repository contains the code I used to generate the speech data for my bachelor thesis dealing with "The Effect of Duration and Pitch in Social Perceptions of Synthetic Speech". Moreover, files containing the results obtained from the listening test conducted are included. 


# Speech Generation
- 2 synthetic voices (1 male and 1 female) were used for the speech synthesis. To achieve this, the Google Cloud text-to-speech API was used. The code used can be found in the "main.py" file.
- The Google Cloud text-to-speech API (https://cloud.google.com/text-to-speech) allows pitch and speaking rate manipulation.

### Duration Manipulation
- For each voice a speech sample was generated with normal speaking rate (speaking_rate=1) and increased/decreased speaking rate by 20/50 percent.
- 2 sentences from the Harvard database (https://www.cs.columbia.edu/~hgs/audio/harvard.html) were used as text_input: *"It was a bad error on the part of the new judge. The streets are narrow and full of sharp turns."*.

### Pitch Manipulation
- Each speech sample was generated with normal pitch (pitch=0) and increased/decreased pitch by 6/15 semitones (without affecting the tempo).
- 2 sentences from the Harvard database (https://www.cs.columbia.edu/~hgs/audio/harvard.html) were used as text_input: *"Clothes and lodging are free to new men. Four hours of steady work faced us."*.

Accordingly, for each voice 10 different speech samples with different speaking rates (5 files) and different pitches (5 files) were generated.

Note: Two additional speech samples for the control questions were generated. The first one contains: *"For this question, please select rating 1 for all attributes."*. and the second: *"For this question, please select rating 4 for all attributes."*


------------

# Survey Results
A listening test with the altered speech samples was carried out to study the effects of the manipulation on the speech perception. 
- The raw data obtained from the survey is in the rawData.xlsx file. The file contains the 117 collected responses.
- In the categorized_raw_data.xlsx file, the raw data is organized (answers are categorized by speech sample and attributes).

PS: In speech sample 9 (SS9) participants were asked to choose rating 1 for all attributes and in SS21 they were asked to choose rating 4 for all attributes. these two questions were used to clean the data. 

- In the cleanedResults.xlsx file, the answers of participants who had failed at least one of the control questions were deleted. In the end, 66 answers were kept. There are 3 tables in this file. In the first one, the answers of female and male speakers are presented. The second contains only the answers of male participants and the third table contains the answers of female listeners. In the lower part of each table, the average age of the participants and the MOS for each attribute and dimension are calculated.

- The calculations performed in the previous files were used to create diagrams. These can be found in the diagramsData.xlsx file. The graphs representing the profile of the respondents (distribution by gender, age, and English level) can be found on the left side. On the right side, the calculated MOS were used to visualize the effects of the pitch and speaking rate manipulations on warmth and competence ratings. This was also done three times (all participants vs. female participants vs. male participants). 









