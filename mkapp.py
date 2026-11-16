"""웹 게임(index.html)을 앱용으로 바꾼다: 3D 엔진을 파일 안에 넣어 인터넷 없이도 열리게 한다."""
import sys,shutil,os
src=sys.argv[1] if len(sys.argv)>1 else '../dangjik/index.html'
s=open(src,encoding='utf-8').read()
tag='<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>'
assert tag in s,'three 태그 없음'
three=open('../dangjik/node_modules/three/build/three.min.js',encoding='utf-8').read()
s=s.replace(tag,'<script>'+three+'</script>',1)
open('www/index.html','w',encoding='utf-8').write(s)
for f in ['og.jpg','icon-192.png','icon-512.png','apple-touch-icon.png','favicon-32.png']:
    p='../dangjik-game/'+f
    if os.path.exists(p):shutil.copy(p,'www/'+f)
print('www/index.html',len(s))
