from bot import Bot

messages = {
    'START': 'START MSG',
    'FSUB': 'fsub msg',
    'ABOUT': 'ABOUT MSG',
    'START_PHOTO': '',
    'FSUB_PHOTO': ''
}

app = Bot('ses', 8, -1001834737715, [-1001834737715], '7643757891:AAFEm1tWpBovyMbzOz64E8Y6ebz5txhxgmk', [6321064549], messages, 5, 'mongodb+srv://mackenzie411685:RMo2hyASvSI8bZQ3@cluster0.jfjrm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0', 'name', 26634100, '9ea49405d5a93e784114c469f5ce4bbd', False, True, 'reply_text')

app.run()