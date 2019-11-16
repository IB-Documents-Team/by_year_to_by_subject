import shutil, os

# Written originally by batmansmaster, intended to be run by templarknight98.
# Some new modifications such as additions and deletions by templarknight98.
# Create this folder --> D:\International Baccalaureate Documents\IB PAST PAPERS - SUBJECT\
# Probaly best you go to line 33 now and go the copying file function later once it gets called

# copying file function

def copyingfile():
    # checking for language of paper
    paperslanguages = ["Spanish", "German", "French"]  # other languages which may appear for subject groups 3-6
    paperslanguage = "English"  # setting it to english since that is the most common one

    # check to see if other languages of the papers exist and creates separate folders for them, at least for group 3-6
    if (Group == Group3 or Group == Group4 or Group == Group5 or Group == Group6):
        for paperlanguage in paperslanguages:
            if paperlanguage in file_in_dir:
                paperslanguage = paperlanguage
    movingto = "D:\International Baccalaureate Documents\IB PAST PAPERS - SUBJECT\\" + Groupname + "\\" + Subject + "_" + subjectLevel + "\\" + session + " " + str(
        year) + " Examination Session\\" + paperslanguage + " Papers\\"

    # could have used an else, but this is used so it causes an error if it
    if (Group == Group1 or Group == Group2):
        movingto = "D:\International Baccalaureate Documents\IB PAST PAPERS - SUBJECT\\" + Groupname + "\\" + Subject + "_" + subjectLevel + "\\" + session + " " + str(
            year) + " Examination Session\\"
    # actually copying files
    # the if not statment is to ignore .DS_store files on mac
    if not (file_in_dir).startswith('.'):
        # this is to create the directory if it does not exist
        if not os.path.exists(movingto):
            os.makedirs(movingto)
        # finally the file is copied
        shutil.copy(workingdirectory + Groupname + "\\" + file_in_dir, movingto)


# all the years for past papers you want to organize, from 1991 to...
years = ["1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"]

