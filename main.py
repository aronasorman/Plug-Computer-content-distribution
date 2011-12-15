import web
import utils
import os.path

urls = (
    '/', 'index'
    , '/video_player/(.*)', 'video_player'
    )

app = web.application(urls, globals())

templates = web.template.render('templates/')

class index:
    def GET(self):
        vids = utils.list_videos()
        vids = [(vid, os.path.join(utils.VIDEO_PATH,vid)) for vid in vids]
        return templates.index(vids)

class video_player:
    def GET(self, video_name):
        video_url = os.path.join(utils.VIDEO_PATH, video_name)
        return templates.video_player(video_name, video_url)

if __name__ == '__main__':
    app.run()
