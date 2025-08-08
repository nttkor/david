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
### Image
<font size="5"> 코디세이 </font>  
[![코디세이](logo_white.png)](https://usr.codyssey.kr/)


## Lists

You can make an unordered list by preceding one or more lines of text with -, *, or +.

- George Washington
* John Adams
+ Thomas Jefferson


### Task lists

To create a task list, preface list items with a hyphen and space followed by [ ]. To mark a task as complete, use [x].

- [x] #739
- [ ] https://github.com/octo-org/octo-repo/issues/740
- [ ] Add delight to the experience when all tasks are complete :tada:


### Using emojis

You can add emoji to your writing by typing :EMOJICODE:, a colon followed by the name of the emoji.

@octocat :+1: This PR looks great - it's ready to merge! :shipit:

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
