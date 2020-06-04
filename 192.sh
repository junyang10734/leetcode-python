# Word Frequency
# runtime: faster than 100.00% 

# https://www.cnblogs.com/grandyang/p/5386475.html
grep -oE '[a-z]+' words.txt | sort | uniq -c | sort -nr | awk '{print $2" "$1}' 