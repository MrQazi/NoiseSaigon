import json
from pprint import pprint
from groqAI import ParseWithAI
from modules.event.events import Getevents,AddDummyEvent


########################################

desc = """
[english description below]
Hiếm khi ở Việt Nam mình có thể xem một show nhạc vừa kim loại nặng như metal và đẹp như một bức tranh của post-rock. Vì thế vào 26 tháng 5 này Out The Run sẽ tổ chức một show diễn của một ban nhạc như vậy có tên The Ocean đến từ Đức!
"This complex, resonant music is complemented by a considered philosophical and critical analysis of humanity’s troubling trajectory, thus providing intellectual food for thought as much as emotional gratification."
- Metal Hammer (UK)
"...a dynamic crusher that opens with trip-hop beats and psychedelic vibes inspired by Massive Attack and builds to the sort of massive, tectonic heaviness that fans have come to expect from the Berlin-based group."
- Revolver Magazine
"This is an outstanding work of art, and I can only implore you to make yourselves comfortable, and allow the time to fully immerse in the pleasure of enjoying this record from start to finish."
- Ghost Cult
Đó chỉ là một vài trích dẫn về The Ocean từ các tạp chí âm nhạc lớn trên thế giới. Trong thời gian trước ngày show Out The Run sẽ viết một số bài về lịch sử của ban nhạc, thể loại post-metal và cái gì có thể xảy ra ở show của The Ocean.
Các ban nhạc cùng biểu diễn lần này:
- Rắn Cạp Đuôi (vừa hoàn thành tour Châu Âu)
- Kaali (với sự thay đổi thành viên chơi guitar mới!!)
- Bedlam Royals (ban nhạc post-metal với các thành viên đến từ Kaali và Taiyoken)
📍 Địa điểm: 142 Trần Não, Q2 HCM (ex-Coco Bongo, ex-The Axe...)
⏰ Thời gian: 18:30, 26 tháng 5 năm 2024
💵 Vé mua trước: 450.000đ
💰 Vé tại cửa: 600.000đ
Timeline:
- 18:30 doors open
- 19:30 Bedlam Royals
- 20:10 Kaali
- 20:50 Rắn Cạp Đuôi
- 21:30 The Ocean
- 23:00 end
Như những lần trước, Out The Run tiếp tục hợp tác với Rooster Beers (một loại bia Việt Nam rất là ngon) để tiếp quản quầy bar và phục vụ các bạn đồ uống với giá rất phải chăng. Mỗi đồ uống bạn mua tại quầy sẽ ủng hộ các ban nhạc tham gia chương trình cũng như giúp chúng ta có thêm nhiều sự kiện thú vị như thế này trong tương lai! Hãy nhớ gọi bồ, Grab hoặc Be đến địa điểm để uống bia thả ga - đảm bảo an toàn trên đường về nhà. Ngoài bia, tụi mình cũng sẽ chuẩn bị các loại nước giải khát và nước suối.
Các link nghe nhạc của The Ocean và các band support ở bên thảo luận. Hãy chia sẻ event này để bạn bè đến giật cúp nhé! Hẹn gặp bạn ở đó!!
----------------------------------
It's not very often that we in Vietnam have a chance to see a live show that is both heavy as metal music, but also beautiful as post-rock. But on May 26th Out The Run will host a band just like that called The Ocean from Germany!
"This complex, resonant music is complemented by a considered philosophical and critical analysis of humanity’s troubling trajectory, thus providing intellectual food for thought as much as emotional gratification."
- Metal Hammer (UK)
"...a dynamic crusher that opens with trip-hop beats and psychedelic vibes inspired by Massive Attack and builds to the sort of massive, tectonic heaviness that fans have come to expect from the Berlin-based group."
- Revolver Magazine
"This is an outstanding work of art, and I can only implore you to make yourselves comfortable, and allow the time to fully immerse in the pleasure of enjoying this record from start to finish."
- Ghost Cult
These are just a couple of quotes about The Ocean from various popular music magazines. During the time before the show day, Out The Run will write a number of articles about the band's history, about the history of that whole musical genre of post-metal and also will introduce you to The Ocean live shows, so that you know better what to expect when you come to see the event.
Supporting bands this time are:
- Rắn Cạp Đuôi (just coming back from their another Europe tour)
- Kaali (first show with their new guitarist!!)
- Bedlam Royals (new post-metal band featuring members of Kaali and Taiyoken)
📍 Venue: 142 Trần Não Q2 HCM (ex-Coco Bongo, ex-The Axe...)
⏰ Time: 18:30, mùng 26 tháng 5 năm 2024
💵 Pre-sale ticket: 450.000đ
💰 Door ticket: 600.000đ
Timeline:
- 18:30 doors open
- 19:30 Bedlam Royals
- 20:10 Kaali
- 20:50 Rắn Cạp Đuôi
- 21:30 The Ocean
- 23:00 end
As a few previous times, this time Out The Run joins the forces with Rooster Beers (the best beer in the World!) to take over the bar and sell you beverages with very affordable prices. Each drink that you get at the bar this night will support the bands that participate this show and will help us to have more cool events like this in the future! Make sure to get a Grab or Be to the venue if you're planning on having beers - this will ensure your safety on the way back home. Soft drinks and water will also be available.
Links to The Ocean music and supporting bands are in the discussion tab. Please, share this event to get your friends to know! See you there!! See less
"""

def ResolveMissingData():
    query = f"""
    return a json file only containing BookingTicketPrice,DoorTicketPrice,Venue and Lineup fields
    no extra details
    preserve the currency in given format
    lineup as array of names 
    use full address

    {desc}
    """
    pprint(ParseWithAI(query))

#ResolveMissingData()

#event = GetEventData("https://web.facebook.com/events/1144131884055628")


Getevents()

#AddDummyEvent()