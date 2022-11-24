2 synthetic voices (1 male and 1 female) were used to generate synthetic speech.
To achieve this, the Google Cloud text-to-speech API was used.
the code can be found in the "main.py" file.

The google cloud text-to-speech api allows pitch and speaking rate manipulation.

- Duration shifting:
For each voice a speech sample was generated with normal speaking rate (speaking_rate=1), increased/decreased speaking rate by 20/50 percent.
2 sentences from the Harvard database were used as text_input: "It was a bad error on the part of the new judge. The streets are narrow and full of sharp turns."

- Pitch Shifting:
each speech sample was generated with normal pitch (pitch=0), increased/decreased pitch by 6/15 semitones (without affecting the tempo).
2 sentences from the Harvard database were used as text_input: "Clothes and lodging are free to new men. Four hours of steady work faced us."

-> Accordingly, for each voice 10 different speech samples with different speaking rates (5 files) and different pitches (5 files) were generated.


Note: two additional speech samples for the control questions were generated. The first one contains: "For this question, please select rating 1 for all attributes.". and the second: "For this question, please select rating 4 for all attributes."
