# Trump Ipsum

## Description

I hid the flag in this huge, great [speech](https://github.com/FlyN-Nick/BlueHatsCTF/blob/main/misc/trump_ipsum/trump.txt.gz).

## Solution

We can first try opening trump.txt in a text editor so we can cmd+f for the file. However, as the file is so large, most text editors won't be able to open the file, so we need to take a different approach.

As this is a searching problem, we can try using `grep`. If we run the command `grep BlueHats{ trump.txt`, we get back no results, so the flag must've been altered in some manner.

We can widen our search to just `grep { trump.txt`, however when we run this it just keeps on printing out the file. Weird. We can investigate this behavior by searching for a word we know is in the file, such as China: `grep China trump.txt`. The same thing happens, except China is printed in a different color. So it's not an issue of it finding the word, but how it is displaying it. If we run `man grep` to look at the documentation of the command, we find out that it prints out the entire line that a pattern is found in. So most likely, the file has no new line characters, and so grep cannot be used.

At this point, it seems like our best option is to just write a script that will find a curly brace and print the text surrounding it. This short script does the trick:

```python
with open("trump.txt", "r") as f: # open file
    for line in f: # go through line by line (will only run once, as there is no new lines)
        for word in line.split(): # separate the text by whitespace characters
            if "{" in word:
                print(word)
```

Running the script takes around a minute, printing out *nice."}HCRA35_3GUh{staHeulB*. The flag has been reversed, hence why `grep BlueHats trump.txt` was unsuccessful. We can just reverse the text to get the flag.

## Flag
`BlueHats{hUG3_53ARCH}`
