# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aqtxARyTakx7O7ZZSdZWowJp6Dz8k1Re
"""

import pandas as pd
baza={
    "FISH":[   "Qadamova Zulayho", "Xalilov Durbek", "Jo'rayeva Gulnoza","Jo'rayeva Gulnoza" , "Djalilov Mamatisa", "Arabboyev Alisher"  ],
    "Fan nomi":[   "Sun'iy intellekt", "Sun'iy intellekt" , "Elektronika va sxemalar" ,"Elektronika va sxemalar", "Kompyuterni tashkil etish" ,"Kiberxavfsizlik"   ],
    "Mashg'ulot turi":[ "Amaliy", "ma'ruza" ,"Ma'ruza" , "Amaliy", "Ma'ruza", "Amaliy"  ],
    "Kafedrasi":[ "Axborot texnalogiyalari", "Axborot texnalogiyalari", "Tabiiy fanlar","Tabiiy fanlar", "Kompyuter injineringi va suniy intellekt", "Axborot texnalogiyalari"]

}
db=pd.DataFrame(baza)
print(db)

db.to_excel("o'qituvchilar.xlsx")