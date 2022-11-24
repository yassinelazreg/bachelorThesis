4 synthetic voices (2 males and 2 females) were used to generate synthetic speech.
To achieve this google cloud text-to-speech API was used.
The google cloud text-to-speech api allows pitch and speaking rate manipulation.

- Duration shifting:
For each voice a speech sample was generated with normal speaking rate (speaking_rate=1), increased/decreased speaking rate by 20/50 percent.
2 sentences from the Harvard database were used as text_input: "It was a bad error on the part of the new judge. The streets are narrow and full of sharp turns."

- Pitch Shifting:
each speech sample was generated with normal pitch (pitch=0), increased/decreased pitch by 6/15 semitones (without affecting the tempo).
2 sentences from the Harvard database were used as text_input: "Clothes and lodging are free to new men. Four hours of steady work faced us."

-> Accordingly, for each voice 10 different speech samples with different speaking rates (5 files) and different pitches (5 files) were generated.

Note: The files have been converted to video files so that they can be embedded in the questionnaire. (Audio files cannot be embedded in Google forms and other survey tools).

Note: A controlQuestion file was generated as a control question for the survey. It contains following sentence: "For this question, please select rating 1 for all attributes.".
