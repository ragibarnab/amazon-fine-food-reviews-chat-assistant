# Amazon Fine Food Review Chat Assistant

Dipping my toes into the hype of Large Language Models. Created a assistant that answers questions about Amazon food reviews stored in an external data source. Uses retrieval from a vector database to augment the generation (RAG).

## Example Usage


```
$ python3 assistant.py
(Optional) Enter product id: 

(Optional) Enter user id: 

Enter your prompt:
Give me a detailed summary of products being offered by Green Mountain Coffee Roasters.

Message sent to assistant:
# # # # # # # # # #

Use the following retrieved reviews from the dataset to answer the subsequent prompt.

Review #1:
"""
Product Id: B00412K49A; User Id: AT997T4MTH9B7; Rating: 5; Summary: Love this stuff; Content: This Green Mountain dark magic coffee is just what I was looking for. Strong enough taste to enjoy and it gets me going almost immediately. Haven't noticed any after taste and buying the 120 count it pans out to like $.61 a cup. Try it you'll like it.
"""

Review #2:
"""
Product Id: B00954NYVY; User Id: A2S29X1UALPLSO; Rating: 5; Summary: Green Mountain kcup Black Magic, Black Diamond Extra Bold, Nantucket Blend; Content: I have tried many of the available coffee's available but, I enjoy a robust coffee in the morning and both Black Magic and Black Diamond Extra Bold meet and exceed what I was expecting.  The Nantucket Blend is a great coffee for anytime of day or night.  I usually wait until Amazon has a sale on these to make my purchase...Make sure when you buy k cups that the Amazon Prime logo appears...Without the Amazon Prime Logo, I have found what I received in the past did not reflect what I had ordered.. Substitution get made without your knowledge and sometimes count is short, etc...
"""

Review #3:
"""
Product Id: B0045IPX14; User Id: A1IQUAUSHJPFUC; Rating: 5; Summary: Coffee great, seller not so great.; Content: We drink Green Mountain coffee all the time, and it is one of the few suppliers that provide it in Half-Caf. I am a decafinated coffee drinker most of the time but my wife likes a little kick to start her morning and the Half-Caf does the trick, and Green Mountain's Half-Caf has a very good taste without the decalf after taste. We also buy other flavors provided by Green Mountain and they all have a great coffee taste.
"""

Review #4:
"""
Product Id: B007TJGZ18; User Id: A2S29X1UALPLSO; Rating: 5; Summary: Green Mountain kcup Black Magic, Black Diamond Extra Bold, Nantucket Blend; Content: I have tried many of the available coffee's available but, I enjoy a robust coffee in the morning and both Black Magic and Black Diamond Extra Bold meet and exceed what I was expecting.  The Nantucket Blend is a great coffee for anytime of day or night.  I usually wait until Amazon has a sale on these to make my purchase...Make sure when you buy k cups that the Amazon Prime logo appears...Without the Amazon Prime Logo, I have found what I received in the past did not reflect what I had ordered.. Substitution get made without your knowledge and sometimes count is short, etc...
"""

Review #5:
"""
Product Id: B007PA32KI; User Id: A9YEAAQVHFUTX; Rating: 5; Summary: Blackcat; Content: Great coffee!  Love all Green Mountain coffee and all the wonderful flavors.  Would and do recommend this coffee to all my friends.
"""

Review #6:
"""
Product Id: B003AP2GKY; User Id: A9YEAAQVHFUTX; Rating: 5; Summary: Blackcat; Content: Great coffee!  Love all Green Mountain coffee and all the wonderful flavors.  Would and do recommend this coffee to all my friends.
"""

Review #7:
"""
Product Id: B007TGDXMU; User Id: ADGSALGMJYHOV; Rating: 5; Summary: Great coffee, not bitter.; Content: I'm not a big fan of the green mountain coffees, because they all seem to be bitter.  This is a nice brew that is strong enough for me without being bitter.  Their version of the K cup works great in my Keurig machine, 70+ cups without a hitch.  They come nicely sealed in 10 separate 8 count packages.  I just opened my last package and it tastes as good as the first.
"""

Review #8:
"""
Product Id: B008YA1LQK; User Id: A9YEAAQVHFUTX; Rating: 5; Summary: Blackcat; Content: Great coffee!  Love all Green Mountain coffee and all the wonderful flavors.  Would and do recommend this coffee to all my friends.
"""

Review #9:
"""
Product Id: B001EO5Y52; User Id: AO4IX8RD1ZP8M; Rating: 5; Summary: Very very good coffee; Content: <a href="http://www.amazon.com/gp/product/B006N3I3Q6">Green Mountain Coffee Fair Trade Organic Sumatran Reserve, K-Cup Portion Pack for Keurig Brewers</a> This is a real treat for a coffee snob! Not only is this a great coffee overall, but even compared to other Sumatran coffees and Sumatran blends this one can hold it's own against most other roasters. I enjoy it better than both the Sumatran offerings from Starbucks. I would say it is right on par with the caribou Sumatran product. only ones that I have enjoyed even a little more were products from  Cats Ass Coffee harvested from animal droppings (Kopi luwak)at over $150 a pound 0.o and the Sumatran offered by S&D... But the S&D product is hard to find or discontinued/seasonal. I would tell friends and Coffee people all over to try this! (And yes, I grew up in Portland and Seattle so I just may know better than you)  :P  LoL<br /><br />Enjoy!
"""

Review #10:
"""
Product Id: B006N3I3Q6; User Id: AO4IX8RD1ZP8M; Rating: 5; Summary: Very very good coffee; Content: <a href="http://www.amazon.com/gp/product/B006N3I3Q6">Green Mountain Coffee Fair Trade Organic Sumatran Reserve, K-Cup Portion Pack for Keurig Brewers</a> This is a real treat for a coffee snob! Not only is this a great coffee overall, but even compared to other Sumatran coffees and Sumatran blends this one can hold it's own against most other roasters. I enjoy it better than both the Sumatran offerings from Starbucks. I would say it is right on par with the caribou Sumatran product. only ones that I have enjoyed even a little more were products from  Cats Ass Coffee harvested from animal droppings (Kopi luwak)at over $150 a pound 0.o and the Sumatran offered by S&D... But the S&D product is hard to find or discontinued/seasonal. I would tell friends and Coffee people all over to try this! (And yes, I grew up in Portland and Seattle so I just may know better than you)  :P  LoL<br /><br />Enjoy!
"""

Prompt: Give me a detailed summary of products being offered by Green Mountain Coffee Roasters.

# # # # # # # # # #

Assistant response (gpt-3.5-turbo): 
Based on the retrieved reviews from the dataset, Green Mountain Coffee Roasters offers a variety of coffee products in K-Cup portion packs for Keurig Brewers. Some of the products mentioned in the reviews include:

1. Green Mountain Dark Magic Coffee: A strong and flavorful coffee that provides an immediate boost without any noticeable aftertaste. It is available in a 120-count pack, making it cost-effective at around $0.61 per cup.

2. Black Magic, Black Diamond Extra Bold, and Nantucket Blend: These are robust coffee options suitable for morning consumption. They are described as meeting and exceeding expectations in terms of flavor and strength. The Nantucket Blend is highlighted as a versatile option for any time of day.

3. Half-Caf Coffee: Green Mountain offers a Half-Caf option for those who prefer a mix of decaffeinated and regular coffee. The Half-Caf blend is praised for its good taste without the typical aftertaste associated with decaf coffee.

4. Various Flavors: Green Mountain Coffee Roasters provides a range of flavors beyond the specific ones mentioned, all of which are appreciated for their great taste and variety. Customers enjoy recommending these coffees to friends.

5. Fair Trade Organic Sumatran Reserve: This particular product is highlighted as a treat for coffee enthusiasts, with a rich flavor profile that competes well with other Sumatran coffees on the market. It is recommended for its quality and taste, even compared to offerings from other popular coffee brands.

Overall, Green Mountain Coffee Roasters offers a diverse selection of high-quality coffee products, catering to different preferences and tastes, including strong, bold blends, flavored options, and specialty coffees like the Fair Trade Organic Sumatran Reserve.
```