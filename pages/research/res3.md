title: Koo App - A Glance Into OSINT Collection
date: 24 Apr 21
research: research
tagosint: osint
tagtraining: training
author: ka4n6
description: Koo App is an Indian microblogging and social networking site based in Bangalore.  It is being projected as an alternative of twitter in India and has features almost similar to twitter.  One unique feature of Koo is that it is available in multiple languages allowing people to communicate in local languages. As of now it is supporting five languages (English, Hindi, Kannada, Tamil and Telugu).



![koo](\static\research\koo1.png)

[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)]()	 [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)]() 	[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)]()


'Koo App' is an Indian microblogging and social networking site based in Bangalore. Koo is available for download on both Android and iOS platforms. It can also be used directly on web browsers but I have observed some bugs on web browsers. As per latest data (February 2021) Koo has over 3 million users and most of the users are Indians. It is being projected as an alternative of twitter in India and has features almost similar to twitter.  One unique feature of Koo is that it is available in multiple languages allowing people to communicate in local languages. As of now it is supporting five languages (English, Hindi, Kannada, Tamil and Telugu), but has plans to add seven more Indian languages. 

​Therefore Koo application could be very handy for OSINTers especially if they are working on targets based in India. Koo can also pose challenge to local law enforcement agencies in criminal investigations and intelligence gathering. Keeping these in mind I have written this general blog which demonstrates methods to access Koo data without logging in.

### 1. Finding User Profile

Open [Koo App](https://www.kooapp.com/) on a web browser and search for username or Koo handle of your target. Every profile URL will be in the following format;

https://www.kooapp.com/profile/HANDLE

Where 'HANDLE' is the username or Koo Handle name displayed in the profile. It is unique to every account and are generally based on their name or profession or other interests. For example if user's name is 'Rakesh Singh', his handle is likely to contain 'rakesh' or 'singh', but may have other additional characters.

> Example:
>
>https://www.kooapp.com/profile/kanganarofficial

Koo allows handles in other languages where the HANDLE may be in Hindi, Kannada, Telugu and Tamil. HANDLE may also be mix of one of the above languages and English. 

> Example:

<textarea rows="4" cols="100">
https://www.kooapp.com/profile/%E0%B2%A8%E0%B2%BE_%E0%B2%95%E0%B2%82%E0%B2%A1__%E0%B2%95%E0%B2%A8%E0%B3%8D%E0%B2%A8%E0%B2%A1_%E0%B2%B2%E0%B3%8B%E0%B2%95</textarea>

Above example is a HANDLE in Kannada but may show as above due to URL Encoding. If you face problem in decoding the URL, you can use [CyberChef Tool](https://gchq.github.io/CyberChef/) on [GitHub](https://github.com/). 



```

Step 1: Open https://gchq.github.io/CyberChef/

Step 2: Drag "URL Decode" on the extreme left and drop it on 'Recipe' box

Step 3: Copy and paste encoded URL in 'Input' box (Encoded URL will look like the example mentioned above)

Step 3: Decoded URL will be displayed in the 'Output' box 

```


You can also use [Google Translate](https://translate.google.com/) to change HANDLE to different languages.

### 2. Finding Account ID

Similar to HANDLE, every user also has a unique Account ID or Profile ID which can be used to access additional information pertaining to the target user. Follow the steps mentioned below to find the Account ID;

> Step 1: Open Profile https://www.kooapp.com/profile/HANDLE



> Step 2: Click 'Koo'



> Step 3: Copy the Account ID (8+4+4+4+12 = 32 Characters separated by '-' (hyphen)) in the URL 
>
>  https://www.kooapp.com/profile/HANDLE/ID/Koos


For example in https://www.kooapp.com/profile/drashwathnarayan/2aa3d69e-7824-44d0-950b-8cd7cbc22ff5/Koos  the Account ID is **'2aa3d69e-7824-44d0-950b-8cd7cbc22ff5'**.



You can also find the Account ID by right clicking on the profile page and selecting **'View Page Source'** . Then search for 'IMP-'. The very first ID found next to 'IMP-' is the account ID. This should not be confused with many post IDs found on the page.

Other information can also be directly accessed using the above Profile ID also called as Account ID

> **To access 'Liked' posts:**
>
>  https://www.kooapp.com/profile/HANDLE/ID/Liked



> **To access 'Re-koo & Comment':**
>
>  https://www.kooapp.com/profile/HANDLE/ID/RekooAndComment



> **To check the where this account is mentioned/tagged:**
>
>  https://www.kooapp.com/profile/HANDLE/ID/Mentions



> **To get the list of followers:**
>
> https://www.kooapp.com/followers/ID/1

Here number '1' can be replaced by any number, but actually it is the number of followers denoted in one to three digits as ''1" or "12" or "130" and as "120K" if it crosses 999.



> **To get the names of the persons target is following:**
>
> https://www.kooapp.com/followings/ID/1

> Example: https://www.kooapp.com/followings/2aa3d69e-7824-44d0-950b-8cd7cbc22ff5/34

Again, similar to 'followers', last number '1' can be any number up to three digits depending on number of persons being followed.

### 3. Search Using Google Search

Alternatively, [Google Search](https://www.google.com/) can also be used to search Koo profiles and other information. While searching, operators  'inurl:' and 'site:' can also be used for better search results.

**To find Koo handles with complete or partial match:**

> inurl:kooapp.com/profile/ "HANDLE"

For example: 

> inurl:https://www.kooapp.com/profile/ "ka"
>
> or
>
> inurl:kooapp.com/profile/ "ka"



**To find people by Profile Names:**

> site:kooapp.com "PROFILE NAME"

Example:

> site:kooapp.com "rakesh singh"



**To search for any word mentioned in the profile (profession, place, interests, surname, affiliation etc.):**

> site:kooapp.com/profile “any word in the profile”

Example:

> site:kooapp.com/profile “farmer”
>
> site:kooapp.com/profile “bidar"



**To search any post content with key words:**

> site:kooapp.com/profile/ "KEYWORD"



**To search any post of target user with key words:**

> site:kooapp.com/profile/HANDLE "KEYWORD"

Example:

> site:kooapp.com/profile/marymillbenusa "god"



**To search trending topics using hashtags:**

> site:kooapp.com/ "HASHTAG" 

Example 

> site:kooapp.com/ "goodmorning"
>
> site:kooapp.com/ "COVID19"



### 4. Using [Wayback Machine](https://archive.org/) To Find Old Stuff

It is understood that every user changes the way his/her account looks and they keep changing their names, profile pictures, bio details, contact details, privacy settings etc. They also delete posts which might contain information useful for OSINTers. To find out these details [Archive.org](https://archive.org/) can be used. URL can  be pasted on the search bar of the website and archives can be examined.

> Step 1: Open https://archive.org/
>
> Step 2: Copy and Paste URL in this format:  https://www.kooapp.com/profile/HANDLE
>
> Step 3: Examine the profile contents of target on different dates after joining Koo



### Scraping

Anyone interested in scraping user details available on homepage can try this Python Script on Github
[https://github.com/ka4n6/Koo_Scraping](https://github.com/ka4n6/Koo_Scraping). But keep legal provisions of the country in mind before venturing into this.

Thanks for reading! I will conclude with the statement that Koo will continue to grow and there are a lot of things that needs to be done with respect to OSINT data collection from Koo.
