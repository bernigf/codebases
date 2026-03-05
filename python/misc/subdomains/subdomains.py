def subdomainVisits(cpdomains):
    # STEP 1: Initialize a dictionary to store counts.
    # Using a dictionary allows O(1) average time complexity for updates.
    counts = {}

    for cpdomain in cpdomains:
        # STEP 2: Split the input string into "count" and "full domain".
        # Example: "9001 discuss.leetcode.com" -> ["9001", "discuss.leetcode.com"]
        count_str, domain = cpdomain.split()
        count = int(count_str)

        # STEP 3: Break the domain into its fragments.
        # Example: "discuss.leetcode.com" -> ["discuss", "leetcode", "com"]
        fragments = domain.split('.')

        # STEP 4: Iterate through the fragments to reconstruct all subdomains.
        # We use a loop that goes through every possible suffix.
        for i in range(len(fragments)):
            # Join the fragments from index 'i' to the end.
            # i=0: "discuss.leetcode.com"
            # i=1: "leetcode.com"
            # i=2: "com"
            subdomain = ".".join(fragments[i:])

            # STEP 5: Update the count in our dictionary.
            # .get(subdomain, 0) returns 0 if the subdomain is not yet in the map.
            counts[subdomain] = counts.get(subdomain, 0) + count

    # STEP 6: Format the dictionary back into the required list of strings.
    # Example: "9001 discuss.leetcode.com"
    return [f"{v} {k}" for k, v in counts.items()]

# Example 1

# Input list with one entry
test_1 = ["9001 api.github.com"]

# Running the function
result_1 = subdomainVisits(test_1)

# Logic explanation:
# 1. "api.github.com" -> 9001 visits
# 2. "github.com"     -> 9001 visits
# 3. "com"            -> 9001 visits

print("Example 1 Output:")
for entry in result_1:
    print(entry)