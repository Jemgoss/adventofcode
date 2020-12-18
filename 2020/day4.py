import re

with open("day4.input") as f:
    passports = [x.replace("\n", " ").strip() for x in f.read().split("\n\n")]

# Part 1
required_fields = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    #"cid", # Allow this to be omitted.
}
valid_count = 0
for passport in passports:
    keys = [kv.split(":")[0] for kv in passport.split(" ")]
    missing = required_fields - set(keys)
    if not missing:
        valid_count += 1
print(valid_count)

# Part 2
hgt_pat = re.compile("^([0-9]+)(cm|in)$")
def height_val(h):
    m = hgt_pat.match(h)
    return m and (\
        (150 <= int(m.group(1)) <= 193) if m.group(2) == "cm" else \
        (59 <= int(m.group(1)) <= 76) if m.group(2) == "in" else \
        False)
hcl_pat = re.compile("^#[0-9,a-f]{6}$")
ecl_vals = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
pid_pat = re.compile("^[0-9]{9}$")

validators = {
    "byr" : lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
    "iyr" : lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
    "eyr" : lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
    "hgt" : height_val,
    "hcl" : lambda x: hcl_pat.match(x),
    "ecl" : lambda x: x in ecl_vals,
    "pid" : lambda x: pid_pat.match(x),
    #"cid", # Allow this to be omitted.
    }
valid_count = 0
for passport in passports:
    passport_dict = dict([kv.split(":") for kv in passport.split(" ")])
    if all(k in passport_dict and validator(passport_dict[k]) for k, validator in validators.items()):
        valid_count += 1
print(valid_count)
