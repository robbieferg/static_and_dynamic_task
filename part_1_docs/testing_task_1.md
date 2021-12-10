### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False

# ERROR - line 21: If conditional should use double equals sign (==) for value comparison instead of single eauals sign.
# ERROR - line 23: else statement should include a colon afer "else".
   

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2

# ERROR - line 30: New method should be declared with "def", not "dif".
# ERROR - line 30: comma missing between "card1" and "card2"
# ERROR - line 31: If statement should be indented.
# ERROR - line 32: Variable "card" has not been defined. Value should be "card1".  


def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
# ERROR - line 42: method declaration should be indented.
# ERROR - line 42: "total" should be assigned value of 0 on declaration ie. "total = 0".
# ERROR - line 45: Return statement should not be within for loop. It should be indented to the same level as the for statement.
# ERROR - line 45: Method cannot return a string and an integer at once. In order to return a single string the information should be contained within a format string ie. "f"You have a total of {total}"
```
