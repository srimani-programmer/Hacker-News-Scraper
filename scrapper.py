import requests
import bs4
import re


stroy_count = input('How many number of stories do you want? ')

if int(stroy_count) <= 30 and int(stroy_count) > 0:

    # Making the web request
    req = requests.get('https://news.ycombinator.com/')
    soup_obj = bs4.BeautifulSoup(req.text, 'lxml')
    storyNames = soup_obj.find_all('a', attrs={'class':'storylink'})   # For only the text within the story link.
    story_link = soup_obj.find_all('a' , attrs={'href' : re.compile("((http|https)s?://.*?)")})
    link_list = list()

    for link in story_link:
        link_list.append(link.get('href'))
    for story in range(int(stroy_count)):
        print(storyNames[story].string)
        print(link_list[story])

       # print(story.string) # To extract the text from the anchor tag
else:
    count = 0
    req = None
    story_list = list()
    while True:
        if count == 0:
            req = requests.get('https://news.ycombinator.com/')
            count += 1
        else:
            req = requests.get('https://news.ycombinator.com/news?p={}'.format(count + 1))
            count += 1
        
        soup_obj = bs4.BeautifulSoup(req.text, 'lxml')

        storyNames = soup_obj.find_all('a', attrs={'class':'storylink'})

        for story in storyNames:
            story_list.append(story.string)
            if len(story_list) == int(stroy_count):
                break
        if len(story_list) == int(stroy_count):
            break
    
    for story in story_list:
        print(story)