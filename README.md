## 반달곰 커피 홈페이지 (H2 헤더)

* [참조링크 https://반달곰 커피](https://github.com/nttkor/david/blob/main/README.md)  

* [참조링크 반달곰 커피](https://반달곰%20커피])  

오디오 출력 소스코드

```python
lang = request.args.get('lang', DEFAULT_LANG)
fp = BytesIO()
gTTS(text, "com", lang).write_to_fp(fp)
encoded_audio_data = base64.b64encode(fp.getvalue())
david.jpg 파일을 이미지로 삽입한다.
```
<font size="5"> 코디세이 </font>  
[![코디세이](logo_white.png)](https://usr.codyssey.kr/)

### foot note  
Here is a simple footnote[^1].

A footnote can also have multiple lines[^2].

[^1]: My reference.  
[^2]: To add line breaks within a footnote, prefix new lines with 2 spaces.
  This is a second line.

### Aleart
>[!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.
