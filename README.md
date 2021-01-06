# macpack
A helpful mac changer interface for linux

## Objectives
I need a one-stop shop to change MAC address on my NICs.
- revert to factory MAC
- change to a known MAC in a database of hostnames/MAC
- change to a random MAC
- change to a blatantly obvious MAC like "DEADBEEFCAFE"
- change to an invalid MAC

## Origin
I began to write this in bash. I don't think I like regex, but hey, I know how to modify streams in python/java/etc so I quickly switched code over.

## Operation
If you plan to change your MAC to one of a list of MACs, populate your own mac.list file in a ./data/ subfolder.
###TODO: add a command flag to set path to mac.list if it lives elsewhere.

That's all for now. Development might stop once I get a working prototype. I'm happy to see how others might adapt this.
