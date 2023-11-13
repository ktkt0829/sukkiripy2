a = {'読書','ゲーム','映画','音楽','サッカー'}
b = {'野球','サッカー','ゲーム','テニス','ゴルフ'}
input('心の準備ができたらEnterキーを押してください')
common = a & b
total = a | b
compatibility_rate = len(common)/len(total)*100
print(f'相性度は{compatibility_rate}%でした')