# These are ALL the Group 1 subjects from 1991 to 2019.
Group1 = ["Afrikaans_A1", "Afrikaans_A_Literature", "Akan_A1", "Albanian_A1", "Albanian_A_Literature", "Amharic_A1", "Amharic_A_Literature", "Arabic_A1", "Arabic_A_Language_and_literature", "Arabic_A_Literature", "Aremenian_A1", "Armenian_A_Literature", "Assyrian_A_Literature", "Azerbaijani_A1", "Azerbaijani_A_Literature", "Belarusian_A1", "Belarusian_A_Literature", "Belarussian_A1", "Bemba_A1", "Bemba_A_Literature", "Bengali_A1", "Bengali_A_Literature", "Bosnian_A1", "Bosnian_A_Literature", "Bulgarian_A1", "Bulgarian_A_Literature", "Burmese_A1", "Burmese_A_Literature", "Catalan_A1", "Catalan_A_Literature", "Chichewa_A1", "Chichewa_A_Literature", "Chinese_A1", "Chinese_A_Language_and_literature", "Chinese_A_Literature", "Croatian_A1", "Croatian_A_Literature", "Czech_A1", "Czech_A_Literature", "Danish_A1", "Danish_A_Literature", "Dhivehi_A1", "Dhivehi_A_Literature", "Dutch_A1", "Dutch_A_Language_and_literature", "Dutch_A_Literature", "Dzongkha_A1", "Dzongkha_A_Literature", "English_A1", "English_A_Language_and_literature", "English_A_Literature", "Estonian_A1", "Estonian_A_Literature", "Faroese_A1", "Faroese_A_Literature", "Filipino_A_Literature", "Finnish_A1", "Finnish_A_Literature", "French_A1", "French_A_Language_and_literature", "French_A_Literature", "Galician_A1", "Georgian_A1", "Georgian_A_Literature", "German_A1", "German_A_Language_and_literature", "German_A_Literature", "Greenlandic_A1", "Greenlandic_A_Literature", "Greenlandic_A_literature", "Gujarati_A1", "Hebrew_A1", "Hebrew_A_Literature", "Hindi_A1", "Hindi_A_Literature", "Hungarian_A1", "Hungarian_A_Literature", "Icelandic_A1", "Icelandic_A_Literature", "Igbo_A_Literature", "Indonesian_A1", "Indonesian_A_Language_and_literature", "Indonesian_A_Literature", "Irish_A_Literature", "Italian_A1", "Italian_A_Language_and_literature", "Italian_A_Literature", "Japanese_A1", "Japanese_A_Language_and_literature", "Japanese_A_Literature", "Kannada_A1", "Karen_A1", "Kazakh_A1", "Kazakh_A_Literature", "Khmer_A1", "Khmer_A_Literature", "Kinyarwanda_A1", "Kinyarwanda_A_Literature", "Korean_A1", "Korean_A_Language_and_literature", "Korean_A_Literature", "Kurdish_A_Literature", "Lao_A1", "Lao_A_Literature", "Latvian_A1", "Latvian_A_Literature", "Literature_and_performance", "Lithuanian_A1", "Lithuanian_A_Literature", "Luganda_A1", "Luganda_A_Literature", "Macedonian_A1", "Macedonian_A_Literature", "Malagasy_A_Literature", "Malay_A1", "Malay_A_Literature", "Malayalam_A1", "Maori_A1", "Maori_A_Literature", "Marathi_A1", "Marathi_A_Literature", "Modern_Greek_A1", "Modern_Greek_A_Language_and_literature", "Modern_Greek_A_Literature", "Mongolian_A1", "Mongolian_A_Literature", "Ndebele_A1", "Ndebele_A_Literature", "Nepali_A1", "Nepali_A_Literature", "Norwegian_A1", "Norwegian_A_Language_and_literature", "Norwegian_A_Literature", "Oriya_A1", "Oromo_A1", "Oromo_A_literature", "Oshikwanyama_A1", "Pashto_A1", "Pashto_A_Literature", "Persian_A1", "Persian_A_Literature", "Pilipino_A1", "Polish_A1", "Polish_A_Literature", "Portuguese_A1", "Portuguese_A_Language_and_literature", "Portuguese_A_Literature", "Punjabi_A1", "Punjabi_A_Literature", "Q'eqchi_A1", "Romanian_A1", "Romanian_A_Literature", "Rumantsch_A", "Rumantsch_A_Literature", "Russian_A1", "Russian_A_Language_and_literature", "Russian_A_Literature", "Serbian_A1", "Serbian_A_Literature", "Sesotho_A1", "Sesotho_A_Literature", "Setswana_A1", "Setswana_A_literature", "Shona_A1", "Shona_A_Literature", "Sinhalese_A1", "Sinhalese_A_Literature", "Siswati_A1", "Siswati_A_Literature", "Slovak_A1", "Slovak_A_Literature", "Slovene_A1", "Slovene_A_Literature", "Somali_A1", "Somali_A_Literature", "Spanish_A1", "Spanish_A_Language_and_literature", "Spanish_A_Literature", "Swahili_A1", "Swahili_A_Literature", "Swedish_A1", "Swedish_A_Language_and_literature", "Swedish_A_Literature", "Tajik_A1", "Tajik_A_Literature", "Tajik_A_literature", "Tamil_A1", "Tamil_A_Literature", "Telugu_A1", "Telugu_A_Literature", "Telugu_A_literature", "Text_and_performance", "Thai_A1", "Thai_A_Language_and_literature", "Thai_A_Literature", "Tibetan_A1", "Tibetan_A_Literature", "Tigrinya_A1", "Tigrinya_A_Literature", "Tonga_A1", "Turkish_A1", "Turkish_A_Language_and_literature", "Turkish_A_Literature", "Ukrainian_A1", "Ukrainian_A_Literature", "Urdu_A1", "Urdu_A_Literature", "Uzbek_A1", "Vietnamese_A1", "Vietnamese_A_Literature", "Welsh_A1", "Welsh_A_Literature", "Xhosa_A1", "Yoruba_A1", "Zulu_A1", "Zulu_A_Literature"]

