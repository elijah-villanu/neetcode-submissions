class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # . are ignored, anything right of + is ignored
        # Run through filter and then add to hash map to check if visited
        # WTF are these test cases btw
        unique = set()

        for e in emails:
            local, domain = e.split('@')
            local = local.split("+")[0]
            local = local.replace(".", "")
            unique.add((local, domain))
        return len(unique)
            
