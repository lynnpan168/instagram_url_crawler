# instagram_url_crawler
Except for Crawler 2, the crawling part of this repository is from [huaying/instagram-crawler](https://github.com/huaying/instagram-crawler) for getting the url. Because huaying's work of hashtag mode is not crawling the full metadata of the post, this repository is adding the Crawler 2 part for getting the content, likes, img... in the post.

Below is what you can do with this program:
- Get Instagram posts/profile/hashtag data without using Instagram API. `crawler.py`
- Get full metadata from instagram url that get from hashtag mode. `recrawl_url.py`

This crawler could fail due to updates on instagram’s website. If you encounter any problems, please contact me.

## Install
1. Make sure you have Chrome browser installed.
2. Download [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/) and put it into bin folder: `./inscrawler/bin/chromedriver`
3. Install Selenium: `pip install -r requirements.txt`
4. `cp inscrawler/secret.py.dist inscrawler/secret.py`

## Crawler 1
### Usage
```
positional arguments:
  mode
    options: [posts, posts_full, profile, hashtag]

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        number of returned posts
  -u USERNAME, --username USERNAME
                        instagram's username
  -t TAG, --tag TAG     instagram's tag name
  -o OUTPUT, --output OUTPUT
                        output file name(json format)
```


### Example
```
python crawler.py posts -u cal_foodie -n 100 -o ./output
python crawler.py posts_full -u cal_foodie -n 100 -o ./output
python crawler.py profile -u cal_foodie -o ./output
python crawler.py hashtag -t taiwan -o ./output
```
1. Choose mode `posts`, you will get url, caption, first photo for each post; choose mode `posts_full`, you will get url, caption, all photos, time, comments, number of likes and views for each posts. Mode `posts_full` will take way longer than mode `posts`. **[`posts` is deprecated. For the recent posts, there is no quick way to get the post caption]**
1. Return default 100 hashtag posts(mode: hashtag) and all user's posts(mode: posts) if not specifying the number of post `-n`, `--number`.
2. Print the result to the console if not specifying the output path of post `-o`, `--output`.
3. It takes much longer to get data if the post number is over about 1000 since Instagram has set up the rate limit for data request.
4. Don't use this repo crawler Instagram if the user has more than 10000 posts.

The data format of `posts`:
![screen shot 2018-10-11 at 2 33 09 pm](https://user-images.githubusercontent.com/3991678/46835356-cd521d80-cd62-11e8-9bb1-888bc32af484.png)

## Crawler 2
- Install : put your hashtag mode output file(json) in instagram_url_crawler folder, and name it as 'output'.

After getting the output file from crawler 1, run `recrawl_url.py` for getting metadata from the instagram url.
This crawler only focus on the top 2 poster message. If the poster leave hashtag or content out of the top 2 message, the data of hashtag/content will be None.

Metadata contain:
1. hashtag
2. content : message include hashtag
3. likes
4. datetime
5. img_desc : image description. Same as the caption data we get from Crawler 1, but in Chinese.
6. img_url
