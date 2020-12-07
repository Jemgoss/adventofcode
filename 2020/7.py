with open("7.input") as f:
    data = f.readlines()

# Part 1
ruleMap = {}
for rule in data:
    # striped bronze bags contain 4 striped white bags, 1 dim yellow bag, 5 clear aqua bags.
    # muted aqua bags contain 5 plaid green bags.
    # wavy teal bags contain no other bags.
    if rule:
        bag, contains = rule.rstrip(".\n").split(" bags contain ")
        if contains == "no other bags":
            containsBags = []
        else:
            containsBags = [" ".join(b.split(' ')[1:3]) for b in contains.split(", ")]
        ruleMap[bag] = containsBags

def contains(bag, container):
    contents = ruleMap[container]
    for b in contents:
        if b == bag or contains(bag, b):
            return True
    return False

def entriesContaining(bag):
  for b in ruleMap.keys():
      yield contains(bag, b)

print(sum(entriesContaining("shiny gold")))

# Part 2
ruleMap2 = {}
for rule in data:
    # striped bronze bags contain 4 striped white bags, 1 dim yellow bag, 5 clear aqua bags.
    # muted aqua bags contain 5 plaid green bags.
    # wavy teal bags contain no other bags.
    if rule:
        bag, contains = rule.rstrip(".\n").split(" bags contain ")
        if contains == "no other bags":
            containsBags = []
        else:
            containsBags = [(int(word[0]), " ".join(word[1:3])) for word in \
                (b.split(' ') for b in contains.split(", "))]
        ruleMap2[bag] = containsBags

def countBagContents(bag):
    return sum([bagCount[0] * (countBagContents(bagCount[1]) + 1) for bagCount in ruleMap2[bag]])

print(countBagContents("shiny gold"))