# These are ALL the Group 2 subjects from 1991 to 2019.
Group2 = ["Afrikaans_B", "Arabic_A2", "Arabic_B", "Arabic_ab_initio", "Bengali_B", "Cantonese_B", "Chinese_A2", "Classical_Greek", "Danish_B", "Dutch_A2", "Dutch_B", "English_A2", "English_B", "English_ab_initio", "Finnish_B", "French_A2", "French_B", "French_ab_initio", "German_A2", "German_B", "German_ab_initio", "Hebrew_B", "Hindi_B", "Hindi_ab_initio", "Indonesian_B", "Indonesian_ab_initio", "Italian_A2", "Italian_B", "Italian_ab_initio", "Japanese_A2", "Japanese_B", "Japanese_ab_initio", "Korean_B", "Latin", "Malay_ab_initio", "Mandarin_B", "Mandarin_ab_initio", "Modern_Greek_A2", "Modern_Greek_B", "Norwegian_A2", "Norwegian_B", "Pilipino_A2", "Polish_B", "Portuguese_A2", "Portuguese_B", "Russian_A2", "Russian_B", "Russian_ab_initio", "Spanish_A2", "Spanish_B", "Spanish_ab_initio", "Swahili_B", "Swahili_ab_initio", "Swedish_A2", "Swedish_B", "Tamil_B", "Thai_A2", "Thai_B", "Turkish_B", "Urdu_B", "Welsh_B"]

# These are ALL the Group 3 subjects from 1991 to 2019.
Group3 = ["Art_history", "Brazilian_social_studies", "Business_and_management", "Business_and_organisation", "Business_management", "Classical_Greek_and_Roman_studies", "Economics", "Geography", "Global_politics", "History_of_the_Islamic_World", "History", "History_route_1", "History_route_2", "Islamic_history", "ITGS", "Peace_and_conflict_studies", "Philosophy", "Political_thought", "Psychology", "Social_and_cultural_anthropology", "World_cultures", "World_politics", "World_religions"]

# These are ALL the Group 4 subjects from 1991 to 2019.
Group4 = ["Astronomy", "Biology", "Chemical_and_physical_systems", "Chemistry", "Computer_science", "Design_technology", "Ecosystems_and_societies", "Environmental_systems", "Environmental_systems_and_societies", "Physics", "Sports_exercise_and_health_science"]

# These are ALL the Group 5 subjects from 1991 to 2019.
Group5 = ["Mathematical_studies", "Mathematics", "Further_Mathematics", "Mathematical_methods"]

# This is the only subject that has past papers for Group 6 from 1991 to 2019.
Group6 = ["Music"]
Groups = [Group1, Group2, Group3, Group4, Group5, Group6]
months = ["May", "November"]
subjectLevels = ["SL", "HL"]

# If you want to do this for your computer change the workingdirectory and movingto below to the where you have/want your files
coredirectory = "D:\International Baccalaureate Documents\IB PAST PAPERS\\"

# This is probably not needed, not to sure tbh
os.chdir(coredirectory)

# For x in y, basically runs for every year (items) which are in the array called years, the other for x in y are doing the same.
# To give you a better idea, the first time it runs year=1999 (since that is the first item in the array years) then 2000 and so on until it is done with the array.
for year in years:
    # print (year)
    for session in months:
        # print(session)
        workingdirectory = coredirectory + str(year) + " Examination Session\\" + session + " " + str(
            year) + " Examination Session\\"
        # generates the group names from the workingdirectory, by looking at their names and seeing if they start with Group
        Groupnames = [filename for filename in os.listdir(workingdirectory) if filename.startswith("Group")]
        for Groupname in Groupnames:
            # print(Groupname)
            for Group in Groups:
                # print(Group)
                for Subject in Group:
                    # print(Subject)
                    os.chdir(workingdirectory + Groupname)
                    # creates a list of the files
                    files_in_dir = os.listdir(workingdirectory + Groupname)
                    # goes through files one by one
                    for file_in_dir in files_in_dir:
                        # print (Subject)
                        if Subject in file_in_dir:
                            for subjectLevel in subjectLevels:
                                # calls the copyingfile function
                                if subjectLevel in file_in_dir:
                                    copyingfile()
                                # checks for papers which are both for HL and SL
                                elif ("HLSL") in file_in_dir:
                                    for subjectLevel in subjectLevels:
                                        copyingfile()