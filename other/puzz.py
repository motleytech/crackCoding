from time import time








test_cases = [
    ["send", "more", "money"],
    ["zeroes", "ones", "binary"],
    ["send", "a", "tad", "more", "money"],
    ["seven", "seven", "six", "twenty"],
    ["saturn", "uranus", "neptune", "pluto", "planets"],
    ["donald", "gerald", "robert"],
    ["fifty", "twenty", "nine", "one", "eighty"],
    ["forty", "ten", "ten", "sixty"],
    ["ein", "ein", "ein", "ein", "vier"],
    ["lets", "solve", "this", "little", "teaser"],
    ["eleven", "lagers", "revive", "general"],
    ["she", "will", "wash", "these", "shirts"],
    ["have", "a", "happy", "happy", "easter"],
    ["ohio", "hawaii", "kansas", "alaska", "indiana"],
    ["tonto", "andthe", "lone", "ranger"],
    ["accentuate", "concertina", "transsonic", "instructor"],
    ["apolitical", "penicillin", "pickpocket", "knickknack"],
    ["coincidence", "electrician", "accelerator"],
    ["compromise", "stretchiest", "microscopic", "homestretch"],
    ["happy", "holidays", "to", "all", "hohohoho"],
    ["aries", "leo", "libra", "pisces"],
    ["gemini", "virgo", "cancer"],
    ["see", "three", "little", "wolves"],
    ["earth", "air", "fire", "water", "nature"],
    ["dclix", "dlxvi", "mccxxv"],
    ["couple", "couple", "quartet"],
    ["fish", "n", "chips", "supper"],
    ["store", "and", "name", "brands"],
    ["this", "isa", "great", "time", "waster"],
    ["the", "dog", "got", "her", "on", "the", "hand", "again"],
    ["when", "i", "really", "want", "a", "thrill"],
    ["what", "a", "week", "at", "news", "this", "has", "been"],
    ["this", "it", "seems", "to", "me", "is", "the", "heart", "of", "the", "matter"],
    ['apperception', 'aristocratic', 'concessionaire', 'conscription',
     'inappropriate', 'incapacitate', 'inconsistent',
     'interception', 'osteoporosis', 'perspiration', 'prescription',
     'proscription', 'prosopopoeia', 'protectorate', 'protestation',
     'statistician', 'transoceanic', 'transpiration', 'antiperspirant'],
]







st = time()
for case in test_cases:
    print
et = time() - st

print "elapsed time : %10.6f" % (et)
print "average time : %10.6f" % (et / len(test_cases))


