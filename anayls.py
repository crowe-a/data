import pandas



# data=pandas.read_csv("dosyalar/all_features_300_scene_1_complete - Kopya.xlsx.csv",encoding="UTF-8")

# #data.to_excel("val.xlsx",header=['max_time', 'mean_time', 'positive_score', 'negative_score', 'subjective_score', 'negative', 'positive', 'Segment', 'WC', 'Analytic', 'Clout', 'Authentic', 'Tone', 'WPS', 'BigWords', 'Dic', 'Linguistic', 'function', 'pronoun', 'ppron', 'i', 'we', 'you', 'shehec', 'function', 'pronoun', 'ppron', 'i', 'we', 'you', 'shehe', 'they', 'ipron', 'det', 'article', 'number', 'prep', 'auxverb', 'adverb', 'conj', 'negate', 'verb', 'adj', 'quantity', 'Drives', 'affiliati','insight', 'cause', 'discrep', 'tentat', 'certitude', 'diffeon', 'achieve', 'power', 'Cognition', 'allnone', 'cogproc', 'insight', 'cause', 'discrep', 'tentat', 'certitude', 'differ', 'memory', 'Affect', 'tone_pos', 'tone_neg', 'emotion', 'emo_pos', 'emo_neg', 'crefs', 'family', 'friend', 'female', 'male', 'Culture', 'poemo_anx', 'emo_anger', 'emo_sad', 'swear', 'Social', 'socbehav', 'prosocial', 'polite', 'conflict', 'moral', 'comm', 'socrefs', 'family', 'friend', 'female', 'male', 'Culture', 'politic', 'ethnicity', 'quire', 'lack', 'fulfill', 'fatigue', 'reward', 'risk', 'curtech', 'Lifestyle', 'leisure', 'home', 'work', 'money', 'relig', 'Physical', 'health', 'illness', 'wellness', 'mental', 'substances', 'sexual', 'food', 'death', 'need', 'want', 'acquire', 'lack', 'fulfiler', 'AllPunc', 'Period', 'Comma', 'QMark', 'Exclam', 'Aposll', 'fatigue', 'reward', 'risk', 'curiosity', 'allure', 'Perception', 'attention', 'motion', 'space', 'visual', 'auditory', 'feeling', 'time', 'focuspast', 'focuspresent', 'focusfuture', 'Conversation','er_utter', 'label', 'netspeak', 'assent', 'nonflu', 'filler', 'AllPunc', 'Period', 'Comma', 'QMark', 'Exclam', 'Apostro', 'OtherP', 'anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust', 'ttr', 'cttr', 'diversity', 'herdan', 'summer', 'dugast', 'maas', 'utterances', 'WC', 'unique', 'word_per_utter', 'label'])

# data.to_excel("val.xlsx")

# data2=pandas.read_csv("dosyalar/all_features_300_scene_2_complete - Kopya.csv",encoding="UTF-8")

# data2.to_excel("val2.xlsx")

data=pandas.read_excel("data1/val.xlsx")
data.to_csv("data1//valtime.csv",columns=["max_time","mean_time"])