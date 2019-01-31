# rodin_helpers_py

Rodin collection of useful helpers to display data

### show_link(url, title='Authorize')

Display clickable link

### video(id)

Display youtube video

### walk(item)

Prints:

```
 
 [dict  
 [list  reports
 [dict  reports > 0
 [dict  reports > 0 > columnHeader
 [list  reports > 0 > columnHeader > dimensions
 [dict  reports > 0 > columnHeader > metricHeader
 [dict  reports > 0 > data
 [list  reports > 0 > data > rows
 [list  reports > 0 > data > totals
 |      reports > 0 > data > rowCount=27
 [list  reports > 0 > data > minimums
 [list  reports > 0 > data > maximums
 |      reports > 0 > data > isDataGolden=True
 [dict  reports > 1
 [dict  reports > 1 > columnHeader
 [list  reports > 1 > columnHeader > dimensions
 [dict  reports > 1 > columnHeader > metricHeader
 [dict  reports > 1 > data
 [list  reports > 1 > data > rows
 [list  reports > 1 > data > totals
 |      reports > 1 > data > rowCount=27
 [list  reports > 1 > data > minimums
 [list  reports > 1 > data > maximums
 |      reports > 1 > data > isDataGolden=True
```

### print_rows()

Display data as markdown table

campaign_id|date|utm_term|utm_source|account_id|spent|utm_campaign|clicks|utm_content|impressions|ad_id|reach
---|---|---|---|---|---|---|---|---|---|---|---
1010819423|2019-01-20|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|12|49726084|8
1010819423|2019-01-21|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|15|49726084|13
1010819423|2019-01-22|retarg-mob|vk|1603421955|13.00|dr4|None|kiborg-vid|7|49726084|7
1010819423|2019-01-23|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|9|49726084|8
1010819423|2019-01-24|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|5|49726084|5
1010819423|2019-01-25|retarg-mob|vk|1603421955|4.60|dr4|None|kiborg-vid|4|49726084|3
1010819423|2019-01-26|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|4|49726084|3
1010819423|2019-01-27|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|6|49726084|5
1010819423|2019-01-28|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|3|49726084|3
1010819423|2019-01-29|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|5|49726084|5
1010819423|2019-01-30|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|2|49726084|2

internally convert to markdown table and display them

```
campaign_id|date|utm_term|utm_source|account_id|spent|utm_campaign|clicks|utm_content|impressions|ad_id|reach
---|---|---|---|---|---|---|---|---|---|---|---
1010819423|2019-01-20|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|12|49726084|8
1010819423|2019-01-21|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|15|49726084|13
1010819423|2019-01-22|retarg-mob|vk|1603421955|13.00|dr4|None|kiborg-vid|7|49726084|7
1010819423|2019-01-23|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|9|49726084|8
1010819423|2019-01-24|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|5|49726084|5
1010819423|2019-01-25|retarg-mob|vk|1603421955|4.60|dr4|None|kiborg-vid|4|49726084|3
1010819423|2019-01-26|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|4|49726084|3
1010819423|2019-01-27|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|6|49726084|5
1010819423|2019-01-28|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|3|49726084|3
1010819423|2019-01-29|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|5|49726084|5
1010819423|2019-01-30|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|2|49726084|2
```